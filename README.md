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

## **Test your Bot**
For the lucky ones who made it work first try, test with various commands: 
!ping : should respond with Pong!

space fact : the bot will send a space fact

launch fact: the bot will send a launch fact 

!kurzegsagt : should provide a link to the latest kurz video. 

!3blue1Brown: Should link you to the latest video of the creator. 

And that's a wrap. Enjoy playing with your bot! 
