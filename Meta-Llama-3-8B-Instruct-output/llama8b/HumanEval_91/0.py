def is_bored(S):
    sentences = S.split('. ')
    sentences = [sentence.strip() for sentence in sentences if sentence]
    return sum(1 for sentence in sentences if sentence and sentence[0].lower() == 'i')