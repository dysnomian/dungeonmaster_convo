from tempfile import TemporaryDirectory
from typing import Annotated, List

from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_experimental.utilities import PythonREPL
from langgraph.prebuilt.tool_executor import ToolExecutor


def tool_executor(tool_list):
    return ToolExecutor(tool_list)


class Tools:
    def __init__(self, params={}):
        self.working_directory = params.get(
            "working_directory", TemporaryDirectory(prefix="dm_convo_").name
        )
        self.tavily_tool = TavilySearchResults(max_results=5)
        self.repl = PythonREPL()
        self.read_tool, self.write_tool, self.list_tool = self.fs_tools()
        self.tool_list = [
            self.tavily_tool,
            self.python_repl_tool,
            self.read_tool,
            self.write_tool,
            self.list_tool,
        ]

    def functions(self):
        return [convert_to_openai_function(t) for t in self.tool_list]

    def fs_tools(self):
        fs_tools = FileManagementToolkit(
            root_dir=str(self.working_directory),
            selected_tools=["read_file", "write_file", "list_directory"],
        ).get_tools()
        return fs_tools
