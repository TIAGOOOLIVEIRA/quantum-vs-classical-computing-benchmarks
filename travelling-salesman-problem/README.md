# Travelling Salesman Problem (TSP)

## Overview

The Travelling Salesman Problem is a classic NP-hard optimization problem in graph theory. Given a list of cities and the distances between each pair of cities, the goal is to find the shortest possible route that visits each city exactly once and returns to the origin city.

## Problem Statement

Find the minimum cost Hamiltonian cycle in a weighted graph, where:
- Each vertex (city) must be visited exactly once
- The tour must return to the starting vertex
- The total distance/cost should be minimized

## Approaches

### Classical Algorithms
- **Brute Force**: O(n!) - Examines all possible permutations
- **Dynamic Programming (Held-Karp)**: O(n²2ⁿ) - More efficient for small to medium instances
- **Heuristics**: Nearest neighbor, 2-opt, genetic algorithms
- **Approximation Algorithms**: Christofides algorithm (1.5-approximation)

### Quantum Algorithms
- **Quantum Annealing**: Using quantum effects to find optimal or near-optimal solutions
- **Variational Quantum Eigensolver (VQE)**: Hybrid quantum-classical approach
- **Grover's Algorithm**: Quadratic speedup for search problems
- **Quantum Approximate Optimization Algorithm (QAOA)**: Designed for combinatorial optimization

## Applications

- **Logistics and Route Optimization**: Delivery routes, supply chain management
- **Manufacturing**: Circuit board drilling, robotic arm movement
- **DNA Sequencing**: Optimizing the order of fragment assembly
- **Network Design**: Efficient network routing and data packet delivery

## Benchmarks

This folder will contain implementations comparing:
- Runtime complexity for different problem sizes
- Solution quality (optimality vs. approximation)
- Scalability limits of classical vs. quantum approaches
- Hardware requirements and practical considerations

## Future Work

- Implementation of classical baseline algorithms
- Quantum algorithm implementations using frameworks like Qiskit, Cirq, or D-Wave
- Performance comparison and visualization
- Analysis of quantum advantage thresholds
