import feedparser
from utils import retry

async def fetch(url):
    return await retry(lambda: feedparser.parse(url))