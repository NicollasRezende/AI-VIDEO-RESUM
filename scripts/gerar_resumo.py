import openai

"configure sua chave de api aqui"

def gerar_resumo(texto):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Resuma o seguinte texto: {texto}"}],
        max_tokens=100
    )
    
    return response['choices'][0]['message']['content']
