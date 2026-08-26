# 🔐 Project 11: Dead Man's Switch (Raspberry Pi 5)

> **Context**: Automated cryptographic vault using Shamir's Secret Sharing (Mersenne prime ^{521}-1$) to distribute contingency emergency keys if regular heartbeats lapse.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/11-deadmans-switch`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/11-deadmans-switch)  

---

## 1. Mathematical Architecture

Shamir's Secret Sharing (569Xof-$ threshold scheme) over the finite field $\mathbb{F}_p$ with Mersenne prime  = 2^{521} - 1$:
- **Splitting**: Generates polynomial (x) = S + a_1 x + \dots + a_{k-1} x^{k-1} \pmod p$.
- **Reconstruction**: Uses Lagrange polynomial interpolation with Fermat's Little Theorem modular inverses:
  55556S = \sum_{i=1}^k y_i \prod_{j 
eq i} rac{-x_j}{x_i - x_j} \pmod p55556

## 2. Verified Functionality & Test Suite

- `projects/11-deadmans-switch/tests/test_deadmans_switch.py`: Validates 521-bit Shamir polynomial splitting, 3-of-5 share reconstruction, and heartbeat timeout trigger logic.
- **Test Results**: 2/2 passing tests.
