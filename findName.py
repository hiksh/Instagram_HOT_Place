import openai
import pandas as pd
import time
openai.api_key = input("Enter the API_KEY: ")

data = pd.read_csv('crawlingdata.csv', index_col=0)

data['name'] = ""

for idx, row in data.iterrows():
    # print(row.loc["content"])
    if row.loc["name"] != "":
        continue
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system", "content":"you should find the name of restaurant"},
            {"role":"user", "content": f'{row.loc["content"]} print only name of restaurant '},
        ]
    )

    #time.sleep(20) - try this!
    response= response.choices[0].message.content
    print(f"response in {idx}: {response}")
    row.loc["name"] = response
    time.sleep(10)

data.to_csv("crawlingdata.csv", mode='w')
