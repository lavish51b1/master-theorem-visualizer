# Master Theorem Visualizer

An interactive visualization tool for understanding the basic Master Theorem used in the analysis of divide-and-conquer algorithms.

## Features

- User-defined values of `a` and `b`
- Selection of common forms of `f(n)`
- Displays the recurrence `T(n) = aT(n/b) + f(n)`
- Calculates `n^(log_b a)`
- Identifies Master Theorem Case 1, Case 2, or Case 3
- Displays the resulting asymptotic complexity
- Visualizes recursive growth across different recursion levels

## Technologies Used

- Python
- Streamlit
- Matplotlib

## Installation

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your web browser.

## Example

For the input:

- `a = 2`
- `b = 2`
- `f(n) = n`

The recurrence is:

`T(n) = 2T(n/2) + n`

The program calculates:

`n^(log_2 2) = n`

Since `f(n) = n` has the same polynomial growth as `n^(log_b a)`, Case 2 of the Master Theorem applies.

Therefore:

`T(n) = Θ(n log n)`

## Project Structure

```text
master-theorem-visualizer/
├── app.py
├── requirements.txt
└── README.md
```

## Purpose

This project demonstrates how the Master Theorem determines the asymptotic complexity of divide-and-conquer recurrences. The interactive visualization helps connect the mathematical cases of the theorem with the recursive structure of an algorithm.