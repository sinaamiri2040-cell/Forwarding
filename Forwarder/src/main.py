from telethon import TelegramClient, events
import asyncio

# اطلاعات اکانت انسانی شما
api_id = 20977947  # عدد
api_hash = 'c0dd0662c37d4b45e342b73b3c388166'  # رشته
phone = '+989902484287'  # با +98 شروع شود (مثلاً +989123456789)

# آیدی عددی گروه خصوصی (مثلاً -1004881204443)
group_id = -1002848563043  # اینجا آیدی عددی گروه را قرار بده (بدون کوتیشن)

# user id عددی ربات ارسال‌کننده پیام (ربات اول)
sender_bot_id = 7273522561  # اینجا user id عددی ربات اول را قرار بده

# یوزرنیم ربات ثبت‌کننده (ربات دوم)
your_bot_username = '@MyKharidTrackerBot'  # مثلاً @yourbot

async def main():
    client = TelegramClient('forward_session', api_id, api_hash)
    await client.start(phone=phone)

    @client.on(events.NewMessage(chats=group_id))
    async def handler(event):
        sender = await event.get_sender()
        if sender.id == sender_bot_id:
            # فروارد پیام به ربات دوم (در PV)
            await event.forward_to(your_bot_username)
            print('پیام ربات اول فروارد شد:', event.text)

    print('در حال گوش دادن به پیام‌های گروه...')
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
