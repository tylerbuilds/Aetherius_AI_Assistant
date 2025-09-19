import warnings
warnings.filterwarnings("ignore", message=".*torch.utils._pytree._register_pytree_node is deprecated.*")
import os
import time
import sys
import importlib.util
import platform
import tkinter as tk
import customtkinter
import json
from tkinter import PhotoImage, messagebox
import webbrowser
from Aetherius_API.Main import *




def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def set_mac_theme():
    # macOS-inspired color scheme
    background_color = "#1C1C1E"  # macOS dark background
    foreground_color = "#FFFFFF"  # Pure white text
    button_color = "#007AFF"  # macOS system blue
    button_hover_color = "#0056CC"  # Darker blue for hover
    secondary_button_color = "#48484A"  # macOS secondary button
    accent_color = "#FF9500"  # macOS orange accent
    text_color = '#FFFFFF'

    return background_color, foreground_color, button_color, button_hover_color, secondary_button_color, accent_color


        



class Application(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Set macOS-style appearance
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        
        # Configure window with Mac aesthetics
        self.title('Aetherius AI Assistant')
        self.geometry("600x500")
        self.minsize(500, 400)
        
        # macOS-style window positioning (center on screen)
        self.center_window()
        
        # Set window background
        self.configure(fg_color="#1C1C1E")
        
        # Get theme colors
        self.colors = set_mac_theme()
        
        self.create_widgets()

    def center_window(self):
        """Center the window on the screen - macOS style"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        with open('./Aetherius_API/chatbot_settings.json', 'r', encoding='utf-8') as f:
            settings = json.load(f)

        # Use system fonts for macOS
        mac_font = "SF Pro Display" if platform.system() == "Darwin" else "Segoe UI"
        
        # Create main container with proper spacing
        main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Header section with macOS styling
        header_frame = customtkinter.CTkFrame(main_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 30))
        
        # Title with macOS typography
        title_label = customtkinter.CTkLabel(
            header_frame, 
            text="Aetherius AI Assistant", 
            font=(mac_font, 28, "bold"),
            text_color="#FFFFFF"
        )
        title_label.pack(pady=(0, 8))
        
        # Subtitle
        subtitle_label = customtkinter.CTkLabel(
            header_frame, 
            text="Advanced AI Assistant with Long-Term Memory",
            font=(mac_font, 14),
            text_color="#8E8E93"
        )
        subtitle_label.pack(pady=(0, 15))
        
        # Support message with better styling
        support_label = customtkinter.CTkLabel(
            header_frame, 
            text="⭐ Please star on GitHub to support development!",
            font=(mac_font, 12),
            text_color="#FF9500"
        )
        support_label.pack()
        
        # Action section
        action_frame = customtkinter.CTkFrame(main_frame, fg_color="transparent")
        action_frame.pack(fill="both", expand=True)
        
        # Section title
        section_label = customtkinter.CTkLabel(
            action_frame, 
            text="Launch Interface",
            font=(mac_font, 18, "bold"),
            text_color="#FFFFFF"
        )
        section_label.pack(pady=(0, 20))
        
        # Button container with proper spacing
        button_frame = customtkinter.CTkFrame(action_frame, fg_color="transparent")
        button_frame.pack(fill="x")
        
        # Create Mac-style buttons for scripts
        scripts = [file for file in os.listdir('Aetherius_GUI') if file.endswith('.py')]
        for i, script in enumerate(scripts):
            script_name = script[:-3].replace('Menu_', '').replace('_', ' ')
            
            # Primary button styling for first item, secondary for others
            if i == 0:
                fg_color = "#007AFF"
                hover_color = "#0056CC"
            else:
                fg_color = "#48484A"
                hover_color = "#636366"
            
            button = customtkinter.CTkButton(
                button_frame, 
                text=script_name,
                command=lambda s=script: self.run_script(s),
                font=(mac_font, 14),
                fg_color=fg_color,
                hover_color=hover_color,
                corner_radius=8,
                height=44,
                border_width=0
            )
            button.pack(fill="x", pady=8)
        
        # Footer with Ko-fi support
        footer_frame = customtkinter.CTkFrame(main_frame, fg_color="transparent")
        footer_frame.pack(side="bottom", fill="x", pady=(20, 0))
        
        # Ko-fi button as text link (more Mac-like)
        kofi_button = customtkinter.CTkButton(
            footer_frame,
            text="☕ Support on Ko-fi",
            command=self.open_kofi_link_direct,
            font=(mac_font, 12),
            fg_color="transparent",
            hover_color="#48484A",
            text_color="#FF9500",
            corner_radius=6,
            height=32,
            border_width=1,
            border_color="#FF9500"
        )
        kofi_button.pack(side="left")

    def open_kofi_link(self, event):
        webbrowser.open('https://ko-fi.com/libraryofcelsus')
    
    def open_kofi_link_direct(self):
        webbrowser.open('https://ko-fi.com/libraryofcelsus')

    def run_script(self, script):
        module_name = script[:-3]
        spec = importlib.util.spec_from_file_location(module_name, f"./Aetherius_GUI/{script}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        function_name = module_name
        if hasattr(module, function_name):
            func = getattr(module, function_name)
            if callable(func):
                if "self" in func.__code__.co_varnames:
                    func(self)  # Call with self if the function expects it
                else:
                    func()  # Call without self if the function does not expect it
        else:
            messagebox.showerror("Error", f"No {function_name} function found in the script")




if __name__ == '__main__':
    app = Application()
    app.mainloop()