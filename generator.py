from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from tabulate import tabulate

def create_timetable_pdf(data, output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)

    # Container for the 'Flowable' objects
    elements = []

    # Make the table
    table = Table(data)

    # Add the table to the elements
    elements.append(table)

    # Write the document to disk
    doc.build(elements)

# Example timetable data
data = [
    ["Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    ["9:00 - 10:00", "Maths", "Physics", "Chemistry", "Biology", "English"],
    ["10:00 - 11:00", "English", "Maths", "Physics", "Chemistry", "Biology"],
    ["11:00 - 12:00", "Biology", "English", "Maths", "Physics", "Chemistry"],
    # Add more timetable entries here...
]

create_timetable_pdf(data, "timetable.pdf")
