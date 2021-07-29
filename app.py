from telegram.ext import Updater, MessageHandler,Filters 
from Adafruit_IO import Client 

aio = Client('Mamidi_Kalpana', os.getenv('Mamidi_Kalpana'))

def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://cdn.mos.cms.futurecdn.net/HaPnm6P7TZhPQGGUxtDjAg-320-80.jpg'
  bot.message.reply_text('Light is turned ON')  
  aio.send('light',1)
  data1 = aio.receive('light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo2(bot,update): 
  chat_id = bot.message.chat_id
  path = 'https://cdn3.vectorstock.com/i/1000x1000/89/72/object-bulb-off-vector-1858972.jpg'
  bot.message.reply_text('Light is turned OFF')  
  aio.send('light',0)
  data1 = aio.receive('light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path) 
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://thumbs.dreamstime.com/z/fan-turned-room-air-cooling-hot-climates-working-near-window-190362135.jpg'
  bot.message.reply_text('Fan is turned ON')  
  aio.send('fan',1)
  data2 = aio.receive('fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update): 
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-photo/hand-presses-button-on-control-260nw-771738067.jpg'
  bot.message.reply_text('Fan is turned OFF')  
  aio.send('fan',0)
  data2 = aio.receive('fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
  a=bot.message.text.lower()
  print(a) 

  if a =="light on" or a=="turn on light":
    demo1(bot,update)
  elif a =="light off" or a=="turn off light":
    demo2(bot,update)
  elif a =="switch on the fan" or a=="turn on fan":
    demo3(bot,update)
  elif a =="switch of the fan" or a=="turn off fan":
    demo4(bot,update)
  else:
     bot.message.reply_text('Invalid Text')   
BOT_TOKEN =os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle() 
