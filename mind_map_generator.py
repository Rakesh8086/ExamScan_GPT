import tempfile
from graphviz import Digraph
from PIL import Image
import streamlit as st
import os


def generate_mind_map_from_list(keywords_list):
    central_topic = keywords_list[0]
    keywords = keywords_list[1:]

    # Create a new directed graph with the twopi layout
    mind_map = Digraph(comment='Mind Map', engine='twopi')

    # Set graph attributes to make it more spacious
    mind_map.attr(size='50,50', nodesep='3.0', ranksep='4.0')

    # Add the central topic node
    mind_map.node('A', central_topic, shape='rectangle', style='filled', color='lightblue', width='1.5', height='0.5')

    # Add keyword nodes and connect them to the central topic
    for i, keyword in enumerate(keywords):
        node_id = f'B{i}'
        mind_map.node(node_id, keyword, shape='rectangle', style='filled', color='lightgreen', width='1.5',
                      height='0.5')
        mind_map.edge('A', node_id)

    # Render the mind map to a temporary file
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_file_path = os.path.join(tmpdirname, 'mind_map.png')
        mind_map.render(tmp_file_path, format='png', cleanup=True)
        # st.write(tmp_file_path)

        # Open the image file
        with open(tmp_file_path + '.png', 'rb') as image_file:
            image = Image.open(image_file)
            image.load()

        # Display the image in Streamlit
        st.image(image, caption='Generated Mind Map', use_column_width=True)


ist = ['Indian Independence Movement', 'Early Nationalist Movements (1857-1905)', 'Moderate Phase (1885-1905)', 'Extremist Phase (1905-1919)', 'Ghadar Movement (1913-1915)', 'Non-Cooperation Movement (1920-1922)', 'Civil Disobedience Movement (1930-1934)', 'Quit India Movement (1942)', 'Role of Mahatma Gandhi', 'Partition of India (1947)']
generate_mind_map_from_list(ist)