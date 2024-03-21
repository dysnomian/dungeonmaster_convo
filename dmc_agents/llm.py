from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

from dmc_agents.tools import Tools


class LLM:
    def __init__(self, params={}):
        self.temperature = params.get("temperature", 0)
        self.streaming = params.get("streaming", True)
        self.model_name = params.get("model_name", "gpt-3.5-turbo")
        self.tool_list = params.get("tool_list", Tools().tool_list)

        # We will set streaming=True so that we can stream tokens
        # See the streaming section for more information on this.
        self.instance = ChatOpenAI(
            temperature=self.temperature,
            streaming=self.streaming,
            model_name=self.model_name,
        )

    def bind_functions(self, functions):
        return self.instance.bind_functions(functions)
