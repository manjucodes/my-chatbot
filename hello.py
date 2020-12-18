from flask import Flask
from chatterbot import ChatBot
from flask import  render_template, request
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from PyDictionary import PyDictionary
import time
import json
import requests

app = Flask(__name__)


from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    'Terminal'
)

trainer = ChatterBotCorpusTrainer(bot)
dictionary=PyDictionary()

trainer.train(
    "chatterbot.corpus.english"
)

trainer = ListTrainer(bot)
trainer.train(
['bye',
'bye have a great day'
]
)












@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    try:
     user_input = request.args.get('msg')

     if 'meaning' in user_input.split() or 'meant' in user_input:
                  k=user_input.split()
            
                  s=dictionary.meaning(k[len(k)-1])
               
                  a="wait..let me see"
                  time.sleep(4)
                  return str(s.get('Noun'))
       
     elif 'joke' in user_input:
              
         

             url = "https://joke3.p.rapidapi.com/v1/joke"

             headers = {
    'x-rapidapi-host': "joke3.p.rapidapi.com",
    'x-rapidapi-key': "58e1d41cbbmsh90556945dd73f72p193078jsnb1b6e734ac26"
             }

             response = requests.request("GET", url, headers=headers)
             d=response.json()
             print("here no problem")
             
             print("good")
             return str("here you go\n"+d['content'])
             print("here mark this")
             print(d[content])













     else:        
                  time.sleep(2)
                  return str(bot.get_response(user_input))
                 


       



       




    
    
    except(AttributeError):
            return str("bot:sorry i dont know")
    




























    









if __name__ == '__main__':
   app.run()