
from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)

    # Get the pixel data
    pixels = image.load()

    # Encrypt each pixel using the key
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Perform encryption using the key
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            # Update the pixel data
            pixels[x, y] = (r, g, b)

    # Save the encrypted image
    encrypted_image_path = image_path.replace('.png', '_encrypted.png')
    image.save(encrypted_image_path)

    # Return the path of the encrypted image
    return encrypted_image_path

# Test the encryption function
image_path = 'path/to/image.png'
key = 10
encrypted_image_path = encrypt_image(image_path, key)
print(f"Encrypted image saved at: {encrypted_image_path}")
