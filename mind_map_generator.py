import tempfile
import os
from graphviz import Digraph
import streamlit as st
import ast


def generate_mind_map_from_list(keywords_list, mind_map_type):
    try:
        # print(keywords_list)
        # Ensures that the input is a list, not a string representation of a list.
        if isinstance(keywords_list, str):
            # Convert string representation of list to actual list.
            keywords_list = ast.literal_eval(keywords_list)

        # Print statements for debugging
        # print("Keywords List:", keywords_list)

        # Check if the list is empty
        # if not keywords_list:
        #   raise ValueError("The list of keywords is empty.")

        central_topic = keywords_list[0]
        # print("Central Topic:", central_topic)
        keywords = keywords_list[1:]
        # print("Keywords:", keywords)

        if mind_map_type == "Circo":
            mind_map = Digraph(comment='Mind Map', engine='Circo')
            mind_map.attr(size='40,40!', nodesep='2', ranksep='2')

        elif mind_map_type == "Dot":
            mind_map = Digraph(comment='Mind Map', engine='dot')
            mind_map.attr(size='100,20!', nodesep='1', ranksep='1')

        # Add central topic node
        mind_map.node('A', central_topic, shape='ellipse', style='filled', color='lightblue', width='1.5', height='0.5')

        # Add keyword nodes and connect them to the central topic
        for i, keyword in enumerate(keywords):
            node_id = f'B{i}'
            mind_map.node(node_id, keyword, shape='ellipse', style='filled', color='lightgreen', width='1.5',
                          height='0.5')
            mind_map.edge('A', node_id)

        # Store the mind map to a temporary file
        with tempfile.TemporaryDirectory() as tempdirname:
            temp_file_path = os.path.join(tempdirname, 'mind_map')
            mind_map.render(temp_file_path, format='png', cleanup=True)
            image_path = temp_file_path + '.png'

            st.image(image_path, caption='Generated Mind Map', use_column_width=True)

            with open(image_path, 'rb') as image_file:
                st.download_button(label="Download Mind Map", data=image_file, file_name="mind_map.png",
                                   mime="image/png")

    except SyntaxError as e:
        st.error(f"An unexpected error occurred")

    except ValueError as e:
        st.error(f"An unexpected error occurred")
