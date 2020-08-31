import config
import telebot
import discord
import threading
from discord import Webhook, RequestsWebhookAdapter, File
import random
import time

bot_t = telebot.TeleBot(config.T_TOKEN)
bot_d = discord.Client()
content = {}
content2 = {}
webhook = Webhook.partial('748454165277310977', 'FR0d4TzJLM95M-gQ7S4gB_EJlKbd-XyS2wEXXDDiqyEwsSavZs6cX7jRIswEuNJn8Czt',
                          adapter=RequestsWebhookAdapter())

stickers = {'1': 'static/yuno.webp', '2': 'static/eyes.webp', '3': 'static/sticker.webp', '4': 'static/sticker2.webp', '5': 'static/sticker3.webp', '6': 'static/sticker4.webp', '7': 'static/sticker5.webp',
            '8': 'static/sticker6.webp', '9': 'static/sticker7.webp', '10': 'static/sticker8.webp', '11': 'static/sticker9.webp', '12': 'static/yunobad.webp', '13': 'static/yunogood.webp', '14': 'static/yunoknife.webp', }
text = 'Нц '


@bot_d.event
async def on_ready():
    print(f'Logged in as {bot_d.user.name}')


@bot_d.event
async def on_message(msg):
    if msg.author == bot_d.user or msg.author.name == 'Юно' or msg.channel.id != 716362467717939303:
        return
    else:
        content['name'] = msg.author.name
        content['msg'] = msg.content
        # content['channel'] = msg.channel.id
        # await msg.channel.send(msg.content)
        t_send_msg(msg)


first = threading.Thread(target=bot_d.run, args=(config.D_TOKEN,))
first.start()


@ bot_t.message_handler(commands=['start'])
def start_message(message):
    sti = open('static/eyes.webp', 'rb')
    bot_t.send_sticker(message.chat.id, sti)


@ bot_t.message_handler(func=lambda message: True, content_types=['text'])
def look_for_message(message):
    if message.text == 'Юно':
        sti = open(stickers[random.choice(list(stickers.keys()))], 'rb')
        bot_t.send_sticker(message.chat.id, sti)

    d_send_msg(message)


def t_send_msg(msg):
    time.sleep(1)
    bot_t.send_message(
        '-1001401097714', str(msg.from_user.username) + '\n' + str(msg.text))


def d_send_msg(msg):
    if msg.reply_to_message == None:
        webhook.send(str(msg.from_user.username) +
                     '\n' + str(msg.text) + '\n' + str('_'*70))
    else:
       # Якщо повідомлення не було переслане кимось
        webhook.send('От ' + str(
            msg.from_user.username) + ' Ответ для:' + str(msg.reply_to_message.from_user.username) +
            '\n' + str(msg.reply_to_message.text) + '\n'  '\n' + str(msg.text) + '\n' + str('_'*70))


# -1001401097714
# -187201834
second = threading.Thread(target=bot_t.polling)
second.start()


# {'content_type': 'text', 'message_id': 47962, 'from_user': {'id': 948975971, 'is_bot': False, 'first_name': 'Ruslan', 'username': 'Talfun', 'last_name': None, 'language_code': 'ru', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None},
# 'date': 1598591535, 'chat': {'id': -1001401097714, 'type': 'supergroup', 'title': 'ВКС и только', 'username': None, 'first_name': None, 'last_name': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'sticker_set_name': None, 'can_set_sticker_set': None},
# 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_date': None,
# 'reply_to_message': {'content_type': 'text', 'message_id': 47961, 'from_user': < telebot.types.User object at 0x04D31700 >, 'date': 1598591492, 'chat': < telebot.types.Chat object at 0x04D313D0 > , 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': 1598591509, 'media_group_id': None, 'author_signature': None, 'text': 'Всем привет', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title':
#                    None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 47961, 'from': {'id': 630635903, 'is_bot': False, 'first_name': 'Доктор', 'last_name': 'Азан', 'username': 'Impfri'}, 'chat': {'id': -1001401097714, 'title': 'ВКС и только', 'type': 'supergroup'}, 'date': 1598591492, 'edit_date': 1598591509, 'text': 'Всем привет'}}, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'привет', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 47962, 'from': {'id': 948975971, 'is_bot': False, 'first_name': 'Ruslan', 'username': 'Talfun', 'language_code': 'ru'}, 'chat': {'id': -1001401097714, 'title': 'ВКС и только', 'type': 'supergroup'}, 'date': 1598591535, 'reply_to_message': {'message_id': 47961, 'from': {'id': 630635903, 'is_bot': False, 'first_name': 'Доктор', 'last_name': 'Азан', 'username': 'Impfri'}, 'chat': {'id': -1001401097714, 'title': 'ВКС и только', 'type': 'supergroup'}, 'date': 1598591492, 'edit_date': 1598591509, 'text': 'Всем привет'}, 'text': 'привет'}}
