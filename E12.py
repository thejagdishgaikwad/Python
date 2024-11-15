#Write a program to create a message widget to show the text message in python.
import tkinter as tk

root = tk.Tk()
root.title("Message Widget Example")
root.geometry("300x150")

message = tk.Message(root, text="Hello, welcome to the message widget example!", width=250)
message.pack(pady=20)

root.mainloop()
