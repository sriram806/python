from PIL import Image
import matplotlib.pyplot as plt

# Load your images
friend_img = Image.open("saiteja.jpg").convert("RGBA")
peach_img = Image.open("peech.webp").convert("RGBA")

# Resize peach to roughly fit the head size
peach_resized = peach_img.resize((180, 180))

# Make a copy of the original photo
combined = friend_img.copy()

# Paste the peach image onto the head (you may need to tweak coordinates)
combined.paste(peach_resized, (260, 40), peach_resized)

# Show the result
plt.imshow(combined)
plt.axis('off')
plt.title("Peach Head 🤣")
plt.show()

# Optionally save it
combined.save("funny_peach_head.png")
