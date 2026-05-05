# age=12
 
# if (age>18):
#   print("you can drive a car.") 
#   print("Thank you")
  
# print("end of program")  



# age2=111
# if (age2>12):
#   print("youre eligible for the exam ")
#   print("Thank you guys")


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Step 1: Generate synthetic data with Gaussian noise
np.random.seed(42)
X = np.linspace(0, 10, 50)
true_theta = 2.5
noise = np.random.normal(0, 2, size=X.shape)  # Gaussian noise
y = true_theta * X + noise

# Step 2: Fit line using least squares
X_matrix = np.vstack([X, np.ones(len(X))]).T
theta_hat = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ y
y_pred = X_matrix @ theta_hat

# Step 3: Compute residuals
residuals = y - y_pred

# Step 4: Plot histogram of residuals + Gaussian curve
plt.figure(figsize=(10,5))

# Histogram of residuals
plt.hist(residuals, bins=15, density=True, alpha=0.6, color='skyblue', label="Residuals")

# Gaussian curve using mean and std of residuals
mu, std = np.mean(residuals), np.std(residuals)
xmin, xmax = plt.xlim()
x_vals = np.linspace(xmin, xmax, 100)
plt.plot(x_vals, norm.pdf(x_vals, mu, std), 'r-', lw=2, label="Gaussian curve")

plt.title("Residuals vs Gaussian Assumption")
plt.xlabel("Residual value")
plt.ylabel("Density")
plt.legend()
plt.show()