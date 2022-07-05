def summa(x,y,*sonlar):
    """Kiritilgan sinlarni hisoblaydigan funksiya"""
    return x+y+sum(sonlar)
print(summa(10,15,17,18,54,595,45))
print(summa(0,1))
print(summa(23,56,89))
    