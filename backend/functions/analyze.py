from functions.completion import completion

def analyze(body):
    
    prompt_input = body['prompt_input']

    
    prompt = "Você é um especialista em inteligência artificial e engenharia de prompts. " + "\n\n"
    prompt += "Sua tarefa é analisar o prompt fornecido e sugerir melhorias para torná-lo mais claro, específico e eficaz. " + "\n\n"
    prompt += "Considere os seguintes aspectos ao analisar o prompt: " + "\n"
    prompt += "1. Clareza: O prompt é fácil de entender? " + "\n"
    prompt += "2. Especificidade: O prompt é específico o suficiente para orientar a resposta? " + "\n"
    prompt += "3. Contexto: O prompt fornece contexto suficiente para a tarefa? " + "\n"
    prompt += "4. Objetivo: O objetivo do prompt está claramente definido? " + "\n"
    prompt += "5. Linguagem: A linguagem usada é apropriada para o público-alvo? " + "\n\n"
    prompt += "Forneça sugestões detalhadas para melhorar o prompt, incluindo exemplos de reformulações, se aplicável. " + "\n\n"
    prompt += "Lembre-se de ser construtivo e específico em suas sugestões."
    
    messages = []
    messages.append({ "role": "system", "content": prompt })
    messages.append({ "role": "system", "content": f'''Responda no formato JSON com esse padrão: {{ "text": "texto"}}'''})
    messages.append({ "role": "user", "content": f"Analise esse prompt: {prompt_input}." })
    resp = completion(messages, "gpt-4o", "", body['language'])
    
    return resp