import nltk
from nltk import pos_tag, word_tokenize

# Ensure all required NLTK resources are available (new NLTK versions)
REQUIRED_RESOURCES = [
    "punkt",
    "punkt_tab",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng"
]

for resource in REQUIRED_RESOURCES:
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(resource)

def extract_keywords(text: str):
    tokens = word_tokenize(text.lower())
    tagged = pos_tag(tokens, lang="eng")

    keywords = []
    for word, tag in tagged:
        if tag.startswith("NN") or tag.startswith("VB"):
            if len(word) > 2:
                keywords.append(word)

    return list(set(keywords))
