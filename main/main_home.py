import qfish
import time

cls = "\n" * 1000

while_i = True
while while_i == True:
    print(cls)
    tHH = time.strftime("%H", time.localtime())
    tMM = time.strftime("%M", time.localtime())
    tSS = time.strftime("%S", time.localtime())
    tYY = time.strftime("%Y", time.localtime())
    tmm = time.strftime("%m", time.localtime())
    tdd = time.strftime("%m", time.localtime())

    clock_ent_file = open("clock_ent.txt")
    clock_ent = clock_m_file.read()

    if clock_ent == "on":
        clock_h_file = open("clock_h.txt")
        clock_m_file = open("clock_m.txt")
        clock_h = clock_h_file.read(2)
        clock_m = clock_m_file.read(2)
        clock_h_file.close()
        clock_m_file.close()

    clock_ent_file.close()
    if clock_ent == "on":
        bell_ent = "[ Bell ]"
    else:
        bell_ent = "[      ]"

    print("|----------------------------|")
    print(" ",tHH,":",tMM,":",tSS)
    print("",tYY,"/",tmm,"/",tdd)
    print(bell_ent)
    print("|----------------------------|")
    if clock_ent == "on":
        if clock_m == tMM:
            if  clock_h == tHH:
                print("\a")

    time.sleep(1)