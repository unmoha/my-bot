import asyncio
from telethon import TelegramClient
from config import BOT_TOKEN, API_ID, API_HASH, CHANNEL_ID, RSS_FEEDS
from rss_fetcher import fetch
from processor import process
from poster import post

client = TelegramClient("bot", API_ID, API_HASH)

async def run():
    await client.start(bot_token=BOT_TOKEN)

    while True:
        for url in RSS_FEEDS:
            feed = await fetch(url)

            for entry in feed.entries[:5]:
                title = entry.get("title", "")
                summary = entry.get("summary", "")
                link = entry.get("link", "")

                msg = process(title, summary, link)

                if msg:
                    await post(client, CHANNEL_ID, msg)

        await asyncio.sleep(600)

asyncio.run(run())