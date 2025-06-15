import streamlit as st
from queueing_theory import mm1, mmc

st.set_page_config(page_title="Queueing Simulator", page_icon="📊")
st.title("📊 Queueing Simulator")

st.markdown("This simulator assumes **rates are per hour**.")
st.markdown("Ensure that **arrival rate (λ) is less than service rate (μ)** for the system to be stable.")

model_type = st.selectbox("Choose a model", ["M/M/1", "M/M/c"])

arrival_rate = st.number_input("Arrival Rate λ (customers per hour)", min_value=0.01, value=0.10, step=0.01)
service_rate = st.number_input("Service Rate μ (customers per hour)", min_value=0.01, value=0.10, step=0.01)

if model_type == "M/M/c":
    num_servers = st.number_input("Number of Servers (c)", min_value=1, step=1, value=1)

if st.button("Run Simulation"):
    if arrival_rate >= service_rate and model_type == "M/M/1":
        st.error("Error: Arrival rate (λ) must be less than service rate (μ) for M/M/1.")
    elif model_type == "M/M/1":
        result = mm1(arrival_rate, service_rate)
        st.subheader("Results")
        for key, value in result.items():
            st.write(f"**{key}:** {value:.4f}")
    else:
        if arrival_rate >= service_rate * num_servers:
            st.error("Error: Arrival rate (λ) must be less than c × μ for M/M/c.")
        else:
            result = mmc(arrival_rate, service_rate, num_servers)
            st.subheader("Results")
            for key, value in result.items():
                st.write(f"**{key}:** {value:.4f}")
