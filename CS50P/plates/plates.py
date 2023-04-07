def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    if 2 <= len(s) <= 6:
        for char in s:
            if char.isalpha() or char.isdigit():
                if char.isdigit() and s.index(char) > 1:
                    if i == 0 and int(char) == 0:
                        return False
                    i = s.index(char)
                    while i < len(s):
                        if s[i].isdigit():
                            i += 1
                            continue
                        return False
                    return True
                elif char.isdigit():
                    return False
                continue
            return False
        return True
    return False

if __name__ == "__main__":
    main()