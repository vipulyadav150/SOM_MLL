import csv

def fetch_data():
    filename = 'new_train.csv'

    fields = []

    patterns = []

    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            patterns.append([float(k) for k in line])

    patterns = [e for e in patterns if e]


    print("Training patterns available :" + str(len(patterns)))
    # print(patterns)
    # for x in patterns:
    #     print(x)
    return patterns
