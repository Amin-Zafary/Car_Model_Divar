import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from xgboost import XGBRegressor
#from catboost import CatBoostRegressor
#from lightgbm import LGBMRegressor

df = pd.read_csv('cars_data_from_divar.csv')

#delete extera columns
df = df.drop(columns=[ 'exhibition' , 'adـtype',  'car_name' , 'insurance' ,'exchange' ])
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


new_df = df


#dunnies string features
new_df = pd.get_dummies(columns=["color","name_brand","fuel","engine_status","chassis_status","front_chassis",
                                "rear_chassis","body_status" , 'gearbox' ],data=new_df)

#scale numerical features
scaler = StandardScaler()
num_columns = ["traveled_kilometers" , "production_year" ]
new_df[num_columns] = scaler.fit_transform(new_df[num_columns])

new_df.to_csv("test.csv")

#create sparate dataframe for target value and features
x = new_df.drop(columns=["price"])
y = new_df["price"]

print(y.shape)
print(x.shape)

#creating teat and train set 
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


model_prediction(LinearRegression())
model_prediction(DecisionTreeRegressor())
model_prediction(XGBRegressor())
model_prediction(AdaBoostRegressor())
model_prediction(GradientBoostingRegressor())
model_prediction(RandomForestRegressor())
#model_prediction(LGBMRegressor())
#model_prediction(CatBoostRegressor(verbose=False))

#plt.figure(figsize=(14,6))
#counts = df["name_brand"].value_counts()
#sns.barplot(x=counts.index, y=counts.values)
#plt.xlabel("Name Brand")
#plt.ylabel("Total No. of cars sold")
#plt.title("Total numbers of a Cars", pad=20, fontweight="black", fontsize=20)
#plt.xticks(rotation=90)
#plt.show()
