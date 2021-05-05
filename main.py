import sys
import asyncio
import aiosmtplib
from email.message import EmailMessage


if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

emails = ['example1@yandex.ru', 'example2@gmail.com']

your_email = input('Введите свой email: ')
your_hostname = input('Введите свой hostname: ')
your_port = int(input('Введите свой port: '))


async def send_email_message(email_from, email_to, hostname, port):
    message = EmailMessage()
    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = 'Спасибо за доверие!'
    message.set_content(f'Уважаемый {email_to}!\nСпасибо, что пользуетесь нашим сервисом объявлений.')

    await aiosmtplib.send(message, hostname=hostname, port=port)


async def main():
    tasks = []
    for email in emails:
        task = asyncio.create_task(send_email_message(your_email, email, your_hostname, your_port))
        tasks.append(task)

    for task in tasks:
        await task


asyncio.run(main())
