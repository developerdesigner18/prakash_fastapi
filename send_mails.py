from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import Environment, FileSystemLoader

conf = ConnectionConfig (
   MAIL_USERNAME="developer.designer18@gmail.com",
   MAIL_FROM="developer.designer18@gmail.com",
   MAIL_PASSWORD="bvtl fjku jjpe kyws",
   MAIL_PORT=587, 
   MAIL_SERVER="smtp.gmail.com",
   MAIL_FROM_NAME="Developer.Designer",
   MAIL_STARTTLS = True,
   MAIL_SSL_TLS = False
)

async def send_mail(subject: str, email_to: list, templatevars: dict, template_name:str):
    
   try:

      env = Environment(loader=FileSystemLoader('.'))
      template = env.get_template(f"templates/{template_name}")
      html_content = template.render(**templatevars)

      message = MessageSchema(
         subject=subject,
         recipients=email_to,
         body = html_content,
         subtype="html",
      )
      fm = FastMail(conf)
      await fm.send_message(message)

      print("sent")
   
   except Exception as e:

      print(e)

      print("Email Not Sent. Reception List: ", email_to)

