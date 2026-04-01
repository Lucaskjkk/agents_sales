import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

COMPANY_NAME = os.getenv("COMPANY_NAME", "TechSales Inc.")
COMPANY_PRODUCTS = [
    {
        "name": "Plano Starter",
        "price": "R$ 99/mês",
        "description": "Ideal para pequenas empresas. Inclui 5 usuários, suporte básico e 10GB de armazenamento.",
    },
    {
        "name": "Plano Pro",
        "price": "R$ 299/mês",
        "description": "Para empresas em crescimento. Inclui 20 usuários, suporte prioritário e 50GB de armazenamento.",
    },
    {
        "name": "Plano Enterprise",
        "price": "Sob consulta",
        "description": "Solução completa e personalizada para grandes empresas. Usuários ilimitados e suporte dedicado.",
    },
    {
        "name": "Plano Anual",
        "price": "10% de desconto para pagamento anual",
        "description": "Pague 12 meses adiantado e economize 10% no valor total do plano escolhido.",
    },
    {
        "name": "Plano Mensal",
        "price": "Sem desconto para pagamento mensal",
        "description": "Pague mês a mês sem compromisso, ideal para quem quer testar antes de se comprometer.",
    }
    {
        "name": "Plano Trimestral",
        "price": "5% de desconto para pagamento trimestral",
        "description": "Pague 3 meses adiantado e economize 5% no valor total do plano escolhido.",
    }
]
