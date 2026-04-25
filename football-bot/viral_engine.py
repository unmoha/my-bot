import random

def score(text):
    text = text.lower()
    s = 0

    keywords = ["transfer", "deal", "signed", "official", "here we go", "agreement"]
    clubs = ["madrid", "barcelona", "man united", "chelsea", "psg", "city"]

    for k in keywords:
        if k in text:
            s += 3

    for c in clubs:
        if c in text:
            s += 4

    if "breaking" in text:
        s += 5

    return s


def format_post(title, summary, link):
    prefixes = ["🚨 BREAKING", "💣 HERE WE GO", "🔥 JUST IN", "⚡ UPDATE"]
    return f"""
{random.choice(prefixes)}

<b>{title}</b>

{summary[:200]}

🔗 {link}

#Football #Transfers
"""