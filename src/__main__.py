from .monkey import Monkey

def main():
    with open("casos/caso0200.txt") as f:
        lines = f.readlines()
        #if Macaco
        for line in lines:
            if "\n" in line:
                line = line.split(" ")
                print(f"{line[0]} {line[1]}")




if __name__ == "__main__":
    main()