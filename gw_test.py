from discordapi.gateway import DiscordGateway
import logging

logger = logging.getLogger("NicoBot")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

ch.setFormatter(
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
)

logger.addHandler(ch)

with open("token") as f:
    client = DiscordGateway(f.read())

client.connect()

try:
    for event, data in client.event_handler.event_generator():
        print(event)
        if event == "MESSAGE_CREATE":
            message = data
            author = message.author
            try:
                nick = message.member.nick
            except:
                nick = None
            print(f"{author.username}#{author.discriminator}({nick}): {message.content}")
finally:
    client.disconnect()
