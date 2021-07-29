import tkinter as tk
app = tk.Tk(__name__)
app.title('Registration Form')
app.geometry('400x250')

## Create a files to store the data
with open('reg_entries.csv', 'w') as file:
    file.write('name,email,phone'+'\n')
    file.close()
    
## Variables to store form data
name = tk.Variable(app)
name.set('')
email = tk.Variable(app)
email.set('')
phone = tk.Variable(app)
phone.set('')
error = tk.Variable(app)
error.set('')

## Labels and Entries
tk.Label(app, text="Name", font=('Arial',15)).place(x=30,y=40)
tk.Entry(app, textvariable = name, font=('Arial',15)).place(x=100, y=40)

tk.Label(app, text="Email", font=('Arial',15)).place(x=30,y=80)
tk.Entry(app, textvariable = email, font=('Arial',15)).place(x=100, y=80)

tk.Label(app, text="Phone", font=('Arial',15)).place(x=30,y=120)
tk.Entry(app, textvariable = phone, font=('Arial',15)).place(x=100, y=120)

tk.Label(app, textvariable=error, fg='red').place(x=170, y=10)
error.set('')

## Store data, 
def submit():
    n = name.get()
    e = email.get()
    p = phone.get()
    entry = n + ',' + e + ',' + p + '\n'
    if n == '' or e == '' or p == '':
        error.set("Fill all filelds")
    elif not n.isalpha():
        error.set("Name Invalid")
    elif '@' not in e:
        error.set("Email Invalid")
    elif not p.isnumeric():
        error.set("Phone number Invalid")
    else:
        with open('reg_entries.csv', 'r') as file:
            content = file.read()
            file.close()
        if entry[entry.index(','):] in content:
            error.set("User already exists")
            file.close()
        else:
            with open('reg_entries.csv', 'a') as file:
                file.write(entry)
                file.close()
            error.set("Entry Succesful")
            print("Submission Successful")
            
## Display existing entries
def show_reg():
    with open('reg_entries.csv', 'r') as file:
        content = file.read()
        file.close()
    print('---------Registered Users----------')
    for entry in content.split('\n')[1:-1:]:
        print(entry.replace(',', ' | '))
    print('-----------End of File-------------')

## buttons
tk.Button(app, text='Submit', command=submit, font=('Arial',15)).place(x=100,y=160) #submit data
tk.Button(app, text='Show', command=show_reg, font=('Arial',15)).place(x=250,y=160) #Show registered entries

app.mainloop()

