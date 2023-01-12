import os
from dotenv import load_dotenv
import openai
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt_get_image(prompt):
    response = openai.Image.create(prompt=prompt, n=2, size="1024x1024")

    data_length = len(response['data'])
    print(data_length)
    print(response['data'])

    try:
        for i in range(data_length):
            image_url = response['data'][i]['url']
            res = requests.get(image_url)
            if res.status_code != 200:
                print(f'Error: {res.status_code}')
            else:
                with open(f'image_{i}.jpg', 'wb') as f:
                    f.write(res.content)
                print(f"{i + 1}th image was downloaded")

        return "Success"

    except:
        return "An error occurred"


prompt = 'A beautiful picture that describes Uzbekistan and its tradition'
result = gpt_get_image(prompt)
print(result)


prompt = 'A beautiful picture that describes Gijduvan in Uzbekistan and its tradition'
result = gpt_get_image(prompt)
print(result)

