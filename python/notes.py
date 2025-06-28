import tkinter as tk

root = tk.Tk()
root.title("Notes App")
root.geometry('600x400')
root.configure(bg="#f0f4f8")

title_var = tk.StringVar()
notes = []  

def submit():
    title = title_var.get().strip()
    description = description_entry.get("1.0", tk.END).strip()
    
    if title and description:
        note = {
            "title": title,
            "description": description
        }
        notes.append(note)
        print(f"Note saved: {note}")
        
        title_var.set("")
        description_entry.delete("1.0", tk.END)
    else:
        print("Both title and description are required.")

def viewNote():
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. Title: {note['title']}\n   Description: {note['description']}\n")
    if not notes:
        print("No notes available.")

notes_label = tk.Label(root, text=" My Notes", font=('Helvetica', 24, 'bold'), bg="#f0f4f8", fg="#333")
notes_label.pack(pady=5)

form_frame = tk.Frame(root, bg="#f0f4f8")
form_frame.pack(padx=20, pady=10, fill='x')

title_label = tk.Label(form_frame, text="Title", font=('Helvetica', 12), bg="#f0f4f8")
title_label.grid(row=0, column=0, sticky='w', pady=5)
title_entry = tk.Entry(form_frame, textvariable=title_var, font=('Helvetica', 12), width=50)
title_entry.grid(row=0, column=1, pady=5)

description_label = tk.Label(form_frame, text="Description", font=('Helvetica', 12), bg="#f0f4f8")
description_label.grid(row=1, column=0, sticky='nw', pady=5)
description_entry = tk.Text(form_frame, font=('Helvetica', 12), width=50, height=6)
description_entry.grid(row=1, column=1, pady=5)

submit_button = tk.Button(
    root,
    text='Save Note',
    command=submit,
    font=('Helvetica', 12, 'bold'),
    bg="#4caf50",
    fg="white",
    padx=10,
    pady=5,
    relief="flat"
)
view_button = tk.Button(
    root,
    text='View Notes',
    command=viewNote,
    font=('Helvetica', 12, 'bold'),
    bg="#2196f3",
    fg="white",
    padx=10,
    pady=5,
    relief="flat"
)

submit_button.pack(padx=20, pady=5)
view_button.pack(padx=10)

root.mainloop()
