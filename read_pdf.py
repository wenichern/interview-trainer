import sys

try:
    import PyPDF2
    pdf_library = 'PyPDF2'
except ImportError:
    try:
        import pypdf
        pdf_library = 'pypdf'
    except ImportError:
        print("No PDF library found. Trying pdfplumber...")
        try:
            import pdfplumber
            pdf_library = 'pdfplumber'
        except ImportError:
            print("Please install a PDF library: pip install pypdf")
            sys.exit(1)

pdf_file = sys.argv[1] if len(sys.argv) > 1 else 'REUResearchProjectsVINSEVanderbiltUniversity.pdf'

if pdf_library == 'pdfplumber':
    import pdfplumber
    with pdfplumber.open(pdf_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n\n'
        print(text)
elif pdf_library == 'pypdf':
    import pypdf
    with open(pdf_file, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n\n'
        print(text)
else:  # PyPDF2
    import PyPDF2
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n\n'
        print(text)
