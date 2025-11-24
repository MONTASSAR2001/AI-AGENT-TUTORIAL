from langchain_core.tools import Tool
from utils import search_google, wiki_search, save_to_file

search_tool = Tool(
    name="google_search",
    func=search_google,
    description="Search Google and return results"
)

wiki_tool = Tool(
    name="wikipedia_search",
    func=wiki_search,
    description="Search Wikipedia"
)

save_tool = Tool(
    name="save_to_txt",
    func=save_to_file,
    description="Save results to a text file"
)

# Add all tools here
ALL_TOOLS = [search_tool, wiki_tool, save_tool]
