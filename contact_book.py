from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("550x550+250+50")
root.title("Contact Book")
root.config(bg="light green")

def add_contact():
    name=e_name.get()
    number=e_number.get()
    email=e_email.get()
    address=e_address.get()
    if len(name)==0 or len(number)==0 or len(email)==0 or len(address)==0:
        messagebox.showerror("Error", "Please enter all the details")
    else:
        contact_list.insert(END, f"{name}  |  {number}  |  {email}  |  {address}")
        e_name.delete(0, "end")
        e_number.delete(0, "end")
        e_email.delete(0, "end")
        e_address.delete(0, "end")
    
def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")
        
def update_contact():
    try:
        data=contact_list.focus()
        dictionary=contact_list.item(data)
        data_list=dictionary["values"]
        
        name=str(data_list[0])
        number=str(data_list[0])
        email=str(data_list[0])
        address=str(data_list[0])
        
        e_name.insert(0, name)
        e_number.insert(0, number)
        e_email.insert(0, email)
        e_address.insert(0, address)
        
        def confirm():
            new_name=e_name.get()
            new_number=e_number.get()
            new_email=e_email.get()
            new_address=e_address.get()
            
            contact_list.insert(END, f"{new_name}  |  {new_number}  |  {new_email}  |  {new_address}")
            
            #update(contact_list)
            
            e_name.delete(0, "end")
            e_number.delete(0, "end")
            e_email.delete(0, "end")
            e_address.delete(0, "end")
            
            for widget in frame_3.winfo_children():
                widget.destroy()
                
            b_confirm=Button(frame_2, text="Confirm", width=10, height=1, font="Ivy 8 bold", bg="navy blue", fg="white", command=confirm)
            b_confirm.place(x=300, y=120)
            
    except IndexError:
        messagebox.showerror("Error","Select One of them")

def search_contact():
    e_number=e_search.get()
    data=search(e_number)
    
    def delete_command():
        contact_list.delete(contact_list.get_childrem())
        
        delete_command()
        
        for item in data:
            contact_list.insert("","end",Values=item)

def clear_contacts():
    contact_list.delete(0, END)

frame_1=Frame(root, width=550, height=100, bg="orange")
frame_1.grid(row=0, column=0, padx=0, pady=1)

frame_2=Frame(root, width=550, height=200, bg="white")
frame_2.grid(row=1, column=0, padx=0, pady=1)

frame_3=Frame(root, width=550, height=250, bg="white", relief="solid")
frame_3.grid(row=3, column=0, padx=1, pady=1)


name=Label(frame_1, text="Contact Book", font="ariel 20 bold", bg="orange", fg="black")
name.place(x=180, y=30)

l_name=Label(frame_2, text="Name *", font="Ivy 10", bg="white", fg="black", anchor=NW)
l_name.place(x=10, y=20)
e_name=Entry(frame_2, width=25, justify="left", highlightthickness=1, relief="solid")
e_name.place(x=110, y=20)
 
l_number=Label(frame_2, text="Phone Number *", font="Ivy 10", bg="white", fg="black", anchor=NW)
l_number.place(x=10, y=50)
e_number=Entry(frame_2, width=25, justify="left", highlightthickness=1, relief="solid")
e_number.place(x=110, y=50)

l_email=Label(frame_2, text="Email id *", font="Ivy 10", bg="white", fg="black", anchor=NW)
l_email.place(x=10, y=80)
e_email=Entry(frame_2, width=25, justify="left", highlightthickness=1, relief="solid")
e_email.place(x=110, y=80)

l_address=Label(frame_2, text="Address *", font="Ivy 10", bg="white", fg="black", anchor=NW)
l_address.place(x=10, y=110)
e_address=Entry(frame_2, width=25, justify="left", highlightthickness=1, relief="solid")
e_address.place(x=110, y=110)

b_search=Button(frame_2, text="Search", height=1, font="Ivy 8 bold", bg="navy blue", fg="white", command=search_contact)
b_search.place(x=290, y=20)
e_search=Entry(frame_2, width=16, font="Ivy 11", justify="left", highlightthickness=1, relief="solid")
e_search.place(x=350, y=20)

b_clear_all=Button(frame_2, text="Clear All", width=12, height=2, font="Ivy 10 bold", bg="sky blue", fg="black", command=clear_contacts)  
b_clear_all.place(x=300, y=50)

b_add=Button(frame_2, text="Add", width=12, height=2, font="Ivy 10 bold", bg="sky blue", fg="black", command=add_contact)
b_add.place(x=420, y=50)

b_update=Button(frame_2, text="Update", width=12, height=2, font="Ivy 10 bold", bg="sky blue", fg="black", command=update_contact)
b_update.place(x=420, y=100)

b_delete=Button(frame_2, text="delete", width=12, height=2, font="Ivy 10 bold", bg="sky blue", fg="black", command=delete_contact)
b_delete.place(x=300, y=100)

contact_list = Listbox(frame_3,width=40, height=10,font="times 14", bd=1, fg='#464646', highlightthickness=0, selectbackground='#a6a6a6', activestyle="underline")
contact_list.pack(side=LEFT, fill=BOTH)

root.mainloop()