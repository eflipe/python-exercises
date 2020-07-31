username = ''
password = ''


def send_mail(text='email body', subject='Mensaje largo', from_email=EMAIL, to_emails=None):
    assert isinstance(to_emails, list)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    # login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=547)
    server.quit()