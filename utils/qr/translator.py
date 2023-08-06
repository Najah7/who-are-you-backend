"""
Generate QR code image from URL.

NOTE: it works only generating QR code image when using this as script.
"""

import sys

import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# NOTE: nothing special, just for refer to a sample code.
PIXEL_SIZE = 10
BORDER_SIZE = 4

def generate_qr(url, output_file, pixel_size=PIXEL_SIZE, border_size=BORDER_SIZE):
    """Generate QR code image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=pixel_size, 
        border=border_size,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

def read_qr(image_file):
    """Read QR code image."""
    img = Image.open(image_file)
    decoded_qr = decode(img)
    output_text = decoded_qr[0].data.decode("utf-8")
    
    return output_text

if __name__ == "__main__":
    
    read_or_generate = input("Do you want to generate or read QR code image? (g/r): ")
    if read_or_generate.startswith("g"):
        print("Generate QR code image.\n")
        url = input("text: ")
        output_file = input("output file: ") + ".png"
        generate_qr(url, output_file)
        print(f"Generated QR code image: {output_file}\n")
    elif read_or_generate.startswith("r"):
        print("Read QR code image.\n")
        image_file = input("image file: ")
        output_text = read_qr(image_file)
        print(f"Read QR code image: {image_file}")
        print(f"Output text: {output_text}\n")
    