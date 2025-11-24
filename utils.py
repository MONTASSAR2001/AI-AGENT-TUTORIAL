import wikipedia
from googlesearch import search

def search_google(query):
    """Searches Google and returns top 5 results with titles and descriptions."""
    print(f"🔎 Searching Google for: {query}...")
    results = []
    try:
        # advanced=True returns objects with title, description, and url
        for j in search(query, num_results=5, advanced=True):
            results.append(f"Title: {j.title}\nDescription: {j.description}\nURL: {j.url}")
        return "\n\n".join(results)
    except Exception as e:
        return f"Error performing Google search: {e}"

def wiki_search(query):
    """Searches Wikipedia and returns a summary."""
    print(f"📚 Searching Wikipedia for: {query}...")
    try:
        return wikipedia.summary(query, sentences=4)
    except Exception as e:
        return f"Error searching Wikipedia: {e}"

def save_to_file(content):
    """Appends the content to a text file named research.txt."""
    filename = "research.txt"
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n" + "="*50 + "\n")
        return f"✅ Content successfully saved to {filename}"
    except Exception as e:
        return f"Error saving file: {e}"
