import csv


def getHeaders():
    header_1 = input("Enter first header: ")
    header_2 = input("Enter seccond header: ")

    return header_1, header_2


def getData(header_1, header_2):
    data = []
    temp_dict = {header_1: header_1, header_2: header_2}
    data.append(temp_dict)

    for i in range(3):
        column_1 = input(f"Enter data for {header_1}: ")

        column_2 = input(f"Enter data for {header_2}: ")

        temp_dict = {header_1: column_1, header_2: column_2}
        data.append(temp_dict)

    return data


def writeCSV(rows, header_1, header_2):
    with open("myCSV.csv", 'w') as outfile:
        fieldnames = [header_1, header_2]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writerows(rows)


def main():
    header_1, header_2 = getHeaders()
    rows = getData(header_1, header_2)
    writeCSV(rows, header_1, header_2)


if __name__ == "__main__":
    main()