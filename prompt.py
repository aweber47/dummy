from dummy.helper import count_tkns

def report_counts(token, file_path="corpus.txt"):
    count = count_tkns(token, file_path)
    return f"The term {token} shows up in the corpus {count} times."