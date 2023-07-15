import discord
import openai
import json

DISCORD_MAX_LEN = 2000

class PythonbotChatgpt(discord.Client):
    def __init__(self, config_file):
        super().__init__()
        self.config = self.load_config(config_file)
        self.openai_organization = self.config.get("openai-organization-id")
        self.openai_api_key = self.config.get("openai-api-key")
        self.openai_engine = self.config.get("openai_engine")
        self.discord_token = self.config.get("discord-auth-token")
        self.channel_id = self.config.get("discord-channel-id")

    def load_config(self, config_file):
        with open(config_file, "r") as f:
            return json.load(f)

    async def on_ready(self):
        print('You are now logged in:', self.user)

    async def on_message(self, message):
        print(str(message.channel.id))
        print(self.channel_id)
        print(str(message.channel.id) == self.channel_id)
        if str(message.channel.id) == self.channel_id:
            print(message.content.startswith("/chatgpt "))
            if message.content.startswith("/chatgpt "):
                msg = message.content.replace("/chatgpt ", "").strip()

                response = self.generate_chat_response(msg)

                if response is None:
                    await message.channel.send("ChatGPT is currently unavailable. Please try again later.")
                else:
                    for chunk in self.split_message_chunks(response):
                        await message.channel.send(chunk)

    def generate_chat_response(self, message):
        try:
            openai.api_key = self.openai_api_key
            openai.organization = self.openai_organization

            response = openai.Completion.create(
                engine=self.openai_engine,
                prompt=message,
                temperature=0.5,
                max_tokens=2000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )

            return response.choices[0].text.strip()
        except Exception as e:
            print("An error occurred while interacting with ChatGPT:", str(e))
            return None

    def split_message_chunks(self, message):
        chunks = [message[i:i+DISCORD_MAX_LEN] for i in range(0, len(message), DISCORD_MAX_LEN)]
        return chunks

config_file = "config.json"
bot = PythonbotChatgpt(config_file)
bot.run(bot.discord_token)
