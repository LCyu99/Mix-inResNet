from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PIL import Image
import os
from IPython.display import display, FileLink
from reportlab.lib.colors import black, blue, red
from reportlab.lib.utils import ImageReader
import datetime

images_dir = "C:\\Users\\Administrator\\Desktop\\深度学习文章\\影像报告2"



def create_diagnosis_report(patient_info, diagnosis, filename, images_dir):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    # Draw border for the page
    border_margin = 50  # adjust this value to change the margin of the border
    c.rect(0, 0, width, height)
    # Draw the report header
    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(0,0,0)
    title = "Medical Imaging Diagnosis Report"
    title_width = c.stringWidth(title,"Helvetica-Bold", 24)
    c.drawString((width-title_width)/2, height - 50, title)

    # Draw a line below the report header
    c.setLineWidth(3)
    c.line(50, height - 70, width - 50, height - 70)

    # Draw the patient information table
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0,0,0)
    keys = list(patient_info.keys())
    for i in range(0, len(keys), 2):
        c.drawString(50, height - 100 - (i*15), f"{keys[i]}: {patient_info[keys[i]]}")
        if i+1 < len(keys):
            c.drawString(300, height - 100 - (i*15), f"{keys[i+1]}: {patient_info[keys[i+1]]}")

    # Draw a rectangle around the image section
    c.rect(50, 100, width - 100, height - 300)

    # Draw the image placeholders and titles
    image_files = [os.path.join(images_dir, img) for img in os.listdir(images_dir) if img.endswith('.png')][:3]

    box_width = (width - 100) // 3
    box_height = (height - 370) // 3
    offset = 50  # Change this value to adjust the vertical position of the images

    for i, image_file in enumerate(image_files):
        x = 50 + (i%3*box_width) + 10  # Added 10 as an indent
        y = 100 + offset + ((2-(i//3))*box_height)  # Changed the order of the images

        # Load the image and get its width and height
        img = Image.open(image_file)
        img_width, img_height = img.size

        # Calculate the scale factor to fit the image to the box
        scale = min(box_width / img_width, box_height / img_height)

        # Calculate the new image size
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)

        # Draw the image with the new size
        c.drawImage(image_file, x, y, new_width, new_height)

        c.setFont("Helvetica-Bold", 10)
        c.setFillColorRGB(0,0,1)
        c.drawString(x, y + new_height + 5, f"MRI Image {i+1}")

    # Draw a line below the images
    c.setLineWidth(3)
    c.line(50, 100 + offset + box_height, width - 50, 100 + offset + box_height)

    # Draw the diagnosis information
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(0,0,1)
    c.drawString(50, 80 + offset + box_height + 5, "Diagnosis:")

    # Draw diagnosis text
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0,0,0)
    max_width = width - 100 - 60  # width of the rectangle - left margin
    lines = diagnosis.split("\n")
    line_height = 14
    y = 80 + offset + box_height + 5 - 15  # starting y position
    for line in lines:
        line = line.strip()
        while len(line) > 0:
            split_index = len(line)
            while split_index > 0 and c.stringWidth(line[:split_index], "Helvetica", 12) > max_width:
                split_index -= 1
            c.drawString(60, y, line[:split_index])
            y -= line_height  # move to the next line
            line = line[split_index:].strip()
   
    # Add date and signature at the bottom right
    c.setFont("Helvetica", 10)
    c.setFillColorRGB(0,0,0)
    c.drawString(width - 200, 30, "Date: " + datetime.datetime.now().strftime("%Y-%m-%d"))
    c.drawString(width - 200, 15, "Signature: _______________")

    c.showPage()
    c.save()
    # display the PDF
    display(FileLink(filename))

# Test code
patient_info = {
    "Name": "John Doe",
    "ID": "123456789",
    "Gender": "Male",
    "Age": "50",
    "Origin": "USA",
    "Address": "123 Street, City, State",
    "Phone": "1234567890"
}

diagnosis = "MRI images showed moderate overall lumbar disc degradation,moderate lumbar 4/5 central spinal canal stenosis with bilateral recess stenosis, mild lumbar 4/5 left foramen compression with severe right compression, mild lumbar 4/ sacral 5 central spinal canal stenosis with mild left foramen compression."

create_diagnosis_report(patient_info, diagnosis, "diagnosis_report.pdf", "C:\\Users\\Administrator\\Desktop\\深度学习文章\\影像报告2")