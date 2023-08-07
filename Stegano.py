

from tkinter import*
from tkinter.filedialog import*
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox



def encode():
    main.destroy()
    enco=Tk()
    enco.title("Encode")
    enco.geometry("500x400+300+150")

    Label1=Label(text="Hidden message")
    Label1.place(relx=0.1,rely=0.1,height=20,width=100)

    entry=Entry()
    entry.place(relx=0.4,rely=0.1)
    Label2=Label(text="File name")
    Label2.place(relx=0.1,rely=0.2,height=20,width=100)
    
    entrysave=Entry()
    entrysave.place(relx=0.4,rely=0.2)

    def openfile():
         global fileopen
         fileopen=StringVar()
         file_path = filedialog.askopenfilename(initialdir="/Desktop",title="Select a file",filetypes=(("JPEG files", "*.jpg"), ("All files", "*.*")))
         label3=Label(text=fileopen)
         label3.place(relx=0.3,rely=0.3)
         

    def encode():
        response=messagebox.askyesno("pop up","do you want to encode")
        if response==1:
           
            stg.hide(fileopen,entrysave.get()*'.jpg',entry.get())
            messagebox.showinfo("pop up","successfully encoded")
        else:
            messagebox.showwarning("pop up","unsuccessful")

    buttonselect=Button(text="select file")
    buttonselect.place(relx=0.1,rely=0.3)

    buttoncode=Button(text="Encode")
    buttoncode.place(relx=0.4,rely=0.5)


main=Tk()
main.title("Image Steganography")
main.geometry("500x400+300+150")




encodeBut=Button(text="Encode",command=encode)
encodeBut.place(relx=0.3,rely=0.3,height=40,width=80)

decodeBut=Button(text="Decode")
decodeBut.place(relx=0.5,rely=0.3,height=40,width=80)
main.mainloop()
