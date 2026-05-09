from typing import List, Optional, Annotated, TypedDict
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:0.5b", temperature=0.7)

# Define the Movie schema
class Movie(TypedDict):
    title: Annotated[str, "The title of the movie"]
    release_year: Annotated[int, "Year the movie was released"]
    genres: Annotated[List[str], "List of genres the movie belongs to"]
    rating: Annotated[float, "Average rating of the movie on scale 1 to 10"]
    box_office: Annotated[Optional[float], "Worldwide box office in millions USD if known"]

# Get structured output
prompt = "Details of the movie Inception"
structured_llm = llm.with_structured_output(Movie)
response = structured_llm.invoke(prompt)

print("Structured Output:")
print(response)
print(f"Type: {type(response)}")

# Get unstructured output for comparison
ans = llm.invoke(prompt)
print("\nUnstructured Output:")
print(ans.content)
print(f"Type: {type(ans)}")