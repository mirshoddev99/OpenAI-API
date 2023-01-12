import os
from dotenv import load_dotenv
import openai
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
my_api_key = openai.api_key

"""
Parameters = {
  "model": "text-davinci-edit-001",
  "input": "What day of the wek is it?",
  "instruction": "Fix the spelling mistakes",
}

response = {
  "object": "edit",
  "created": 1589478378,
  "choices": [
    {
      "text": "What day of the week is it?",
      "index": 0,
    }
  ],
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 32,
    "total_tokens": 57
  }
}
"""


def gpt3(txt):
    res = openai.Completion.create(
        engine='davinci-instruct-beta',
        prompt=txt,
        temperature=0,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return res.choices[0].text


query = 'what is global warming?'
response = gpt3(query)
print(response)

query = 'who is Elon Mask?'
response = gpt3(query)
print(response)



