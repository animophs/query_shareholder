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
    sendData = ''
    for tabledata in soup.find_all('tr'):
        if tabledata.get('data-code') == maCK:
            for rowdata in tabledata.find_all('td'):
                if rowdata.get('data-property') =='priorClosePrice':
                    sendData += '\r\nTham chieu: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='dealPrice':
                    sendData += '\r\nKhop lenh: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='dealVolume':
                    sendData += ' --- So luong: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='best1Bid':
                    sendData += '\r\nGia mua cao nhat: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='best1BidVolume':
                    sendData += ' --- So luong: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='best1Offer':
                    sendData += '\r\nGia ban thap nhat: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='best1OfferVolume':
                    sendData += ' --- So luong: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='highest':
                    sendData += '\r\nGia cao nhat: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='lowest':
                    sendData += '\r\nGia thap nhat: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='lowest':
                    sendData += '\r\nGia thap nhat: ' + rowdata.contents[0].strip()
                elif rowdata.get('data-property') =='totalShare':
                    sendData += '\r\nTotal Volume: ' + rowdata.contents[0].strip()
            print(sendData)
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
    
    
