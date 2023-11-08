import os
import openai
from dotenv import load_dotenv
import pandas as pd
import time

def extract_name(data):
    n_lst=[]
    openai.api_key=input("Enter the API_KEY: ")

    for idx,row in data.iterrows():
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"you should find the name of restaurant"},
                {"role":"user","content":f'{row.loc["Context"]} find only name of restaurant and print the name in ""'},
            ]
        )
    
    time.sleep(20)
    response=response.choices[0].message.content
    print(f"responze in {idx}: {response}")
    time.sleep(3)
    n_lst.append(response)
    
    return n_lst

df=pd.read_csv('ex_clean_data.csv')
o_data=df[df["name"]!=""]
ex_data=df[df["name"] == ""]
name=[]

for i in range(0,len(ex_data),10):
    if i+10>len(ex_data):
        i_df=ex_data[i:]
        n_df=extract_name(i_df)
    else:
        i_df=ex_data[i:i+10]
        n_df=extract_name(i_df)
    name.extend(n_df)


ex_data.loc["name"]=name
df=pd.concat([o_data,ex_data],ignore_index=True)
df.to_csv("ex_clean_data.csv",index=False)

