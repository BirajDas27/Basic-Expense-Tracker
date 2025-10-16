import customtkinter as ctk

ctk.set_appearance_mode = "system"
ctk.set_default_color_theme = "blue"

app = ctk.CTk()

app.title('Expense Tracker')
app.geometry('900x600')

navbar = ctk.CTkFrame(app,
    width = 900,
    height = 80,
    fg_color = '#600080'
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
    fg_color = 'red',
    width = 90,
    corner_radius = 200,
    height = 480,
    
    
)
sidebar.pack(padx = 15, pady = 15, side = 'left')

app.mainloop()