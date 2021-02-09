#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rnd
from itertools import combinations as com

#team = [Ppg, Pall, SD_ppg, SD_oppg, name, games won, conf(1=west, 2=east)]
lakers = [114.66, 107.17, 12,11.50, "lakers",0, 1]
clippers = [114.10, 104.7, 13.56,13.26, "clippers",0,1]
warriors = [112.96, 118.78, 12.37,12.51, "warriors", 0,1]
suns = [115.8, 108.93, 12.12,10.49, "suns",0, 1]
kings = [117.5,113.17,11.09,12.23,"kings",0,1]
thunder = [103.32,111.68, 11.69,10.95, "thunder", 0,1]
nuggets = [103.89, 104, 11.14,11.66, "nuggets",0,1]
timberwolves =[113.53, 118.71, 11.4,12.87, "timberwolves",0,1]
blazers = [116.93, 115.51, 11.25, 10.8, "blazers", 0,1]
jazz = [108.99, 100.86, 11.16, 11.84, "jazz",0,1]
spurs = [105.03, 108.94, 10.7, 10.94, "spurs",0,1]
mavericks = [115.23, 109.64,11.75,11.95,"mavericks",0,1]
rockets = [106.73, 107.47, 13.72,11.33, "rockets", 0, 1]
grizzlies = [111.26, 113.91, 11.37,13.73, "grizzlies",0,1]
pelicans = [112.4, 108.7, 10.91,11.54, "pelicans",0,1]

#east
bulls = [110.7, 115.24, 11.06,10.46, "bulls",0,2]
cavs = [106.16, 113.24, 10.10,12.75,"cavs", 0,2]
pistons = [102.76,110.48, 12.28,10.41,"pistons",0,2]
pacers =[110.13, 109.6, 10.29, 10.93, "pacers",0,2]
bucks = [116.37,107.6, 11.54, 13.03, "bucks", 0,2]
magic = [104.46, 110.91, 13.62,11.91, "magic",0,2]
heat = [109.56, 110.94, 12.11,10.87, "heat",0,2]
hawks = [118.63,117.48, 13.84, 13.94 ,"hawks",0,2]
hornets =[111.83, 115.24, 11.53, 12.43, "hornets",0,2]
wizards =[118.07, 120.08, 13.04, 14.24, "wizards",0,2]
knicks = [105.59, 114.58, 13.26, 13.68, "knicks",0,2]
nets = [119.20, 112.97, 12, 12.53, "nets", 0,2]
sixers = [107.86, 104.8, 11.57,11.7, "sixers",0,2]
celtics = [107.29, 105.5, 11.89,10.89, "celtics",0,2]
raptors = [108.43, 103.47, 12.59, 10.9, "raptors", 0,2]


teams = [lakers, clippers, warriors, suns, kings, thunder, nuggets, timberwolves, blazers, jazz, spurs, mavericks, rockets,
         grizzlies, pelicans,       bulls, cavs, pistons, pacers, bucks, magic, heat, hawks, hornets, wizards, knicks, nets,
        sixers, celtics, raptors]
games= list(com(teams,2))

num_teams = 30
# this is number of games if every teams played every other team just once (adjusted for repeats yields 1080 total games)
num_games = 435



def game(t1,t2):
    t1s =((rnd.gauss(t1[0],t1[2]) + rnd.gauss(t2[1],t2[3]))/2)
    t2s = ((rnd.gauss(t2[0],t2[2]) + rnd.gauss(t1[1], t1[3]))/2)
    if t1s > t2s:
        t1[5]= t1[5]+1
        
    else:
        t2[5]= t2[5]+1
            
    #print(t1[3],":",t1s,"  ",t2[3],":",t2s)
    #print("(", t1[4],")", "                         " , "(",t2[4],")" )


def season():
    x=0
    for i in range(num_games):

        t1= games[x][0]
        t2= games[x][1]
        
        if (t1[6] == t2[6]):
            game(t1,t2)
            game(t1,t2)
            game(t1,t2)
        else:
            game(t1,t2)
            game(t1,t2)
        
        x=x+1
    x=0
    for i in range(num_teams):
    
        #print( teams[x][4], "(", teams[x][5],"," , 4-teams[x][5], ")")
        x=x+1
        
        
        
#season()

   
# now lets iterate over multiple seasons


def mult_seasons(x):
    
    for i in range(x):
        season()
        x=0
        for i in range(num_teams):
    
            print( teams[x][4], "(", teams[x][5],"," , 72-teams[x][5], ")")
            x=x+1
        
        #this starts the season from the begining
        p=0
        for i in range(num_teams):
            teams[p][5]=0
            p=p+1
    print('\n') 
    

#mult_seasons(5)

def avg_mult_seasons(s):
    
    
    for i in range(s):
        season()
        
    r=0
    #iterates over the number of teams
    for i in range(num_teams):
        print(teams[r][4],"(" ,round((teams[r][5])/s,0),",",round(72-(teams[r][5]/s),0)  ,")")
        r = r+1
        
avg_mult_seasons(1000)


        


    
    


        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




