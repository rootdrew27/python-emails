import smtplib, ssl
from EnvVarReader.env_var_reader import Secrets

try:
    secrets = Secrets("ENV_VARS.json")

    ##via SMTP_SSL
    port = 465 # for ssl
    
    sender_email = secrets.getSecret("SENDER")
    receiver_email = secrets.getSecret("RECEIVER")
    app_password = secrets.getSecret("APP_PASSWORD")

    message = """\
    Subject: Hello

    This is my message body."""

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, app_password)
        #send email here
        output = server.sendmail(sender_email, receiver_email, message)
        print(output)

except Exception as ex:
    print("\n" + ex)

#via .starttls()

# smtp_server = "smtp.gmail.com"
# port = 587 # for starttls
# sender_email = "rootydrew@gmail.com"
# password = "ThenameofmyDog32!"

# context = ssl.create_default_context()

# try: 
#     server = smtplib.SMTP(smtp_server, port)
#     server.ehlo()
#     server.starttls(context=context)
#     server.ehlo()
#     server.login(sender_email, password)
#     #send emial here

# except Exception as e:
#     print(e)
# finally:
#     server.quit()