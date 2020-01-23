import speech_recognition as sr
import pyttsx3
from time import sleep
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def commands(value):
    global root
    global frame
    print("helloo command")
    e1.insert(0,value)
    e1.grid(row=3,column=0)
def Bot():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    print(sr.__version__)
    command1=""
    while(command1!="exit"):
        r=sr.Recognizer()
        mic=sr.Microphone()
        try:
            with mic as source:
                engine.say("Hi, How can i assist you?")
                engine.runAndWait()
                print("Listening..")
                r.adjust_for_ambient_noise(source)
                audio=r.record(source,duration=3)
            command1=str(r.recognize_google(audio))
            commands(command1)
            label=Label(frame,text=command1)
            label.grid(row=2,column=0)
            sleep(5)  
            print(command1)
            if((command1)=="send email"):
                import smtplib
                gmail_user = 'v.nivedha20@gmail.com'
                gmail_password = 'v.nivedha20@1830'
                pwd="cnqcfmsumcjxsroi"
                sent_from = gmail_user
                engine.say("Who do you want to send the email?")
                engine.runAndWait()
                confirm=""
                while(confirm!="yes"):
                    with mic as source:    
                        print("Listening...")
                        r.adjust_for_ambient_noise(source)
                        reciever=r.record(source,duration=10)
                        
                    to1=r.recognize_google(reciever).split(" ")
                    to="".join(to1)
                    to=str(to)
                    print(to)
                    engine.say("Are you sure you want to send the email?")
                    engine.runAndWait()
                    with mic as src:    
                        print("Listening")
                        r.adjust_for_ambient_noise(src)
                        a=r.record(src,duration=3)
                    confirm=r.recognize_google(a)
                    print(confirm)        
                message = MIMEMultipart("alternative")
                engine.say("Subject:")
                engine.runAndWait()
                flags=1
                while(flags):
                    try:
                        with mic as source:    
                            r.adjust_for_ambient_noise(source)
                            subject=r.record(source,duration=5)
                            
                        message["Subject"] =r.recognize_google(subject)
                        flags=0
                    except:
                        engine.say("Repeat Subject")
                        engine.runAndWait()
                print(message["Subject"])
                message["From"] = gmail_user
                message["To"] = to
                engine.say("Message:")
                engine.runAndWait()
                flagm=1
                while(flagm):
                    try:
                        with mic as source:    
                            r.adjust_for_ambient_noise(source)
                            msg=r.record(source,duration=5)
                        text = """\
                        Hi,
                        """+r.recognize_google(msg)
                        flagm=0
                    except:
                        engine.say("Repeat Message")
                        engine.runAndWait()
                print(text)
                part1 = MIMEText(text, "plain")
                message.attach(part1)
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(gmail_user, pwd)
                    server.sendmail(sent_from, to, message.as_string())
                    server.close()
                    engine.say('Email sent!')
                    engine.runAndWait()
                except Exception as e:
                    print ('Something went wrong...',e)
        except Exception as e:
            print("Command not understood.Please repeat.",e)
    engine.say("Bot exited")
    engine.runAndWait()
if __name__=="__main__":
    root=Tk()
    root.title("Email Bot")
    frame=LabelFrame(root,text="Bot",padx=10,pady=10)
    frame.pack(padx=10,pady=10)
    e1=Entry(frame,width=50,borderwidth=10)
    e1.grid(row=0,column=0)

    BotButton=Button(frame,text="Click to activate bot!",command=Bot)
    BotButton.grid(row=1,column=0)
    root.mainloop()