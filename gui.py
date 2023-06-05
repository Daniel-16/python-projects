import tkinter as tk

window = tk.Tk()
window.title("Tkinter Project")
# window.geometry("900x500")
frame = tk.Frame(master=window)

#Event Listener
def signIn():
    print("User signed in")
def getStarted():
    print("Welcome to this platform")
def logOut():
    print("User logged out")

button1 = tk.Button(master=frame, text="Sign in", command=signIn)
button2 = tk.Button(master=frame, text="Get started", command=getStarted)
button3 = tk.Button(master=frame, text="Log out", command=logOut)

frame.grid(row=0, column=0)
button1.grid(row=0, column=1)
button2.grid(row=1, column=1)
button3.grid(row=2, column=1)


window.mainloop()
