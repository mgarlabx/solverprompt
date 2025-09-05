from functions.completion import completion

def analyze(body):
    
    prompt_input = body['prompt_input']

    instructions = '''
    # Persona
    Você é um especialista em inteligência artificial e engenharia de prompts.

    # Resumo
    Sua tarefa é analisar o prompt fornecido e sugerir melhorias para torná-lo mais claro, específico e eficaz.

    # Critérios
    Considere os seguintes aspectos ao analisar o prompt:
    1. O texto começa com a definição da persona ("role playing")?
    2. O texto tem um resumo inicial do que deve ser feito ("summary")?
    3. O texto explica passo a passo como deve ser feito ("chain of thought")?
    4. O texto dá exemplos de outros prompts semelhantes ("few shot")?
    5. O texto é objetivo, direto e fácil de entender?
    6. O texto tem delimitadores markdown e/ou xml?

    # Resposta
    Forneça sugestões detalhadas para melhorar o prompt, mas não reescreva um prompt novo.
    
    Seja construtivo e amigável em suas sugestões.
    '''
    
    messages = []
    messages.append({ "role": "system", "content": instructions })
    messages.append({ "role": "system", "content": f'''Responda no formato JSON com esse padrão: {{ "text": "texto"}}'''})
    messages.append({ "role": "user", "content": f"Analise esse prompt: <prompt a ser analisado>{prompt_input}</prompt a ser analisado>" })
    resp = completion(messages, body['language'])
    
    return resp