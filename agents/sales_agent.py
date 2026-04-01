from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage

from config.settings import MODEL_NAME, TEMPERATURE, COMPANY_NAME, COMPANY_PRODUCTS, OPENAI_API_KEY
from prompts.sales_prompts import get_sales_prompt
from agents.tools import get_tools


def _format_products(products: list) -> str:
    lines = []
    for p in products:
        lines.append(f"- {p['name']} ({p['price']}): {p['description']}")
    return "\n".join(lines)


class SalesAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            api_key=OPENAI_API_KEY,
        )
        self.tools = get_tools()
        self.prompt = get_sales_prompt()
        self.chat_history: list = []

        agent = create_openai_tools_agent(self.llm, self.tools, self.prompt)
        self.executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
        )

    def chat(self, user_message: str) -> str:
        response = self.executor.invoke({
            "input": user_message,
            "chat_history": self.chat_history,
            "company_name": COMPANY_NAME,
            "products": _format_products(COMPANY_PRODUCTS),
        })

        output = response["output"]
        self.chat_history.append(HumanMessage(content=user_message))
        self.chat_history.append(AIMessage(content=output))
        return output

    def reset(self):
        """Limpa o histórico da conversa."""
        self.chat_history = []
