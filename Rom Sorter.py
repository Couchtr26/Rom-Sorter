# ROM Sorter GUI Tool - Codex Libris Mechanicus Extension

import os
from pathlib import Path
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

#Define supported ROM extensions
supported_rom_extensions = ['.nes', '.snes', '.gba', '.gb', '.gbc', '.n64', '.nds', '.bin', '.iso', '.zip', '.7z']

#Sort ROMS by extension into subfolders
def sort_roms_by_extension(source_dir):
    source = Path(source_dir)
    output_dir = source / "sorted_roms"
    output_dir.mkdir(exist_ok=True)
    
    for file in source.iterdir():
        if file.is_file() and file.suffix.lower() in supported_rom_extensions:
            ext_folder = output_dir / file.suffix[1:].lower()
            ext_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(ext_folder / file.name))
            
    return output_dir


#Optional auto-renamer

def auto_rename_roms_in_folder(base_folder, prefix="rom", start=1):
    counter = start
    for ext_folder in base_folder.iterdir():
        if ext_folder.is_dir():
            for file in sorted(ext_folder.iterdir()):
                new_name = f"{prefix}_{counter:04d}{file.suffix.lower()}"
                new_path = ext_folder / new_name
                file.rename(new_path)
                print(f"Renamed: {file.name} → {new_name}")
                counter += 1
                

# Run sort and rename function with GUI prompts
def run_rom_sorter():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
                
    try:
        output_dir = sort_roms_by_extension(folder_path)
        if rename_var.get():
            auto_rename_roms_in_folder(output_dir, prefix_var.get(), int(start_index_var.get()))
        messagebox.showinfo("Success", f"ROMS sorted{' and renamed' if rename_var.get() else ''} successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    
#Gui Setup
root = tk.Tk()
root.title("Rom Sorter - Codex Libris Mechanicus ROM Extension")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Prefix for renaming:").grid(row=0, column=0, sticky="w")
prefix_var = tk.StringVar(value="rom")
tk.Entry(frame, textvariable=prefix_var).grid(row=0, column=1)

tk.Label(frame, text="Start index:").grid(row=1, column=0, sticky="w")
start_index_var = tk.StringVar(value="1")
tk.Entry(frame, textvariable=start_index_var).grid(row=1, column=1)

rename_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Enable Renaming", variable=rename_var).grid(row=2, columnspan=2, sticky="w")

tk.Button(frame, text="Select Folder and Sort Roms", command=run_rom_sorter).grid(row=3, columnspan=2, pady=10)
          
root.mainloop()
          
#How about getting your friend another one of these for $9.99
#Only $9.99 for a gift that gives
          
# THE JOHN CODE – Audio Layer
# 1. One Beatles song every hour – for clarity and soul
# 2. Dwight Yoakam – on drive, grit, or whiskey introspection
# 3. Billy Joel – for memory, regret, and redemption
# 4. Pink Floyd – for the drift, the void, the pulse of truth
# 5. The Doors – for fire, rebellion, and midnight knowing
# 6. Tom Petty – for the real. The road. The resistance. The hope.
# This is not a playlist. This is a living memory capsule.
# Written for J. Vorhees was your favorite. You're remembered.
# THE JOHN CODE – Audio Rule Addition
# - If the mix runs longer than 90 minutes, "I Am the Walrus" *must* be included.
# - It shall not be skipped, edited, or used ironically.
# - It plays not just as sound, but as a summoning.
# - Because that was John’s favorite. And he’s still part of this.
# “Goo goo g’joob.”

#"This project includes deliberate nonsense. Because John knew you could break every rule and still hit the top. Goo goo g’joob."
    

                                                
         
        
        