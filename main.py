from agents.sales_agent import SalesAgent


def main():
    print("=" * 50)
    print("  Agente de Vendas - TechSales Inc.")
    print("=" * 50)
    print("Digite 'sair' para encerrar ou 'reset' para reiniciar a conversa.\n")

    agent = SalesAgent()

    while True:
        user_input = input("Você: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "sair":
            print("Agente: Obrigado pelo contato! Até logo.")
            break
        if user_input.lower() == "reset":
            agent.reset()
            print("Agente: Conversa reiniciada. Como posso ajudar?\n")
            continue

        response = agent.chat(user_input)
        print(f"\nAgente: {response}\n")


if __name__ == "__main__":
    main()
