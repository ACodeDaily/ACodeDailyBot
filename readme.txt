The bot when completely functional should perform the following operations 

1. Accept input for posting doubts on cp-doubts channel from 
    a. codeforces 
    b. codechef
    c. cses

2. Suggest the best problems [based on individuals profile], specially picked for you from 
    a. codeforces
    b. cses
3. Make you a softdrink as and when you require (Lol just kidding)
4. Check if the doubt has already been posted earlier if so then return the id of that post, or state when it was raised before [Date..]
    #open problem-give the solution to the user! 


Issues to be fixed. 
    1. async operations
    2. timeout for same user (5 mins at max) [specify in the message]       -- alert while timing out! 
PS- please help to add more feaures to this bot!
Happy coding!





--------------------------------------------------
Tasks for Abhay PSC:

1. rename scraping.py and make it apt -> I wanna see separation of concerns. 
        -> maybe make 2 files?    [System design!]
2. edit the scraping.py to include cses. 

gimme problemName,gimmeProblemRating,ProblemTags.

--------------------------------------------------

cses: 
use cses-analyser backend for ratings, [also check if it can be used for tag]