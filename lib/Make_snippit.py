def make_snippet(text):
    words = text.split()
    if len(words) <= 5:
        return ' '.join(words)
    else:
        return ' '.join(words[:5]) + ' ...'