# Kütüphanelerin Yüklenmesi
from scipy.stats import poisson

# Problem: % 10 hatalı ilan veren bir ajansın 3 hatalı ilan verme olaslığı nedir?
lambda_ = 0.10
rv = poisson( mu= lambda_)
print (rv.pmf(k=3))
# 0.00015080623633932676


