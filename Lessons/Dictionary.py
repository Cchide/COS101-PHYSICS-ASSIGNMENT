from tkinter import Tk, Entry, Button, Label, StringVar

window =Tk()
window.geometry("600x250")
window.title("Igala dictionary")

label = Label( text="Dictionary", font=("Algerian", 20))
label.pack(padx=20, pady=20)

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label =  Label(window, textvariable=result)
result_label.pack()

igala_dict = {
    'good morning': 'olodudu',
    'thanks': 'agba',
    'come': 'lia',
    'go': 'lo',
    'god': 'ojo',
    'eat': 'jeun',
    "one": "oka",
    'two': 'eji',
    'twins': 'ogwu',
    'floor': 'ane',
    'three': 'eta',
    'room': 'ejefu',
    'kitchen': 'obuka',
    'leg': 'ere',
    'who': 'ene',
    'love': 'ufedo',
    'water': 'omi',
    'head': 'oji',
    'bed': 'ate',
    'amen': 'ami'
}


def search():
    word = entry_text.get()
    print(word)
    if word in igala_dict:
     result.set(igala_dict[word])
     print(igala_dict[word])
    else:
       result.set("Not found")
       print("Not found")

search_btn = Button(window, text="Search", command=search)
search_btn.pack()

window.mainloop()