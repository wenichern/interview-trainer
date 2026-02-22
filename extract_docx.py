import sys
try:
    from docx import Document
    docx_file = sys.argv[1] if len(sys.argv) > 1 else 'Copy of Copy of Personal Statement Georgia.docx'
    doc = Document(docx_file)
    for para in doc.paragraphs:
        print(para.text)
except ImportError:
    print("python-docx not installed. Install it with: pip install python-docx")
    sys.exit(1)
