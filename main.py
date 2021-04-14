from tkinter import *
import random

TOTAL_SEC="Total Seconds\n 60"
BG_APP="#f7f3e9"
counts = 60
acc = None
gross=None
net=None
PARA =["Some people combine touch typing and hunt and peck by using a buffering method.\n In the buffer method, the typist " \
      "looks at the source copy,\n mentally stores one or several sentences,\n then looks at the keyboard and types out the " \
      "buffer of sentences.\n This eliminates frequent up and down motions with the head \nand is used in typing competitions" \
      " in which the typist is not well versed in touch typing.\n Not normally used in day-to-day contact with keyboards,\n " \
      "this buffer method is used only when time is of the essence"]

# randomly choose a paragraph
r = random.choice(PARA)

window = Tk()
# creating frame for ordering row and column
content = Frame(window)
window.title("Typing Speed Tester")
window.minsize(600,500)
window.config(bg=BG_APP)
logo = PhotoImage(file="key icon.png")
# setting "window" icon
window.iconphoto(True, logo)
frame = Label(content, text=TOTAL_SEC, width=20, height=10, borderwidth=6, relief="flat",bg="#1b2021",fg="#54e346")
info = Label(content, text="TYPING SPEED TESTER GUI  ⌨ ", width=40,height=10, borderwidth=6, relief="flat",bg="#1b2021",
             fg="#fff")
count = Label(content, text=str(counts), width=20, height=10, borderwidth=6, relief="flat",bg="#1b2021", fg="#f05945")
paragraph = Label(content, text=r,width=80,height=10,bg="#dbf6e9",fg="#2b2e4a",padx=19)
# rs is waiting for text input
rs = Text(content,bg="#9dbeb9",width=60,height=9)
button = Label(content, text="Running", bg="#03c4a1", width=15,height=2)

def time():
    """
    This time function checks the secs, if the secs is hit '0' then
    -> the whole app is changing the bg color and text
    -> typed_rs is variable name for getting and storing the text input
    -> calculating the gross, net speed, accuracy
    -> created function called "second()", This function returns the new child window shows the results.
    if the secs not hit '0' :
    -> keep repeating the 'time' function until the counts get '0'
    :return:
    """
    global counts,acc,gross,net
    counts -= 1
    count.config(text= counts)
    if counts==0:
        # changing bg color and Shows the TimesUp text on the screen
        button.config(text="TimesUp", bg="#ce1212", fg="#fff")
        paragraph.config(text="TimesUp", bg="#ce1212", fg="#fff")
        content.config(bg="#1b2021")
        frame.config(text="TimesUp", fg="#ce1212")
        count.config(text="TimesUp", fg="#ce1212")
        typed_rs = rs.get("1.0",'end-1c')

        def second():
            #  Child window
            result = Toplevel()
            result.title("Result")
            result.minsize(400, 250)
            result.config(bg="#9dbeb9")
            result.iconphoto(True, logo)
            info_result = Label(result, text="Your Result", width=45, height=5,bg="#9dbeb9",fg="#1b2021",font=("arial",12,"bold"))
            info_ = Label(result, text=f"{gross}\n{net}\n{acc}%", width=40, height=9,bg=BG_APP)
            # grid
            info_result.grid(column=0, row=0, columnspan=1)
            info_.grid(column=0, row=1, columnspan=1)

        if typed_rs:
            correct = 0
            mistake = 0
            split_rs = typed_rs.split()
            para_rs = r.split()
            for i in range(len(split_rs)):
                if split_rs[i] == para_rs[i]:
                    correct +=1
                else:
                    mistake +=1
            gross_wpm = (len(typed_rs)/5)/1
            net_wpm = (gross_wpm-mistake)/1
            accuracy = (correct/len(r))*100
            acc =f"Accuracy: %.2f"% accuracy
            gross = f"Gross Speed: {gross_wpm}WPM"
            net = f"Net Speed: %.2f WPM"% net_wpm

        second()
        # deleting all the inputs from 'Text'
        rs.delete("1.0", 'end')
    elif counts!=0:
        # after one second the time function is calling
        window.after(1000, time)

# Total sec label
content.grid(column=0, row=0)
frame.grid(column=0, row=0)
info.grid(column=1,row=0)
count.grid(column=2, row=0)
paragraph.grid(column=0,row=1, columnspan=3)
rs.grid(column=0, row=2, columnspan=3)
button.grid(column=1, row=3)

# updating values by calling the time function (window.after())
time()
window.mainloop()