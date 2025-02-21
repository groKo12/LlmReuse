import os, discord, asyncio
from dotenv import load_dotenv
from discord.ext import commands
from LlmAbstraction.groq import GroqModel
from llama_index.core.agent import ReActAgent

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
MODEL = os.getenv('MODEL')
TOKEN = os.getenv('DISCORD_KEY')
GUILD = os.getenv('DISCORD_SERVER')
CHANNEL1 = os.getenv('CHANNEL_ID')

# Set intents for discord
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Instantiate bot
bot = commands.Bot(intents=intents, command_prefix='!')
channel = bot.get_channel(CHANNEL1)

# Instantiate llm and Agent
Llm = GroqModel(api_key=GROQ_API_KEY, model=MODEL,temperature=1,max_tokens=0)
DiscAgent = ReActAgent(llm=Llm.get_model(), verbose=True, tools=[],memory=None)

# lmk when connected
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# ------------ Bot Commands ---------------
@bot.command(name="Hello!", help="Say Hello!")
async def greeting(ctx):
    response = "Hi!"
    await ctx.send(response)

@bot.command(name="Ask", help="Chat with an AI agent")
async def talk(ctx, *args):

    # Join user text into AI query
    talk_string = ' '.join(args)

    # Notify users of process
    await ctx.send("------ Agent Response ------")


    # Send question to Agent
    resp = str(DiscAgent.chat(talk_string))
    await ctx.send(resp)


# Run Bot
bot.run(TOKEN)