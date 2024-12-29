import re

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        char_counts = get_char_counts(file_contents)
        sorted = sort_dict(char_counts)
        for i in sorted:
            print(f"The '{i["name"]}' character was found {i["num"]} times.")

def get_word_count(text):
    return len(re.split(r'[\s]+', text))

def get_char_counts(text):
    char_counts = {}
    text_lowercase = text.lower()

    for i in text_lowercase:
        if i in char_counts:
            char_counts[i] += 1
        else:
            char_counts[i] = 1
        
    return char_counts


def sort_dict(dict):
    count_list = []
    sort_on = lambda d: d["num"]
    for i in dict:
        if i.isalpha():
            count_list.append({"name": i, "num": dict[i]})
    
    count_list.sort(reverse=True, key=sort_on)
    return count_list

main()