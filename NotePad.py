import tkinter as tk
from tkinter import ttk, filedialog
import os,sys

# Functions for the file menu

def new_file():
    try:
        text_box.delete(1.0, tk.END)
    except Exception as e:
        print(f"Error in new_file: {e}")

def open_file():
    try:
        file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, content)
    except Exception as e:
        print(f"Error in open_file: {e}")

def save_file():
    try:
        file_path = filedialog.asksaveasfilename(title="Save File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = text_box.get(1.0, tk.END)
                file.write(content)
    except Exception as e:
        print(f"Error in save_file: {e}")

def save_file_as():
    try:
        file_path = filedialog.asksaveasfilename(title="Save File As", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = text_box.get(1.0, tk.END)
                file.write(content)
    except Exception as e:
        print(f"Error in save_file_as: {e}")

# function to view menu

def undo():
    try:
        text_box.edit_undo()
    except Exception as e:
        print(f"Error in undo: {e}")

def cut():
    try:
        text_box.event_generate("<<Cut>>")
    except Exception as e:
        print(f"Error in cut: {e}")

def copy():
    try:
        text_box.event_generate("<<Copy>>")
    except Exception as e:
        print(f"Error in copy: {e}")

def paste():
    try:
        text_box.event_generate("<<Paste>>")
    except Exception as e:
        print(f"Error in paste: {e}")

def delete():
    try:
        text_box.event_generate("<<Clear>>")
    except Exception as e:
        print(f"Error in delete: {e}")

# Create a sub window for find and replace

def find_replace():
    try:
        sub_window = tk.Toplevel(window)
        sub_window.title('Find and Replace')
        sub_window.geometry('300x150')
        sub_window.minsize(300, 150)

        # Add a frame
        frame = ttk.Frame(sub_window, padding=2)
        frame.pack(fill=tk.BOTH, expand=True)

        # Add a label
        find_label = ttk.Label(frame, text='Find:')
        find_label.grid(row=0, column=0, padx=5, pady=5)

        # Add a text box
        find_text = ttk.Entry(frame, width=30)
        find_text.grid(row=0, column=1, padx=5, pady=5)

        # Add a label
        replace_label = ttk.Label(frame, text='Replace:')
        replace_label.grid(row=1, column=0, padx=5, pady=5)

        # Add a text box
        replace_text = ttk.Entry(frame, width=30)
        replace_text.grid(row=1, column=1, padx=5, pady=5)

        def find(find_text):
            print(find_text)
            text = text_box.get(1.0, tk.END)
            print(text)
            if find_text in text:
                print('Found')
            else:
                print('Not found')

        # Add a button
        find_button = ttk.Button(frame, text='Find', command=lambda: find(find_text.get()))
        find_button.grid(row=2, column=0, padx=5, pady=5)

        def replace(find_text, replace_text):
            print(find_text)
            print(replace_text)
            text = text_box.get(1.0, tk.END)
            print(text)
            if find_text in text:
                print('Found')
                text = text.replace(find_text, replace_text)
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, text)
            else:
                print('Not found')

        # Add a button
        replace_button = ttk.Button(frame, text='Replace', command=lambda: replace(find_text.get(), replace_text.get()))
        replace_button.grid(row=2, column=1, padx=5, pady=5)

    except Exception as e:
        print(f"Error in find_replace: {e}")

# Create a sub window for go to a specific line

def go_to():
    try:
        sub_window = tk.Toplevel(window)
        sub_window.title('Go To')
        sub_window.geometry('300x150')
        sub_window.minsize(300, 150)

        # Add a frame
        frame = ttk.Frame(sub_window, padding=2)
        frame.pack(fill=tk.BOTH, expand=True)

        # Add a label
        line_label = ttk.Label(frame, text='Line:')
        line_label.grid(row=0, column=0, padx=5, pady=5)

        # Add a text box
        line_text = ttk.Entry(frame, width=30)
        line_text.grid(row=0, column=1, padx=5, pady=5)

        # Add a button
        go_to_button = ttk.Button(frame, text='Go To')
        go_to_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # go to the line
        def go_to_line():
            line = line_text.get()
            print(line)
            text_box.mark_set('insert', f"{line}.0")
            text_box.see('insert')
            text_box.focus_set()
            sub_window.destroy()

        go_to_button.config(command=go_to_line)
    except Exception as e:
        print(f"Error in go_to: {e}")

# function to select all text

def select_all():
    try:
        text_box.tag_add('sel', '1.0', 'end')
    except Exception as e:
        print(f"Error in select_all: {e}")

# Create a sub window for about

def about():
    try:
        sub_window = tk.Toplevel(window)
        sub_window.title('About')
        sub_window.geometry('300x150')
        sub_window.minsize(300, 150)

        # Add a frame
        frame = ttk.Frame(sub_window, padding=2)
        frame.pack(fill=tk.BOTH, expand=True)

        # Add a label
        about_label = ttk.Label(frame, text='This is a simple text editor using Tkinter.')
        about_label.pack(padx=5, pady=5)

        # Add a second label
        about_label2 = ttk.Label(frame,
                                 text='Created by: Ibnus Nahiyan Samit\nEmail:nahiyansamit@gmail.com\nVersion: 1.0.0')
        about_label2.pack(padx=5, pady=5)

        # Add a button
        close_button = ttk.Button(frame, text='Close', command=sub_window.destroy)
        close_button.pack(padx=5, pady=5)
    except Exception as e:
        print(f"Error in about: {e}")

# function to get the line number

def line(event):
    try:
        cursor_position = tk.IntVar()
        cursor_position = text_box.index(tk.INSERT)
        line = cursor_position.split('.')[0]
        return line
    except Exception as e:
        print(f"Error in line: {e}")

def on_resize(event):
    try:
        text_box.config(width=event.width, height=event.height)
    except Exception as e:
        print(f"Error in on_resize: {e}")

# Create a resource path
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
        print(base_path)
    except Exception:
        base_path = os.path.abspath(".")
        print(base_path)
    return os.path.join(base_path, relative_path)

# create a window
try:
    window = tk.Tk()
    window.title('NotePad')
    window.geometry('700x750')
    window.minsize(300, 150)
    # add a icon from Resource folder
    window.iconbitmap(resource_path('Resource\\icon.ico'))

    # Add a menu bar
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    # Add a file menu
    file_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='New', command=new_file)
    file_menu.add_command(label='Open', command=open_file)
    file_menu.add_command(label='Save', command=save_file)
    file_menu.add_command(label='Save as', command=save_file_as)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=window.quit)

    # Add a view menu
    view_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label='View', menu=view_menu)
    view_menu.add_command(label='Undo', command=undo)
    view_menu.add_separator()
    view_menu.add_command(label='Cut', command=cut)
    view_menu.add_command(label='Copy', command=copy)
    view_menu.add_command(label='Paste', command=paste)
    view_menu.add_command(label='Delete', command=delete)
    view_menu.add_separator()
    view_menu.add_command(label='Find/Replace', command=find_replace)
    view_menu.add_command(label='Go To', command=go_to)
    view_menu.add_separator()
    view_menu.add_command(label='Select All', command=select_all)

    # Add a info menu
    info_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label='Info', menu=info_menu)
    info_menu.add_command(label='About', command=about)

    # Add a frame
    frame = ttk.Frame(window, padding=2)
    frame.pack(fill=tk.BOTH, expand=True)

    # Add a Scrollbar
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ttk text
    text_box = tk.Text(frame,
                       font=('Arial', 12),
                       yscrollcommand=scrollbar.set,
                       undo=True)
    text_box.pack(expand=True, fill=tk.BOTH)

    # Get the line number at real time and display it in the status bar
    text_box.bind("<KeyRelease>", lambda event: status.config(text=f"Line: {line(event)}"))
    text_box.bind("<ButtonRelease>", lambda event: status.config(text=f"Line: {line(event)}"))

    # Add a status bar in the bottom of the window
    status = ttk.Label(window,
                       text="Line: ",
                       relief=tk.SUNKEN,
                       anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)

    # Add a sizegrip
    sizegrip = ttk.Sizegrip(status)
    sizegrip.pack(side=tk.RIGHT, anchor=tk.SE)

    # Bind the scrollbar to the text box
    scrollbar.config(command=text_box.yview)

    # Bind the resize of the window to the on_resize function
    # window.bind("<Configure>", lambda event: on_resize(event))

    # run
    window.mainloop()
except Exception as e:
    print(f"Error in main: {e}")
