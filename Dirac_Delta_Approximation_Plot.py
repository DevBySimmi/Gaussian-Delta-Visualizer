import numpy as np
import matplotlib.pyplot as plt

# Dark Theme
plt.style.use("dark_background")

# x values
N = 5000
x = np.linspace(-5, 5, N)

# Different sigma values
sigmas = [1.0, 0.5, 0.1, 0.05]

# Gaussian approximation
def gaussian(x, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x**2) / 
                                            (2 * sigma**2))

# Create figure
plt.figure(figsize=(12, 7))

# Plot curves
for sigma in sigmas:
    y = gaussian(x, sigma)

    # Glow effect
    for lw, alpha in zip([10, 8, 6], [0.05, 0.08, 0.12]):
        plt.plot(x, y, color='cyan', lw=lw, alpha=alpha)

    # Main line
    plt.plot(x, y, lw=2,
             label=f'σ = {sigma}')

    # Fill area
    plt.fill_between(x, y, alpha=0.08)

# Axis lines
plt.axhline(0, color='white', lw=0.5, ls='--')
plt.axvline(0, color='white', lw=0.5, ls='--')

# Labels and title
plt.title("Dirac Delta Approximation using Gaussian Functions",
          fontsize=18, pad=15)

plt.xlabel("x", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)

# Equation text
equation = r'$\delta(x)\approx \frac{1}{\sigma\sqrt{2\pi}}e^{-x^2/(2\sigma^2)}$'

plt.text(-4.8, max(gaussian(x, 0.05))*0.75,
         equation,
         fontsize=16,
         color='yellow')

# Limits
plt.xlim(-5, 5)
plt.ylim(0, 10)

# Grid
plt.grid(alpha=0.2)

# Legend
plt.legend(fontsize=12)

# Tight layout
plt.tight_layout()

# Show plot
plt.show()