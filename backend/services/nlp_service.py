# backend/services/nlp_service.py

import spacy

# Load SpaCy English model
nlp = spacy.load('en_core_web_sm')

def process_query(query):
    """
    Process the user query and extract keywords using SpaCy.
    
    Args:
        query (str): The user input query.
    
    Returns:
        List[str]: A list of extracted keywords.
    """
    doc = nlp(query.lower())
    keywords = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return keywords
