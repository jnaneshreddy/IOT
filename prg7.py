import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM_EMAIL="31051999family@gmail.com"
TO_EMAIL="jnaneshreddyv730@gmail.com"
EMAIL_PASSWORD="yajr vgkl ysml uefc"

def send_email( custom_body):
    try:
        msg=MIMEMultipart()
        msg['From']=FROM_EMAIL
        msg['To']=TO_EMAIL
        msg['Subject']="User Message"
        msg.attach(MIMEText(custom_body,'plain'))
        
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(FROM_EMAIL,EMAIL_PASSWORD)
        server.sendmail(FROM_EMAIL,[TO_EMAIL],msg.as_string())
        server.quit()
        print("EMAILsent")
    except Exception as e:
        print("Faild",e)
        
if __name__=="__main__":
    custom_message=str(input("hello"))
    send_email(custom_message)
     