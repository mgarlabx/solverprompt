from functions.completion import completion

def submit(body):

    prompt_input = body['prompt_input']

    
    prompt = "Você é agente de IA. " + "\n\n"
    prompt += "Sua tarefa executar o prompt enviado." + "\n\n"
    
    messages = []
    messages.append({ "role": "system", "content": prompt })
    messages.append({ "role": "system", "content": f'''Responda no formato JSON com esse padrão: {{ "text": "texto"}}'''})
    messages.append({ "role": "user", "content": f"Execute esse prompt: {prompt_input}." })
    resp = completion(messages, body['language'])
    
    return resp