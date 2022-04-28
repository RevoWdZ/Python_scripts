# -*- coding: utf-8 -*-
import smtplib
from string import Template
import time

SEND_FROM = 'ur-email-account'
EMAIL_PWD = "ur-email-password"


def get_users_data(file_name):
    user_name = []
    user_mail = []
    with open(file_name, mode='r') as user_file:
        for user_info in user_file:
            user_name.append(user_info.split()[0])
            user_mail.append(user_info.split()[1])
    return user_name, user_mail


def read_template(file_name):
    with open(file_name, 'r') as msg_template:
        msg_template_content = msg_template.read()
    return Template(msg_template_content)


def main():
    start = time.time()
    # store here user name and email address of recipient
    user_name, user_mail = get_users_data('users.txt')
    message_template = read_template(
        'template.txt')  # message stored as a file

    # Set up the SMTP server
    smtplib_server = smtplib.SMTP(
        host='ur-server-host eg. smtp.gmail.com', port=25)
    # smtplib_server.set_debuglevel(True)
    # smtplib_server.starttls()
    smtplib_server.login(SEND_FROM, EMAIL_PWD)
    for name, email in zip(user_name, user_mail):

        msg = message_template.substitute(PERSON_NAME=name.title())

        smtplib_server.sendmail(SEND_FROM, email, msg)

        end = time.time()

        print("The time the message was sent from the server: %.2fs " % (end-start))

    smtplib_server.quit()


if __name__ == '__main__':
    main()
