import tkinter as tk
import pyperclip

def nextToken(text, cursor) :
    token = ""
    textSize = len(text)
    while cursor < textSize :
        if text[cursor] == ' ' :
                if token == "" :
                     cursor += 1
                     continue
                else :
                    return (token, cursor)
        else :
            token += text[cursor]
            cursor += 1
    
    return (token, cursor)

def formatToken(token) :
    out = ""
    out += "[" + token + "](<https://www.youtube.com/watch?v=dQw4w9WgXcQ>)"
    return out

def formatText(text) :
    character = 0

    (token, character) = nextToken(text, character)
    newText = ""

    while token != "" :
        newText += formatToken(token) + " "
        (token, character) = nextToken(text, character)
    
    return newText

window = tk.Tk()
window.title("Text to Discord rickroll")
window.geometry("800x600")

label = tk.Label(window, text="Texte à rickrolliser : ")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(window)
entry.grid(row=0, column=1, sticky="we")

button = tk.Button(window, text="Rickrolliser")
button.grid(row=0, column=2, sticky="e")

labelOutput = tk.Label(window, text="Sortie : ")
labelOutput.grid(row=1, column=0, sticky="w")

outputText = tk.Text(window, wrap=tk.WORD, height=2, width=30)
outputText.grid(row=1, column=1, sticky="nsew")

window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)

newText = ""

def setNewText(rawText) :
     newText = formatText(rawText)
     outputText.delete("1.0", "end")
     outputText.insert("1.0", newText)
     pyperclip.copy(newText)
     entry.delete(0, "end")

entry.bind("<Return>", lambda event : setNewText(entry.get()))
button.bind("<Button-1>", lambda event : setNewText(entry.get()))

entry.focus_set()
window.mainloop()