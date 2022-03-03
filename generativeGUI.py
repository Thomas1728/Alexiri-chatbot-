import tkinter
from tkinter import *

def evaluateInput(encoder, decoder, searcher, voc):
    input_sentence = ''
#     while(1):
    try:
        # Get input sentence
        input_sentence = EntryBox.get("1.0",'end-1c').strip()
        EntryBox.delete("0.0",END)
        # Check if it is quit case
#         if input_sentence == 'q' or input_sentence == 'quit': break
        # Normalize sentence
        input_sentence = normalizeString(input_sentence)
        # Evaluate sentence
        output_words = evaluate(encoder, decoder, searcher, voc, input_sentence)
        # Format and print response sentence
        output_words[:] = [x for x in output_words if not (x == 'EOS' or x == 'PAD')]
#         print('human:', input_sentence)
#         print('Bot:', ' '.join(output_words))
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + input_sentence + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        ChatLog.insert(END, "Bot: " + ' '.join(output_words) + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    except KeyError:
        print("Error: Encountered unknown word.")
        
base = Tk()
base.title("ChatBot - SL")
base.geometry("400x500")
base.resizable(width=TRUE, height=TRUE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)
#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= lambda: evaluateInput(encoder,decoder,searcher,voc) )
#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")

scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()