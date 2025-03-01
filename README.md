## **Setting Up Your Discord Bot**


## **Create a Discord Developer Account**

Go to: https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications

Log in and create a new application 


## **Create Your Bot User**

Inside the application page, navigate to the bot section. Click on Add Bot. 

After the bot is created you'll get a Token. KEEP THIS PRIVATE. Needed to run the bot so don't lose it either. 


## **Set Up Your Development Environment**

For this project you'll need python and some libraries installed. 

```bash
pip install discord google-api-python-client
```

Clone or donwload this repository that contains the bot code. You can name it whatever you want Buzz Alterin just tickled my fancy. 


## **Replace Necessary Info**

In the bot code there are two things you need to change

1) YOUTUBE_API_KEY: You'll need to either remove this or include your own youtube api key if you want the bot to link users to cool videos.
2) TOKEN: Replace this with the aforementiond Discord bot token.

For the youtube: Go to Google Cloud Console, create a new project, and enable YouTube Data API v3 for that project. 
https://console.cloud.google.com/welcome/new?hl=en-au&project=valiant-index-451019-u0


## **Invite the bot to your server**

1) Go to the OAuth2 page on the Discord Developer Portal
2) Under the OAuth2 URL Generator, check boxes bot and applications.commands. Also enable send messages, read messages, manage messages, whatever.
3) Copy generated URL and paste it into your browser to invite your bot to the party.

```bash
python3 bot.py
```

If the above was successful your bot will be online. If not, I am very sorry for there will be much pain and suffering in the way of debugging. My condolences for I have suffered through it as well in this project. 

## **Markov Chain**

The unique aspect of this project is using a Markov Chain as opposed to a lucid, normal, uninteresting conversational agent. A Markov Chain will include messages mix-mashed from user messages in your server, providing ludicrous, highly entertaining outputs. 
The more people message, the more info the bot "drinks up" and can use for his own messages. Surprisingly fun and always revitalizes an otherwise moribund chat. 

```bash
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
```

The above code will use a Markov chain for message creation. The code in this github also will limit the bot so he only messages if you include his name (which is buzz in this case)
That way he doesn't message every single time you message. 

## **Test your Bot**
For the lucky ones who made it work first try, test with various commands: 
!ping : should respond with Pong!

space fact : the bot will send a space fact

launch fact: the bot will send a launch fact 

!kurzegsagt : should provide a link to the latest kurz video. 

!3blue1Brown: Should link you to the latest video of the creator. 

And that's a wrap. Breathe some life back into your dead servers with your Markov-based comrade-in-text! 


## **For Further Research**

Markov Chain: https://www.geeksforgeeks.org/markov-chain/

Creating a Bot Account: https://discordpy.readthedocs.io/en/stable/discord.html

