import tkinter as tk
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser as wb
import time
import random


greetings =['hello','hi','hey']
intro = ["Myself Chotu! What can i do for you, sir","Hey boss! I am your voice assistant ","It is wonderful to have you again, sir!"]

speaker = pyttsx3.init()
def rec():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        sentence = r.recognize_google(audio,language="en-in")
        words = sentence.split()
        ent2.insert(tk.END,sentence)

    for each in words:
        if each == "what" or each =="who":
            ans = wikipedia.summary(' '.join(words[2:]),sentences =1) # rn voice ain't working may be my mac sucks
            ent1.insert(tk.END,ans)
            speaker.say(ans)
            speaker.runAndWait()
            wb.open_new("https://en.wikipedia.org/wiki/"+'_'.join(words[2:]))   #https://en.wikipedia.org/wiki/Bill_Gates
            
        elif each == 'play' :
            ent1.insert(tk.END,"SWITCHING TO YOUTUBE")
            wb.open_new("https://www.youtube.com/results?search_query="+'+'.join(words[1:]))

        elif each == 'search':
             ent1.insert(tk.END,"SWITCHING TO GOOGLE")
             wb.open_new("https://www.google.com/search?client=safari&rls=en&q="+'+'.join(words[1:])+"&ie=UTF-8&oe=UTF-8")
        
        elif each in greetings:
            x = random.randint(0,len(intro))
            ent1.insert(tk.END,greetings[x])
            speaker.say(intro[x])
            speaker.runAndWait()
            
        
        elif each=='close' or each =="bye" or each == "quit" or each == "exit":
            wish= "BYE ! SEE YA LATER"
            ent1.insert(tk.END,wish+'\n')
            speaker.say("bye bye")
            speaker.runAndWait()
            # time.sleep(3)     #speaker itself terminates the window
            # window.destroy() 

    # ent1.delete('1.0',tk.END)   #--> if executed then no values in text boxes from the very start
    # ent2.delete("1.0",tk.END)

#creating gui

window = tk.Tk()
window.title("Assistant By Abrar")
window.geometry("300x300")
window.configure(bg="#9136a3")

tk.Label(window,text="---->Chotu Says<----",bg="#4a4a82",fg="#fcbd81",width=300).pack(pady=15)
ent1 = tk.Text(window)
ent1.place(x=20,y=50,height = 80,width = 260)

tk.Label(window,text="---->User Says<----",bg="#4a4a82",fg="#fcbd81",width=300).pack(pady=90)
ent2 = tk.Text(window)
ent2.place(x=20,y=180,height = 80,width = 260)

button1 = tk.Button(window,text="Click to Speak",bg='purple',fg="#ff8095",font=("Gill Sans",20),command=rec)
button1.place(x=85,y=270,height=22)


window.mainloop()

