from mylib.nlp import summarize_wikipedia, get_phrases, search_wiki_pages
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def home():
    return {"Welcome!"}


@app.post("/summary")
def get_summary(name: str):
    summary = summarize_wikipedia(name)
    return {summary}


@app.post("/phrases")
def get_nouns(name: str):
    phrases = get_phrases(name)
    return phrases


@app.post("/pages")
def get_pages(page: str):
    pages = search_wiki_pages(page)
    return pages


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
