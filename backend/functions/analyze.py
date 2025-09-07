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
    - Se estiver bom, não mude. Se não estiver, sugira melhorias.
    2. O texto tem um resumo inicial do que deve ser feito ("summary")?
    - Se estiver bom, não mude. Se não estiver, sugira melhorias.
    3. O texto explica passo a passo como deve ser feito ("chain of thought")?
    - Se estiver bom, não mude. Se não estiver, sugira melhorias.
    4. O texto dá exemplos de outros prompts semelhantes ("few shot")?
    - Se estiver bom, não mude. Se não estiver, sugira melhorias.
    5. O texto é objetivo, direto e fácil de entender?
    - Se estiver bom, não mude. Se não estiver, sugira melhorias.
    6. O texto tem delimitadores markdown e/ou xml?
    - Se estiver bom, não mude. Se não estiver, sugira melhorias.

    # Resposta
    Em cada um dos itens, forneça sugestões apenas se forem relevantes.
    Mas se o prompt já estiver bom, diga que está ótimo e não faça sugestões.
    Não reescreva um prompt novo.
    
    Seja construtivo e amigável em suas sugestões.
    '''
    
    messages = []
    messages.append({ "role": "system", "content": instructions })
    messages.append({ "role": "user", "content": f"Analise esse prompt: <prompt a ser analisado>{prompt_input}</prompt a ser analisado>" })
    resp = completion(messages, body['language'])
    
    return resp