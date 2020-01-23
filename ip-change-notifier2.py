from requests import get
import smtplib, ssl, time

email = input("Enter your email: ")
password = input("Enter your email's password: ")
old_ip = new_ip = ''


def get_id_address():
    global new_ip, old_ip
    old_ip = new_ip
    try:
        new_ip = get('https://api.ipify.org').text
    except Exception:
        print("No Internet Connection")


def send_email():
    message = """Subject: Your automated IP notifier change mail

    Hi, how are you doing?

    This E-Mail is sent to you from your python ip getter bot.

    Your external ip address now is : {}

    Have a nice day!""".format(new_ip)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email, password)
        server.sendmail(email, email, message)


if __name__ == '__main__':
    while True:
        get_id_address()
        if new_ip != old_ip:
            send_email()
        time.sleep(59)
