import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.preprocessing import StandardScaler , OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from xgboost import XGBRegressor


df1 = pd.read_csv('cars_data_from_divar.csv')

df = df1.iloc[0:2000 , :]

#delete extera columns
df = df.drop(columns=[ 'exhibition' , 'adـtype',  'car_name' , 'insurance' ,'exchange' , 'gearbox'])
df = df.drop(df.columns[0] , axis=1)

#delete that rows haven't any value
df.dropna(subset=['name_brand'], inplace=True)

#delete rows that have fake value for price
df = df[df.price != 111111111.0]
df = df[df.price != 11111111.0]
df = df[df.price != 0.0]

#fill fuel column for rows that have nan value with 'بنزینی'
df['fuel'] = df['fuel'].fillna(df.loc[1,'fuel'])
#print(df.loc[: , 'fuel'])

#fill engine_status column for rows that have nan value with 'نیاز به تعمیر'
df['engine_status'] = df['engine_status'].fillna('نیاز به تعمیر')


selected_rows = df[df['chassis_status'].isnull()]

for index in selected_rows.index : 
    #print(index)
    if(str(df.loc[index , 'front_chassis']) == 'ضربه‌خورده' or str(df.loc[index , 'front_chassis']) == 'رنگ‌شده'):
        if(df.loc[index , 'rear_chassis'] == 'ضربه‌خورده' or df.loc[index , 'rear_chassis'] == 'رنگ‌شده'):
            df.loc[index , 'chassis_status'] = 'ضربه‌خورده'

    if(df.loc[index , 'front_chassis'] == 'ضربه‌خورده' or df.loc[index , 'front_chassis'] == 'رنگ‌شده'):
        if(df.loc[index , 'rear_chassis'] == 'سالم و پلمپ' ):
            df.loc[index , 'chassis_status'] = 'جلو ضربه‌خورده'

    if(df.loc[index , 'front_chassis'] == 'سالم و پلمپ' ):
        if(df.loc[index , 'rear_chassis'] == 'ضربه‌خورده' or df.loc[index , 'rear_chassis'] == 'رنگ‌شده'):
            df.loc[index , 'chassis_status'] = 'عقب ضربه‌خورده' 
    
    if((df.loc[index , 'front_chassis'] == 'سالم و پلمپ' and df.loc[index , 'rear_chassis']=='') or (df.loc[index , 'rear_chassis'] == 'سالم و پلمپ' and df.loc[index , 'front_chassis'] == '')):
        df.loc[index , 'chassis_status'] = 'سالم و پلمپ'

    else :
        df.loc[index , 'chassis_status'] = 'ضربه‌خورده'

df = df.drop(columns=[ 'front_chassis' , 'rear_chassis'])

df.to_csv('test3.csv')




num_df = df.select_dtypes(include=np.number)

cat_df=df.select_dtypes(include=object)

encoding=OrdinalEncoder()

cat_cols=cat_df.columns.tolist()

encoding.fit(cat_df[cat_cols])

cat_oe=encoding.transform(cat_df[cat_cols])

cat_oe=pd.DataFrame(cat_oe,columns=cat_cols)

cat_df.reset_index(inplace=True,drop=True)

cat_oe.head()

num_df.reset_index(inplace=True,drop=True)

cat_oe.reset_index(inplace=True,drop=True)

new_df=pd.concat([num_df,cat_oe],axis=1)



scaler = StandardScaler()
num_columns = ["traveled_kilometers" , "production_year" ]
new_df[num_columns] = scaler.fit_transform(new_df[num_columns])

new_df.to_csv('test2.csv')

x = new_df.drop(columns=["price"])
y = new_df["price"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=42)

training_score = []
testing_score = []
def model_prediction(model):
    model.fit(x_train,y_train)
    x_train_pred = model.predict(x_train)
    x_test_pred = model.predict(x_test)
    a = r2_score(y_train,x_train_pred)*100
    b = r2_score(y_test,x_test_pred)*100
    training_score.append(a)
    testing_score.append(b)
    
    print(f"r2_Score of {model} model on Training Data is:",a)
    print(f"r2_Score of {model} model on Testing Data is:",b)


#model_prediction(LinearRegression())
#model_prediction(DecisionTreeRegressor())
model_prediction(XGBRegressor())
#model_prediction(AdaBoostRegressor())
#model_prediction(GradientBoostingRegressor())
#model_prediction(RandomForestRegressor())