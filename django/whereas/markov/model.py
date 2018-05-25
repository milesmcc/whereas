import random
import nltk

def build_model(sentences):
    words = {}
    for sentence in sentences:
        sentence = sentence.replace("(", "").replace(")", "")
        grams = nltk.word_tokenize(sentence)
        i = 0
        while i < len(grams):
            word = grams[i].lower()
            if word not in words:
                words[word] = {
                    "children": []
                }
            if i < len(grams) - 2:
                words[word]["children"].append(grams[i+1].lower())
            else:
                words[word]["children"].append("[end]")
            i += 1
    return words

def generate_sentence(model, stem):
    if stem not in model:
        raise ValueError("the given stem `%s` does not exist in the model" % stem)
    chain = [stem.lower()]
    limit = 64
    i = 0
    while i < limit:
        candidates = model[chain[i]]["children"]
        if len(candidates) == 0:
            break
        choice = random.choice(candidates)
        if choice == "[end]":
            break
        chain.append(choice)
        i += 1
    return chain

def compose(words):
    sentence = ' '.join(words)
    sentence = sentence.replace(" ,", ",").replace(" .", ".").replace(" :", ":").replace(" ;", ";").replace(" '", " ")
    if sentence[-1] != ';':
        sentence = sentence + ";"
    return sentence.upper()
