def make_csvtable(data_num, row):
    line = data_num // row
    arow = row
    csv = ""
    for i in range(line+1):
        if i == line:
            arow = data_num % arow
        csv += ",".join([str(x+1) for x in range(arow)]) + "\n"
        csv += "[__]," * arow + "\n"
    return csv


if __name__ == "__main__":
    plan = list()
    while True:
        todo = input("やること: ")
        if todo:
            plan.append(todo)
        else:
            break
    plan = [i.replace(",", " ") for i in plan]
    dates_num = int(input("日数: "))
    csv = "table\n" + "\n".join([x for x in plan]) + "\n"
    csv += make_csvtable(dates_num, 7)
    with open("plan.csv", mode="w") as f:
        f.write(csv)