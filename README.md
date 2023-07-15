# discordbot-chatgpt
A simple Discord Bot in Python interacting with ChatGPT API

# Setup

Modify the config.json with the following instruction.

## OpenAI
Visit OpenAI [keys settings](https://platform.openai.com/account/api-keys) and follow the steps to create your API key. Remember to save your keys.

Next add your [organization id](https://platform.openai.com/account/org-settings).

## Discord


Login to Discord through the web browser.

Open “Developer Tools” and look in the Networks tab.

Reload the page and look through the requests.

Filter by /api

In the headers look for Authorization. That is your token. Do not share it.

To get a Channel ID right click the channel and click on "Copy Link". The id is the last number after ../channels/

## GPT Model

Refere to [this documentation](https://platform.openai.com/docs/models) on which model is best for you. Default in the configuration is set to text-davinci-003.


# How to Run

pip3 install -r requirements.txt
python3 main.py

In the discord channel type /chatgpt to ask ChatGPT questions.