import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("🔥 Modern Touch Editor")
root.geometry("1000x700")
root.configure(bg="#121212")

images = []
default_font = "Consolas"
default_size = 14

# ---------------- FUNCTIONS ----------------
def insert_image():
    file = filedialog.askopenfilename(
        filetypes=[("Images", "*.png *.jpg *.jpeg")]
    )
    if not file:
        return

    img = Image.open(file)
    img.thumbnail((350, 350))
    photo = ImageTk.PhotoImage(img)
    images.append(photo)

    text.image_create(tk.INSERT, image=photo)
    text.insert(tk.INSERT, "\n\n")

def insert_video():
    file = filedialog.askopenfilename(
        filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
    )
    if file:
        text.insert(tk.INSERT, f"[🎬 VIDEO]: {file}\n")

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))

# ---------------- TEXT FORMATTING ----------------
def apply_tag(tag, **options):
    text.tag_configure(tag, **options)
    text.tag_add(tag, "sel.first", "sel.last")

def make_bold():
    apply_tag("bold", font=(default_font, default_size, "bold"))

def make_italic():
    apply_tag("italic", font=(default_font, default_size, "italic"))

def make_underline():
    apply_tag("underline", font=(default_font, default_size, "underline"))

def set_color():
    color = colorchooser.askcolor()[1]
    if color:
        apply_tag(f"color_{color}", foreground=color)

def set_highlight():
    color = colorchooser.askcolor()[1]
    if color:
        apply_tag(f"highlight_{color}", background=color)

def set_font_size(size):
    apply_tag(f"size_{size}", font=(default_font, size))

def heading1():
    apply_tag("h1", font=(default_font, 28, "bold"))

def heading2():
    apply_tag("h2", font=(default_font, 22, "bold"))

def heading3():
    apply_tag("h3", font=(default_font, 18, "bold"))

def bullet_list():
    text.insert("sel.first", "• ")

def quote_style():
    apply_tag("quote", foreground="#00e0ff")
    text.insert("sel.first", "❝ ")
    text.insert("sel.last", " ❞")

# ---------------- TOOLBAR ----------------
toolbar = tk.Frame(root, bg="#1f1f1f", height=50)
toolbar.pack(fill="x")

def tool_btn(label, cmd):
    return tk.Button(
        toolbar,
        text=label,
        command=cmd,
        bg="#2a2a2a",
        fg="white",
        activebackground="#3a3a3a",
        activeforeground="cyan",
        relief="flat",
        font=("Segoe UI", 11),
        padx=10,
        pady=5
    )

# Insert
tool_btn("🖼 Sawir", insert_image).pack(side="left", padx=4)
tool_btn("🎬 Video", insert_video).pack(side="left", padx=4)

# Basic formatting
tool_btn("𝐁", make_bold).pack(side="left", padx=4)
tool_btn("𝑰", make_italic).pack(side="left", padx=4)
tool_btn("U̲", make_underline).pack(side="left", padx=4)

tool_btn("🎨 Color", set_color).pack(side="left", padx=4)
tool_btn("🖍 Highlight", set_highlight).pack(side="left", padx=4)

# Font sizes
tool_btn("A 12", lambda: set_font_size(12)).pack(side="left", padx=4)
tool_btn("A 16", lambda: set_font_size(16)).pack(side="left", padx=4)
tool_btn("A 20", lambda: set_font_size(20)).pack(side="left", padx=4)
tool_btn("A 26", lambda: set_font_size(26)).pack(side="left", padx=4)

# Headings
tool_btn("H1", heading1).pack(side="left", padx=4)
tool_btn("H2", heading2).pack(side="left", padx=4)
tool_btn("H3", heading3).pack(side="left", padx=4)

# Lists & Quotes
tool_btn("• Bullet", bullet_list).pack(side="left", padx=4)
tool_btn("❝ Quote", quote_style).pack(side="left", padx=4)

# Save
tool_btn("💾 Save", save_file).pack(side="right", padx=10)

# ---------------- TEXT AREA ----------------
text = tk.Text(
    root,
    bg="#181818",
    fg="#e0e0e0",
    insertbackground="white",
    font=(default_font, default_size),
    wrap="word",
    relief="flat",
    padx=15,
    pady=15
)
text.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()
