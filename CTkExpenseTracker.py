import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode = "system"
ctk.set_default_color_theme = "blue"

app = ctk.CTk()

app.title('Expense Tracker')
app.geometry('890x590')
app.configure(fg_color = "#BCDCE6")
app.resizable(True, True)

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
inner_sidebar.pack(padx = 2,pady = 40)

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


def add_on_enter(event):
    hover_desc.configure(text = "Add expense", fg_color = "#2b6777", text_color = "white", font = ("Helvetica", 17, 'bold'))

def add_on_leave(event):
    hover_desc.configure(text = '', fg_color = 'transparent')

def add():
    title.configure(text = 'add button pressed')

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
    title.configure(text = 'view button pressed')

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
    text_color = 'black',
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
    text_color = 'black'
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
        text_color="black",
        fg_color="transparent",
        font=('Helvetica', 100, 'bold'),
        height=100,
        width=100
    )
    icon_label.grid(row=row, column=col, pady=(5, 0))

    text_label = ctk.CTkLabel(
        feature1,
        text=text,
        text_color="black",
        font=("Helvetica", 15, 'bold')
    )
    text_label.grid(row=row + 1, column=col, pady=(0, 10))


app.mainloop()