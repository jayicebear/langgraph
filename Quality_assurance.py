from langchain_core import LangGraph
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# Define the State class to represent the graph's state
class State:
    def __init__(self, query, current_role, messages, current_judge, judgement_reason):
        self.query = query
        self.current_role = current_role
        self.messages = messages
        self.current_judge = current_judge
        self.judgement_reason = judgement_reason

# Define the node functions that simulate the steps in your flow
def selection_node(state: State):
    # Simulate a selection operation
    state.current_role = "selected role"
    return state

def answering_node(state: State):
    # Simulate answering
    state.messages.append("Generated answer")
    return state

def check_node(state: State):
    # Simulate checking
    if state.current_judge == "approved":
        state.judgement_reason = "Valid"
    else:
        state.judgement_reason = "Invalid"
    return state

# Define a LangGraph to handle the graph structure
graph = LangGraph()

# Add nodes
graph.add_node("selection", selection_node)
graph.add_node("answering", answering_node)
graph.add_node("check", check_node)

# Add edges to define the flow between nodes
graph.add_edge("selection", "answering", condition=lambda state: state.query != "")
graph.add_edge("answering", "check", condition=lambda state: "Generated answer" in state.messages)

# Add conditional edges to handle different conditions, if necessary
graph.add_conditional_edges("check", "END", condition=lambda state: state.judgement_reason == "Valid")

# Function to process the graph
def process_graph(state: State):
    graph.set_entry_point("selection")
    while True:
        current_node = graph.get_current_node()
        if current_node == "END":
            break
        state = graph.run_node(current_node, state)
        graph.move_to_next_node(state)
    return state

# Initialize state
initial_state = State(
    query="What is the weather like?",
    current_role="user",
    messages=[],
    current_judge="approved",
    judgement_reason=""
)

# Process the graph
final_state = process_graph(initial_state)

# Display the final state
print(f"Final State: {final_state.judgement_reason}, {final_state.messages}")
