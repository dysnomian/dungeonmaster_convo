import functools
import json

import dmc_agents.llm
import dmc_agents.router as router
from dmc_agents.agent_state import AgentState
from dmc_agents.tools.research_toolbox import scrape_webpages, tavily_tool
from dmc_agents.tools.documentation_toolbox import create_outline, read_document, write_document, edit_document, python_repl
from dmc_agents.helpers import create_agent, agent_node, create_team_supervisor

toolbox = Tools()
tool_executor = tool_executor(toolbox.tool_list)


def main():


if __name__ == "__main__":
    main()
