def main():
    rangenum = {
        "1-10": 0,
        "11-20": 0,
        "21-30": 0,
        "31-40": 0,
        "41-50": 0
    }
    while True:
        try:
            num = input("Baks, lagay ka number 1 - 50 (pag mali nilagay mo, idisplay ko na lang pinaglalagay mue!): ")
            num = int(num)
            if num < 1 or num > 50:
                print("woi, mali! Dapat 1 - 50 kasi, baks")
                break 
            else:
                if 1 <= num <= 10:
                    rangenum["1-10"] += 1
                elif 11 <= num <= 20:
                    rangenum["11-20"] += 1
                elif 21 <= num <= 30:
                    rangenum["21-30"] += 1
                elif 31 <= num <= 40:
                    rangenum["31-40"] += 1
                elif 41 <= num <= 50:
                    rangenum["41-50"] += 1
        except ValueError:
            print("Baks, mali! Parang di nag-grade 2, number nga eh!")
            break
    print("\nayan pinaglalagay mo baks:")
    for rangelabel, rangecount in rangenum.items():
        print(f"{rangelabel} = {rangecount}")
if __name__ == "__main__":
    main()
    print("ano masaya ka na ba?")
