import streamlit as st
import math
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Master Theorem Visualizer",
    page_icon="📊",
    layout="wide"
)

st.title("Master Theorem Visualizer")
st.write(
    "Explore recurrences of the form "
    r"$T(n)=aT(n/b)+f(n)$ and visualize how the recursive work grows."
)

st.sidebar.header("Recurrence Parameters")

a = st.sidebar.number_input(
    "Number of subproblems (a)",
    min_value=1,
    value=2,
    step=1
)

b = st.sidebar.number_input(
    "Reduction factor (b)",
    min_value=2,
    value=2,
    step=1
)

f_choice = st.sidebar.selectbox(
    "Choose f(n)",
    ["1", "log n", "n", "n log n", "n²", "n³"]
)

n_value = st.sidebar.slider(
    "Input size for visualization",
    min_value=8,
    max_value=1024,
    value=64,
    step=8
)

f_data = {
    "1": (0, 0, "1"),
    "log n": (0, 1, r"\log n"),
    "n": (1, 0, "n"),
    "n log n": (1, 1, r"n\log n"),
    "n²": (2, 0, r"n^2"),
    "n³": (3, 0, r"n^3")
}

f_power, log_power, f_latex = f_data[f_choice]

critical_power = math.log(a, b)

st.subheader("1. Recurrence")

st.latex(
    rf"T(n)={a}T\left(\frac{{n}}{{{b}}}\right)+{f_latex}"
)

st.subheader("2. Identify the Parameters")

col1, col2, col3 = st.columns(3)

col1.metric("a", a)
col2.metric("b", b)
col3.metric("log_b(a)", f"{critical_power:.3f}")

st.latex(
    rf"n^{{\log_b a}}=n^{{\log_{{{b}}}{a}}}"
    rf"\approx n^{{{critical_power:.3f}}}"
)

st.subheader("3. Compare the Growth Rates")

epsilon = 1e-9

if f_power < critical_power - epsilon:
    case = "Case 1"
    result = rf"\Theta(n^{{{critical_power:.3f}}})"
    explanation = (
        "f(n) grows polynomially slower than "
        "the recursive contribution."
    )

elif abs(f_power - critical_power) <= epsilon:
    case = "Case 2"

    final_log_power = log_power + 1

    if f_power == 0:
        if final_log_power == 1:
            result = r"\Theta(\log n)"
        else:
            result = rf"\Theta((\log n)^{{{final_log_power}}})"
    else:
        if final_log_power == 1:
            result = rf"\Theta(n^{{{f_power}}}\log n)"
        else:
            result = (
                rf"\Theta(n^{{{f_power}}}"
                rf"(\log n)^{{{final_log_power}}})"
            )

    explanation = (
        "f(n) has the same polynomial growth as "
        "the recursive contribution."
    )

else:
    regularity_ratio = a / (b ** f_power)

    if regularity_ratio < 1:
        case = "Case 3"

        if log_power == 0:
            result = rf"\Theta(n^{{{f_power}}})"
        else:
            result = (
                rf"\Theta(n^{{{f_power}}}"
                rf"(\log n)^{{{log_power}}})"
            )

        explanation = (
            "f(n) grows polynomially faster than the recursive "
            "contribution and the regularity condition is satisfied."
        )
    else:
        case = "Not directly applicable"
        result = "Use another recurrence-solving method."
        explanation = (
            "The conditions of the basic Master Theorem "
            "are not satisfied."
        )

st.info(explanation)

left, right = st.columns(2)

with left:
    st.markdown("### Applicable Case")
    st.success(case)

with right:
    st.markdown("### Final Complexity")

    if case == "Not directly applicable":
        st.warning(result)
    else:
        st.latex(result)

st.subheader("4. Recursion Tree Visualization")

levels = max(1, int(math.log(n_value, b)))

level_numbers = list(range(levels + 1))
number_of_nodes = []
problem_size = []

for level in level_numbers:
    number_of_nodes.append(a ** level)
    problem_size.append(n_value / (b ** level))

fig, ax = plt.subplots()

ax.plot(level_numbers, number_of_nodes, marker="o")
ax.set_xlabel("Recursion Level")
ax.set_ylabel("Number of Subproblems")
ax.set_title("Growth of Recursive Subproblems")
ax.grid(True)

st.pyplot(fig)

st.write("### Level-wise Recursion")

for level in level_numbers:
    nodes = a ** level
    size = n_value / (b ** level)

    st.write(
        f"Level {level}: {nodes} subproblem(s), "
        f"each of size approximately {size:.2f}"
    )

st.subheader("5. Interpretation")

st.write(
    f"At each recursive level, one problem produces {a} "
    f"subproblems, while the size of each problem is reduced "
    f"by a factor of {b}. The Master Theorem compares the "
    f"resulting recursive growth with f(n) = {f_choice}."
)