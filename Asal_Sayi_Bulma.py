def asalsayi(num):
    num = int(num)
    if num <= 3:
        return True
    sayi = 0
    liste=[]
    for i in range(1, num):
        while i<num+1:
            if num%i == 0:
                sayi +=1
                liste.append(i)
            i +=1
        print(f"Bölünebildiği asa ve asal olmayan sayılar: {liste}")
        if sayi == 2:
            return True
        else:
            return False

print(asalsayi(input()))