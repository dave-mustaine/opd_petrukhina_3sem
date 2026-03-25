import numpy as np
import matplotlib.pyplot as plt

f = 6.5e9
c = 299792458

lam = c / f
k = 2 * np.pi / lam
l = (0.01 / 2) * lam
theta_an = np.linspace(1e-6, np.pi - 1e-6, 1000)
num = np.cos(k * l * np.cos(theta_an)) - np.cos(k * l)
den = np.sin(theta_an)

F = np.abs(num / den)
F_norm = F / np.max(F)

d_theta = theta_an[1] - theta_an[0]
integral = 2 * np.pi * np.sum((F_norm**2) * np.sin(theta_an) * d_theta)

D_max_lin_an = 4 * np.pi / integral
D_max_db_an = 10 * np.log10(D_max_lin_an)
D_an_lin = (F_norm**2) * D_max_lin_an
D_an_db = 10 * np.log10(np.clip(D_an_lin, 1e-12, None))

print(f"Максимальное значение КНД (разы): {D_max_lin_an:.4f}")
print(f"Максимальное значение КНД (дБи):   {D_max_db_an:.4f}")

data_cst = np.loadtxt('cst_data.txt', skiprows=2, usecols=(0, 2))
cst_theta_deg = data_cst[:, 0]
cst_D_db = data_cst[:, 1]
cst_theta_rad = np.deg2rad(cst_theta_deg)
cst_D_lin = 10**(cst_D_db / 10)

plt.figure(figsize=(8, 5))
plt.plot(np.rad2deg(theta_an), D_an_lin, 'b-', label='Аналитика')
plt.plot(cst_theta_deg, cst_D_lin, 'r--', label='CST')
plt.title('D (разы) - Декартова система')
plt.grid(True)
plt.legend()

plt.figure(figsize=(8, 5))
plt.plot(np.rad2deg(theta_an), D_an_db, 'b-', label='Аналитика')
plt.plot(cst_theta_deg, cst_D_db, 'r--', label='CST')
plt.title('D (dBi) - Декартова система')
plt.grid(True)
plt.legend()
plt.figure(figsize=(6, 6))

ax3 = plt.subplot(111, projection='polar')
ax3.plot(theta_an, D_an_lin, 'b-', label='Аналитика')
ax3.plot(cst_theta_rad, cst_D_lin, 'r--', label='CST')
ax3.set_theta_zero_location('N')
ax3.set_title('D (разы) - Полярная система', pad=15)
ax3.legend(loc='lower right')

plt.figure(figsize=(6, 6))
ax4 = plt.subplot(111, projection='polar')
ax4.plot(theta_an, np.maximum(D_an_db, -20), 'b-', label='Аналитика')
ax4.plot(cst_theta_rad, np.maximum(cst_D_db, -20), 'r--', label='CST')
ax4.set_theta_zero_location('N')
ax4.set_ylim(-20, np.max(D_an_db) + 1)
ax4.set_title('D (dBi) - Полярная система', pad=15)
ax4.legend(loc='lower right')

plt.show()
