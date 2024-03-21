import json

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from dmc_agents.llm import LLM
from dmc_agents.tools import Tools


class Agent:
    def __init__(self, params={}) -> None:
        self.tools = params.get("tools", Tools())
        self.llm = params.get("llm", LLM().instance)
        self.system_message = params.get("system_message")

    def create(self, system_message: str):
        """Create an agent."""
        functions = self.tools.functions()

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " If you are unable to fully answer, that's OK, another assistant with different tools "
                    " will help where you left off. Execute what you can to make progress."
                    " If you or any of the other assistants have the final answer or deliverable,"
                    " prefix your response with FINAL ANSWER so the team knows to stop."
                    " You have access to the following tools: {tool_names}.\n{system_message}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        prompt = prompt.partial(system_message=self.system_message)
        prompt = prompt.partial(tool_names=self.tool_names())
        return prompt | self.llm.bind_functions(functions)

    def tool_names(self):
        return ", ".join([tool.name for tool in self.tools.tool_list])
