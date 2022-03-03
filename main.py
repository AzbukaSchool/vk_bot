import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll

vk_session = vk_api.VkApi(token='00512b82138f907e4a1ae4b3e93a274f001260f8fab92a95efb4803b44803507810ee3df025133ad28b83')
longpoll_bot = VkBotLongPoll(vk_session, 210994750)
vk = vk_session.get_api()

for event in longpoll_bot.listen():
         print(event)
         if event.object.text == 'Hello!':
            vk.messages.send(
            random_id=random.getrandbits(30),
            peer_id=event.object.peer_id,
            message='Hello!',
            )