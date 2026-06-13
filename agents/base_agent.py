from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core,.messages import (
    HumanMessage,
    SystemMessage
)

class BaseAgent:
    def __init__(self, system_prompt):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
        self.system_prompt = system_prompt

    def run(self, prompt):
        response = self.llm.invoke([
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=prompt)
        ])
        return response.content