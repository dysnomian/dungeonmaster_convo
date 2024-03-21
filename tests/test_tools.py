from dungeonmaster_convo.tools import Tools


def test_executor():
    tools = Tools()
    assert tools.executor() == "Expected result"


def test_functions():
    tools = Tools()
    assert tools.functions() == "Expected result"
