import re


def word_count(s):
    # Implement me.

    cache = {}
    s = s.replace("\r", " ").replace("\t", " ").replace("\n", " ")
    s = re.sub("[^0-9a-zA-Z' ]+", "", s)

    # if s == "":
    #     return cache

    for word in s.split(" "):

        if word == "":
            continue
        word = word.lower()

        if word in cache.keys():
            cache[word] += 1
        else:
            cache[word] = 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
