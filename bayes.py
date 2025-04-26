import streamlit as st

# Set page title
st.set_page_config(page_title="Bayes' Theorem Visualizer", layout="centered")

st.title("🔮 Bayes' Theorem Visualizer")

st.write("""
Adjust the sliders to set your prior and likelihoods, and observe how the posterior probability changes!
""")

# Inputs
st.header("Input Parameters") 

prior = st.slider('Prior Probability P(A)', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
likelihood = st.slider('Likelihood P(B|A)', min_value=0.0, max_value=1.0, value=0.7, step=0.01)
likelihood_not = st.slider('Likelihood P(B|¬A)', min_value=0.0, max_value=1.0, value=0.2, step=0.01)

# Calculate
p_b = likelihood * prior + likelihood_not * (1 - prior)
if p_b == 0:
    posterior = 0
else:
    posterior = (likelihood * prior) / p_b

# Output
st.header("Results")

st.metric(label="Posterior Probability P(A|B)", value=f"{posterior:.4f}")

st.write("---")
st.subheader("Bayes' Theorem Formula")
st.latex(r"""
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
""")
st.latex(r"""
P(B) = P(B|A) \times P(A) + P(B|\neg A) \times P(\neg A)
""")

# Extra: Show all intermediate calculations
with st.expander("See detailed calculations"):
    st.write(f"**Prior P(A):** {prior}")
    st.write(f"**Likelihood P(B|A):** {likelihood}")
    st.write(f"**Likelihood P(B|¬A):** {likelihood_not}")
    st.write(f"**Marginal Probability P(B):** {p_b:.4f}")
    st.write(f"**Posterior P(A|B):** {posterior:.4f}")
