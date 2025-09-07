import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def completion(messages, language):
    
    if language == "en": 
        messages.append({ "role": "system", "content": "Write the texts in English" })
    elif language == "es":
        messages.append({ "role": "system", "content": "Escriba los textos en español" })
    elif language == "pt":
        messages.append({ "role": "system", "content": "Escreva os textos em português" })


    client = OpenAI(api_key=os.getenv('API_KEY'))
    chat_completion = client.chat.completions.create(
        messages=messages,
        model='gpt-4o-mini',
    )
    resp = chat_completion.choices[0].message.content
    
    return resp