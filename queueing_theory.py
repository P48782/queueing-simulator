import math

def get_user_input():
    print("Welcome to the Queueing Simulator!")
    arrival_rate = float(input("Enter the arrival rate (λ): "))
    service_rate = float(input("Enter the service rate (μ): "))
    return arrival_rate, service_rate


def mm1(arrival_rate, service_rate):
    if arrival_rate >= service_rate:
        return {"Error": "System is unstable (λ ≥ μ)"}

    rho = arrival_rate / service_rate
    L = rho / (1 - rho)
    Lq = rho ** 2 / (1 - rho)
    W = 1 / (service_rate - arrival_rate)
    Wq = arrival_rate / (service_rate * (service_rate - arrival_rate))

    return {
        "Utilization (ρ)": rho,
        "Avg # in System (L)": L,
        "Avg # in Queue (Lq)": Lq,
        "Avg Time in System (W)": W,
        "Avg Time in Queue (Wq)": Wq
    }


def mmc(arrival_rate, service_rate, c):
    from math import factorial

    if arrival_rate >= service_rate * c:
        return {"Error": "System is unstable (λ ≥ cμ)"}

    rho = arrival_rate / (c * service_rate)
    a = arrival_rate / service_rate

    # Compute P0 (probability of zero customers in system)
    def calc_p0():
        sum_terms = sum([(a ** n) / factorial(n) for n in range(c)])
        last_term = ((a ** c) / (factorial(c) * (1 - rho)))
        return 1 / (sum_terms + last_term)

    p0 = calc_p0()

    # Probability that a customer has to wait
    pw = ((a ** c) * p0) / (factorial(c) * (1 - rho))

    Lq = pw * rho / (1 - rho) * c
    L = Lq + a
    Wq = Lq / arrival_rate
    W = Wq + 1 / service_rate

    return {
        "Utilization (ρ)": rho,
        "Probability Wait (Pw)": pw,
        "Avg # in System (L)": L,
        "Avg # in Queue (Lq)": Lq,
        "Avg Time in System (W)": W,
        "Avg Time in Queue (Wq)": Wq
    }
if __name__ == "__main__":
    arrival_rate, service_rate = get_user_input()

    model = input("Enter model type (M/M/1 or M/M/c): ").strip().lower()

    if model == "m/m/1":
        result = mm1(arrival_rate, service_rate)
    elif model == "m/m/c":
        c = int(input("Enter number of servers (c): "))
        result = mmc(arrival_rate, service_rate, c)
    else:
        result = {"Error": "Invalid model type."}

    print("\n--- Simulation Results ---")
    for key, value in result.items():
        print(f"{key}: {value}")
