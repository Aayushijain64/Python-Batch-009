import pandas as pd
Studentname = pd.Series(['Aayushi Jain','Anshika','Yash','Yashi'])
marks = pd.Series([8,56,98,100,78])
pd.DataFrame({'StudentNames' : Studentname,"Marks" : marks})

Dataset = pd.read_csv("https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/ff414a1bcfcba32481e4d4e8db578e55872a2ca1/titanic.csv")
Dataset.describe()
Dataset.head()