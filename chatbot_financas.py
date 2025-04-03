import openai
import time
import sys
import json
from dotenv import load_dotenv, find_dotenv
import yfinance as yf

_ = load_dotenv(find_dotenv())

client = openai.Client()




def retorna_cotacao_historica(ticker, periodo="max"):
    ticket = yf.Ticker(f"{ticker}")
    hist = ticket.history(period = periodo, auto_adjust=False)
    if len(hist) > 30:
        slice_size = int(len(hist) / 30)
        hist = hist.iloc[::-slice_size][::-1]
    hist.index = hist.index.strftime("%m-%d-%Y")
    return hist["Close"].to_json()


tools = [
    {
        "type": "function",
        "function": {
            "name": "retorna_cotacao_historica",
            "description": "Obtém a cotação de um ativo em um determinado dia, mês e ano",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker":{
                        "type": "string",
                        "description": "Nome do ativo financeiro. Ex: TSLA ou Ambev.SA (Coloque SA caso seja algo da bolsa brasileira)"
                    },
                    "periodo": {
                        "type": "string",
                        "description": "Quantidade de dias que quer pesquisar no passado. Ex: 100d"
                    }
                },
                "required": [
                    "ticker",
                    "periodo"
                ],
            },
        },
    }
]

funcoes_disponiveis = {
    "retorna_cotacao_historica": retorna_cotacao_historica,
}

def gera_texto(mensagens, model="gpt-4o-mini", max_tokens=1000, temperature=0):
    resposta = client.chat.completions.create(
        messages = mensagens,
        model = model,
        max_tokens = max_tokens,
        temperature = temperature,
        tools=tools,
        tool_choice="auto",
    )
    
    print("BW: ", end="", flush=True)
    
    texto = resposta.choices[0].message
    tool_calls = texto.tool_calls
    
    tokens_totais = resposta.usage.total_tokens
    
    if tool_calls:
        mensagens.append(texto)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = funcoes_disponiveis[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                ticker=function_args.get("ticker"),
                periodo=function_args.get("periodo"),
            )
            mensagens.append(
                {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
                }
            )
        segunda_resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensagens,
        )
        texto = segunda_resposta.choices[0].message.content

        
    for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        
    tokens_totais += segunda_resposta.usage.total_tokens
        
    print(f" Tokens usados {tokens_totais}", end="")
    
    mensagens.append({"role": "assistant", 'content': texto})
    
    return mensagens






mensagens = []

print("\nBem-vindo ao BW, seu assistente pessoal")

while True:
    prompt = input("\nUser: ")
    if prompt.lower() == "exit()":
        break
    mensagens.append({"role": "user", 'content': prompt})
    mensagens = gera_texto(mensagens)