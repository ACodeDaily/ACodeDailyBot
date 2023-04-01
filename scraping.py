import requests
from bs4 import BeautifulSoup
import discord
import os
intents = discord.Intents.default()  
intents.message_content = True
client = discord.Client(intents=intents)


CHANNEL_ID=1082254805591928872        #THIS IS THE CHANNEL ID FOR CP-DOUBTS   
TOKEN=os.getenv('TOKEN')               # don't share this live. 

#the bot right now can't handle multiple requests simultaneously! --> need to use asynchronisations properly.. what a SHIT code this is. 

def getPageAndPreprocess(URL):          # returns the name, tag and difficulty 
    ProblemName="IDK"       # this would mever happen unless you messed up big time!
    problemDifficulty="IDK" #this can happen. 
    problemTags=[]          
    page=requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    ProblemName=soup.find("div",class_="title").contents[0][2:]
    scraped_tags=soup.find_all("span",class_="tag-box")
    for pt in scraped_tags:
        name=pt.contents[0].lstrip().rstrip()
        if(name[0]=='*'):
            problemDifficulty=name[1:]
        else: 
            problemTags.append(name)
    return ProblemName,problemTags,problemDifficulty


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


async def post_doubt_on_channel(problem,tags,difficulty,doubt,url,userId):
    channel=client.get_channel(CHANNEL_ID)
    doubt=url+'' +' asked by : '+' <@'+str(userId)+'> \n issue faced: '+doubt
    await channel.create_thread(name=f'[Codeforces][{difficulty}][{problem}]{tags}',content=doubt)


def isNotCodeforcesUrl(url):
    return ((not url.startswith('https://codeforces.com/')) and (not url.startswith('http://codeforces.com/')) and (not url.startswith('https://www.codeforces.com/')) and (not url.startswith('http://www.codeforces.com/')) and (not url.startswith('www.codeforces.com/')))


async def processContentAndPost(message,contents):      #'url issue'
    seperator=contents.find(' ')
    if(seperator==-1):
        await message.channel.send('Invalid Input - Please mention the url and then your doubt')
    else:
        url=contents[:seperator]
        if(isNotCodeforcesUrl(url)):
           await message.channel.send('bruhhh the admin was busy so he could only do this for codeforces..... please wait for other platforms')
        else:           #the handle is valid and is a codeforces handle!    
            doubt=contents[seperator:]
            problemName,problemTags,problemDifficulty=getPageAndPreprocess(url)
            await message.channel.send(f'you entered: {url} \nproblem name: {problemName} \nproblem tags: {problemTags} \nproblem difficulty: {problemDifficulty} \nyour doubt: {doubt}')
            await post_doubt_on_channel(problemName,problemTags,problemDifficulty,doubt,url,message.author.id)    

@client.event
async def on_message(message):          #
    if message.author == client.user:   #if I client is the author. 
        return
    if message.content.startswith('`~postDoubt`') or message.content.startswith('~postdoubt'):
        await message.channel.send('Enter the URL followed by the doubt you\'re having:')
        def check(m):
            return m.author == message.author and m.channel == message.channel
        recd = await client.wait_for('message', check=check)
        contents = recd.content
        await processContentAndPost(message=message,contents=contents)      #not a good prac, explained...
client.run(TOKEN)





