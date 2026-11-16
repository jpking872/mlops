from textblob import TextBlob
import wikipedia
import click
import nltk

nltk.download('brown')
nltk.download('punkt_tab')

@click.group()
def cli():
    pass

def search_wikipedia(name):
    """ Search Wikipedia """
    print(f"Searching Wikipedia for {name}...")
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """ Summarize Wikipedia """
    print(f"Summarizing Wikipedia for {name}...")
    summary = wikipedia.summary(name)
    return summary

def get_text_blob(text):
    """ Get TextBlob """
    print(f"Getting TextBlob for {text}...")
    blob = TextBlob(text)
    return blob

#@cli.command('search')
#@click.argument('name', type=str)
def get_phrases(name):
    """ Get phrases from TextBlob """
    print(f"Getting phrases from TextBlob for {name}...")
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    print(f"Phrases: {phrases}")

    return phrases  

def search_wiki_pages(page):
    return wikipedia.search(page)

if __name__ == "__main__":
    cli()

# get all the player names for the given team   

