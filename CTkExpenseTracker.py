import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode = "system"
ctk.set_default_color_theme = "blue"

app = ctk.CTk()

app.title('Expense Tracker')
app.geometry('800x500')
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
    corner_radius = 30,
    height = 450,
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
add_button.pack(pady = 5)

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
view_button.pack(pady = 5)

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
update_button.pack(pady = 5)

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
remove_button.pack(pady = 5)

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
total_button.pack(pady = 5)

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
search_button.pack(pady = 5)

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
sort_button.pack(pady = 5)

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
periodic_button.pack(pady = 5)
    


main_container = ctk.CTkFrame(app,
    border_width = 1,
    border_color = "#2b6777",
    corner_radius = 15,
    fg_color = "#f2f2f2",
    height = 600
)
main_container.pack(padx = (15, 15), pady = (15, 20), fill = 'both')
main_container.pack_propagate(False)

title_font = ctk.CTkFont(family = 'Helvetica', size = 27, weight = 'bold')
title = ctk.CTkLabel(
    main_container,
    text = 'Overview',
    text_color = 'black',
    font = title_font,
    fg_color = '#82A4BA',
    corner_radius = 15,
    height = 50
)
title.pack(padx = (0, 0), pady = (0, 0), anchor = 'center' , fill = 'both')

container2 = ctk.CTkFrame(
    main_container,
    fg_color = '#C0DAF0',
    corner_radius = 15,
    border_width = 0,
    height = 600

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



app.mainloop()