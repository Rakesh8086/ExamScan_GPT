import tempfile
import os
from graphviz import Digraph
import streamlit as st


def generate_mind_map_from_list(keywords_list):
    print(keywords_list)
    central_topic = keywords_list[0]
    print(central_topic)
    keywords = keywords_list[1:]
    print(keywords)

    # Create a new graph with the dot layout which is simple
    mind_map = Digraph(comment='Mind Map', engine='dot')

    mind_map.attr(size='100,70!', nodesep='0.75', ranksep='0.75')

    # central topic node
    mind_map.node('A', central_topic, shape='ellipse', style='filled', color='lightblue', width='1.5', height='0.5')

    # Keyword nodes connected to central node
    for i, keyword in enumerate(keywords):
        node_id = f'B{i}'
        mind_map.node(node_id, keyword, shape='ellipse', style='filled', color='lightgreen', width='1.5', height='0.5')
        mind_map.edge('A', node_id)

    # Store the mind map to a temporary directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_file_path = os.path.join(tmpdirname, 'mind_map')
        mind_map.render(tmp_file_path, format='png', cleanup=False)
        # Open the image file
        with open(tmp_file_path + '.png', 'rb') as image_file:
            st.download_button(label="Download Mind Map", data=image_file, file_name="mind_map.png", mime="image/png")
