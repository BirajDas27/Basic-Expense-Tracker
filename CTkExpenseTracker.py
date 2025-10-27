import os
import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode = "system"
theme_path = os.path.join(os.path.dirname(__file__), "theme.json")
ctk.set_default_color_theme(theme_path)

app = ctk.CTk()

app.title('Expense Tracker')
app.geometry('890x590')
app.configure(fg_color = "#BCDCE6")
app.resizable(True, True)

class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.msg = ''

    def add_expense(self, expense):
        if not os.path.exists('expenses.csv'):
            with open('expenses.csv', 'w') as file:
                file.write(f'1,{expense.date},{expense.description},{expense.amount}\n')
            self.msg = 'File not found — created new file and added expense.'
            return 
        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            last_index = len(lines)
        with open('expenses.csv', 'a') as file:
            file.write(f'{last_index+1},{expense.date},{expense.description},{expense.amount}\n')
        self.msg = 'Expense added successfully.'
        return

    def view_expense(self):
        if not os.path.exists('expenses.csv'):
            self.msg = 'No file named expenses found in common directory.'
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

            if len(lines) == 0:
                self.msg = 'No expense found, your expense list is empty.'
                return
            self.msg = 'Successfully extracted expenses.'
            return
            
    def update_expense(self):
        if not os.path.exists('expenses.csv'):
            self.msg = 'No file named expenses found in common directory.'
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                self.msg = 'No expense found, your expense list is empty.'
                return

            else:
                self.msg = 'OK'
                
    def remove_expense(self):
        if not os.path.exists('expenses.csv'):
            self.msg = 'No file named expenses found in common directory.'
            return

        updated_list = []
        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

        if len(lines) == 0:
            self.msg = 'No expense found, your expense list is empty.'
            return

        else:
            self.msg = 'OK'

    def search_expense(self):
        if not os.path.exists('expenses.csv'):
            self.msg = 'No file named expenses found in common directory.'
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                self.msg = 'No expense found, your expense list is empty.'
                return
            else:
                self.msg = 'OK'
                
    def sort_expense(self):
        if not os.path.exists('expenses.csv'):
            self.msg = 'No file named expenses found in common directory.'
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                self.msg = 'No expense found, your expense list is empty.'
                return
            else:
                self.msg = 'OK'
                # sorted = []
                # for line in lines:
                #     parts = line.strip().split(',')
                #     idx, date, description, amount = parts
                #     sorted.append([int(idx), date, description, float(amount)])
                    
                # opt = input('\nSort the amount(asce/desc): ').lower().strip()
                # reverse = True if opt == 'desc' else False
                # sorted.sort(key = lambda x: x[3], reverse = reverse)

                # for i, row in enumerate(sorted, start = 1):
                #     row[0] = i

                # headers = ['Index', 'date', 'description', 'Amount']
                # print(tabulate(sorted, headers = headers, tablefmt = 'grid'))

navbar = ctk.CTkFrame(app,
    width = 900,
    height = 200,
    fg_color = '#2b6777',
)
navbar.pack()

my_label = ctk.CTkLabel(navbar,
    text = "Expense Tracker",
    font = ("Helvetica", 25, "bold"),
    text_color = "white",
    padx = 900,
    pady = 15

)
my_label.pack()

sidebar = ctk.CTkFrame(app,
    fg_color = '#52ab98',
    width = 60,
    corner_radius = 15,
    height = 700,
    border_width = 1,
    border_color = "#87C3D4",
)
sidebar.pack(padx = (15, 0), pady = (15, 20), side = 'left')

inner_sidebar = ctk.CTkFrame(sidebar,
    fg_color = 'transparent',
    corner_radius = 20,
    width = 60,
    height = 600
)
inner_sidebar.pack(padx = 2,pady = 30)

image_path = "screenshots/icons/wallet.png"
my_image = Image.open(image_path)
add_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/search.png"
my_image = Image.open(image_path)
view_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/changes.png"
my_image = Image.open(image_path)
update_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/trash.png"
my_image = Image.open(image_path)
remove_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

# image_path = "screenshots/icons/sum.png"
# my_image = Image.open(image_path)
# total_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/magnifier.png"
my_image = Image.open(image_path)
search_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/sort.png"
my_image = Image.open(image_path)
sort_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/calendar.png"
my_image = Image.open(image_path)
periodic_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/refresh.png"
my_image = Image.open(image_path)
refresh_icon = ctk.CTkImage(light_image=my_image, size=(15, 15))


tracker = ExpenseTracker()


def add_on_enter(event):
    hover_desc.configure(text = "Add expense", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def add_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def add():
    title.configure(text = 'Add new expense')

    for widget in container2.winfo_children():
        widget.destroy()

    form_frame = ctk.CTkFrame(container2, fg_color="transparent")
    form_frame.pack(pady=(40, 10))

    #Date
    date_label = ctk.CTkLabel(
        form_frame, 
        text="Enter date:", 
        font = ("Helvetica", 13, 'bold')
    )
    date_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'e')
    date_entry = ctk.CTkEntry(
        form_frame, 
        placeholder_text="YYYY-MM-DD",
        width = 200,
        font = ('Helvetica', 12, 'bold')
    )
    date_entry.grid(row = 0, column = 1)

    # Category
    description_label = ctk.CTkLabel(
        form_frame, 
        text="Enter category:", 
        font = ("Helvetica", 13, 'bold')
    )
    description_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'e')
    description_entry = ctk.CTkEntry(
        form_frame, 
        placeholder_text="Eg grocery",
        width=200,
        font = ('Helvetica', 12, 'bold')
    )
    description_entry.grid(row = 1, column = 1)

    # Amount
    amount_label = ctk.CTkLabel(
        form_frame, 
        text="Enter amount:", 
        font = ("Helvetica", 13, 'bold')
    )
    amount_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'e')
    amount_entry = ctk.CTkEntry(
        form_frame, 
        placeholder_text="xxxxx",
        width=200,
        font = ('Helvetica', 12, 'bold')
    )
    amount_entry.grid(row = 2, column = 1)

    new_input = ctk.CTkFrame(
        container2,
        border_width=1,
        corner_radius=5,
        border_color="black",
        fg_color='white'
    )

    def insertion():
        try:
            date = date_entry.get().strip()
            description = description_entry.get().strip().lower()
            amount = float(amount_entry.get().strip())
            expense = Expense(date, description, amount)
            tracker.add_expense(expense) 
            notice.configure(
                text=tracker.msg, 
                text_color='green'
            ) 
            date_entry.delete(0, 'end') 
            description_entry.delete(0, 'end') 
            amount_entry.delete(0, 'end')

            for widget in new_input.winfo_children():
                widget.destroy()

            new_input.pack(padx=100, pady=(0, 15), fill='x')            #defined outside to renew the new input with latest

            date_label = ctk.CTkLabel(
                new_input, 
                text=date,
                font=("Helvetica", 13), 
                width=100, 
                anchor='w',
            )
            date_label.grid(row=0, column=0, padx=(50, 10), pady=5, sticky='w')

            desc_label = ctk.CTkLabel(
                new_input, 
                text=description,
                font=("Helvetica", 13), 
                width=200, 
                anchor='w'
            )
            desc_label.grid(row=0, column=1, padx=10, pady=5, sticky='nesw')

            amt_label = ctk.CTkLabel(
                new_input, 
                text = f"₹{amount:.2f}",
                font=("Helvetica", 13, 'bold'), 
                width=140, 
                anchor='e'
            )
            amt_label.grid(row=0, column=2, padx=10, pady=5, sticky='e')
        except ValueError: 
            notice.configure(text='Please enter a valid amount!', text_color='red')

    insert_button = ctk.CTkButton(
        container2, 
        text="ADD", 
        font = ('Helvetica', 15, 'bold'),
        height = 30,
        width = 200,
        command=insertion
    )
    insert_button.pack(pady=5)

    notice = ctk.CTkLabel(
        container2, 
        text="", 
        text_color="green",
        font = ('Helvetica', 14, 'bold')
    )
    notice.pack(pady=(10, 10))

    footer = ctk.CTkFrame(
        container2,
        height = 5,
        width = 300,
        
    )
    footer.place(relx = 0.3, rely = 0.95)


add_button = ctk.CTkButton(
    inner_sidebar,
    image = add_icon,
    text="",
    fg_color="transparent",
    bg_color="transparent",
    width=50,
    height=40,
    hover_color="#2b6777",
    command = add
)
add_button.pack(pady = 12)
add_button.bind("<Enter>", add_on_enter)
add_button.bind("<Leave>", add_on_leave)

def view_on_enter(event):
    hover_desc.configure(text = "View expenses", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def view_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def view():
    title.configure(text = 'View expenses')

    for widget in container2.winfo_children():
        widget.destroy()

    def viewing():
        total_amount = 0
        def clear_csv():
            with open('expenses.csv', 'w') as file:
                pass
            notice.configure(text = 'All expenses deleted successfully.', text_color = 'Red')

            for widget in container2.winfo_children():
                if widget == notice:
                    continue
                else:
                    widget.destroy()

        tracker.view_expense()
        button.destroy()

        notice.configure(
            text=tracker.msg,
            text_color='green' if tracker.msg == 'Successfully extracted expenses.' else 'red'
        )

        del_button = ctk.CTkButton(
            container2,
            text='Delete all',
            fg_color='red',
            hover_color='#9C2007',
            font=('Helvetica', 13, 'bold'),
            command=clear_csv
        )

        if tracker.msg == 'Successfully extracted expenses.':
            del_button.place(x=618, y=10)
        else:
            del_button.place_forget()
            return

        if tracker.msg != 'Successfully extracted expenses.':
            return

        header = ctk.CTkFrame(
            container2,
            height = 55,
            fg_color = '#84B6D9'
        )
        header.pack(padx = 10, pady = (5, 0), fill = 'x')

        headings = ['INDEX', 'DATE', 'DESCRIPTION', 'AMOUNT']
        for i, text in enumerate(headings):
            ctk.CTkLabel(
                header,
                text=text,
                justify='center',
                text_color='black',
                font=('Helvetica', 14, 'bold'),
                fg_color='transparent',
            ).grid(row=0, column=i, padx=60)
        view_frame = ctk.CTkScrollableFrame(
            container2,
            fg_color = 'white',
            height =250
        )
        view_frame.pack(padx = (10, 10), pady=(0, 5), fill = 'both')

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

        for line in lines:
            row = line.strip().split(',')
            total_amount += float(row[3])
            ctk.CTkLabel(
                view_frame,
                text = row[0],
                font = ('Helvetica', 13, 'bold')
            ).grid(row = int(row[0]), column = 0, padx = (67, 60))
            ctk.CTkLabel(
                view_frame,
                text = row[1],
                font = ('Helvetica', 13, 'bold')
            ).grid(row = int(row[0]), column = 1, padx = (63, 60))
            ctk.CTkLabel(
                view_frame,
                text = row[2],
                font = ('Helvetica', 13, 'bold')
            ).grid(row = int(row[0]), column = 2, padx = (42, 60))
            ctk.CTkLabel(
                view_frame,
                text = row[3],
                font = ('Helvetica', 13, 'bold')
            ).grid(row = int(row[0]), column = 3, padx = (62, 0))

        total = ctk.CTkFrame(
            container2,
            fg_color = 'transparent'
        )
        total.pack(pady = 5, anchor = 'e')
        total_label = ctk.CTkLabel(
            total,
            text = 'Total expenditure',
            text_color = 'black',
            font = ('Helvetica', 15, 'bold'),

        )
        total_label.grid(row = 0, column = 0)
        total_amt = ctk.CTkLabel(
            total,
            text = f'₹ {total_amount:.2f}',
            font = ('Helvetica', 15, 'bold'),
            text_color = 'green'
        )
        total_amt.grid(row = 0, column = 1, padx = (20, 10))
            
    button = ctk.CTkButton(
        container2, 
        text="Extract", 
        font = ('Helvetica', 15, 'bold'),
        height = 30,
        width = 150,
        command=viewing
    )
    button.pack(pady=15)

    notice = ctk.CTkLabel(
        container2,
        text="",
        text_color="green",
        font=('Helvetica', 14, 'bold')
    )
    notice.pack(pady=(15, 0))

    footer = ctk.CTkFrame(
        container2,
        height = 5,
        width = 300,
    )
    footer.place(relx = 0.3, rely = 0.95)

view_button = ctk.CTkButton(
    inner_sidebar,
    image = view_icon,
    text="",
    fg_color="transparent",
    bg_color="transparent",
    width=50,
    height=40,
    hover_color="#2b6777",
    command = view
)
view_button.pack(pady = 12)
view_button.bind("<Enter>", view_on_enter)
view_button.bind("<Leave>", view_on_leave)

def update_on_enter(event):
    hover_desc.configure(text = "Update expense", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def update_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def update():
    title.configure(text = 'Update expense')

    for widget in container2.winfo_children():
        widget.destroy()

    tracker.update_expense()

    notice = ctk.CTkLabel(
        container2,
        text = tracker.msg,
        text_color = 'red',
        font=('Helvetica', 14, 'bold')

    )

    if tracker.msg == 'OK':
        notice.place_forget()
    else:
        notice.pack(pady = (15, 0))

    if tracker.msg != 'OK':
        footer = ctk.CTkFrame(
            container2,
            height = 5,
            width = 300,
        )
        footer.place(relx = 0.3, rely = 0.95)
        return

    header = ctk.CTkFrame(
            container2,
            height = 55,
            fg_color = '#84B6D9'
        )
    header.pack(padx = 10, pady = (10, 0), fill = 'x')

    headings = ['INDEX', 'DATE', 'DESCRIPTION', 'AMOUNT']
    for i, text in enumerate(headings):
        ctk.CTkLabel(
            header,
            text=text,
            justify='center',
            text_color='black',
            font=('Helvetica', 14, 'bold'),
            fg_color='transparent',
        ).grid(row=0, column=i, padx=60)
    view_frame = ctk.CTkScrollableFrame(
        container2,
        fg_color = 'white',
        height =30
    )
    view_frame.pack(padx = (10, 10), pady=(0, 5), fill = 'both')
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
    for line in lines:
        row = line.strip().split(',')
        ctk.CTkLabel(
            view_frame,
            text = row[0],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 0, padx = (67, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[1],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 1, padx = (63, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[2],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 2, padx = (42, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[3],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 3, padx = (62, 0))

    idx_frame = ctk.CTkFrame(
        container2,
        width = 500,
        fg_color = 'transparent'
    )
    idx_frame.pack(pady = 10)

    ctk.CTkLabel(
        idx_frame,
        text = 'Enter index to update expense: ',
        font = ('Helvetica', 13, 'bold')
    ).grid(row = 0, column = 0, padx = (0, 5))

    idx_value = ctk.CTkEntry(
        idx_frame,
        font = ('Helvetica', 12, 'bold')
    )
    idx_value.grid(row = 0, column = 1)

    def call():
        try:
            i = int(idx_value.get())
        except ValueError:
            notice1.configure(text='Please enter a numeric index.', text_color='red')
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

        if 0 < i <= len(lines):
            notice1.configure(text = 'Found your expense!', text_color = 'green')
            idx_frame.destroy()
            idx_button.destroy()
            form_frame = ctk.CTkFrame(
                container2,
                fg_color = 'transparent'
            )
            form_frame.pack(pady = (10, 0))
            date = ctk.CTkLabel(
                form_frame,
                text = 'Date:',
                font = ('Helvetica', 13, 'bold')
            )
            date.grid(row = 0, column = 0, padx = (0, 10), sticky = 'e')
            date_entry = ctk.CTkEntry(
                form_frame,
                placeholder_text = 'YYYY-MM-DD',
                font = ('Helvetica', 12, 'bold')
            )
            date_entry.grid(row = 0, column = 1)

            description = ctk.CTkLabel(
                form_frame,
                text = 'Description:',
                font = ('Helvetica', 13, 'bold')
            )
            description.grid(row = 1, column = 0, padx = (0, 10), sticky = 'e')
            desc_entry = ctk.CTkEntry(
                form_frame,
                placeholder_text = 'Eg travel',
                font = ('Helvetica', 12, 'bold')
            )
            desc_entry.grid(row = 1, column = 1)

            amount = ctk.CTkLabel(
                form_frame,
                text = 'Amount:',
                font = ('Helvetica', 13, 'bold')
            )
            amount.grid(row = 2, column = 0, padx = (0, 10), sticky = 'e')
            amt_entry = ctk.CTkEntry(
                form_frame,
                placeholder_text = 'xxxxx',
                font = ('Helvetica', 12, 'bold')
            )
            amt_entry.grid(row = 2, column = 1)

            def submit_update():
                try:
                    date = date_entry.get()
                    description = desc_entry.get()
                    amount = float(amt_entry.get())

                    lines[i-1] = f'{i},{date},{description},{amount}\n'
                    with open('expenses.csv', 'w') as file:
                        file.writelines(lines)
                    notice1.configure(text = 'Your expense is successfully edited', text_color = 'green')

                except ValueError:
                    notice1.configure(text = 'Invalid inputs', text_color = 'red')

            buttons = ctk.CTkFrame(
                container2,
                fg_color = 'transparent'
            )
            buttons.pack(pady = 5)

            submit_button = ctk.CTkButton(
                buttons,
                text = 'SUBMIT',
                font = ('Helvetica', 12, 'bold'),
                command = submit_update
            )
            submit_button.grid(row = 0, column = 0)

            refresh_button = ctk.CTkButton(
                buttons,
                text = '',
                image = refresh_icon,
                width = 10,
                command = update
            )
            refresh_button.grid(row = 0, column = 1, padx = (5, 0))
        
        else:
            notice1.configure(text = 'Invalid indexing', text_color = 'red')

    idx_button = ctk.CTkButton(
        container2,
        text = 'SUBMIT',
        command = call,
         font = ('Helvetica', 12, 'bold')
    )
    idx_button.pack(pady = 10)

    notice1 = ctk.CTkLabel(
        container2,
        text = '',
        font = ("Helvetica", 13, 'bold')
    )
    notice1.pack(pady = (10, 0))

update_button = ctk.CTkButton(
    inner_sidebar,
    image = update_icon,
    text="",
    fg_color="transparent",
    bg_color="transparent",
    width=50,
    height=40,
    hover_color="#2b6777",
    command = update
)
update_button.pack(pady = 12)
update_button.bind("<Enter>", update_on_enter)
update_button.bind("<Leave>", update_on_leave)


def remove_on_enter(event):
    hover_desc.configure(text = "Remove expense", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def remove_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def remove():
    title.configure(text = 'Delete expense')

    for widget in container2.winfo_children():
        widget.destroy()

    tracker.remove_expense()

    notice = ctk.CTkLabel(
        container2,
        text = tracker.msg,
        text_color= 'red',
        font=('Helvetica', 14, 'bold')
    )

    if tracker.msg == 'OK':
        notice.place_forget()
    else:
        notice.pack(pady = (15, 0))

    if tracker.msg != 'OK':
        footer = ctk.CTkFrame(
            container2,
            height = 5,
            width = 300,
        )
        footer.place(relx = 0.3, rely = 0.95)
        return

    header = ctk.CTkFrame(
            container2,
            height = 55,
            fg_color = '#84B6D9'
        )
    header.pack(padx = 10, pady = (10, 0), fill = 'x')

    headings = ['INDEX', 'DATE', 'DESCRIPTION', 'AMOUNT']
    for i, text in enumerate(headings):
        ctk.CTkLabel(
            header,
            text=text,
            justify='center',
            text_color='black',
            font=('Helvetica', 14, 'bold'),
            fg_color='transparent',
        ).grid(row=0, column=i, padx=60)
    view_frame = ctk.CTkScrollableFrame(
        container2,
        fg_color = 'white',
        height =30
    )
    view_frame.pack(padx = (10, 10), pady=(0, 5), fill = 'both')
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
    for line in lines:
        row = line.strip().split(',')
        ctk.CTkLabel(
            view_frame,
            text = row[0],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 0, padx = (67, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[1],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 1, padx = (63, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[2],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 2, padx = (42, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[3],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 3, padx = (62, 0))

    def remove_expense():
        try:
            i = int(idx_value.get())
        except ValueError:
            notice1.configure(text = 'Invalid input. Please enter a number.')
            return

        if 0 < i <= len(lines):
            del lines[i - 1]
            for i, line in enumerate(lines, start = 1):
                if len(line.split(',')) == 4:
                    index, date, description, amount = line.split(',')
                else:
                    date, description, amount = line.split(',')

                if i == 1:
                    with open('expenses.csv', 'w') as file:
                        new_lines = (f'{i},{date},{description},{amount}')
                        file.writelines(new_lines)
                else:
                    with open('expenses.csv', 'a') as file:
                        new_lines = (f'{i},{date},{description},{amount}')
                        file.write(new_lines)

            notice1.configure(text = 'Expense removed successfully.')
        else:
            notice1.configure(text = 'Index out of range.')
        
    idx_frame = ctk.CTkFrame(
        container2,
        width = 500,
        fg_color = 'transparent'
    )
    idx_frame.pack(pady = 10)

    ctk.CTkLabel(
        idx_frame,
        text = 'Enter index to remove expense:',
        font = ('Helvetica', 13, 'bold')
    ).grid(row = 0, column = 0, padx = (0, 5))

    idx_value = ctk.CTkEntry(
        idx_frame,
        font = ('Helvetica', 12, 'bold')
    )
    idx_value.grid(row = 0, column = 1)

    buttons = ctk.CTkFrame(
        container2,
        fg_color = 'transparent'
    )
    buttons.pack(pady = 5)

    button = ctk.CTkButton(
        buttons,
        text = 'DELETE',
        fg_color = 'red',
        font = ('Helvetica', 13, 'bold'),
        command = remove_expense
    )
    button.grid(row = 0, column = 0)

    refresh_button = ctk.CTkButton(
        buttons,
        text = '',
        image = refresh_icon,
        width = 10,
        command = remove
    )
    refresh_button.grid(row = 0, column = 1, padx = (5, 0))

    notice1 = ctk.CTkLabel(
        container2,
        text = '',
        text_color= 'red',
        font=('Helvetica', 14, 'bold')
    )
    notice1.pack(pady = 5)

    footer = ctk.CTkFrame(
        container2,
        height = 5,
        width = 300,
    )
    footer.place(relx = 0.3, rely = 0.95)
    return

remove_button = ctk.CTkButton(
    inner_sidebar,
    image = remove_icon,
    text="",
    fg_color="transparent",
    bg_color="transparent",
    width=50,
    height=40,
    hover_color="#2b6777",
    command = remove
)
remove_button.pack(pady = 12)
remove_button.bind("<Enter>", remove_on_enter)
remove_button.bind("<Leave>", remove_on_leave)


# def total_on_enter(event):
#     hover_desc.configure(text = "Total expense", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

# def total_on_leave(event):
#     hover_desc.configure(text = '', fg_color = 'transparent')

# def total():
#     title.configure(text = 'Total expense')

#     for widget in container2.winfo_children():
#         widget.destroy()

# total_button = ctk.CTkButton(
#     inner_sidebar,
#     image = total_icon,
#     text="",
#     fg_color="transparent",
#     bg_color="transparent",
#     width=50,
#     height=40,
#     hover_color="#2b6777",
#     command = total
# )
# total_button.pack(pady = 7)
# total_button.bind("<Enter>", total_on_enter)
# total_button.bind("<Leave>", total_on_leave)


def search_on_enter(event):
    hover_desc.configure(text = "Search expenses", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def search_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def search():
    title.configure(text = 'Search category')

    for widget in container2.winfo_children():
        widget.destroy()

    tracker.search_expense()

    notice = ctk.CTkLabel(
        container2,
        text = tracker.msg,
        text_color= 'red',
        font=('Helvetica', 14, 'bold')
    )

    if tracker.msg == 'OK':
        notice.place_forget()
    else:
        notice.pack(pady = (15, 0))

    if tracker.msg != 'OK':
        footer = ctk.CTkFrame(
            container2,
            height = 5,
            width = 300,
        )
        footer.place(relx = 0.3, rely = 0.95)
        return

    categories = []
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        row = line.strip().split(',')
        if row[2] not in categories:
            categories.append(row[2])
        else:
            continue

    table = ctk.CTkFrame(
        container2,
        width = 800,
        fg_color = 'transparent'
    )
    table.pack(pady = 2, anchor = 'w')

    header = ctk.CTkFrame(
        table,
        height=55,
        fg_color='#84B6D9'
    )
    header.pack(padx=10, pady=(10, 0), fill='x', expand = True)

    headings = ['INDEX', 'DATE', 'DESCRIPTION', 'AMOUNT']
    for i, text in enumerate(headings):
        ctk.CTkLabel(
            header,
            text=text,
            justify='center',
            text_color='black',
            font=('Helvetica', 14, 'bold'),
            fg_color='transparent',
        ).grid(row=0, column=i, sticky='nsew', pady=5)

    for i in range(4):
        header.grid_columnconfigure(i, weight=1, uniform='col')

    view_frame = ctk.CTkScrollableFrame(
        table,
        fg_color='white',
        height=150,
        width = 550
    )
    view_frame.pack(padx=10, pady=(0, 5), fill='x', expand = True)

    for i in range(4):
        view_frame.grid_columnconfigure(i, weight=1, uniform='col')

    with open('expenses.csv', 'r') as file:
        lines = file.readlines()

    for idx, line in enumerate(lines):
        row = line.strip().split(',')
        for j, value in enumerate(row):
            ctk.CTkLabel(
                view_frame,
                text=value,
                font=('Helvetica', 13, 'bold'),
                justify='center'
            ).grid(row=idx, column=j, sticky='nsew', pady=2, padx = 30)

    def show_table(category=None):
        if not category:
            notice1.configure(text='Please enter a category to search.')
            total_label.configure(text = '')
            total_amt.configure(text = '')
            return

        elif category not in categories:
            notice1.configure(text=f'"{category}" not found in your expense list.')
            total_label.configure(text = '')
            total_amt.configure(text = '')
            return

        else:
            notice1.configure(text='')

        for widget in table.winfo_children():
            widget.destroy()

        header = ctk.CTkFrame(
            table,
            height=55,
            fg_color='#84B6D9'
        )
        header.pack(padx=10, pady=(10, 0), fill='x')

        headings = ['INDEX', 'DATE', 'DESCRIPTION', 'AMOUNT']
        for i, text in enumerate(headings):
            ctk.CTkLabel(
                header,
                text=text,
                justify='center',
                text_color='black',
                font=('Helvetica', 14, 'bold'),
                fg_color='transparent',
            ).grid(row=0, column=i, sticky='nsew', pady=5)

        for i in range(4):
            header.grid_columnconfigure(i, weight=1, uniform='col')

        view_frame = ctk.CTkScrollableFrame(
            table,
            fg_color='white',
            height=150,
            width = 550
        )
        view_frame.pack(padx=10, pady=(0, 5), fill='both')

        for i in range(4):
            view_frame.grid_columnconfigure(i, weight=1, uniform='col')

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

        filtered_lines = []
        total_cost = 0
        for line in lines:
            row = line.strip().split(',')
            if category is None or row[2] == category:
                filtered_lines.append(row)
                total_cost += float(row[3])

        for idx, row in enumerate(filtered_lines):
            for j, value in enumerate(row):
                ctk.CTkLabel(
                    view_frame,
                    text=value,
                    font=('Helvetica', 13, 'bold'),
                    justify='center'
                ).grid(row=idx, column=j, sticky='nsew', pady=2)

        total_label.configure(text = f'Total spent:')
        total_amt.configure(text = f'₹ {total_cost}')

    scroll_area = ctk.CTkScrollableFrame(container2, width = 130,  height=390, fg_color='white')
    scroll_area.place(relx=0.78, rely=0.03)

    for button in categories:
        ctk.CTkButton(
            scroll_area,
            text = button,
            font = ('Helvetica', 13, 'bold'),
            command = lambda b=button: show_table(b)
        ).pack(padx = 0, pady = 5, expand = True)

    container3 = ctk.CTkFrame(
        container2,
        fg_color = 'transparent'
    )
    container3.pack(pady = 5, anchor = 'w')

    search_category = ctk.CTkFrame(container3, fg_color = 'transparent')
    search_category.grid(padx = 5, pady = 5, sticky = 'w', row = 0, column = 0)

    search_entry = ctk.CTkEntry(
        search_category, 
        placeholder_text = 'Eg grocery', 
        font = ('Helvetica', 12, 'bold'), 
        width = 200
    )
    search_entry.grid(row = 0, column = 0, padx = 5)
    search_button = ctk.CTkButton(
        search_category, 
        text = 'SEARCH', 
        command = lambda: show_table(search_entry.get().strip().lower()), 
        width = 80, 
        font = ('Helvetica', 12, 'bold')
    )
    search_button.grid(row = 0, column = 1)

    total = ctk.CTkFrame(
        container3,
        fg_color = 'transparent'
    )
    total.grid(padx = (130, 0), pady = 5, sticky = 'w', row = 0, column = 1)

    total_label = ctk.CTkLabel(
        total,
        text = '',
        font = ('Helvetica', 13, 'bold')
    )
    total_label.grid(row = 0, column = 0, padx = (0, 10))
    total_amt = ctk.CTkLabel(
        total,
        text = '',
        text_color = 'green',
        font = ('Helvetica', 13, 'bold')
    )
    total_amt.grid(row = 0, column = 1)


    notice1 = ctk.CTkLabel(
        container2,
        text = '',
        text_color = 'red',
        font = ('Helvetica', 13, 'bold')
    )
    notice1.pack(padx = 10,pady = 5, anchor = 'w')

search_button = ctk.CTkButton(
    inner_sidebar,
    image = search_icon,
    text="",
    fg_color="transparent",
    bg_color="transparent",
    width=50,
    height=40,
    hover_color="#2b6777",
    command = search
)
search_button.pack(pady = 12)
search_button.bind("<Enter>", search_on_enter)
search_button.bind("<Leave>", search_on_leave)


def sort_on_enter(event):
    hover_desc.configure(text = "Sort expenses", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def sort_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def sort():
    title.configure(text = 'Sort expense')

    for widget in container2.winfo_children():
        widget.destroy()

    tracker.sort_expense()

    notice = ctk.CTkLabel(
        container2,
        text = tracker.msg,
        text_color= 'red',
        font=('Helvetica', 14, 'bold')
    )

    if tracker.msg == 'OK':
        notice.place_forget()
    else:
        notice.pack(pady = (15, 0))

    if tracker.msg != 'OK':
        footer = ctk.CTkFrame(
            container2,
            height = 5,
            width = 300,
        )
        footer.place(relx = 0.3, rely = 0.95)
        return

    header = ctk.CTkFrame(
            container2,
            height = 55,
            fg_color = '#84B6D9'
        )
    header.pack(padx = 10, pady = (20, 0), fill = 'x')

    headings = ['INDEX', 'DATE', 'DESCRIPTION', 'AMOUNT']
    for i, text in enumerate(headings):
        ctk.CTkLabel(
            header,
            text=text,
            justify='center',
            text_color='black',
            font=('Helvetica', 14, 'bold'),
            fg_color='transparent',
        ).grid(row=0, column=i, padx=60)
    view_frame = ctk.CTkScrollableFrame(
        container2,
        fg_color = 'white',
        height =30
    )
    view_frame.pack(padx = (10, 10), pady=(0, 5), fill = 'both')
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
    for line in lines:
        row = line.strip().split(',')
        ctk.CTkLabel(
            view_frame,
            text = row[0],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 0, padx = (67, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[1],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 1, padx = (63, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[2],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 2, padx = (42, 60))
        ctk.CTkLabel(
            view_frame,
            text = row[3],
            font = ('Helvetica', 13, 'bold')
        ).grid(row = int(row[0]), column = 3, padx = (62, 0))

    sorting_frame = ctk.CTkFrame(
        container2,
        fg_color = 'transparent'
    )
    sorting_frame.pack(pady = 20)

    notice1 = ctk.CTkLabel(
        container2,
        text = '',
        text_color = 'Green',
        font = ('Helvetica', 13, 'bold')
    )

    def sorting(choice):
        if choice == 1:
            notice1.configure(text = 'The list is sorted in ascending order.')
        else:
            notice1.configure(text = 'The list is sorted in descending order.')

    asc_button = ctk.CTkButton(
        sorting_frame,
        text = 'Ascending',
        text_color = 'black',
        fg_color = '#84B6D9',
        hover_color = '#82A4BA',
        font = ('Helvetica', 15, 'bold'),
        command = lambda: sorting(1)
    )
    asc_button.grid(row = 0, column = 0, padx = 5)

    des_button = ctk.CTkButton(
        sorting_frame,
        text = 'Descending',
        text_color = 'black',
        fg_color = '#84B6D9',
        hover_color = '#82A4BA',
        font = ('Helvetica', 15, 'bold'),
        command = lambda: sorting(2)
    )
    des_button.grid(row = 0, column = 1,padx = 5)

    
    notice1.pack(pady = 20)

sort_button = ctk.CTkButton(
    inner_sidebar,
    image = sort_icon,
    text="",
    fg_color="transparent",
    bg_color="transparent",
    width=50,
    height=40,
    hover_color="#2b6777",
    command = sort
)
sort_button.pack(pady = 12)
sort_button.bind("<Enter>", sort_on_enter)
sort_button.bind("<Leave>", sort_on_leave)


def periodic_on_enter(event):
    hover_desc.configure(text = "Periodic expenses", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def periodic_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def periodic():
    title.configure(text = 'periodic button pressed')

periodic_button = ctk.CTkButton(
    inner_sidebar,
    image = periodic_icon,
    text="",
    fg_color="transparent",
    bg_color="transparent",
    width=50,
    height=40,
    hover_color="#2b6777",
    command = periodic
)
periodic_button.pack(pady = 12)
periodic_button.bind("<Enter>", periodic_on_enter)
periodic_button.bind("<Leave>", periodic_on_leave)
    


main_container = ctk.CTkFrame(app,
    border_width = 1,
    border_color = "#2b6777",
    corner_radius = 15,
    fg_color = "#f2f2f2",
    height = 600
)
main_container.pack(padx = (15, 15), pady = (15, 20), fill = 'both')
main_container.pack_propagate(False)

title_bar = ctk.CTkFrame(
    main_container,
    fg_color = '#82A4BA',
    height = 45
)
title_bar.pack(padx = (0, 0), pady = (0, 0), fill = 'both')
title_bar.pack_propagate(False)

hover_desc = ctk.CTkLabel(
    title_bar,
    text="",
    corner_radius=5,
    font=("Helvetica", 16),
    text_color="white",
    fg_color="transparent",
    height=40,
    width=120
)
hover_desc.pack(anchor = "w", padx = 15, pady = 5)

title_font = ctk.CTkFont(family = 'Helvetica', size = 23, weight = 'bold')
title = ctk.CTkLabel(
    title_bar,
    text="Overview",
    text_color="black",
    font=title_font,
    fg_color="transparent",
    height=45,
    justify="center"
)
title.place(relx = 0.501, rely = 0.5, anchor = 'center')

container2 = ctk.CTkFrame(
    main_container,
    fg_color = '#C0DAF0',
    corner_radius = 15,
    border_width = 0,
    height = 430

)
container2.pack(padx = 10, pady = 15, fill = 'both')
container2.pack_propagate(False)

description = ctk.CTkLabel(
    container2,
    text=(
        "The Expense Tracker app helps you easily manage your daily finances by organizing expenses "
        "into clear categories. You can add, edit, and view your spending patterns through a simple, "
        "modern interface designed for clarity and efficiency. With intuitive controls and visual insights, "
        "it enables you to stay on top of your budget and make smarter financial decisions."
    ),
    font = ('Helvetica', 14),
    wraplength = 650,
    justify = 'center'
)
description.pack(padx = 5, pady = 15)

feature_font = ctk.CTkFont(family = 'Helvetica', size = 20, weight = 'bold', underline = True)
features = ctk.CTkLabel(
    container2,
    text = '      Features      ',
    font = feature_font,
    justify = 'center',
)
features.pack(padx = (10, 5), pady = (0, 0))

image_path = "screenshots/icons/wallet.png"
my_image = Image.open(image_path)
add_icon = ctk.CTkImage(light_image=my_image, size=(60, 60))

image_path = "screenshots/icons/search.png"
my_image = Image.open(image_path)
view_icon = ctk.CTkImage(light_image=my_image, size=(60, 60))

image_path = "screenshots/icons/changes.png"
my_image = Image.open(image_path)
update_icon = ctk.CTkImage(light_image=my_image, size=(60, 60))

image_path = "screenshots/icons/trash.png"
my_image = Image.open(image_path)
remove_icon = ctk.CTkImage(light_image=my_image, size=(60, 60))

image_path = "screenshots/icons/sum.png"
my_image = Image.open(image_path)
total_icon = ctk.CTkImage(light_image=my_image, size=(60, 60))

image_path = "screenshots/icons/magnifier.png"
my_image = Image.open(image_path)
search_icon = ctk.CTkImage(light_image=my_image, size=(60, 60))

image_path = "screenshots/icons/sort.png"
my_image = Image.open(image_path)
sort_icon = ctk.CTkImage(light_image=my_image, size=(60, 60))

image_path = "screenshots/icons/calendar.png"
my_image = Image.open(image_path)
periodic_icon = ctk.CTkImage(light_image=my_image, size=(60, 60))

feature1 = ctk.CTkFrame(
    container2,
    fg_color = "#CCDDED",
    height = 550,
)
feature1.pack(padx = 10, pady = 10, fill = 'both')
feature1.pack_propagate(False)

for i in range(4):
    feature1.grid_columnconfigure(i, weight = 1)

iconlist = [add_icon, view_icon, update_icon, remove_icon, total_icon, search_icon, sort_icon, periodic_icon]
labels = ["Add", "View", "Update", "Remove", "Total", "Search", "Sort", "Periodic"]

for i, (icon, text) in enumerate(zip(iconlist, labels)):
    row = 0 if i < 4 else 2
    col = i % 4

    icon_label = ctk.CTkLabel(
        feature1,
        image=icon,
        text="",
        font=('Helvetica', 100, 'bold'),
        height=100,
        width=100
    )
    icon_label.grid(row=row, column=col, pady=(5, 0))

    text_label = ctk.CTkLabel(
        feature1,
        text=text,
        font=("Helvetica", 15, 'bold')
    )
    text_label.grid(row=row + 1, column=col, pady=(0, 10))


app.mainloop()