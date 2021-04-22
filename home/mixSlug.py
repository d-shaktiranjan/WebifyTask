from home.models import AllTask


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
    return slug
