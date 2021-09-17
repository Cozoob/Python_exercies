# Created by Marcin "Cozoob" Kozub 01.08.2021
import json

def convert_CSV_to_JSON():

    with open("workers.csv", "r") as workers:
        header = workers.readline().strip().split(",")
        # print(header)

        for line in workers:
            line = line.strip().split(",")

            d = {header[i]: line[i] for i in range(4)}
            # print(d)
            with open("new_file_of_workers.json", "a") as file:
                json.dump(d, file, indent=2)




if __name__ == '__main__':
    convert_CSV_to_JSON()