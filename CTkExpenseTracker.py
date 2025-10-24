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
    height = 630,
    border_width = 1,
    border_color = "#87C3D4",
)
sidebar.pack(padx = (15, 0), pady = (15, 20), side = 'left')

inner_sidebar = ctk.CTkFrame(sidebar,
    fg_color = 'transparent',
    corner_radius = 20,
    width = 60
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

image_path = "screenshots/icons/sum.png"
my_image = Image.open(image_path)
total_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/magnifier.png"
my_image = Image.open(image_path)
search_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/sort.png"
my_image = Image.open(image_path)
sort_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))

image_path = "screenshots/icons/calendar.png"
my_image = Image.open(image_path)
periodic_icon = ctk.CTkImage(light_image=my_image, size=(20, 20))


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
        placeholder_text_color = 'black',
        fg_color = '#82A4BA',
        text_color = 'black',
        width=200,
        font = ('Helvetica', 13, 'bold')
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
        placeholder_text_color = 'black',
        fg_color = '#82A4BA',
        text_color = 'black',
        width=200,
        font = ('Helvetica', 14, 'bold')
    )
    description_entry.grid(row = 1, column = 1)

    # Amount
    amount_label = ctk.CTkLabel(
        form_frame, 
        text="Enter amount:", 
        font = ("Helvetica", 14, 'bold')
    )
    amount_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'e')
    amount_entry = ctk.CTkEntry(
        form_frame, 
        placeholder_text="xxxxx",
        placeholder_text_color = 'black',
        fg_color = '#82A4BA',
        text_color = 'black',
        width=200,
        font = ('Helvetica', 14, 'bold')
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
            description = description_entry.get().strip()
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
add_button.pack(pady = 7)
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

        def clear_csv():
            with open('expenses.csv', 'w') as file:
                pass
            notice1.configure(text = 'All expenses deleted successfully.', text_color = 'Red')

            for widget in container2.winfo_children():
                if widget == notice1:
                    pass
                else:
                    widget.destroy()
            

        tracker.view_expense()
        button.destroy()
        notice1.configure(
            text=tracker.msg,
            text_color='green' if tracker.msg == 'Successfully extracted expenses.' else 'red'
        )

        del_button = ctk.CTkButton(
            container2,
            text = 'Delete all',
            fg_color = 'red',
            hover_color = '#9C2007',
            font = ('Helvetica', 13, 'bold'),
            command = clear_csv
        )
        del_button.place(x = 618, y = 10)

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
            height =280
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
            

    button = ctk.CTkButton(
        container2, 
        text="Extract", 
        font = ('Helvetica', 15, 'bold'),
        height = 30,
        width = 150,
        command=viewing
    )
    button.pack(pady=15)

    notice1 = ctk.CTkLabel(
        container2,
        text="",
        text_color="green",
        font=('Helvetica', 14, 'bold')
    )
    notice1.pack(pady=(15, 0))

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
view_button.pack(pady = 7)
view_button.bind("<Enter>", view_on_enter)
view_button.bind("<Leave>", view_on_leave)

def update_on_enter(event):
    hover_desc.configure(text = "Update expense", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def update_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def update():
    title.configure(text = 'update button pressed')

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
update_button.pack(pady = 7)
update_button.bind("<Enter>", update_on_enter)
update_button.bind("<Leave>", update_on_leave)


def remove_on_enter(event):
    hover_desc.configure(text = "Remove expense", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def remove_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def remove():
    title.configure(text = 'remove button pressed')

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
remove_button.pack(pady = 7)
remove_button.bind("<Enter>", remove_on_enter)
remove_button.bind("<Leave>", remove_on_leave)


def total_on_enter(event):
    hover_desc.configure(text = "Total expense", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def total_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def total():
    title.configure(text = 'total button pressed')

total_button = ctk.CTkButton(
    inner_sidebar,
    image = total_icon,
    text="",
    fg_color="transparent",
    bg_color="transparent",
    width=50,
    height=40,
    hover_color="#2b6777",
    command = total
)
total_button.pack(pady = 7)
total_button.bind("<Enter>", total_on_enter)
total_button.bind("<Leave>", total_on_leave)


def search_on_enter(event):
    hover_desc.configure(text = "Search expenses", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def search_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def search():
    title.configure(text = 'search button pressed')

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
search_button.pack(pady = 7)
search_button.bind("<Enter>", search_on_enter)
search_button.bind("<Leave>", search_on_leave)


def sort_on_enter(event):
    hover_desc.configure(text = "Sort expenses", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def sort_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def sort():
    title.configure(text = 'sort button pressed')

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
sort_button.pack(pady = 7)
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
periodic_button.pack(pady = 7)
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