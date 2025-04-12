## Quality assurance using langgraph flow. <br/> <br/> 

Key Elements:<br/> 

State Class: Holds the relevant state information (query, current_role, messages).<br/> 

Node Functions: Each function (selection_node, answering_node, check_node) modifies the state as per the flow.<br/> 

LangGraph: The main graph object where nodes and transitions are defined.<br/> 

Processing: The process_graph function runs the nodes in the graph sequentially, updating the state and moving between nodes.

## Conversation between LLMs using langgraph flow. <br/> <br/> 

Key Elements:<br/> 

State Class:<br/> 

messages: A list that holds the conversation messages exchanged between LLMs (A and B).<br/> 

current_response: Stores the response generated by the current LLM in the conversation.<br/> 

LLM Nodes:<br/> 

llm_a_node: LLM A processes the conversation state and generates a response, which is added to the messages list.<br/> 

llm_b_node: LLM B works similarly, generating a response based on the messages and appending it to the messages list.<br/> 

Graph:<br/> 

The graph starts at the _start_ node, where LLM A generates a response. Then, it passes the flow to LLM B, which generates a response, and the flow returns to LLM A.

Finally, the flow reaches the _end_ node, which terminates the conversation.<br/> 

LLM Integration:<br/> 

The ChatOpenAI class is used to interact with the LLMs (GPT-4o mini in this case). Each LLM processes the state, generates a response, and the conversation continues until the _end_ node is reached.<br/> 

Key Points:<br/> 
LLM Interaction: This code simulates a conversation between two LLMs (LLM A and LLM B), where each LLM generates responses and exchanges messages.<br/> 

State Management: The State class keeps track of the conversation and the current responses.<br/> 

Graph Structure: The flow of the conversation is controlled by the graph structure, with edges defining how the nodes (LLMs) interact with each other.
