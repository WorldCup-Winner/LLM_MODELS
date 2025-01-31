import os
from openai import OpenAI
## the access token are one repository level behind this one
## so we need to change the path to the root directory
## and then run the script

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content" : "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Give me 5 reasons why I should exercise every day."
        }
    ],
    model=model_name,
    stream=True,
    temperature=0.5
)

for update in response:
    if update.choices[0].delta.content:
        print(update.choices[0].delta.content,end="")
