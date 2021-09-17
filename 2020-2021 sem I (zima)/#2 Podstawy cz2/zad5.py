# Created by Marcin "Cozoob" Kozub 01.08.2021

def check_products():

    with open("drinks.txt", "r") as file:
        header = file.readline().strip()
        header = header.split(",")
        for i in range(len(header)):
            header[i] = header[i].strip()

        # print((header, 1))

        file.readline()
        for line in file:
            line = line.strip().split(",")
            for i in range(len(line)):
                line[i] = line[i].strip()

            # print(header, line)
            answer = []
            for i in range(len(header)):
                found = False
                for j in range(len(line)):
                    if header[i] == line[j]:
                        found = True
                        break
                if not found:
                    answer.append(header[i])
            if len(answer) == 0:
                print("ok")
            else:
                print(answer)







if __name__ == '__main__':
    check_products()