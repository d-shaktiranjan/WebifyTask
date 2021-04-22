from home.models import AllTask
from random import randint


def checkSlug(word):
    status = AllTask.objects.filter(slug=word)
    return bool(status)


def formatWord(word):
    new = word.replace(" ", "")
    chars = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    final = ""
    for char in new:
        if char not in chars:
            final += char
    return final


def getSlug(name, about):
    slug = formatWord(name) + formatWord(about)
    return newSlug(slug)


def newSlug(word):
    if checkSlug(word):
        word += str(randint(0, 100))
        if checkSlug(word):
            return newSlug(word)
    return word
