import discord
from discord.ext import commands
import random
import re
from collections import defaultdict
from googleapiclient.discovery import build

# Intents give your bot the ability to access certain events
intents = discord.Intents.all()

# Create a bot instance with the specified command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize global variables
space_fact_index = 0
launch_fact_index = 0

# List of space facts
space_facts = [
    "The Goldilocks zone is a misnomer! Tidally heated moons are more than capable of sustaining liquid water, as are super-Earth planets with hydrogen atmospheres in interstellar space. Hydrogen is a powerful greenhouse gas under extremely high pressures.",
    "Jupiter and Saturn have no clear surface! As the depth increases, so does the temperature and pressure. Eventually, the gassy outer layers of these gas giants give way to a substance known as metallic hydrogen: hydrogen compressed to the point that it acts as a metal instead of a gas. It is believed that a liquid metallic hydrogen dynamo is responsible for the magnetic fields of these graceful giants.",
    "Saturn has a density of less than water (at STP)! It is the only body in our solar system for which this is the case.",
    "The temperature of Venus is higher than that of Mercury, despite Mercury being much closer to the sun. This is because Venus nearly 100 times the atmospheric pressure of Earth, and it is nearly all carbon dioxide.",
    "Venus has a higher concentration of deuterium in its atmospheric hydrogen than Earth does! This is because solar wind is more likely to strip away lighter hydrogen isotopes than heavier ones."
]

launch_facts = [
    "The Falcon 9 is a workhorse rocket made by SpaceX and is capable of carrying both crew and cargo into space. (Known for its reusability.)",
    "Starship, made by SpaceX, is a fully reusable spacecraft currently under development. Once finished, it will have a capacity to carry up to 100 people.",
    "Raptor Engines, used in the Starship project, use a mixture of liquid methane and oxygen. This makes them suited for long-term missions.",
    "Starlink is composed of over 4,000 satellites in low Earth orbit, making it the largest satellite constellation in history."
]

# YouTube API setup
YOUTUBE_API_KEY =   # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# YouTube channel IDs
CHANNEL_IDS = {
    'kurzgesagt': 'UCsXVk37bltHxD1rDPwtNM8Q',  # Kurzgesagt channel ID
    '3blue1brown': 'UCYO_jab_esuFRV4b17AJtAw'  # 3Blue1Brown channel ID
}

def get_videos(channel_id, max_results=5):
    """
    Fetch a list of video URLs from a YouTube channel.
    """
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=max_results,
        order='date',
        type='video'
    )
    response = request.execute()
    videos = []
    for item in response.get('items', []):
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        videos.append(video_url)
    return videos

# Markov chain data structure
markov_chain = defaultdict(list)

def build_markov_chain(text, state_size=2):
    """
    Build a Markov chain model from a text corpus.
    """
    words = text.split()
    for i in range(len(words) - state_size):
        current_state = tuple(words[i:i + state_size])
        next_word = words[i + state_size]
        markov_chain[current_state].append(next_word)

def generate_text(start_state, length=20):
    """
    Generate text using the Markov chain model.
    """
    current_state = start_state
    result = list(current_state)
    for _ in range(length - len(current_state)):
        if current_state not in markov_chain:
            break
        next_word = random.choice(markov_chain[current_state])
        result.append(next_word)
        current_state = tuple(result[-len(current_state):])
    
    return ' '.join(result)

def remove_forbidden_word(text, forbidden_word="buzz"):
    """
    Remove any occurrence of the forbidden word from the text.
    """
    return re.sub(r'\b' + re.escape(forbidden_word) + r'\b', '', text, flags=re.IGNORECASE)

def safe_generate_text(start_state, length=20):
    """
    Generate text and remove any occurrence of the forbidden word.
    """
    text = generate_text(start_state, length)
    return remove_forbidden_word(text)

@bot.event
async def on_ready():
    """
    Event handler for when the bot is ready.
    """
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    """
    Event handler for incoming messages.
    """
    global space_fact_index
    global launch_fact_index

    # Ignore messages from bots (including itself)
    if message.author.bot:
        return

    # Respond to "space fact" messages
    if message.content.lower() == "space fact":
        await message.channel.send(space_facts[space_fact_index])
        space_fact_index = (space_fact_index + 1) % len(space_facts)
        return

    # Respond to "launch fact" messages
    if message.content.lower() == "launch fact":
        await message.channel.send(launch_facts[launch_fact_index])
        launch_fact_index = (launch_fact_index + 1) % len(launch_facts)
        return

    # Handle "buzz" messages for Markov chain generation
    if "buzz" in message.content.lower() and message.author.id != #replace with your bot's ID:
        # Clean the content and build Markov chain
        clean_content = re.sub(r'<@!?(\d+)>', '', message.content)  # Remove mentions
        build_markov_chain(clean_content.lower())

        # Generate a response based on random number and state size
        rng = random.randint(1, 480)
        if rng <= 340:
            response = get_appended_output(message.guild.id, 2)
        elif rng <= 415:
            response = get_appended_output(message.guild.id, 3)
        elif rng <= 465:
            response = get_appended_output(message.guild.id, 4)
        else:
            response = get_appended_output(message.guild.id, 5)
        
        await message.channel.send(response)
        return

    # Process commands (like !ping)
    await bot.process_commands(message)

def get_appended_output(guild_id, state_size):
    """
    Generate Markov chain output based on state size.
    """
    # Randomly select a start state and generate text
    start_state = random.choice(list(markov_chain.keys()))
    return safe_generate_text(start_state, length=20)

 

# Add commands to list videos
@bot.command()
async def kurzgesagt_videos(ctx):
    """
    Command to fetch and list recent Kurzgesagt videos.
    """
    videos = get_videos(CHANNEL_IDS['kurzgesagt'], max_results=5)
    if videos:
        await ctx.send("Here are some recent Kurzgesagt videos:\n" + "\n".join(videos))
    else:
        await ctx.send("Couldn't fetch Kurzgesagt's videos. Please try again later.")

@bot.command()
async def threeblue1brown_videos(ctx):
    """
    Command to fetch and list recent 3Blue1Brown videos.
    """
    videos = get_videos(CHANNEL_IDS['3blue1brown'], max_results=5)
    if videos:
        await ctx.send("Here are some recent 3Blue1Brown videos:\n" + "\n".join(videos))
    else:
        await ctx.send("Couldn't fetch 3Blue1Brown's videos. Please try again later.")

# Command: Respond to !ping with 'Pong!'
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


TOKEN = #replace with your bot's token
bot.run(TOKEN)