async def post(client, channel, message):
    try:
        await client.send_message(channel, message, parse_mode="html")
        return True
    except Exception as e:
        print("Post error:", e)
        return False