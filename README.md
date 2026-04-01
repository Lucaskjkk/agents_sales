# 🤖 Agents Sales

Agente de vendas conversacional construído com **LangChain** e **OpenAI**, capaz de apresentar produtos, registrar leads e calcular descontos de forma autônoma.

## Estrutura

```
agents_sales/
├── agents/
│   ├── sales_agent.py   # AgentExecutor com memória de conversa
│   └── tools.py         # Ferramentas: listar produtos, registrar lead, calcular desconto
├── config/
│   └── settings.py      # Configurações e catálogo de produtos
├── prompts/
│   └── sales_prompts.py # System prompt do agente
├── main.py              # CLI interativa
├── requirements.txt
└── .env.example
```

## Funcionalidades

- Conversa com histórico (memória de sessão)
- **Tools** disponíveis para o agente:
  - `list_products` — lista todos os planos disponíveis
  - `check_product_details` — detalhes de um plano específico
  - `register_lead` — registra cliente interessado
  - `calculate_discount` — calcula desconto por antecipação de pagamento

## Setup

```bash
# 1. Clone e entre na pasta
git clone https://github.com/seu-usuario/agents_sales.git
cd agents_sales

# 2. Crie o ambiente virtual e instale dependências
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

# 3. Configure as variáveis de ambiente
cp .env.example .env
# edite .env e adicione sua OPENAI_API_KEY

# 4. Execute
python main.py
```

## Personalização

Edite `config/settings.py` para alterar:
- `COMPANY_NAME` — nome da sua empresa
- `COMPANY_PRODUCTS` — catálogo de produtos e preços

## Tech Stack

- [LangChain](https://python.langchain.com/)
- [OpenAI GPT-4o-mini](https://platform.openai.com/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## Licença

MIT
