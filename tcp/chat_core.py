from tkinter import *
import socket


class Chat:
    def __init__(self):
        window = Tk()
        window.title("Chat")

        self.text = Text()
        self.text.pack()

        frame1 = Frame(window)
        frame1.pack()

        label = Label(frame1, text="Enter your message:")
        self.Message = StringVar()
        entryMessage = Entry(frame1, textvariable=self.Message)
        btSend = Button(frame1, text='Send', command=self.processSendButton)
        btLink = Button(window, text='Link', command=self.processLinkButton)
        btLink.pack()

        label.grid(row=1, column=1)
        entryMessage.grid(row=1, column=2)
        btSend.grid(row=1, column=3)
        self.text.insert(END, 'Welcome!')
        window.mainloop()


    def processSendButton(self):
        self.text.insert(END, "[You Message] :"+self.Message.get()+"\n")


    def processLinkButton(self):
        pass

Chat()


