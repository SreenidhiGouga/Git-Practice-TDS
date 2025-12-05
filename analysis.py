# Interactive Marimo Notebook Example
# Email: 21f3001224@ds.study.iitm.ac.in

import marimo as mo

# -------------------------
# Cell 1: Input widget
# -------------------------
# This cell creates an interactive slider.
# Other cells depend on `slider.value`.

slider = mo.ui.slider(1, 10, label="Select a number")

slider

# -------------------------
# Cell 2: Derived variable
# -------------------------
# This cell depends on the slider's value.
# When the slider changes, this cell recomputes automatically.

value_squared = slider.value ** 2

value_squared

# -------------------------
# Cell 3: Dynamic Markdown
# -------------------------
# This cell uses both the slider and the derived value.
# It documents the relationship reactively.

mo.md(f"""
### 📊 Interactive Output

- **Slider Value:** {slider.value}  
- **Squared Value:** {value_squared}  

{"🟢" * slider.value}
""")

