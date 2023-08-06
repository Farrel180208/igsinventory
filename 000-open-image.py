from PIL import Image, ImageDraw

# Create a list of images to be used in the GIF
frames = []

# Create a blank canvas
width, height = 200, 200
background_color = (255, 255, 255)
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Create frames by drawing on the canvas
for i in range(10):
    # Clear the canvas by filling it with the background color
    draw.rectangle((0, 0, width, height), fill=background_color)
    
    # Draw a rectangle that moves from left to right
    rect_color = (255, 0, 0)
    rect_width = 30
    rect_height = 30
    x_position = i * 20
    y_position = height // 2 - rect_height // 2
    draw.rectangle((x_position, y_position, x_position + rect_width, y_position + rect_height), fill=rect_color)
    
    # Append the current frame to the list of frames
    frames.append(image.copy())

# Save the frames as a GIF
frames[0].save("animation.gif", save_all=True, append_images=frames[1:], loop=0, duration=100)

print("GIF created successfully!")
