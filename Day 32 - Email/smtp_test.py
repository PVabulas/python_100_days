import smtplib

gmail = "phil.vabulas@gmail.com"
yahoo = "mellowed_out98@yahoo.co.uk"

gmail_smtp = "smtp.gmail.com"
yahoo_smtp = "smtp.mail.yahoo.com"

gmail_pwd = "a"
yahoo_pwd = "mqserjlsphtvnwry"

with smtplib.SMTP(yahoo_smtp) as connection:
    connection.starttls()
    connection.login(user=yahoo, password=yahoo_pwd)
    connection.sendmail(
        from_addr=yahoo, to_addrs=gmail, msg=f"Subject:Hello\n\nThis is a test"
    )
