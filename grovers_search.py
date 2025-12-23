import numpy as np
from qrisp import QuantumVariable, h, x, z, mcx, control, measure
from qrisp.interface import IQMBackend

SECRET_KEY = 26
N_QUBITS = 8

#to be honest I am too lazy to explain this in text
#but if you dont know it, you should definitly check it on youtube, absolutely beautiful
#in a very very short explanation, the algorithm comes from the unit chamber
#we are basicly trying to get our guessing vector closer step by step to target vector, and there is actually a formula to know after how many iterations it will be closest -or same in a perfect simulation- to target value
#when certain number of iterations are done, you measure the guessing vector and with %99 chance -or %100 in a perfect simulation- you will find the target value
#the time complexity is O(sqrt(N))

def oracle(our_guess, secret_key):
    print("Debug: Oracle is being used")
    for i in range(N_QUBITS):
        if not (secret_key >> i) & 1:
            x(our_guess[i])
    
    with control(our_guess[:-1]):
        z(our_guess[-1])

    for i in range(N_QUBITS):
        if not (secret_key >> i) & 1:
            x(our_guess[i])

def diffuser(our_guess):
    print("Debug: Diffuser is being used")
    h(our_guess)
    x(our_guess)

    with control(our_guess[:-1]):
        z(our_guess[-1])
    
    x(our_guess)
    h(our_guess)

def main():
    api_token = input("Give me your precious token or one kitty will explode: ")
    try:
        QuantumComputer = IQMBackend(api_token = api_token, device_instance="garnet")
        print("Connected to IQM backend")

    except Exception:
        print("Couldn't connect to IQM backend")
        exit

    our_guess = QuantumVariable(N_QUBITS, name="our_guess")
    h(our_guess)

    N = 2**N_QUBITS
    optimal_iterations = int(np.floor((np.pi / 4) * np.sqrt(N)))
    print(f"Searching for secret key {SECRET_KEY} in {N} possibilities")
    print(f"Running {optimal_iterations} Grover iterations")

    for i in range(optimal_iterations):
        oracle(our_guess, SECRET_KEY)
        diffuser(our_guess)

    print("Debug: Measuring the guess")
    results = our_guess.get_measurement(QuantumComputer)
    print(f"Result: {results}")

if __name__ == "__main__":
    main()