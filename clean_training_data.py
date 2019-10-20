import numpy as np 
import pandas as pd 

raw = pd.read_csv('train_FD004.txt',header=None)
splits = raw[0].str.split(' ')
df = splits.apply(pd.Series)

#remove two extaneous columns at the end of file (to the right)
df = df.iloc[:,:-2]

df.rename({0: 'Unit Number', 1: 'Time',2: 'OPS1',3: 'OPS2',4: 'OPS3',
5:'SM1',6:'SM2',7:'SM3',8:'SM4',9:'SM5',10:'SM6',11:'SM7',12:'SM8',
13:'SM9',14:'SM10',15:'SM11',16:'SM12',17:'SM13',18:'SM14',19:'SM15',
20:'SM16',21:'SM17',22:'SM18',23:'SM19',24:'SM20',25:'SM21'}, 
axis='columns',inplace=True)

df.to_csv('train_data.csv')