from PIL import Image

img = Image.open("static/tie-fighter-white.png")

# Crop off the bottom (where signature usually is)
# Format: (left, top, right, bottom)
width, height = img.size
cropped = img.crop((0, 100, width, height - 180))  # adjust 30 to taste

cropped.save("static/tie-fighter.png")