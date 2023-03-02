import srsly
import spacy
import random
import string
model = spacy.load("./training/model-best/")  # type: ignore

# Inferencing
for i in range(500):
    random_strings = []
    for j in range(1,i%5+2):
        random_string=''.join(random.Random(i*10+j).choices(string.ascii_lowercase, k=5))
        random_strings.append(random_string)
    test_data=' '.join(random_strings)

    doc: spacy.tokens.doc.Doc = model(test_data)
    result_dictionary = {}
    for ent in doc.ents:
        result_dictionary[str(ent.label_)] = str(ent)

    print(test_data)
    print(result_dictionary)
