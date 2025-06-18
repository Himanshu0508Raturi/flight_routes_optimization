import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Flight Route Optimization System",
    page_icon="✈️",
    layout="wide"
)

# ----------------------
# Title & Description
# ----------------------
st.title("✈️ Flight Route Optimization System")
st.subheader("An Graph-Based Travel Planner")

st.markdown("""
Welcome to the **Flight Route Optimization System** – a graph-theory-powered platform that simulates real-world flight networks using the most efficient algorithms:

- 🔄 **Bellman-Ford Algorithm** for finding shortest route between source to destination in terms of cost , distance and time.
- 🔁 **Floyd-Warshall Algorithm** for finding all-pair shortest paths.
- 🌐 **Kruskal’s Algorithm** for building the most cost-effective airline network (Minimum Spanning Tree).

You can:
- 💡 Explore how different algorithms work on flight networks.
- 🔎 Visualize and interact with airports and routes.
- ✍️ Learn how each algorithm optimizes different aspects of air travel.

---
""")

# ----------------------
# Project Overview Image
# ----------------------
image = Image.open("image.png")  # Replace with your actual project diagram/image if needed
st.image(image, use_container_width=True, caption="Flight Graph Network Overview")

# ----------------------
# Interactive Buttons to External Streamlit Apps
# ----------------------

st.markdown("## 🌐 Choose an Algorithm to Explore")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("###  Bellman-Ford")
    st.markdown("Used for **Flight Cost Optimization** in networks with possible negative weights.")
    if st.button(" Launch Bellman-Ford App"):
        st.markdown("[Click here to open Bellman-Ford UI](https://flightroutesoptimization-dh2nau4vpqkeijvmibvb35.streamlit.app/)", unsafe_allow_html=True)

with col2:
    st.markdown("###  Floyd-Warshall")
    st.markdown("Used to find **All-Pairs Shortest Paths**, and suggest **Alternative Flight Routes**.")
    if st.button(" Launch Floyd-Warshall App"):
        st.markdown("[Click here to open Floyd-Warshall UI](https://flightroutesoptimization-tubftzjzbytg3mjdo96ubc.streamlit.app/)", unsafe_allow_html=True)

with col3:
    st.markdown("###  Kruskal’s Algorithm")
    st.markdown("Used to build an **Optimal Flight Network** with Minimum Cost using MST.")
    if st.button(" Launch Kruskal App"):
        st.markdown("[Click here to open Kruskal UI](https://flightroutesoptimization-mfiszawnwa8hzvo8n3wecq.streamlit.app/)", unsafe_allow_html=True)

# ----------------------
# Footer
# ----------------------
st.markdown("---")
st.markdown("Created By:")
st.markdown("[Tanish Kothiyal](https://www.linkedin.com/in/tanish-kothiyal-752448298/)")
st.markdown("[Himanshu Raturi](https://www.linkedin.com/in/himanshu-raturi-99ab0728b/)")
st.markdown("[Priyanshu Joshi](https://www.linkedin.com/in/priyanshu-joshi-1a1a782b8/)")
