# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 15:22:45 2026

@author: user
"""

import streamlit as st
import pandas as pd
#import numpy as np

# Title of the app
st.title("Researcher Profile Page of Dr Adeola Oluwatoyin Osundiran")

# Collect basic information
name = "Dr.Adeola Oluwatoyin Osundiran"
field = "Maritime Transportation and Supply Chain"
institution = "University of South Africa"

# Display basic profile information
st.header("Researcher \Overview")
st.write("Adeola Oluwatoyin Osundiran")
st.write("Maritime Supply Chain")
st.write("University of South Africa")

st.write("Dr Adeola Oluwatoyin Osundiran is a scholar in maritime logistics and supply chain management, with research interests in port efficiency, maritime supply chain performance, digital ports, and trade facilitation in Africa. Her work bridges academic research and policy, focusing on how technology and governance reforms can improve port competitiveness and regional trade integration. She has supervised postgraduate research at Master’s and PhD levels and contributes to capacity building in maritime transport, logistics, and supply chain education.")
st.image("https://github.com/niyot31-sys/css_streamlit_2026/blob/main/Dr%20Mrs%20Adeola%20Oluwatoyin%20Osundiran.jpg")



#Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
st.write("Osundiran  Adeola Oluwatoyin (2026) The SWOT Analysis of Block Chain Technology: Framework for Sub Saharan African Ports Journal of Maritime Research Vol. 22 No. 3 (2025) https://www.jmr.unican.es/jmr/issue/view/76")

st.write("Osundiran A.O and Tshehla M(2025)An Examination of the Impact of Artificial Intelligence on Maritime Port Efficiency and Businesses. Huibrecht Margaretha van der Poll, John Andrew van der Poll, Collins Chigaemecha Ngwakwe (Eds) (2025) Diversity, AI, and Sustainability for Financial Growth. Projected Release Date: January, 2025|Copyright: © 2025 |Pages: 430.DOI: 10.4018/979-8-3693-6011-8. ISBN13: 9798369360118|ISBN13 Softcover: 9798369360125|EISBN13:9798369360132")
st.write("Osundiran Adeola Oluwatoyin (2024) Chapter 10: An Exploration of the Indispensability and Challenges of Digitalisation through the Lens of Women in Maritime Domain. Ojo, T.A., & Ndzendze, B. (Eds.). (2024). African Women in the Fourth Industrial Revolution: Change, Policies, and Approaches (1st ed.). Pages 154-171Routledge. https://doi.org/10.4324/9781003517443. Published December 2024")
       


st.header("Contact Information")
email = "adeolaoluwatoyinosundiran@gmail.com"

st.write(f"You can reach {name} at {email}.")
