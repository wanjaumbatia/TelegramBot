import time
import tkinter as tk
from metaapi_rest import get_account_info, get_open_trades
root = tk.Tk()
root.title("Wroot Signals Bot")
root.geometry("600x400")
root.resizable(False, False)
root.iconify()

menu_bar_color = '#383838'
toggle_icon = tk.PhotoImage(file='images/toggle_btn_icon.png')

home_icon = tk.PhotoImage(file='images/home_icon.png')
services_icon = tk.PhotoImage(file='images/services_icon.png')
updates_icon = tk.PhotoImage(file='images/updates_icon.png')
contact_icon = tk.PhotoImage(file='images/contact_icon.png')
about_icon = tk.PhotoImage(file='images/about_icon.png')
close_icon = tk.PhotoImage(file='images/close_btn_icon.png')


def swith_indications(indicator_lbl, page):
    home_btn_indicator.config(bg=menu_bar_color)
    services_btn_indicator.config(bg=menu_bar_color)
    updates_btn_indicator.config(bg=menu_bar_color)
    # contact_btn_indicator.config(bg=menu_bar_color)
    # about_btn_indicator.config(bg=menu_bar_color)

    indicator_lbl.config(bg='white')

    if menu_bar_frame.winfo_width() > 45 :
        fold_menu_bar()

    for frame in page_frame.winfo_children():
        frame.destroy()

    if indicator_lbl == home_btn_indicator:
        frame.destroy()
    
    page()

def extending_animation():
    current_width = menu_bar_frame.winfo_width()
    if not current_width > 200 :
        current_width += 10
        menu_bar_frame.config(width=current_width)
        root.after(ms=8, func=extending_animation)
        
def folding_animation():
    current_width = menu_bar_frame.winfo_width()
    if current_width != 45 :
        current_width -= 10
        menu_bar_frame.config(width=current_width)
        root.after(ms=8, func=folding_animation)
        
def extend_menu_bar():
    extending_animation()
    toggle_menu_btn.config(image=close_icon)
    toggle_menu_btn.config(command=lambda: fold_menu_bar())

def fold_menu_bar():
    folding_animation()
    toggle_menu_btn.config(image=toggle_icon)
    toggle_menu_btn.config(command=lambda: extend_menu_bar())

def account_info():
    print(get_account_info())

def home_page():
    info = get_account_info()
    postions = get_open_trades()
    
    home_page_frame = tk.Frame(page_frame, pady=20)
    home_page_frame.grid(sticky="nsew")
    if info['type'] == 'ACCOUNT_TRADE_MODE_DEMO':
        type = 'DEMO'
    else:
        type = 'REAL'
    name_lbl = tk.Label(home_page_frame, text=f"{info['broker']} - {type}", font=("Helvetica", 18, "bold", "italic", "underline"))
    name_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Server Text
    label2 = tk.Label(home_page_frame, text="Server: ", font=("Helvetica", 12, "bold"))
    label2.grid(row=1, column=0, padx=10, pady=3, sticky="w")
    
    label2 = tk.Label(home_page_frame, text=f"{info['server']}", font=("Helvetica", 12, "bold"))
    label2.grid(row=1, column=1, padx=10, pady=3, sticky="w")


    # Account Text
    label2 = tk.Label(home_page_frame, text="Account: ", font=("Helvetica", 12, "bold"))
    label2.grid(row=2, column=0, padx=10, pady=3, sticky="w")
    
    label2 = tk.Label(home_page_frame, text=f"{info['name']} - {info['login']}", font=("Helvetica", 12, "bold"))
    label2.grid(row=2, column=1, padx=10, pady=3, sticky="w")

    # Balance Text
    label2 = tk.Label(home_page_frame, text="Balance: ", font=("Helvetica", 12, "bold"))
    label2.grid(row=3, column=0, padx=10, pady=3, sticky="w")
    
    label2 = tk.Label(home_page_frame, text=f"{info['balance']} {info['currency']}", font=("Helvetica", 12, "bold"))
    label2.grid(row=3, column=1, padx=10, pady=3, sticky="w")

    # Equity Text
    label2 = tk.Label(home_page_frame, text="Equity: ", font=("Helvetica", 12, "bold"))
    label2.grid(row=4, column=0, padx=10, pady=3, sticky="w")
    
    label2 = tk.Label(home_page_frame, text=f"{info['equity']} {info['currency']}", font=("Helvetica", 12, "bold"))
    label2.grid(row=4, column=1, padx=10, pady=3, sticky="w")
    
    # Leverage Text
    label2 = tk.Label(home_page_frame, text="Leverage: ", font=("Helvetica", 12, "bold"))
    label2.grid(row=5, column=0, padx=10, pady=3, sticky="w")
    
    label2 = tk.Label(home_page_frame, text=f"{info['leverage']}", font=("Helvetica", 12, "bold"))
    label2.grid(row=5, column=1, padx=10, pady=3, sticky="w")

    # Leverage Text
    label2 = tk.Label(home_page_frame, text="Positions: ", font=("Helvetica", 12, "bold"))
    label2.grid(row=5, column=0, padx=10, pady=3, sticky="w")
    
    label2 = tk.Label(home_page_frame, text=f"{len(postions)} trades running", font=("Helvetica", 12, "bold"))
    label2.grid(row=5, column=1, padx=10, pady=3, sticky="w")

    

def services_page():  
    positions = get_open_trades()  
    services_page_frame = tk.Frame(page_frame)
        
    lbl = tk.Label(services_page_frame, text="Trades Page", font=('Bold', 30))
    lbl.place(x=100, y=200)
    services_page_frame.pack(fill=tk.BOTH, expand=True)

def updates_page():
    updates_page_frame = tk.Frame(page_frame)
    lbl = tk.Label(updates_page_frame, text="Updates Page", font=('Bold', 30))
    lbl.place(x=100, y=200)
    updates_page_frame.pack(fill=tk.BOTH, expand=True)


page_frame = tk.Frame(root)
page_frame.place(relwidth=1.0, relheight=1.0, x=50)
home_page()

menu_bar_frame = tk.Frame(root, bg= menu_bar_color)

toggle_menu_btn = tk.Button(menu_bar_frame, image=toggle_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: extend_menu_bar())
toggle_menu_btn.place(x=4, y=10)

home_button = tk.Button(menu_bar_frame, image=home_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: swith_indications(indicator_lbl=home_btn_indicator, page=home_page))
home_button.place(x=9, y=130, width=30, height=40)
home_btn_indicator = tk.Label(menu_bar_frame, bg="white")
home_btn_indicator.place(x=3, y=130, width=3, height=40)
home_lbl = tk.Label(menu_bar_frame, text="Home", bg=menu_bar_color, fg="white", font=('Bold', 15), anchor=tk.W)
home_lbl.place(x=45, y=130, width=100, height=40)
home_lbl.bind("<Button-1>", lambda e: swith_indications(indicator_lbl=home_btn_indicator, page=home_page))


services_button = tk.Button(menu_bar_frame, image=services_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color,  command=lambda: swith_indications(indicator_lbl=services_btn_indicator, page=services_page))
services_button.place(x=9, y=190, width=30, height=40)
services_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
services_btn_indicator.place(x=3, y=190, width=3, height=40)
services_lbl = tk.Label(menu_bar_frame, text="Trades", bg=menu_bar_color, fg="white", font=('Bold', 15), anchor=tk.W)
services_lbl.place(x=45, y=190, width=100, height=40)
services_lbl.bind("<Button-1>", lambda e: swith_indications(indicator_lbl=services_btn_indicator, page=services_page))

updates_button = tk.Button(menu_bar_frame, image=updates_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: swith_indications(indicator_lbl=updates_btn_indicator, page=updates_page))
updates_button.place(x=9, y=250, width=30, height=40)
updates_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
updates_btn_indicator.place(x=3, y=250, width=3, height=40)
updates_lbl = tk.Label(menu_bar_frame, text="Updates", bg=menu_bar_color, fg="white", font=('Bold', 15), anchor=tk.W)
updates_lbl.place(x=45, y=250, width=100, height=40)
updates_lbl.bind("<Button-1>", lambda e: swith_indications(indicator_lbl=updates_btn_indicator, page=updates_page))

# contact_button = tk.Button(menu_bar_frame, image=contact_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: swith_indications(indicator_lbl=contact_btn_indicator, page=contact_page))
# contact_button.place(x=9, y=310, width=30, height=40)
# contact_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
# contact_btn_indicator.place(x=3, y=310, width=3, height=40)
# contact_lbl = tk.Label(menu_bar_frame, text="Contact Us", bg=menu_bar_color, fg="white", font=('Bold', 15), anchor=tk.W)
# contact_lbl.place(x=45, y=310, width=100, height=40)
# contact_lbl.bind("<Button-1>", lambda e: swith_indications(indicator_lbl=contact_btn_indicator, page=contact_page))

# about_button = tk.Button(menu_bar_frame, image=about_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: swith_indications(indicator_lbl=about_btn_indicator, page=about_page))
# about_button.place(x=9, y=370, width=30, height=40)
# about_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
# about_btn_indicator.place(x=3, y=370, width=3, height=40)
# about_lbl = tk.Label(menu_bar_frame, text="About", bg=menu_bar_color, fg="white", font=('Bold', 15), anchor=tk.W)
# about_lbl.place(x=45, y=370, width=100, height=40)
# about_lbl.bind("<Button-1>", lambda e: swith_indications(indicator_lbl=about_btn_indicator, page=about_page))

menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=4)
menu_bar_frame.pack_propagate(flag=False)

menu_bar_frame.configure(width=45)

root.mainloop()