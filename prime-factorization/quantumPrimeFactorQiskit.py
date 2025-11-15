from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit import transpile
from qiskit.algorithms import Shor
import time

def run_shor(N):
    #statevector/unitary simulator
    backend = Aer.get_backend('aer_simulator')
    qi = QuantumInstance(backend, shots=1024)
    shor = Shor(quantum_instance=qi)
    t0 = time.time()
    result = shor.factor(N)
    t1 = time.time()
    return result, t1 - t0

if __name__ == "__main__":
    N = 1000  #(8051) large N on simulator may be infeasible locally (be aware of local machine computer power)
    print("Running Shor for N =", N)
    res, secs = run_shor(N)
    print("Result:", res)
    print("Elapsed (s):", secs)
