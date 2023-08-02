from PIL import Image, ImageDraw

# Create a list to store frames for the GIF
frames = []

# Create a loop to generate frames
for i in range(10):
    # Create a new image with a white background
    img = Image.new('RGB', (200, 200), 'white')
    
    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Draw a colored rectangle that changes with each frame
    draw.rectangle([50 + i*10, 50 + i*10, 150 + i*10, 150 + i*10], fill=(255, 0, 0))
    
    # Append the image to the frames list
    frames.append(img)

# Save the frames as a GIF
frames[0].save('animated.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)






