from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
import qrcode
from datetime import datetime
import io
import tempfile
import os
import webbrowser


def add_logo(canvas, logo_path, x, y, width, height):
    try:
        canvas.drawImage(logo_path, x, y, width=width, height=height, preserveAspectRatio=True, mask='auto')
    except Exception as e:
        print(f"Error loading logo: {e}")


def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


def get_input(prompt, default=None):
    user_input = input(prompt)
    if not user_input and default is not None:
        return default
    return user_input


def create_receipt():
    receipt_id = get_input("Enter Receipt ID: ", "123456")
    customer_name = get_input("Enter Customer Name: ", "John Doe")

    items = {}
    while True:
        item_name = input("Enter Item Name (leave blank to finish): ").strip()
        if not item_name:
            break
        description = input(f"Enter Description for {item_name}: ").strip()
        price = float(input(f"Enter Price for {item_name}: "))
        items[item_name] = (description, price)

    if not items:
        items = {
            "Item A": ("Description A", 29.99),
            "Item B": ("Description B", 49.99),
            "Item C": ("Description C", 9.99)
        }

    total_amount = sum(price for _, (_, price) in items.items())

    logo_path = "logo.png"  # Replace with your logo path

    filename = f"receipt_{receipt_id}.pdf"
    document_title = "Payment Receipt"
    title = "Payment Receipt"
    receipt_info = f"Receipt ID: {receipt_id}"
    date = f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    payment_method = "Payment Method: Credit Card"
    company_info = [
        "Company Name",
        "1234 Main St",
        "City, State ZIP",
        "Phone: (123) 456-7890",
        "Email: info@company.com"
    ]

    c = canvas.Canvas(filename, pagesize=letter)
    c.setTitle(document_title)

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(300, 750, title)

    # Receipt Information
    c.setFont("Helvetica", 12)
    c.drawString(30, 700, receipt_info)
    c.drawString(400, 700, date)
    c.drawString(30, 680, payment_method)

    # Customer Information
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, 650, "Customer Information")
    c.setFont("Helvetica", 12)
    c.drawString(30, 630, f"Name: {customer_name}")

    # Items Purchased
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, 600, "Items Purchased")
    c.setFont("Helvetica", 12)

    y_position = 580
    for item, (description, price) in items.items():
        c.drawString(30, y_position, f"{item} ({description}): ${price:.2f}")
        y_position -= 20

    # Total Amount
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y_position - 20, f"Total Amount: ${total_amount:.2f}")

    # Company Contact Information
    c.setFont("Helvetica", 12)
    y_position -= 60
    for line in company_info:
        c.drawString(30, y_position, line)
        y_position -= 15

    # QR Code
    qr_data = f"Receipt ID: {receipt_id}\nDate: {date}\nTotal Amount: ${total_amount:.2f}"
    qr_image = generate_qr_code(qr_data)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
        tmpfile.write(qr_image.getvalue())
        tmpfile_path = tmpfile.name
    c.drawImage(tmpfile_path, 450, y_position - 50, width=1 * inch, height=1 * inch)
    os.remove(tmpfile_path)  # Clean up the temporary file

    # Terms and Conditions
    c.setFont("Helvetica", 10)
    c.drawString(30, y_position - 120, "Terms and Conditions: All sales are final. No refunds or exchanges.")

    # Closing
    c.setFont("Helvetica", 12)
    c.drawString(30, y_position - 150, "Thank you for your purchase!")

    # Draw the logo below the "Thank you" note
    if logo_path:
        logo_width = 225 / 96 * inch  # converting pixels to inches (assuming 96 dpi)
        logo_height = 225 / 96 * inch
        add_logo(c, logo_path, 30, y_position - 350, width=logo_width, height=logo_height)

    c.save()
    print(f"Receipt saved as {filename}")

    # Open the PDF automatically
    webbrowser.open_new(filename)


# Call the function to create the receipt
create_receipt()
