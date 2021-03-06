def generate_hashtag(s: str) -> str:
    """
    >>> generate_hashtag("Python Is Nice")
    '#PythonIsNice'
    >>> generate_hashtag("c i u")
    '#CIU'
    >>> generate_hashtag("python is  nice")
    '#PythonIsNice'
    """
    if s == "":
        return False
    if len(s) > 140:
        return False
    res = "#"
    for i in s.split():
        res = res + i.capitalize()
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    sen = input("Enter the sentence: ")
    print(generate_hashtag(sen))
