from tkinter import *
import socket, threading


def acceptMessage(s, text, theSystem):
    sock, addr = s.accept()
    theSystem.sock = sock
    while True:
        print(sock.recv(1024).decode()+"\n")
        #text.insert(END, "[Other's Message] :"+sock.recv(1024).decode()+"\n")


class Chat:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 12345
        self.s.bind((host, port))
        self.s.listen(1)

        window = Tk()
        window.title("Chat")

        self.text = Text(window)
        self.text.pack()

        frame1 = Frame(window)
        frame1.pack()

        label = Label(frame1, text="Enter your message:")
        self.Message = StringVar()
        entryMessage = Entry(frame1, textvariable=self.Message)
        btSend = Button(frame1, text='Send', command=self.processSendButton)

        label.grid(row=1, column=1)
        entryMessage.grid(row=1, column=2)
        btSend.grid(row=1, column=3)
        self.text.insert(END, 'Welcome, I am client 2!\n')
        self.text.insert(END, 'Wait for another one\n')
        t = threading.Thread(target=acceptMessage, args=(self.s, self.text, self))
        t.start()
        window.mainloop()


    def processSendButton(self):
        self.sock.send(self.Message.get().encode())
        self.text.insert(END, "[You Message] :"+self.Message.get()+"\n")



Chat()
