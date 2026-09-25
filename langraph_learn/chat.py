from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    print("\n\ninside chatbot", state)
    return{ "messages": ["hi, this is a message from chatbot node"]}

def samplenode(state: State):
    print("\n\ninside samplenode", state)
    return {"messages": ["Smaple messages is appended"]}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode",samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)


graph = graph_builder.compile()


upadated_state = graph.invoke(State({"messages": ["Hi, Mu=y name is alok maurya"]}))

print("\n\nupdated_state", upadated_state)
