from qrisp import QuantumVariable, h
from qrisp.interface import IQMBackend

random_number = QuantumVariable(4, name="random_number")

# hadamard gate (h) 
# this quantum gate transforms the qubit into superposition 
# and superposition means that qubit can be %50 chance |0> and %50 chance |1>
h(random_number[0])
h(random_number[1])
h(random_number[2])
h(random_number[3])

api_token = input("Bip Bop token token: ")
QuantumComputer = IQMBackend(api_token = api_token, device_instance="garnet")

result = random_number.get_measurement(backend=QuantumComputer, shots=1000)
print(result)

#results

#{'1011': 0.075, '0011': 0.074, '1100': 0.073, '0101': 0.071, '0001': 0.068, '0000': 0.067, '1001': 0.065, '0010': 0.064, '0100': 0.063, '0110': 0.063, '1000': 0.056, '1010': 0.056, '1101': 0.056, '0111': 0.051, '1111': 0.051, '1110': 0.047}

#as it is shown here that the chances are not equal beacuse of noise interruption in the quantum computer
#running this again and again probably give different results each time
