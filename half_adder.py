from qrisp import QuantumVariable, x, cx, mcx
from qrisp.interface import IQMBackend

#We created here 2 inputs and 2 outputs
a = QuantumVariable(1, name="a")
b = QuantumVariable(1, name="b")
carry = QuantumVariable(1, name="carry")
sum_bit = QuantumVariable(1, name="sum")

#by default, every Quantum Variable starts as 0
#but we are going to calculate 1+1, so we need to apply X gates
#it is the equivalent of NOT gate in classical computing
x(a[0])
x(b[0])

# This is the carry part, mcx gate is the equivalent of the AND gate
mcx([a[0], b[0]], carry[0])

# This is the sum part, cx gate is the equivalent of XOR gates
cx(a[0], sum_bit[0])
cx(b[0], sum_bit[0])

# connecting to IQM's Quantum Computer named Garnet
api_token = input("Enter your IQM Resonance API token here: ")
quantum_computer = IQMBackend(api_token=api_token, device_instance="garnet")

# a little feedback
print("Running on Quantum Computer...")

# measuring the sum
res_sum = sum_bit.get_measurement(backend=quantum_computer)
print(f"Sum bit result: {res_sum}")

# measuring the carry
res_carry = carry.get_measurement(backend=quantum_computer)
print(f"Carry bit result: {res_carry}")