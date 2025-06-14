import math

def get_user_input():
    print("Welcome to the Queueing Simulator!")
    arrival_rate = float(input("Enter the arrival rate (λ): "))
    service_rate = float(input("Enter the service rate (μ): "))
    return arrival_rate, service_rate

def mm1():
    arrival_rate, service_rate = get_user_input()

    if arrival_rate >= service_rate:
        print("Warning: Arrival rate must be less than service rate for a stable system.")
        return

    rho = arrival_rate / service_rate
    L = rho / (1 - rho)
    W = 1 / (service_rate - arrival_rate)

    print("\n--- M/M/1 Results ---")
    print(f"System Utilization (ρ): {rho:.3f}")
    print(f"Average number in system (L): {L:.3f}")
    print(f"Average time in system (W): {W:.3f}")

def mmc():
    arrival_rate, service_rate = get_user_input()
    c = int(input("Enter number of servers (c): "))

    rho = arrival_rate / (c * service_rate)

    if rho >= 1:
        print("Warning: System is unstable (ρ ≥ 1).")
        return

    sum_terms = sum([(arrival_rate / service_rate) ** n / math.factorial(n) for n in range(c)])
    last_term = ((arrival_rate / service_rate) ** c) / (math.factorial(c) * (1 - rho))
    p0 = 1 / (sum_terms + last_term)

    lq = (p0 * ((arrival_rate / service_rate) ** c) * rho) / (math.factorial(c) * ((1 - rho) ** 2))
    ls = lq + (arrival_rate / service_rate)
    wq = lq / arrival_rate
    ws = wq + 1 / service_rate

    print("\n--- M/M/c Results ---")
    print(f"Utilization (ρ): {rho:.3f}")
    print(f"P0 (zero in system): {p0:.3f}")
    print(f"Average number in queue (Lq): {lq:.3f}")
    print(f"Average number in system (Ls): {ls:.3f}")
    print(f"Average waiting time in queue (Wq): {wq:.3f}")
    print(f"Average time in system (Ws): {ws:.3f}")

def main():
    print("Select the Queue Model:")
    print("1. M/M/1")
    print("2. M/M/c")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        mm1()
    elif choice == "2":
        mmc()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

