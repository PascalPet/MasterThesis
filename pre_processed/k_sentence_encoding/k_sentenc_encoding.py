import nltk


def split_text_into_sentences(text):
    # Download the required tokenizer data
    nltk.download('punkt')

    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    return sentences


# Example usage
text = "Hello my name is olaf. I like you."
sentences = split_text_into_sentences(text)
print(sentences)