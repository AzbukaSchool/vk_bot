import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll

vk_session = vk_api.VkApi(token='5b9b4e956cc67a7aac20e6bad3fd14b70ef01da1124ac32b81898edf7782e24fa605878a1a5640181e373')
longpoll_bot = VkBotLongPoll(vk_session, 205343326)
vk = vk_session.get_api()

for event in longpoll_bot.listen():
         if event.object.text == '!статус':
                    vk.messages.send(
                        random_id=random.getrandbits(30),
                        peer_id=event.object.peer_id,
                        message='Запись идёт!',
                    )