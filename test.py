import numpy as np
import matplotlib.pyplot as plt

# Define the g1, g2, and g3 functions
def g1(x):
    return (x**4 + 1) / 20

def g2(x):
    return (20 * x - 1)**(1/3)

def g3(x):
    return 20 * x**2 - 1

# Function to perform Fixed-Point Iteration and collect points
def fixed_point_iterations(g, x0, maxiter):
    x_vals = [x0]  # Initial guess
    for _ in range(maxiter):
        x_new = g(x_vals[-1])
        x_vals.append(x_new)
    return x_vals

# Initial guess
x0 = 0.5
maxiter = 10

# Perform the iterations for g1, g2, g3
x_points_g1 = fixed_point_iterations(g1, x0, maxiter)
x_points_g2 = fixed_point_iterations(g2, x0, maxiter)
x_points_g3 = fixed_point_iterations(g3, x0, maxiter)

# Set up the plot
x_vals = np.linspace(-2, 2, 400)
y_vals = x_vals

plt.plot(x_vals, y_vals, label="y = x", color='black', linestyle='--')

# Plot pointwise iterations for each function
plt.plot(x_points_g1, g1(np.array(x_points_g1)), 'ro-', label="g1(x) Pointwise")
plt.plot(x_points_g2, g2(np.array(x_points_g2)), 'go-', label="g2(x) Pointwise")
plt.plot(x_points_g3, g3(np.array(x_points_g3)), 'bo-', label="g3(x) Pointwise")

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Fixed-Point Iterations for g1, g2, and g3')
plt.legend()
plt.grid(True)
plt.show()