#!/usr/bin/env python
# coding: utf-8

# In[28]:


import tkinter as tk

def on_button_click():
    label.config(text="Hello, " +  entry.get())


root = tk.Tk()
root.title("Tkinter Example")
root.geometry("900x1400")
root.

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Say Hello", command=on_button_click)
button.pack()

root.mainloop()


# In[29]:


import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")  # Set the initial size of the window

# Add widgets
label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Say Hello", command=on_button_click)
button.pack()

# Run the application
root.mainloop()


# In[ ]:




