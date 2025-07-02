import PyPDF2

# 1. Read and display PDF file
def read_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            print(f"--- Contents of {file_path} ---\n")
            for page_number, page in enumerate(reader.pages):
                text = page.extract_text()
                print(f"\n--- Page {page_number + 1} ---")
                print(text if text else "[No readable text]")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# ✅ Replace this with the actual path to a PDF file
read_pdf(r"C:\Users\Vaishnavi\Downloads\VaishnaviJagtapResume.pdf")

# 2. Read a Python file and display total number of lines and characters
def count_lines_and_characters(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            lines = content.splitlines()
            total_lines = len(lines)
            total_characters = len(content)

            print(f"\n--- File: {file_path} ---")
            print(f"Total Lines: {total_lines}")
            print(f"Total Characters: {total_characters}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# ✅ Provide a valid .py file here instead of PDF
count_lines_and_characters(r"D:\Gryphon Python\Day-4\filehandling.py")

# 3. Copy only commented lines from one Python file to another
def copy_commented_lines(source_path, destination_path):
    try:
        with open(source_path, "r") as src, open(destination_path, "w") as dest:
            for line in src:
                stripped = line.strip()
                if stripped.startswith("#"):
                    dest.write(line)
        print(f"Commented lines copied from {source_path} to {destination_path}")
    except FileNotFoundError:
        print(f"Error: File '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# ✅ Source and destination must be .py files
copy_commented_lines(
    r"D:\Gryphon Python\Day-4\filehandling.py",
    r"D:\Gryphon Python\Day-4\comments_only.py"
)
