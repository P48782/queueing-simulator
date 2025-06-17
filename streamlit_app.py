# streamlit_app.py

import streamlit as st
from queueing_theory import mm1, mmc

st.set_page_config(page_title="Store Efficiency Simulator", page_icon="🛒")
st.title("🛒 Store vs. SuperCenter: Queueing Efficiency Simulator")
st.markdown("""
Welcome! This tool helps you understand how efficiently your store or supercenter is operating based on customer traffic and service speed.

➡️ **Choose a store type**  
➡️ **Enter how many customers came in today**  
➡️ **Tell us how long it takes to serve one customer**

We'll simulate your system’s performance!
""")

# Step 1: Choose store type
store_type = st.radio("What kind of store do you own?", ["🏪 Store", "🏬 SuperCenter"])
model_type = "M/M/1" if store_type == "🏪 Store" else "M/M/c"

# Step 2: Daily customer input
st.subheader("📥 Daily Operations")
daily_customers = st.number_input("How many customers visited today?", min_value=1, step=1, help="Used to calculate arrival rate (λ)")
arrival_rate = daily_customers / 8  # per hour
st.markdown(f"📈 **Calculated Arrival Rate (λ)**: `{arrival_rate:.2f} customers/hour`")

# Step 3: Service time per customer
service_time_min = st.number_input("How long does a server take to serve one customer? (in minutes)", min_value=1, help="Used to calculate service rate (μ)")
service_time_hr = service_time_min / 60
service_rate = 1 / service_time_hr  # per hour
st.markdown(f"⚙️ **Calculated Service Rate (μ)**: `{service_rate:.2f} customers/hour`")

# Step 4: For SuperCenter, ask number of servers
if model_type == "M/M/c":
    num_servers = st.number_input("How many service counters do you have?", min_value=1, step=1, value=1)

# Step 5: Run simulation
if st.button("🚀 Run My Store Simulation"):
    if model_type == "M/M/1":
        if arrival_rate >= service_rate:
            st.error("System is unstable: Too many customers for one server. (λ ≥ μ)")
        else:
            result = mm1(arrival_rate, service_rate)
    else:
        if arrival_rate >= service_rate * num_servers:
            st.error("System is unstable: Too many customers for the number of servers. (λ ≥ cμ)")
        else:
            result = mmc(arrival_rate, service_rate, num_servers)

    if "Error" in result:
        st.error(result["Error"])
    else:
        st.success("✅ Your Store’s Performance:")
        st.metric("Utilization (ρ)", f"{result['Utilization (ρ)'] * 100:.2f}%")

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"👥 **Avg # in System (L)**: `{result['Avg # in System (L)']:.2f}`")
            st.write(f"⏱️ **Avg Time in System (W)**: `{result['Avg Time in System (W)']:.2f} hrs`")
        with col2:
            st.write(f"🧍‍♂️ **Avg # in Queue (Lq)**: `{result['Avg # in Queue (Lq)']:.2f}`")
            st.write(f"⌛ **Avg Time in Queue (Wq)**: `{result['Avg Time in Queue (Wq)']:.2f} hrs`")

        if model_type == "M/M/c":
            st.markdown(f"🧮 **Probability a customer has to wait (Pw)**: `{result['Probability Wait (Pw)'] * 100:.2f}%`")
