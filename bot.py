import telegram
import json
import time
import requests
import random
from tkinter import *

#pega as frases do arquivo
file = open("file.txt", 'r')
#separa as frases em um array, que se divide a cada quebra de linha
messages = file.read().split('\n')


class bot(object):

    def __init__(self, token, chatId):
        
        self.token = token
        self.chatId = chatId
        self.bot = telegram.Bot(token=self.token)

    def sendmessage(self, message):
        #TROCAR AQUI
        self.bot.send_message(self.chatId, message)
        print("Mensagem enviada: %s"%(message))
        print("Horário: %i:%i"%(time_verifying()[3], time_verifying()[4]))

def main():
    backend(input("\nDigite o token do seu bot: "), input("\nDigite o nome do grupo: "))
    
def backend(token, group_name):
    print("\nO script irá iniciar automaticamente às 06:00\n")
    Bot = bot(token, take_group_id(group_name, token))
    print("\nAguardando horário de postagem...\n")
    #contagem de mensagens enviadas por hora
    sent_messages = 6
    #loop para o envio de mensagens
    while(len(messages) > 0):

        info_time = time_verifying()
        if(info_time[3] >= 6 and info_time[3] <= 22):
            if(sent_messages > 0):
                Bot.sendmessage(take_a_message())
                time.sleep(50)
            else:
                if(info_time[4] == 0):
                    sent_messages = 6
                time.sleep(1)
        else:
            time.sleep(1)
            pass

#Verifica as mensagens enviadas e pega o id do grupo desejado pelo nome 
def take_group_id(group_name, token):
    
    url = "https://api.telegram.org/bot%s/getUpdates"%(token)
    with requests.get(url) as url:
        response = json.loads(url.text)
        for i in response['result']:
            if("title" in i['message']['chat']):

                if(i['message']['chat']['title'].lower() == group_name):
                    return i['message']['chat']['id']
            else:
                pass

#pega uma mensagem do array de mensagens definido no início do script e remove a mensagem para que não seja repetida
def take_a_message():
    
    try:
        message = messages[random.randint(0, len(messages)-1)]
        messages.remove(message)
        return message
    except ValueError:
        print("Valor não encontrado")

def time_verifying():

    date = time.localtime()
    if(date[2] == 3 and date[3] == 22 and date[4] >= 0):
        print("Final do período de postagem.")
        exit()
    else:
        return date



if __name__ == "__main__":
    main()