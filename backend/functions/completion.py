import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def completion(messages, model="gpt-4o-mini", temperature=1, language="pt"):
    
    if model == "": model = "gpt-4o-mini"
    if temperature == "": temperature = 1
    if language == "": language = "pt"
    
    if language == "en": 
        messages.append({ "role": "system", "content": "Write the texts in English" })
    elif language == "es":
        messages.append({ "role": "system", "content": "Escriba los textos en español" })
    elif language == "pt":
        messages.append({ "role": "system", "content": "Escreva os textos em português" })


    client = OpenAI(api_key=os.getenv('API_KEY'))
    chat_completion = client.chat.completions.create(
        messages=messages,
        temperature=temperature,
        model=model,
        response_format={ "type": "json_object" },
    )
    resp = chat_completion.choices[0].message.content
    
    return resp