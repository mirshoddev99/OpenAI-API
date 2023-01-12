import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt3(txt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"correct spelling mistakes in this text: {txt}",
        temperature=0.1,
        max_tokens=2048
    )

    return response["choices"][0]["text"]


query = 'what is globall warming?'
response = gpt3(query)
print(response)

query = 'what day of the wek is it?'
response = gpt3(query)
print(response)

query = 'I am going move to another city'
response = gpt3(query)
print(response)

query = 'I cannot correctl speak in English'
response = gpt3(query)
print(response)




