
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from collections import defaultdict
import os
import pickle

# Fungsi untuk mengekstrak teks dan gambar dari PDF
def extract_text_and_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    words_index = defaultdict(list)
    sentences_index = defaultdict(list)
    images = []
    
    for page_num, page in enumerate(doc):
        text = page.get_text("text")
        sentences = text.split('. ')  # Pemisahan berdasarkan titik untuk kalimat
        words = text.split()  # Pemisahan berdasarkan spasi untuk kata
        
        for word in words:
            words_index[word.lower()].append(page_num + 1)
        
        for sentence in sentences:
            sentences_index[sentence.strip()].append(page_num + 1)
        
        for img_index, img in enumerate(page.get_images(full=True)):
            images.append((page_num + 1, img[0]))  # Simpan indeks halaman dan ID gambar
    
    # Simpan gambar ke file biner
    with open("KG.bin", "wb") as f:
        pickle.dump(images, f)
    
    return words_index, sentences_index

# Fungsi untuk memilih folder dan menampilkan daftar file PDF
def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
        listbox_files.delete(0, tk.END)
        for pdf in pdf_files:
            listbox_files.insert(tk.END, os.path.join(folder_path, pdf))

# Fungsi untuk memilih file PDF manual
def open_pdf_manual():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        process_pdf(file_path)

# Fungsi untuk memproses PDF yang dipilih dari daftar
def open_selected_pdf():
    selected_index = listbox_files.curselection()
    if selected_index:
        file_path = listbox_files.get(selected_index[0])
        process_pdf(file_path)

# Fungsi untuk menampilkan hasil ekstraksi
def process_pdf(pdf_path):
    words_index, sentences_index = extract_text_and_images_from_pdf(pdf_path)
    display_results(words_index, sentences_index)
    messagebox.showinfo("Info", f"Gambar telah disimpan dalam 'KG.bin'")

# Fungsi untuk menampilkan hasil dalam tabel
def display_results(words_index, sentences_index):
    for item in word_tree.get_children():
        word_tree.delete(item)
    for item in sentence_tree.get_children():
        sentence_tree.delete(item)
    
    for word, pages in words_index.items():
        word_tree.insert("", "end", values=(word, ", ".join(map(str, set(pages)))))
    
    for sentence, pages in sentences_index.items():
        sentence_tree.insert("", "end", values=(sentence[:50] + ("..." if len(sentence) > 50 else ""), ", ".join(map(str, set(pages)))))

# Membuat antarmuka pengguna dengan Tkinter
root = tk.Tk()
root.title("PDF Text & Image Indexer")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

# Frame atas untuk pemilihan file/folder
frame_top = ttk.Frame(root, padding=10)
frame_top.pack(fill="x")
btn_folder = ttk.Button(frame_top, text="Pilih Folder PDF", command=open_folder)
btn_folder.pack(side="left", padx=5)
btn_manual = ttk.Button(frame_top, text="Pilih File PDF", command=open_pdf_manual)
btn_manual.pack(side="left", padx=5)
btn_open_selected = ttk.Button(frame_top, text="Buka PDF Terpilih", command=open_selected_pdf)
btn_open_selected.pack(side="left", padx=5)

# Listbox untuk menampilkan file dalam folder
listbox_files = tk.Listbox(root, height=6)
listbox_files.pack(fill="x", padx=10, pady=5)

# Frame untuk indeks kata
frame_words = ttk.LabelFrame(root, text="Indeks Kata", padding=10)
frame_words.pack(fill="both", expand=True, padx=10, pady=5)
word_tree = ttk.Treeview(frame_words, columns=("Kata", "Halaman"), show="headings")
word_tree.heading("Kata", text="Kata")
word_tree.heading("Halaman", text="Halaman")
word_tree.pack(fill="both", expand=True)

# Frame untuk indeks kalimat
frame_sentences = ttk.LabelFrame(root, text="Indeks Kalimat", padding=10)
frame_sentences.pack(fill="both", expand=True, padx=10, pady=5)
sentence_tree = ttk.Treeview(frame_sentences, columns=("Kalimat", "Halaman"), show="headings")
sentence_tree.heading("Kalimat", text="Kalimat")
sentence_tree.heading("Halaman", text="Halaman")
sentence_tree.pack(fill="both", expand=True)

# Jalankan aplikasi
root.mainloop()
