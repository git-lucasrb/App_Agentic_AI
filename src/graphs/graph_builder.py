from langgraph.graph import StateGraph,START,END
from src.llms.google_llm import GeminiLLM
from src.states.blogstate import BlogState

class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate blog posts based on topic
        """

        ##Nodes
        self.graph.add_node("tile_creation",)
        self.graph.add_node("content_generation")

        ##Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation",END)