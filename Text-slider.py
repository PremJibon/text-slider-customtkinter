import customtkinter

root = customtkinter.CTk()
root.geometry("900x600")
root.title("Sliding Text Animation")

txt = "I'm Shahed Hossain Prem, a programming enthusiast rapidly mastering JavaScript and Python. My passion for coding drives me to create efficient solutions and innovate in web development, scripting, and application design."

count = 0
text = ''

label = customtkinter.CTkLabel(root,text=txt,font=("Arial",30),fg_color='white',text_color='red')
label.pack(pady=100)

def slider():
    global count,text
    if( count >= len(txt)):
        count = -1
        text =''
        label.configure(text=text)
    else:
        text = text + txt[count]
        label.configure(text=text)
    count +=1
    label.after(100,slider)
slider()

root.mainloop()