from telethon import TelegramClient, events, sync, utils
import time
from xml.etree.ElementTree import tostring
import  pywhatkit
import configparser
import pyautogui as pg
# from telethon import TelegramClient
# from telethon.sync import TelegramClient,events
# from telethon import TelegramClient, events, sync
from telethon import TelegramClient, events, sync, utils
import asyncio
import keyboard
import webbrowser
import os
flats={
    'Варламова 27А',
'Асем тау 1-100',
'Аскарова 21',
'Аскарова 21/1',
'Аскарова 21/2',
'Аскарова 21/3',
'Аскарова 21/4',
'Аскарова 21/5',
'Аскарова 21/6',
'Аскарова 21/7',
'Аскарова 21/8',
'Аскарова 21/9',
'Аскарова 21/10',
'Аскарова 21/11',
'Аскарова 21/12',
'Аскарова 21/13',
'Аскарова 21/14',
'Аскарова 21/15',
'Аскарова 21/16',
'Аскарова 21/17',
'Аскарова 21/20',
'Аскарова 21/20 к2',
'Алматы Астана 1/18',
'Алматы Астана 1/18 корп 1',
'Алматы Арайлы 2/12 БЛОК 1',
'Алматы Арайлы 2/12 БЛОК 2',
'Алматы Арайлы 2/12 БЛОК 3',
'Алматы Арайлы 2/12 БЛОК 4',
'Алматы Арайлы 2/12 БЛОК 5',
'Алматы Арайлы 2/12 БЛОК 6',
'Алматы Арайлы 2/12 БЛОК 7',
'Алматы Арайлы 2/12 БЛОК 8',
'Алматы Арайлы 2/12 БЛОК 9',
'Алматы Арайлы 2/12 БЛОК 10',
'Алматы Арайлы 2/12 БЛОК 11',
'Алматы Арайлы 2/12 БЛОК 12',
'Алматы Арайлы 2/12 БЛОК 13',
'Афцинао 4/1',
'Афцинао 4/2',
'Афцинао 4/3',
'Аксай 1 11\7',
'Аксай 1 11\9',
'Аксай 1 11\1',
'Аксай 4 119',
'Аксай 4 119а',
'Аксай 5 25',
'Аксай 5 25 ',
'Аксай 5 25 ',
'Аксай 5 3г',
'Аксай 5 3г ',
'Аксай 5 25 ',
'Аккент 50',
'Аккент 51',
'Аккент 52',
'Аккент 53',
'Аккент 54',
'Аккент 55',
'Аккент 56',
'Аккент 57',
'Аккент 58',
'Аккент 59',
'Аккент 60',
'Аккент 61',
'Аккент 62',
'Аккент 63',
'Аккент 64',
'Айнабулак-2 32/2.',
'Айнабулак 2 40а',
'Абая 150/230 блок 1',
'Абая 150/230 блок 2',
'Абая 150/230 блок 3',
'Абая 150/230 блок 4',
'Абая 150/230 блок 5',
'Абая 150/230 блок 6',
'Абая 150/230 блок 8',
'Абая 150/230 блок 9',
'Абая 150/230 блок 10',
'Абая 150/230 блок 11',
'Абая 150/230 блок 12',
'Ади Шарипова 145 к1',
'Ади Шарипова 145 к2',
'Ади Шарипова 145 к3',
'Ади Шарипова 145 к4',
'Ади Шарипова 145 к5',
'Брусиловского 163',
'Брусиловского 167',
'Брусиловского 159 блок 1',
'Брусиловского 159 блок 2',
'Брусиловского 159 блок 3',
'Брусиловского 159 блок 4',
'Брусиловского 159 блок 5',
'Брусиловского 159 блок 6',
'Бальзака 4а ',
'Барибаева 43',
'Барибаева 43\1',
'Барибаева 43\2',
'Барибаева 43\3',
'Барибаева 43\4',
'Барибаева 43\5',
'Барибаева 43\6',
'Барибаева 43\7',
'Барибаева 43\8',
'Барибаева 43\9',
'Бухар Жырау 35',
'Бокеева 1А',
'Бегалина 7',
'Байтурсынова 179 блок 1',
'Байтурсынова 179 блок 2',
'Байтурсынова 179 блок 3',
'Байтурсынова 179 блок 4',
'Байтурсынова 179 блок 5',
'Байтурсынова 179 блок 6',
'Богенбай батыра	23/3',
'Богенбай батыра	23а',
'Басенова 10блок1',
'Басенова 10блок2',
'Басенова 10блок3',
'Басенова 10блок4',
'Бокейханова 510Б',
'Володарского 40',
'Варламова 33',
'Варламова 1/3 блок А',
'Варламова 1/3 блок Б',
'Варламова 1/3 блок В',
'Варламова 27Д корпус 7',
'Варламова 27Д корпус 8',
'Гагарина 124',
'Гагарина 250',
'Гагарина 233/1',
'Гагарина 233/2',
'Гагарина 233/3',
'Гагарина 233к4',
'Гагарина 233к5',
'Достык 138 блок 1',
'Достык 138 блок 2А',
'Достык 138 блок 2Б',
'Достык 	69',
'Жарокова 284/1',
'Жарокова 284/3',
'Жетысу 1 17',
'Жетысу 1 51а',
'Жетысу 1 55а',
'Жетысу 3 69',
'Жетысу 3 71',
'Жангир хана 2 блок 1',
'Жангир хана 2 блок 2',
'Жангир хана 2 блок 3',
'Жангир хана 2 блок 4',
'Зенкова 59',
'Егор Редько 100',
'Егор Редько 100, корпус 1',
'Егор Редько 100, корпус 2',
'Егор Редько 100, корпус 3',
'Кенесары хана 54/19 к2',
'Кенесары хана 54/19 к1',
'Кенесары хана 54/44',
'Кенесары хана 54/43',
'Кенесары хана 54/45',
'Кенесары хана 54/42',
'Кенесары хана 54/41',
'Кенесары хана 54/41 к1',
'Кенесары хана 54/38',
'Кенесары хана 54/39',
'Кенесары хана 54/40',
'Кенесары хана 54/37',
'Кенесары хана 54/33',
'Кенесары хана 54/34',
'Кенесары хана 54/34 к1',
'Кенесары хана 54/35',
'Кенесары хана 54/36',
'Кенесары хана 54/36 к1',
'Кенесары хана 54/16',
'Кенесары хана 54/17',
'Кенесары хана 54/18',
'Кенесары хана 54/15',
'Кенесары хана 54/20',
'Кенесары хана 54/14 к1',
'Кенесары хана 54/14 к2',
'Кенесары хана 54/23',
'Кенесары хана 54/24',
'Кенесары хана 54/24 к1',
'Кенесары хана 54/25',
'Кенесары хана 54/26',
'Кенесары хана 54/27',
'Кенесары хана 54/28',
'Кенесары хана 54/29',
'Кенесары хана 54/30',
'Кенесары хана 54/21 ',
'Кенесары хана 54/21 к1',
'Кенесары хана 54/22',
'Кенесары хана 54/32',
'Кенесары хана 54/31',
'Кенесары хана 54/4',
'Кенесары хана 54/5',
'Кенесары хана 54/6',
'Кенесары хана 54/7',
'Кенесары хана 54/8 к1',
'Кенесары хана 54/8 к2',
'Кенесары хана 54/9',
'Кенесары хана 54/10',
'Кенесары хана 54/1',
'Кенесары хана 54/2',
'Кенесары хана 54/3 к1',
'Кенесары хана 54/3 к2',
'Кенесары хана 54/11',
'Кенесары хана 54/12',
'Кенесары хана 54/13',
'Катаева 218',
'Курмангазы 97',
'Кабанбай батыра 203',
'Коктем 3 24к1',
'Кокмайса 36/2 блок А',
'Кокмайса 36/2 блок Б',
'Кокмайса 57Б',
'Карасай батыра	40',
'Карасай батыра	326',
'Казахфильм 21д',
'Кунаева	15/1 блок 1',
'Кунаева	15/1 блок 2',
'Мусрепова -Бухар Жирау (Esentai Residence)	22',
'Макатаева 131к1',
'Макатаева 131к2',
'Макатаева 131к3',
'Макатаева 131к4',
'Макатаева 131к5',
'Макатаева 131к6',
'Макатаева 131к7',
'Макатаева 131к8',
'Макатаева 127/11, блок 1',
'Макатаева 127/11, блок 2',
'Масанчи 23\1',
'Масанчи 23\2',
'Масанчи 23\3',
'Масанчи 23\4',
'Масанчи 23\5',
'Масанчи 23\6',
'Масанчи 23\7',
'Масанчи 23\8',
'Масанчи 23\9',
'Масанчи 23\10',
'Масанчи 23\11',
'Муканова 241',
'мкр.8 41/6',
'мкр.6 36Б',
'мкр.12 26',
'мкр. Мирас 115,блок1',
'мкр. Мирас 115,блок2',
'мкр. Мирас 115,блок3',
'мкр. Мирас 115,блок4',
'мкр. Мирас 115,блок5',
'мкр. Мирас 115,блок6',
'мкр. Мирас 115,блок7',
'мкр. Мирас 115,блок8',
'мкр. Мирас 116,блок1',
'мкр. Мирас 116,блок2',
'мкр. Мирас 116,блок3',
'мкр. Мирас 116,блок4',
'мкр. Мирас 116,блок5',
'мкр. Мирас 116,блок6',
'мкр. Мирас 116,блок7',
'мкр. Мирас 116,блок8',
'мкр. Мирас 116,блок9',
'мкр. Мирас 116,блок10',
'Навои 7',
'Навои 37',
'Навои 58',
'Навои 62',
'Навои 60',
'Навои 66',
'Навои 70',
'Навои 68',
'Навои 74',
'Навои 72',
'Навои 68/1',
'Навои 68/2',
'Навои 208',
'Навои 208/1',
'Навои 208/2',
'Навои 208/3',
'Навои 208/4',
'Навои 208/5',
'Навои 208/6',
'Навои 208/7',
'Навои 208/8',
'Наурызбай батыра 50',
'Назарбаева 36',
'Назарбаева 34/3',
'Назарбаева 34/4',
'Прокофьева 89А',
'Розыбакиева 237',
'Розыбакиева 247 корпус 1',
'Розыбакиева 247 корпус 2',
'Розыбакиева 247 корпус 3',
'Розыбакиева 247 корпус 4',
'Розыбакиева 247 корпус 5',
'Розыбакиева 247 корпус 6',
'Розыбакиева 247 корпус 7',
'Розыбакиева 247 корпус 8',
'Райымбека 481в',
'Райымбека 590/1',
'Райымбека 590/1к1',
'Райымбека 590/1к2',
'Райымбека 590/1к3',
'Райымбека 590/1к4',
'Райымбека 590/1к5',
'Райымбека 590/1к6',
'Райымбека 590/1к7',
'Райымбека 590/2',
'Райымбека 590/2к1',
'Райымбека 590/2к2',
'Райымбек 522/1',
'Садвакасова 35',
'Сатпаева 7а',
'Сатпаева 145',
'Стрелецкая 1А',
'Стрелецкая 1Б',
'Сарыарка 1/1',
'Сарыарка 1/1к1',
'Сарыарка 1/2',
'Сарыарка 1/2к1',
'Сарыарка 1/2к2',
'Сарыарка 1/2к3',
'Санаторная 38/28 блок 1',
'Санаторная 38/28 блок 2',
'Санаторная 38/28 блок 3',
'Санаторная 38/28 блок 4',
'Санаторная 38/28 блок 5',
'Санаторная 38/28 блок 6',
'Санаторная 38/28 блок 7',
'Санаторная 38/28 блок 8',
'Санаторная 38/28 блок 9',
'Санаторная 38/28 блок 10',
'Санаторная 38/28 блок 11',
'Санаторная 38/28 блок 12',
'Санаторная 38/28 блок 13',
'Санаторная 38/28 блок 14',
'Санаторная 38/28 блок 15',
'Санаторная 38/28 блок 16',
'Санаторная 38/28 блок 17',
'Санаторная 38/28 блок 18',
'Санаторная 38/28 блок 19',
'Санаторная 38/28 блок 20',
'Санаторная 38/28 блок 21',
'Санаторная 38/28 блок 22',
'Санаторная 38/28 блок 23',
'Санаторная 38/28 блок 24',
'Северное кольцо шоссе	86/7',
'Северное кольцо шоссе	86/8',
'Северное кольцо шоссе	86/9',
'Северное кольцо шоссе	86/11',
'Северное кольцо шоссе	86/13',
'Северное кольцо шоссе	86/14',
'Северное кольцо шоссе	86/15',
'Сейфуллина 525',
'СТ Достык 69',
'Скрябина 259',
'Скрябина 259к1',
'Скрябина 28',
'Скрябина 28к1',
'Текелийская 1Б',
'Текелийская 1а',
'Таугуль	4А',
'Тлендиева 223',
'Толе Би 180б',
'Толе Би	286/1',
'Толе Би	286/3',
'Толе Би	286/5',
'Толе Би	286/6',
'Толе Би	286/8',
'Толе Би 189/3 блок 1-В',
'Толе Би 189/3 блок 1-А',
'Толе Би 189/3 блок 2',
'Толе Би 189/3 блок 3-А',
'Толе Би 189/3 блок 3-В',
'Толе Би 189/3 блок 4',
'Толе Би 189/3 блок 5',
'Толе Би 189/3 блок 6-В',
'Толе Би 189/3 блок 6-А',
'Тулебаева 49/1',
'Федосеева 38в корпус 1',
'Федосеева 38в корпус 2',
'Федосеева 38в корпус 3',
'Федосеева 38в корпус 4',
'Федосеева 38в корпус 5',
'Хусаинова 225',
'Ходжанова 77/5',
'Ходжанова 77/5 к1',
'Ходжанова 77/5 к2',
'Шевченко 85',
'Янушкевича 17',
'Ырысты 46/6',
'Ырысты 46/7',
'Ырысты 46/8',
'Ырысты 46/10',
'Илтипат 59г'


   }
config = configparser.ConfigParser()
config.read("config.ini")# Присваиваем значения внутренним переменным
api_id='24554034'
api_hash='0e45a65f58f18df2483f9c80647d5856'
username='TLAPI'

# async def main():
#     about_me = await client.get_entity('me')
#     print('Имя:', about_me.first_name)
#     print('Ник:', about_me.username)
#     print('Id', about_me.id)
#     print('Телефон', about_me.phone)

#+77717620115    
chat='Expert2DayAlmBot'

# with TelegramClient('Азамат', api_id, api_hash) as client:
#     for message in client.iter_messages(chat):
#         print('-----------------------------------------------------')
#         print('')
#         message_button = message.text
#         print(message_button)


client = TelegramClient(username, api_id, api_hash)

# @client.on(events.NewMessage(chats=chat))
# async def my_event_handler(event):
#     print('-----------------------------------------------------')
#     print('')
#     print(event.raw_text)
#     print('')
#     print('-----------------------------------------------------')

# client.start()

# client.run_until_disconnected()

whatsappText=[]
check=[]
result=[]
#---------------------------------------------------------------

tel='+77072446999'

print()
print('Начал работу')
print()
client.start()
wwr = client.get_entity(chat)
url = 'https://web.whatsapp.com'
webbrowser.open(url)
time.sleep(1)
client.send_message(wwr, 'А\nН')
time.sleep(3)
tel='+77072446999'
groupId='GO93vJw7bTFCZ4kRRVVM9G'

@client.on(events.NewMessage(chats=wwr))
async def handler(event):

    buttons = await event.get_buttons()
    #print('button len = ',len(buttons))
    for bline in buttons:
        for button in bline:
            # print(button.button.text)
            messag=button.button.text
            
            for item in flats:    #Проверка на наличии во флэтс адресов
                    if item in messag :     #Проверка на совпадение из button и флэт
                        print()
                        print('messag  is ',messag,'')
                        print()
                        if str(messag) in str(button.button.text):
                            await button.click()
@client.on(events.NewMessage(chats=chat))
async def my_event_handler(event):
                            time.sleep(2)
                            # print(button.text,' clicked')
                            messagOUTPUT=str(event.raw_text)
                            print('')        
                            print(' THIS IS RESPONSE  ',messagOUTPUT)
                            print('Конец итерации')
                            print()
                            try:
                                pywhatkit.sendwhatmsg_to_group_instantly(tel,str(messagOUTPUT),tab_close=True)
                                keyboard.press_and_release('enter')
                                keyboard.press_and_release('enter')
                                print('Message send')
                                # keyboard.press_and_release('ctrl+w')
                            except: 
                                 print("Error in sending the message")

    
async def waiter():
    await asyncio.sleep(300)  # `.sleep` will make your code sleep for x ammout of seconds. 
    print()
    print('Сработал конец 290сек')
    print()
    time.sleep(10)
    os.system("taskkill /im chrome.exe /f")
    
with client:
    client.loop.run_until_complete(waiter())

    # try:
    #     print('(Press Ctrl+C to stop this)')
    #     client.run_until_disconnected()
    #     time.sleep(50)
        
    # finally:
    #   client.run_until_disconnected



                