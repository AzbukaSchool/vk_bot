import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token='00512b82138f907e4a1ae4b3e93a274f001260f8fab92a95efb4803b44803507810ee3df025133ad28b83')
longpoll_bot = VkBotLongPoll(vk_session, 210994750)
vk = vk_session.get_api()

sched = {' Понедельник' : ['Английский', 'Русский Язык', 'Геометрия', "Информатика", "Физика", "Обществознание", "География"]}


def schedule(day):
    global sched
    return sched[day]


for event in longpoll_bot.listen():
    print(event.type)
    if event.type == VkBotEventType.MESSAGE_NEW:
        print(event.object.text)
        if event.object.text == '!Расписание' + event.object.text[11:]:
            vk.messages.send(
                    random_id=random.getrandbits(30),
                    peer_id=event.object.peer_id,
                    message=schedule(event.object.text[11:]),
            )


