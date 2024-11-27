import streamlit as st
import numpy as np
import time
import os
from PIL import Image
import json
import pandas as pd

from src.read_asset_inventory import read_asset_inventory
from src.save_image import save_architecture_image

system_details_a = """System A is a HR system that keep track of staff movement contain employee data. The system is fully outsource and maintain onsite in the agency data centre."""
system_details_b = """System B is a cloud system that keep track of citizen's CPF. It has an mobile application that allows citizen to check their CPF. This is fully insource and maintain by GT staff."""

st.title("🤖 System Risk Advisor")
st.write("Start by uploading the necessary documents below.")


container = st.container(border=True)

sub_system_list = ['-', 'System A (On-prem)', 'System B (Cloud)']
selected_sub_system = container.selectbox("Select a system for assessment:", sub_system_list)

if selected_sub_system == "System A (On-prem)":
    container.markdown(
        f"""
        <div style="
            display: inline-block;
            background-color: #e0f7fa;
            color: #00796b;
            font-size: 13px;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 10px;
            border: 1px solid #00796b;
        ">
            System Details
        </div>
        <p style="margin-top: 10px; font-size: 14px;">
            {system_details_a}
        </p>
        """,
        unsafe_allow_html=True
    )
elif selected_sub_system == "System B (Cloud)":
    container.markdown(
        f"""
        <div style="
            display: inline-block;
            background-color: #e0f7fa;
            color: #00796b;
            font-size: 13px;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 10px;
            border: 1px solid #00796b;
        ">
            System Details
        </div>
        <p style="margin-top: 10px; font-size: 14px;">
            {system_details_b}
        </p>
        """,
        unsafe_allow_html=True
    )
    
# File uploader
container.write(" ")
architecture_diagram = container.file_uploader(
    "Upload system architecture diagram:", 
    accept_multiple_files=False,
    type=["png", "jpg"]
)

if architecture_diagram:
    expander_image = container.expander("Preview")
    expander_image.image(architecture_diagram)


container.write(" ")
asset_inventory = container.file_uploader("Upload asset inventory:", 
                                   accept_multiple_files=False,
                                   type=["csv", "xlsx", "xls"]
                                   )

# read asset inventory item
if asset_inventory:
    asset_inventory_df = read_asset_inventory(asset_inventory)
    expander_asset = container.expander("Preview")
    expander_asset.dataframe(asset_inventory_df)


# Display the button only after at least one file is uploaded

if selected_sub_system != "-":
    # if architecture_diagram and asset_inventory:  # Check if any file is uploaded
        
    save_architecture_image(architecture_diagram)
    
    analyse_btn = st.button("Perform Risk Assessment")
    progress_bar = st.sidebar.empty()
    status_text = st.sidebar.empty()
    message_text = st.sidebar.empty()

    # Initialize session state
    if "function_ran" not in st.session_state:
        st.session_state.function_ran = False

    
    if analyse_btn:
        
        system_name = selected_sub_system
        
        data = {'System': [system_name]}
        
        df = pd.DataFrame(data)
        
        df.to_excel("database/selected_system.xlsx", index = None)
        
        with st.status("Performing risk assessment...", expanded=True) as status:
            
            # Initiate the progress bar and placeholder for percentage
            progress_bar.progress(0)
            
            # Stages and their messages
            stages = [
                ("• Step 1: Validating user inputs ...", 10, 2),
                ("• Step 2: Extracting sub-system information from DGP ...", 10, 1),
                ("• Step 3: Analysing architecture diagram ...", 10, 3),
                ("• Step 4: Analysing asset inventory ...", 10, 3),
                ("• Step 5: Searching web for vulnerabilities ...", 10, 2),
                ("• Step 6: Generating relevant risk scenarios ...", 10, 4),
                ("• Step 7: Retrieving current controls from SSP ...", 10, 1),
                ("• Step 8: Calculating inherent risks ...", 10, 3),
                ("• Step 9: Recommending mitigating controls ...", 10, 2),
                ("• Step 10: Calculating residual risks ...", 5, 4),
                ("• Step 11: Preparing risk assessment report ...", 5, 4),
            ]
            
            # Iterate through stages and update progress bar and percentage
            current_progress = 0
            for stage, progress, timer_sleep in stages:
                st.text(stage)  # Display the stage message
                time.sleep(timer_sleep)  # Simulate time taken for the stage
                current_progress += progress  # Increment progress
                progress_bar.progress(current_progress)  # Update progress bar
                status_text.text(f"{current_progress}% Complete")  # Update percentage
            
            progress_bar.empty()  # Clear progress bar after completion
            status_text.empty()  # Clear percentage after completion

        status.update(label="Risk assessment complete!", state="complete", expanded=False)
        
        st.success("Navigate to the **Chatbot** or **Architecture Review* page to interact with the output.", icon="✅")
        
        st.session_state.function_ran = True
            
    # else:
    #     st.info("Please upload all the required documents to initiate the risk assessment.")
else:
    st.info("ℹ️ Please select a system.")

