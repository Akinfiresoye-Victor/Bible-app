from tkinter import *
import requests
from PIL import Image,ImageTk

root=Tk()
root.title('KJV Bible App')
root.iconbitmap("C:\\Users\\VICT6OR\\Pictures\\notebook.ico")

def find():
    try:
        bok=book.get()
        cpt=chapter.get()
        vrs=verse.get()
        
        api_call=f'https://bible-api.com/{bok}%20{cpt}:{vrs}'
        params = {
            'translation': 'kjv'
        }
        headers = {
            'Authorization': 'Token c0fa75b72d43008250287062a012eea8'
        }
        response = requests.get(api_call, params=params, headers=headers)

        bible=response.json()['text']
        display.insert('1.0', bible)
    except:
        message='Please you have to be specific'
        display.delete('1.0', END)
        display.insert('1.0', message)             









#c0fa75b72d43008250287062a012eea8
book=StringVar()
chapter=StringVar()
verse=StringVar()


book_lbl=Label(root, text='Select book     ')
book_lbl.grid(row=0, column=0, sticky=W)

book=Entry(root, width=30, border=5)
book.grid(row=1,column=0)


chapter_lbl=Label(root, text='Select chapter    ')
chapter_lbl.grid(row=0, column=1)

chapter=Entry(root, width=30, border=5)
chapter.grid(row=1,column=1)


verse_lbl=Label(root, text='Select Verse    ')
verse_lbl.grid(row=0, column=2)

verse=Entry(root, width=30, border=5)
verse.grid(row=1,column=2)

search=Button(root, text='Search', command=find)
search.grid(row=1, column=3)


display=Text(root)
display.grid(row=2, column=0, columnspan=3)








mainloop()