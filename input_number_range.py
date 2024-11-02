while True:
    try:
        num = input("baks, lgay ka number 1 - 50 (pag mali nilagay mo, mag-eexit ako!): ")
        num = int(num)
        if num < 1 or num > 50:
            print("Woi, mali! Dapat 1 - 50 kasi, baks.")
            break
        else:
            print(f"yan galing! {num}")            
    except ValueError:
        print("baks, mali parang di nag grade 2 number nga eh!")
        break