import qrcode
from PIL import Image

# Function to generate QR code with logo
def generate_qr_code_with_logo(link, logo_path, output_path, logo_size, border_size):
    try:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Load the logo image
        logo_img = Image.open(logo_path).convert("L")  # Convert to black and white

        # Crop black border from logo image
        logo_img = crop_black_border(logo_img)

        # Resize logo image
        logo_img = logo_img.resize((logo_size, logo_size))

        # Create a new image with a white border around the logo
        logo_with_border = Image.new("L", (logo_size + 2 * border_size, logo_size + 2 * border_size), color="white")

        # Calculate position to paste the logo on the new image
        paste_pos = ((logo_with_border.width - logo_img.width) // 2, (logo_with_border.height - logo_img.height) // 2)

        # Paste the logo onto the new image with a white border
        logo_with_border.paste(logo_img, paste_pos)

        # Calculate position to center the logo with border on the QR code
        pos = ((qr_img.size[0] - logo_with_border.size[0]) // 2, (qr_img.size[1] - logo_with_border.size[1]) // 2)

        # Paste logo with border on QR code
        qr_img.paste(logo_with_border, pos)

        # Save the image in PNG format
        qr_img.save(output_path, format="PNG")

        print("QR code with logo and white border generated successfully!")
    except Exception as e:
        print("Error generating QR code:", e)
        raise

# Function to crop black border from image
def crop_black_border(img):
    # Get bounding box of non-black pixels
    bbox = img.getbbox()
    # Crop the image to the bounding box
    cropped_img = img.crop(bbox)
    return cropped_img

# Link
link = "https://www.linkedin.com/in/oscar-anandh-s-a14980226/"
# Path to the LinkedIn logo image
logo_path = "linkedin_logo.png"
# Output path and filename for the generated QR code with logo
output_path_with_logo = "linkedin_qr_code_with_logo_and_border.png"
# Size of the logo
logo_size = 100
# Size of the white border around the logo
border_size = 5

# Generate QR code with logo and white border
generate_qr_code_with_logo(link, logo_path, output_path_with_logo, logo_size, border_size)

# Open the generated image
from PIL import Image
image = Image.open(output_path_with_logo)
image.show()
