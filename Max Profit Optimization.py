import streamlit as st

st.set_page_config(page_title="Max Profit Optimizer", layout="centered")

st.title("🏗️ Max Profit Property Optimizer")
st.write("Find the optimal mix of properties to maximize profit.")

n = st.number_input("Enter Time Units", min_value=1, step=1)

if st.button("Calculate"):
    theatres = n // 5
    remaining = n % 5
    pubs = 1 if remaining >= 4 else 0
    earnings = theatres * 1500 + pubs * 1000

    st.success(f"💰 Total Earnings: ${earnings}")
    st.write("### Optimal Properties")
    st.write(f"🏭 Theatre (T): {theatres}")
    st.write(f"🍺 Pub (P): {pubs}")
    st.write("🏢 Commercial Park (C): 0")