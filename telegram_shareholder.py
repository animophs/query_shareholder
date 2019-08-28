import time
import datetime
import os
from requests import get
import telepot
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
from bs4 import BeautifulSoup

idChat = 508772608
bot = telepot.Bot('589913446:AAFCMZ2FfNQrvwqIf8v9GZe3tWrbq-lb5Pg')
mybot = bot.getMe()
print (mybot['username'])
bot.sendMessage (idChat, str("Hi! ThanhNK, I'm starting up ! "))
    
def handle(msg):
    global idChat
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message
    idChat = chat_id
    print ('Received:')
    print('Command: ', command, '--- chat_id: ', chat_id)
    if idChat == 508772608:
        if command == 'Hi':
            bot.sendMessage (chat_id, str("Hi! ThanhNK: "))
            checkIp()
        else:
            listData = command.split(' ')
            if listData[0] == 'MCK':
                checkValueShareHolder(listData[1])
        
def checkIp():
    global idChat
    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))
    if idChat == 508772608:
        bot.sendMessage (idChat, ip)

def checkValueShareHolder(maCK):
    page = get('https://www.hsx.vn/Modules/Rsde/RealtimeTable/LoadStock?indexValue=&requestEtfData=false&requestCWData=false').text
    soup = BeautifulSoup(page, 'html.parser')
    sendData = 'Khop lenh: '
    for tabledata in soup.find_all('tr'):
        if tabledata.get('data-code') == maCK:
            # soup_blockval = BeautifulSoup(tabledata, 'html.parser')
            # print(soup_blockval)
            for rowdata in tabledata.find_all('td'):
                if rowdata.get('data-property') =='dealPrice':
                    sendData += rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='dealVolume':
                    sendData += '\r\nSo luong: ' + rowdata.contents[0].strip()
            if idChat == 508772608:
                bot.sendMessage (idChat, sendData)

            #print(data.get('data-id'))
            #print(soup.tr)
        
def main():
    print ('I am listening...')
    MessageLoop(bot, handle).run_as_thread()
    while 1:
        time.sleep(10)

if __name__ == "__main__":
    main()
    
    
