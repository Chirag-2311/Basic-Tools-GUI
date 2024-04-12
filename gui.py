import customtkinter as ctk
from tkinter import scrolledtext
import threading
import subprocess

# Initialize customtkinter
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

def run_program():
    url = url_entry.get()
    selected_program = program_selector.get()
    console_text.delete(1.0, 'end')  # Clear console text
    
    # Define the command based on the selected program
    if selected_program == 'NMAP Scan':
        command = ["python", "nmapscan.py", url]
    elif selected_program == 'Banner Grabber':
        command = ["python", "banner.py", url]  # Change script name
    elif selected_program == 'Packet Sniffer':
        command = ["python", "packet_sniffing.py", url]
    elif selected_program == 'Geolocation':
        command = ["python", "geolocation.py", url]
    elif selected_program == 'Wifi Scanner':
        command = ["python", "wifiscanner.py", url]    
    else:
        console_text.insert('end', "Invalid selection\n")
        return
    
    def execute_command(cmd):
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            console_text.insert('end', stdout)
            if stderr:
                console_text.insert('end', f"Errors: {stderr}\n")
        except Exception as e:
            console_text.insert('end', f"Error executing command: {e}\n")
    
    threading.Thread(target=execute_command, args=(command,)).start()

def update_url_entry_visibility(event=None):
    selected_program = program_selector.get()
    if selected_program == 'NMAP Scan' or 'Wifi Scanner' or 'Geolocation' or 'Banner Grabber' or 'Packet Sniffer':
        url_entry.place(relx=0.5, rely=0.15, anchor='center')
    else:
        url_entry.place_forget()

# GUI setup
root = ctk.CTk()
root.title("CustomTKinter GUI")
root.geometry("600x400")

# Dropdown for selecting a program
program_selector = ctk.CTkComboBox(root, values=['NMAP Scan', 'Banner Grabber', 'Packet Sniffer','Geolocation','Wifi Scanner'], width=200, height=25, command=update_url_entry_visibility)
program_selector.place(relx=0.5, rely=0.065, anchor='center')

# Entry widget for URL
url_entry = ctk.CTkEntry(root, width=400, placeholder_text="Enter URL or IP here")
# The placement is handled by update_url_entry_visibility based on the selection

# Button to run the selected program
run_button = ctk.CTkButton(root, text="Run", command=run_program)
run_button.place(relx=0.5, rely=0.25, anchor='center')

# Console window for program output
console_text = scrolledtext.ScrolledText(root, width=70, height=10)
console_text.place(relx=0.5, rely=0.55, anchor='center')

# Ensure URL field visibility is correctly initialized
update_url_entry_visibility()

root.mainloop()
