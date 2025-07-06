import tkinter as Tk

app = Tk.Tk()
app.title("Jet's Word Counter")
app.geometry = ('3000x3000')

label = Tk.Label(app, text = "Word counter", font = ("Arial", 18))
label.pack()

textbox = Tk.Text(app, height = 3, font = ("Arial", 18))
label = Tk.Label(padx=10)

text_box = Tk.Text(app, width=300, height=40)
text_box.pack(padx=10, pady=10)

def count_words():
    text = text_box.get("1.0", Tk.END)
    words = text.strip().split()
    word_label.config(text=f"Word Count: {len(words)}")

def count_chr():
    text = text_box.get("1.0", Tk.END)
    word_label2.config(text=f"Word Characters: {len(text.replace(" ",""))-1}")

# Labels
word_label = Tk.Label(app, text="Word Count: 0", font=("Arial", 16))
word_label.pack(pady=10) 

word_label2 = Tk.Label(app, text="Word Characters: 0", font=("Arial", 16))
word_label2.pack(pady=10) 

# Counter buttons
button = Tk.Button(app, text="Count Words", font=("Arial", 16), command=count_words)
button.pack(pady=10)

button2 = Tk.Button(app, text="Count Characters", font=("Arial", 16), command=count_chr)
button2.pack(pady=10)

app.state('zoomed')

app.mainloop()