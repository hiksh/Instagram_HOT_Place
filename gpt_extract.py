import os
import openai
from dotenv import load_dotenv
import pandas as pd
import time

def extract_name(data,Ap_key):
    n_lst=[]
    openai.api_key=Ap_key

    for idx,row in data.iterrows():
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"you should find the name of cafe"},
                {"role":"user","content":f'Find all the name of cafe in {row.loc["Context"]}, and make sure to print the only names in "".'},
            ] #restaurant - Context / Cafe - content
        )
    
        time.sleep(20)
        response=response.choices[0].message.content
        print(f"responze in {idx}: {response}")
        time.sleep(5)
        n_lst.append(response)
    
    return n_lst

df=pd.read_csv('extract_cafe.csv') #restaurant - extract.csv / Cafe - crawlingdataCafe.csv
n=[]
key=input("Enter the API_KEY: ")

for i in range(0,len(df),5):
    if i+5>len(df):
        i_df=df[i:]
        n_df=extract_name(i_df,key)
    else:
        i_df=df[i:i+5]
        n_df=extract_name(i_df,key)
    time.sleep(5)
    n.extend(n_df)
print("Extract Done!")

df["name"]=n
df.to_csv("extract_cafe.csv",index=False)

print("Finish!!")

