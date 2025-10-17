import customtkinter as ctk

ctk.set_appearance_mode = "system"
ctk.set_default_color_theme = "blue"

app = ctk.CTk()

app.title('Expense Tracker')
app.geometry('800x500')
app.configure(fg_color = "#260731")

navbar = ctk.CTkFrame(app,
    width = 900,
    height = 200,
    fg_color = '#993B9C'
)
navbar.pack()

my_label = ctk.CTkLabel(navbar,
    text = "Expense Tracker UI",
    font = ("Helvetica", 25, "bold"),
    text_color = "white",
    padx = 900,
    pady = 15

)
my_label.pack()

sidebar = ctk.CTkFrame(app,
    fg_color = '#683B9C',
    width = 70,
    corner_radius = 150,
    height = 450,
)
sidebar.pack(padx = (15, 0), pady = (15, 20), side = 'left')

main_container = ctk.CTkFrame(app,
    border_width = 2,
    border_color = "#CF48A9",
    corner_radius = 15,
    fg_color = "#937296",
    height = 450
)
main_container.pack(padx = (15, 15), pady = (15, 20), fill = 'both')

app.mainloop()