# Problem:Bir mecrada verilen reklama tıklanma olasılığı 0,01 iken reklamı 100 kişi gördüğünde
# 1, 5, 10 tıklanma oladılığı nedir?

# Kütüphanelerin Yüklenesi
from scipy.stats import binom

p = 0.01 # Tıklanme OlasılığI
n = 100 # 100 kişinin reklam verilen siteyi ziyaret ettiğini kabul edelim.
rv = binom(n, p)
print(rv.pmf(1)) # 100 kişiden 1 kişinin reklama tıklama olasılığı nedir?
print(rv.pmf(5)) # 100 kişiden 5 kişinin reklama tıklama olasılığı nedir?
print(rv.pmf(10)) # 100 kişiden 10 kişinin reklama tıklama olasılığı nedir?

# 0.36972963764972666
# 0.002897787123761478
# 7.006035693977194e-08