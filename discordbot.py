import datetime
import disnake


schedule = {
    "日曜日": "**日曜日は休み**",
    "月曜日": "**月曜日\n\n:one::数学Ⅰ\n:two::国語A\n:three::理科持論\n:four::英語\n:five::数学A\n:six::公民**",
    "火曜日": "**火曜日\n\n:one::GlobalStudy\n:two::技術\n:three::音楽\n:four::英語\n:five::英語\n:six::保健**",
    "水曜日": "**水曜日\n\n:one::LHM\n:two::理科Ⅱ\n:three::国語B\n:four::英語\n:five::国語A\n:six::体育**",
    "木曜日": "**木曜日\n\n:one::国語B\n:two::数学Ⅰ\n:three::歴史\n:four::理科Ⅰ\n:five::美術\n:six::公民**",
    "金曜日": "**金曜日\n\n:one::数学Ⅰ\n:two::理科Ⅰ\n:three::歴史\n:four::英語\n:five::理科Ⅱ\n:six::体育**",
    "土曜日": "**土曜日\n\n:one::数学A\n:two::英語\n:three::数学Ⅰ\n:four::道徳**"
}


def intToDay(num):
    return ["日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"][num%7]


class MyClient(disnake.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.content == "今日":
            today = intToDay(datetime.date.today().day)
            await message.channel.send(f"${schedule[today]}\n\nです")
        elif message.content == "明日":
            tomorrow = intToDay(datetime.date.today().day + 1)
            await message.channel.send(f"${schedule[tomorrow]}\n\nです")
        elif message.content in schedule:
            await message.channel.send(f"${schedule[message.content]}\n\nです")


client = MyClient()
client.run('my token goes here')