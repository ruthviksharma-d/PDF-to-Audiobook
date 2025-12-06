import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Ask user to select a PDF file
book = askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
if not book:
    print("No file selected.")
    exit()

# Read the PDF
pdfreader = PyPDF2.PdfReader(book)  # Updated class name
pages = len(pdfreader.pages)

# Initialize TTS engine only once (important)
player = pyttsx3.init()

# Read each page
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()   # Updated method name
    if text:
        player.say(text)

player.runAndWait()
