import requests
import re
from bs4 import BeautifulSoup
import numpy as np 
from unidecode import unidecode
import pandas as pd
import time


#page = requests.get('https://divar.ir/s/tehran/car')
#
#soup = BeautifulSoup(page.text,'html.parser')
#
#cars_links = soup.find_all('div',attrs={'class' : 'post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46'})
#links = []
#for c in cars_links :
#    tagA = c.find('a')
#    link = re.findall(r'<a class="" href="(.*?)">', str(tagA))
#    link = f'https://divar.ir{link[0]}'
#    links.append(link)
#
#print(len(links))
#i = 0
#columns = ['traveled_kilometers' , 'production_year' , 'color','exhibition', 'adـtype' , 'name_brand' ,'car_name', 'fuel' , 'engine_status' , 'chassis_status' , 'front_chassis' , 'rear_chassis' , 'body_status' , 'insurance' , 'gearbox' , 'exchange' , 'price']
#cars_data = pd.DataFrame(index=range((len(links))),columns=columns)
#
#
#for l in links:
#    j = 0
#    page = requests.get(l)
#    print(l)
#    soup = BeautifulSoup(page.text,'html.parser')
#    kilometer_yaer_color = soup.find_all('span' , attrs={'class':'kt-group-row-item__value'})
#    if(len(kilometer_yaer_color) < 3): continue
#    kilometer_digits = re.findall(r'(\d*),*(\d*),*(\d*)', str(unidecode(kilometer_yaer_color[0].text)))
#    kilometer_digit = kilometer_digits[0][0] + kilometer_digits[0][1] + kilometer_digits[0][2]
#    cars_data.loc[i,'traveled_kilometers'] = float(kilometer_digit)
#    cars_data.loc[i,'production_year'] = float(unidecode(kilometer_yaer_color[1].text))
#    cars_data.loc[i,'color'] = kilometer_yaer_color[2].text
#    
#    other_data = soup.find_all('div', attrs={'class':'kt-base-row kt-base-row--large kt-unexpandable-row'})
#    #print(len(other_data))
#    for data in other_data:
#        name_of_field = data.find('p' , attrs={'class':'kt-base-row__title kt-unexpandable-row__title'})
#        if(name_of_field.text == 'نمایشگاه'):
#            value_of_data = data.find('a' , attrs={"class" : "kt-unexpandable-row__action kt-text-truncate"})
#            cars_data.loc[i,'exhibition'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'نوع آگهی'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'adـtype'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'برند و تیپ'):
#            value_of_data = data.find('a' , attrs={"class" : "kt-unexpandable-row__action kt-text-truncate"})
#            cars_data.loc[i,'name_brand'] = str(value_of_data.text)
#            cars_data.loc[i,'car_name'] = unidecode(str(value_of_data.text))
#            
#        
#        if (name_of_field.text == 'نوع سوخت'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'fuel'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'وضعیت موتور'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'engine_status'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'وضعیت شاسی‌ها'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'chassis_status'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'شاسی جلو'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'front_chassis'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'شاسی عقب'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'rear_chassis'] = str(value_of_data.text)
#            
#
#        if (name_of_field.text == 'وضعیت بدنه'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'body_status'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'مهلت بیمهٔ شخص ثالث'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            mounth_digits = re.findall(r'(\d*).*', str(unidecode(value_of_data.text)))
#            mounth_digit = mounth_digits[0][0]
#            cars_data.loc[i,'insurance'] = float(mounth_digit)
#            
#        
#        if (name_of_field.text == 'گیربکس'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'gearbox'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'مایل به معاوضه'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            cars_data.loc[i,'exchange'] = str(value_of_data.text)
#            
#        
#        if (name_of_field.text == 'قیمت فروش نقدی'):
#            value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
#            only_digits = re.findall(r'(\d*),*(\d*),*(\d*) .*', str(unidecode(value_of_data.text)))
#            only_digit = only_digits[0][0] + only_digits[0][1] + only_digits[0][2]
#            cars_data.loc[i,'price'] = float(only_digit)
#            
#        
#        
#
#    print(i)
#    i = i +1
#    
#print(cars_data)
##cars_data.to_csv('cars_data_from_divar.csv', encoding='utf-8')
#output_path = 'cars_data_from_divar.csv'
#cars_data.to_csv(output_path, mode='a', header=False , encoding='utf-8')
#
#new_df = pd.get_dummies(columns=["color"],data=cars_data)


  
  
while(True):
    page = requests.get('https://divar.ir/s/tehran/car')

    soup = BeautifulSoup(page.text,'html.parser')

    cars_links = soup.find_all('div',attrs={'class' : 'post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46'})
    links = []
    for c in cars_links :
        tagA = c.find('a')
        link = re.findall(r'<a class="" href="(.*?)">', str(tagA))
        link = f'https://divar.ir{link[0]}'
        links.append(link)

    print(len(links))
    i = 0
    columns = ['traveled_kilometers' , 'production_year' , 'color','exhibition', 'adـtype' , 'name_brand' ,'car_name', 'fuel' , 'engine_status' , 'chassis_status' , 'front_chassis' , 'rear_chassis' , 'body_status' , 'insurance' , 'gearbox' , 'exchange' , 'price']
    cars_data = pd.DataFrame(index=range((len(links))),columns=columns)


    for l in links:
        j = 0
        page = requests.get(l)
        print(l)
        soup = BeautifulSoup(page.text,'html.parser')
        kilometer_yaer_color = soup.find_all('span' , attrs={'class':'kt-group-row-item__value'})
        if(len(kilometer_yaer_color) < 3): continue
        kilometer_digits = re.findall(r'(\d*),*(\d*),*(\d*)', str(unidecode(kilometer_yaer_color[0].text)))
        kilometer_digit = kilometer_digits[0][0] + kilometer_digits[0][1] + kilometer_digits[0][2]
        cars_data.loc[i,'traveled_kilometers'] = float(kilometer_digit)
        cars_data.loc[i,'production_year'] = float(unidecode(kilometer_yaer_color[1].text))
        cars_data.loc[i,'color'] = kilometer_yaer_color[2].text
    
        other_data = soup.find_all('div', attrs={'class':'kt-base-row kt-base-row--large kt-unexpandable-row'})
        #print(len(other_data))
        for data in other_data:
            name_of_field = data.find('p' , attrs={'class':'kt-base-row__title kt-unexpandable-row__title'})
            if(name_of_field.text == 'نمایشگاه'):
                value_of_data = data.find('a' , attrs={"class" : "kt-unexpandable-row__action kt-text-truncate"})
                cars_data.loc[i,'exhibition'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'نوع آگهی'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'adـtype'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'برند و تیپ'):
                value_of_data = data.find('a' , attrs={"class" : "kt-unexpandable-row__action kt-text-truncate"})
                cars_data.loc[i,'name_brand'] = str(value_of_data.text)
                cars_data.loc[i,'car_name'] = unidecode(str(value_of_data.text))
            
        
            if (name_of_field.text == 'نوع سوخت'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'fuel'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'وضعیت موتور'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'engine_status'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'وضعیت شاسی‌ها'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'chassis_status'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'شاسی جلو'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'front_chassis'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'شاسی عقب'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'rear_chassis'] = str(value_of_data.text)
            

            if (name_of_field.text == 'وضعیت بدنه'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'body_status'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'مهلت بیمهٔ شخص ثالث'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                mounth_digits = re.findall(r'(\d*).*', str(unidecode(value_of_data.text)))
                mounth_digit = mounth_digits[0][0]
                cars_data.loc[i,'insurance'] = float(mounth_digit)
            
        
            if (name_of_field.text == 'گیربکس'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'gearbox'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'مایل به معاوضه'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                cars_data.loc[i,'exchange'] = str(value_of_data.text)
            
        
            if (name_of_field.text == 'قیمت فروش نقدی'):
                value_of_data = data.find('p' , attrs={'class':'kt-unexpandable-row__value'})
                only_digits = re.findall(r'(\d*),*(\d*),*(\d*) .*', str(unidecode(value_of_data.text)))
                only_digit = only_digits[0][0] + only_digits[0][1] + only_digits[0][2]
                cars_data.loc[i,'price'] = float(only_digit)
            
        
        

        print(i)
        i = i +1
    
    print(cars_data)
    #cars_data.to_csv('cars_data_from_divar.csv', encoding='utf-8')
    output_path = 'cars_data_from_divar.csv'
    cars_data.to_csv(output_path, mode='a', header=False , encoding='utf-8')
    time.sleep(300)
