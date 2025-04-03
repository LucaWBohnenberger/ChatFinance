# Assistente BW - Chatbot com OpenAI e Yahoo Finance

Este projeto é um assistente pessoal baseado em **OpenAI** e **Yahoo Finance** que pode buscar cotações históricas de ativos financeiros e responder perguntas utilizando **GPT-4o-mini**.

## 📌 Funcionalidades

- Integração com a API da OpenAI para gerar respostas inteligentes.
- Busca de cotações históricas de ativos financeiros usando a biblioteca `yfinance`.
- Suporte para ferramentas (`tools`) que permitem chamadas diretas a funções específicas.
- Interface simples via terminal.

## 🛠️ Tecnologias Utilizadas

- Python
- OpenAI API
- Yahoo Finance (`yfinance`)
- `dotenv` para carregar variáveis de ambiente
- JSON para manipulação de dados

## 🚀 Como Executar

1. **Clone este repositório**  
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
2. **Crie um ambiente virtual e ative-o **
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
4. **Crie um arquivo .env e adicione sua chave da OpenAI:**
   ```sh
   OPENAI_API_KEY=your_api_key_here
5. **Execute o chatbot**
   ```sh
   python chatbot_financas.py
