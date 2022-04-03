# Kütüphanelerin Yüklenmesi
from scipy.stats import norm

# Normal dağılım olduğu bilinen standart sapması 5 ve ortalaması 80 olan bir olayın 90' dan büyük olma olasılığı nedir?
1-norm.cdf(90, 80, 5)
# 0.02275013194817921