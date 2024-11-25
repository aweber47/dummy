def count_tkns(token, file_path="corpus.txt"):
    with open(file_path, "r") as file:
        text = file.read()
    return text.lower().split().count(token.lower())
