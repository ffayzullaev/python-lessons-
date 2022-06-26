<<<<<<< HEAD
print("Muzeyga ro'yxattan o'tish dasturi\n")
savol = "Chipta narxini bilish uchun yoshingizni kiriting: \n"
savol += "(Dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing):\n"

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat =='quit':
        break
    yosh = int(qiymat)
    
    if yosh <=7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
        
    if narh==0:
        print("Sizga chipta bepul")
    else:
=======
print("Muzeyga ro'yxattan o'tish dasturi\n")
savol = "Chipta narxini bilish uchun yoshingizni kiriting: \n"
savol += "(Dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing):\n"

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat =='quit':
        break
    yosh = int(qiymat)
    
    if yosh <=7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
        
    if narh==0:
        print("Sizga chipta bepul")
    else:
>>>>>>> 72877a94a5a721b6bd6b0f66840af6775f28326f
        print(f"Chipya {narh} so'm")