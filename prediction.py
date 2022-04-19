"""This is the prediction page of the web app"""

# Import necessary modules

import streamlit as st
import PIL
import cv2
import os
import vehicle_count

def load_image(image):
    return PIL.Image.open(image)


def app():
    """This funciton runs the prediction page"""

    dict_weights = {
                    'car': 3,
                    'motorbike': 1,
                    'bus': 6,
                    'truck': 5
                    }
    st.write("Welcome to the Prediction Page")

    # Create a method to take image input from a user
    lane_images = []
    lane_images.append(st.file_uploader("Upload lane_1 image...", type=['png','jpeg','jpg']))
    lane_images.append(st.file_uploader("Upload lane_2 image...", type=['png','jpeg','jpg']))
    lane_images.append(st.file_uploader("Upload lane_3 image...", type=['png','jpeg','jpg']))
    lane_images.append(st.file_uploader("Upload lane_4 image...", type=['png','jpeg','jpg']))


    #Save images in upload folder.
    for i, img in enumerate(lane_images):
        if img is not None:
            img = load_image(img)
            img.save('upload/image_' + str(i+1)+'.jpg')
            # with open(os.path.join("upload",'image_'+str(i+1)+'.jpg'),"wb") as f: 
            #     f.write(img.getbuffer())         
        

    # Create a button to get the prediction values on click
    if (st.button("Predict")):
        
        lane_1_count = vehicle_count.from_static_image('upload/image_1.jpg', weight_dict=dict_weights, output_path='bounded_images/image_1.png')
        lane_2_count = vehicle_count.from_static_image('upload/image_2.jpg', weight_dict=dict_weights, output_path='bounded_images/image_2.png')
        lane_3_count = vehicle_count.from_static_image('upload/image_3.jpg', weight_dict=dict_weights, output_path='bounded_images/image_3.png')
        lane_4_count = vehicle_count.from_static_image('upload/image_4.jpg', weight_dict=dict_weights, output_path='bounded_images/image_4.png')
        

        lane_1_density = 0
        print(lane_1_count)
        for key, value in lane_1_count.items():
            lane_1_density += dict_weights[key] * value

        lane_2_density = 0
        print(lane_2_count)
        for key, value in lane_2_count.items():
            lane_2_density += dict_weights[key] * value
        lane_3_density = 0
        print(lane_3_count)
        for key, value in lane_3_count.items():
            lane_3_density += dict_weights[key] * value
        lane_4_density = 0
        print(lane_4_count)
        for key, value in lane_4_count.items():
            lane_4_density += dict_weights[key] * value

        
        total_density = lane_1_density + lane_2_density + lane_3_density + lane_4_density

        print(lane_1_density)
        print(lane_2_density)
        print(lane_3_density)
        print(lane_4_density)
        print(total_density)
        
        total_time = 5 * 60
        st.success("Time Allocated")
        st.success(f"lane_1: {lane_1_density*total_time/total_density}")
        st.success(f"lane_2: {lane_2_density*total_time/total_density}")
        st.success(f"lane_3: {lane_3_density*total_time/total_density}")
        st.success(f"lane_4: {lane_4_density*total_time/total_density}")