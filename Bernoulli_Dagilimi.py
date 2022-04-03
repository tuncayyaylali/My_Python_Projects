# Kütüphanelerin Yüklenmesi
from scipy.stats import bernoulli

# Problem atılan paranın % 60 olasılıkla yazı gelme olasılığını hesaplayan Bernoulli formülüdür.
p = 0.6
rv = bernoulli(p)
rv.pmf(k=1)
# 0.6