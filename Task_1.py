import numpy as np

ftb = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hoc = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
sht = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

n1 = 8
n2 = 9
n3 = 11
n = n1 + n2 + n3
k = 3

ftb_m = np.mean(ftb)
hoc_m = np.mean(hoc)
sht_m = np.mean(sht)

sp_all = np.concatenate([ftb, hoc, sht])
sp_mean = np.mean(sp_all)

s2 = np.sum((sp_all - sp_mean) ** 2)
s2_f = ((ftb_m - sp_mean)**2) * n1 + ((hoc_m - sp_mean)**2) * n2 + ((sht_m - sp_mean)**2) * n3
s2_r = s2 - s2_f

sigma2_general = s2 / (n - 1)
sigma2_f = s2_f / (k - 1)
sigma2_r = s2_r / (n - k)

F_h = sigma2_general / sigma2_r
eta_2 = s2_f / s2

print(F_h)
print(eta_2)

