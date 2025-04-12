## Quality assurance using langgraph flow. <br/> <br/> 

Key Elements:<br/> 

State Class: Holds the relevant state information (query, current_role, messages).<br/> 

Node Functions: Each function (selection_node, answering_node, check_node) modifies the state as per the flow.<br/> 

LangGraph: The main graph object where nodes and transitions are defined.<br/> 

Processing: The process_graph function runs the nodes in the graph sequentially, updating the state and moving between nodes.
