def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    #stopword = ["a","an","the","and","is"]
    new_tokens = [word  for word in tokens if word not in stopwords]
    return new_tokens