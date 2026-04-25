from utils import hash_text
from duplicate_store import exists, add
from viral_engine import score, format_post
from ai_rewriter import rewrite

def process(title, summary, link):

    h = hash_text(title, summary)

    if exists(h):
        return None

    s = score(title + summary)

    if s < 5:
        return None

    add(h)

    text = rewrite(title, summary)

    message = format_post(text, summary, link)

    return message