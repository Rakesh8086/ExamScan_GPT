from PIL import Image, ImageDraw, ImageFont
import math
import tempfile
import streamlit as st


def draw_mind_map(central_topic, keywords):
    # Create a blank image
    img = Image.new('RGB', (800, 800), color='white')
    draw = ImageDraw.Draw(img)

    # Load a font
    font = ImageFont.load_default()

    # Define the center position
    center_x, center_y = img.width // 2, img.height // 2

    # Draw the central topic node
    central_bbox = draw.textbbox((0, 0), central_topic, font=font)
    central_width, central_height = central_bbox[2] - central_bbox[0], central_bbox[3] - central_bbox[1]
    draw.rectangle([center_x - central_width // 2 - 10, center_y - central_height // 2 - 10,
                    center_x + central_width // 2 + 10, center_y + central_height // 2 + 10],
                   outline='black', fill='lightblue')
    draw.text((center_x - central_width // 2, center_y - central_height // 2), central_topic, fill='black', font=font)

    # Define the radius for the points around the central topic
    radius = 250
    angle_step = 360 / len(keywords)

    # Draw keyword nodes around the central topic
    for i, keyword in enumerate(keywords):
        angle = math.radians(i * angle_step)
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))

        keyword_bbox = draw.textbbox((0, 0), keyword, font=font)
        keyword_width, keyword_height = keyword_bbox[2] - keyword_bbox[0], keyword_bbox[3] - keyword_bbox[1]
        draw.rectangle([x - keyword_width // 2 - 10, y - keyword_height // 2 - 10,
                        x + keyword_width // 2 + 10, y + keyword_height // 2 + 10],
                       outline='black', fill='lightgreen')
        draw.text((x - keyword_width // 2, y - keyword_height // 2), keyword, fill='black', font=font)

        # Draw lines connecting the central topic to the keywords
        if i == 0:
            draw.line([center_x - 10, center_y, x - 25, y], fill='black')
        elif i == 5:
            draw.line([center_x + 10, center_y, x + 25, y], fill='black')
        elif i in [1, 2, 3, 4]:
            draw.line([center_x, center_y, x, y - 15], fill='black')
        elif i in [6, 7, 8, 9]:
            draw.line([center_x, center_y, x, y + 15], fill='black')

    # Save the image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        img.save(temp_file.name)
        temp_file_path = temp_file.name

    return temp_file_path

# Streamlit application
st.title("Mind Map Generator")

# Example usage
central_topic = "Central Topic"
keywords = ["Point 1", "Point 2", "Point 3", "Point 4", "Point 5", "Point 6", "Topic 7", "Topic 8", "Topic 9", "Topic 10"]

if st.button("Generate Mind Map"):
    mind_map_path = draw_mind_map(central_topic, keywords)
    st.image(mind_map_path, caption='Generated Mind Map', use_column_width=True)
