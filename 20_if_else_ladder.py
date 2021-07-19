

def winter_temp(temp):
    if temp<2 and temp> 5:
        print(" Wear a double breasted trench coat with gloves on")
    else:
        if temp>5 and temp<15:
            print("wear a single breasted trench coat without gloves on")
        else:
            if temp>15 and temp<25:
                print("Wear a simple sweater")
            else:
                if temp>25 and temp<30:
                    print("You can wear t shirt and a full jeans pant")
                else:
                    if temp>30 and temp<35:
                        print(" Wear only shorts")
                    else :
                        print(" Walk around")


winter_temp(4)

winter_temp(10)

winter_temp(26)

winter_temp(32)
