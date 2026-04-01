# 🤖 Agents Sales

> Agente de vendas conversacional com inteligência artificial, construído com **LangChain** e **OpenAI**.

---

## O que é este projeto?

**Agents Sales** é um agente de IA que simula um vendedor humano em uma conversa por texto. Ele é capaz de:

- Entender a necessidade do cliente através do diálogo
- Apresentar produtos e planos disponíveis
- Calcular descontos para pagamentos antecipados
- Registrar o interesse do cliente (lead) para follow-up

O projeto usa o conceito de **Agentes** do LangChain: ao invés do modelo simplesmente responder texto, ele decide de forma autônoma **qual ferramenta usar** em cada etapa da conversa — por exemplo, buscar detalhes de um produto ou registrar um lead no sistema.

---

## Como funciona?

```
Usuário digita uma mensagem
        ↓
   Agente (LLM) analisa a intenção
        ↓
   Decide se precisa usar uma ferramenta
        ↓
   Executa a ferramenta (ex: buscar produto)
        ↓
   Formula a resposta final com base no resultado
        ↓
   Responde ao usuário mantendo o histórico da conversa
```

As **ferramentas (tools)** disponíveis para o agente são:

| Ferramenta | O que faz |
|---|---|
| `list_products` | Lista todos os planos disponíveis |
| `check_product_details` | Retorna detalhes de um plano específico |
| `register_lead` | Registra o cliente interessado para contato |
| `calculate_discount` | Calcula desconto por pagamento antecipado (3, 6 ou 12 meses) |

---

## Estrutura do projeto

```
agents_sales/
├── agents/
│   ├── sales_agent.py   # Classe principal: monta e executa o agente com memória
│   └── tools.py         # Definição das ferramentas disponíveis para o agente
├── config/
│   └── settings.py      # Configurações gerais, chaves e catálogo de produtos
├── prompts/
│   └── sales_prompts.py # Instruções do sistema (personalidade e regras do agente)
├── main.py              # Ponto de entrada: CLI para conversar com o agente
├── requirements.txt     # Dependências do projeto
├── .env.example         # Modelo do arquivo de variáveis de ambiente
└── .gitignore
```

### Explicando cada pasta

- **`agents/`** — Coração do projeto. O `sales_agent.py` instancia o LLM, carrega as tools e cria o `AgentExecutor`, que é responsável pelo loop de raciocínio do agente. O `tools.py` define as funções que o agente pode chamar.

- **`config/`** — Centraliza todas as configurações. Aqui você define o nome da empresa, os produtos e suas chaves de API.

- **`prompts/`** — Define a "personalidade" do agente via system prompt: tom, regras de negócio e o que ele pode ou não fazer.

- **`main.py`** — Interface de linha de comando simples para testar o agente de forma interativa.

---

## Pré-requisitos

- Python 3.10 ou superior
- Uma chave de API da [OpenAI](https://platform.openai.com/)

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/agents_sales.git
cd agents_sales
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo de exemplo e preencha com seus dados:

```bash
cp .env.example .env
```

Abra o `.env` e defina sua chave:

```env
OPENAI_API_KEY=sk-...
MODEL_NAME=gpt-4o-mini
COMPANY_NAME=TechSales Inc.
```

### 5. Execute

```bash
python main.py
```

Durante a conversa, você pode digitar:
- `reset` — limpa o histórico e começa uma nova conversa
- `sair` — encerra o agente

---

## Como personalizar

Edite o arquivo `config/settings.py` para adaptar ao seu negócio:

```python
COMPANY_NAME = "Minha Empresa"

COMPANY_PRODUCTS = [
    {
        "name": "Plano Básico",
        "price": "R$ 49/mês",
        "description": "Descrição do plano...",
    },
    # adicione mais planos aqui
]
```

Para alterar o comportamento do agente (tom, regras, restrições), edite o system prompt em `prompts/sales_prompts.py`.

---

## Tecnologias utilizadas

- [LangChain](https://python.langchain.com/) — framework para construção de agentes e pipelines com LLMs
- [OpenAI API](https://platform.openai.com/) — modelo de linguagem (GPT-4o-mini por padrão)
- [python-dotenv](https://github.com/theskumar/python-dotenv) — gerenciamento de variáveis de ambiente

---

## Licença

MIT
