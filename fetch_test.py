import csv

def fetch_tests():
    filename = 'new_test.csv'

    fields = []

    tests = []

    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            tests.append([float(k) for k in line])

    tests = [e for e in tests if e]


    # print("Tests patterns available :" + str(len(tests)))


    return tests
