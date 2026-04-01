from langchain.tools import tool
from config.settings import COMPANY_PRODUCTS


@tool
def list_products(query: str = "") -> str:
    """Lista todos os produtos disponíveis. Use quando o cliente perguntar sobre produtos ou planos."""
    products_info = []
    for p in COMPANY_PRODUCTS:
        products_info.append(
            f"- {p['name']}: {p['price']}\n  {p['description']}"
        )
    return "Produtos disponíveis:\n" + "\n".join(products_info)


@tool
def check_product_details(product_name: str) -> str:
    """Busca detalhes de um produto específico pelo nome."""
    for p in COMPANY_PRODUCTS:
        if product_name.lower() in p["name"].lower():
            return (
                f"Produto: {p['name']}\n"
                f"Preço: {p['price']}\n"
                f"Descrição: {p['description']}"
            )
    return f"Produto '{product_name}' não encontrado. Use 'list_products' para ver todos os planos."


@tool
def register_lead(customer_name: str, contact: str, interested_plan: str) -> str:
    """Registra um lead de cliente interessado em um plano. Use quando o cliente demonstrar interesse real."""
    # Em produção, aqui você salvaria em um CRM ou banco de dados
    lead = {
        "customer_name": customer_name,
        "contact": contact,
        "interested_plan": interested_plan,
    }
    print(f"\n[LEAD REGISTRADO] {lead}")
    return (
        f"Lead registrado com sucesso!\n"
        f"Cliente: {customer_name}\n"
        f"Contato: {contact}\n"
        f"Plano de interesse: {interested_plan}\n"
        f"Nossa equipe entrará em contato em breve."
    )


@tool
def calculate_discount(plan_name: str, months: int) -> str:
    """Calcula desconto para pagamento antecipado de múltiplos meses."""
    discounts = {1: 0, 3: 5, 6: 10, 12: 20}
    discount = discounts.get(months, 0 if months < 3 else 20)
    if discount == 0 and months < 3:
        return f"Para {months} mês(es) não há desconto disponível. Pague 3, 6 ou 12 meses para obter descontos."
    return (
        f"Para o {plan_name} com pagamento de {months} meses:\n"
        f"Desconto aplicado: {discount}%\n"
        f"Você economiza pagando antecipado!"
    )


def get_tools():
    return [list_products, check_product_details, register_lead, calculate_discount]
