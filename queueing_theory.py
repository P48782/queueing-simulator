# queueing_theory.py

import math
from math import factorial

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
    if arrival_rate >= service_rate * c:
        return {"Error": "System is unstable (λ ≥ cμ)"}

    rho = arrival_rate / (c * service_rate)
    a = arrival_rate / service_rate

    def calc_p0():
        sum_terms = sum((a ** n) / factorial(n) for n in range(c))
        last_term = (a ** c) / (factorial(c) * (1 - rho))
        return 1 / (sum_terms + last_term)

    p0 = calc_p0()
    pw = ((a ** c) * p0) / (factorial(c) * (1 - rho))
    Lq = pw * rho * c / (1 - rho)
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
