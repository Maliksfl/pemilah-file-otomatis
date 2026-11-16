import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Kategori ekstensi file
FOLDERS = {
    "Gambar": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Dokumen": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Arsip": [".zip", ".rar", ".7z", ".tar"],
    "Aplikasi_EXE": [".exe"],
    "File_Python": [".py"],
    "Installer_Lain": [".msi", ".dmg"]
}

def pilih_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_selected)

def mulai_rapikan():
    target_dir = entry_path.get()
    
    if not target_dir or not os.path.exists(target_dir):
        messagebox.showerror("Error", "Silakan pilih folder yang valid terlebih dahulu!")
        return

    total_pindah = 0
    try:
        # Proses pemindaian dan pemindahan file
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            
            if os.path.isdir(file_path):
                continue
                
            file_ext = os.path.splitext(filename)[1].lower()
            
            for folder_name, extensions in FOLDERS.items():
                if file_ext in extensions:
                    folder_tujuan = os.path.join(target_dir, folder_name)
                    os.makedirs(folder_tujuan, exist_ok=True)
                    
                    shutil.move(file_path, os.path.join(folder_tujuan, filename))
                    total_pindah += 1
                    break
                    
        messagebox.showinfo("Berhasil", f"Folder berhasil dirapikan!\nTotal file dipindahkan: {total_pindah}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Inisialisasi Jendela Utama
root = tk.Tk()
root.title("Pemisah File")
root.geometry("500x320")
root.config(bg="#f8fafc")
root.resizable(False, False)

# Bagian Header
tk.Label(root, text="Pemisah File", font=("Poppins", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(pady=(25, 5))
tk.Label(root, text="Rapikan folder berantakan secara otomatis dan instan.", font=("Poppins", 10), bg="#f8fafc", fg="#64748b").pack(pady=(0, 20))

# Bagian Input dan Tombol Pilih Folder
frame_input = tk.Frame(root, bg="#f8fafc")
frame_input.pack(pady=10)

entry_path = tk.Entry(
    frame_input, width=30, font=("Poppins", 10), 
    relief="flat", highlightthickness=1, 
    highlightbackground="#cbd5e1", highlightcolor="#2563eb"
)
entry_path.pack(side=tk.LEFT, padx=(0, 8), ipady=6, ipadx=4)

btn_browse = tk.Button(
    frame_input, text="Pilih Folder", command=pilih_folder, 
    bg="#e2e8f0", fg="#0f172a", font=("Poppins", 9, "bold"), 
    relief="flat", padx=12, pady=5, cursor="hand2"
)
btn_browse.pack(side=tk.LEFT)

# Tombol Eksekusi Utama
btn_proses = tk.Button(
    root, text="Mulai Rapikan", command=mulai_rapikan, 
    bg="#2563eb", fg="white", font=("Poppins", 10, "bold"), 
    relief="flat", padx=20, pady=8, cursor="hand2"
)
btn_proses.pack(pady=20)

root.mainloop()