# Monte Carlo Simulation Assignment

This repository contains Python implementations for Monte Carlo simulations of dice and coin flip experiments as part of the assignment.

## 📌 Problems Covered

1. **Yahtzee Probability (a)**  
   Estimate the probability of rolling a Yahtzee (all 5 dice the same).

2. **Large Straight Probability (b)**  
   Estimate the probability of rolling a large straight (1-2-3-4-5 or 2-3-4-5-6 in any order).

3. **Longest Run in 200 Coin Flips (c)**  
   Estimate the average longest consecutive run of heads/tails in 200 flips.

4. **Flips Until 5 Heads in a Row (d)**  
   Estimate the expected number of flips required before 5 consecutive heads occur.

5. **Flips Until Custom Pattern Appears (e)**  
   Compute the expected waiting time for a custom pattern (e.g., HHTTH) using automaton method.

---

## ⚙️ Setup

```bash
# Clone repo
git clone https://github.com/your-username/montecarlo-assignment.git
cd montecarlo-assignment

# Install dependencies
pip install -r requirements.txt
```

Dependencies:
- numpy
- pytest (for testing)

---

## ▶️ Running Simulations

Run the main script:
```bash
python src/montecarlo.py
```

**Expected sample output:**
```
Monte Carlo Simulation Results
(a) Yahtzee ≈ 0.000760 (theoretical 0.0007716)
(b) Large straight ≈ 0.030820 (theoretical 0.030864)
(c) Longest run in 200 flips ≈ 7.92
(d) Flips until 5 heads ≈ 61.80 (theoretical 62)
(e) Flips until 'HHTTH' ≈ 20.00 (exact)
```

---

## 🧪 Running Tests

```bash
pytest -v
```

**Example test cases included:**
- Yahtzee probability close to 1/1296.
- Large straight probability close to 5/162.
- Expected flips until 5 heads ≈ 62.
- Expected waiting time for pattern "H" ≈ 2.

---

## 📊 Results & Validation

- **(a) Yahtzee** → Theoretical = 1/1296 ≈ 0.0007716. Simulation matches.
- **(b) Large Straight** → Theoretical = 5/162 ≈ 0.030864. Simulation matches.
- **(c) Longest Run (200 flips)** → Typically around 7–8.
- **(d) Flips until 5 Heads** → Theoretical = 62. Simulation ≈ 61–63.
- **(e) Pattern HHTTH** → Exact computed ≈ 20 flips.

---

## 📌 Jira Mapping

- Each assignment part (a–e) is a **Story** in Jira.
- Implementation + testing steps are **Tasks** under each story.
- Any simulation/test failure → **Bug**.

---

## 📖 Report

A short PDF report (`report.pdf`) is included with:
- Problem statement
- Simulation approach
- Results with theoretical comparisons
- Plots & distributions (where applicable)

---

## 👨‍💻 Authors
- Nishad Kadam (VNIT CSE)
