import csv
LABEL_COUNT = 6
truncate_value = -1*(LABEL_COUNT)
training_set = 'emotions_train.csv'
test_set = 'emotions_test.csv'
new_training_set = 'new_train.csv'
new_testing_set = 'new_test.csv'
train = []
test = []
train_label = []
test_label = []
training_labels = []
testing_labels = []
new_train =[]
new_test = []
def filter_data():
    with open(training_set , 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            # print(line[-6:])
            train_label = [float(x) for x in line[truncate_value:]]
            data = line[:truncate_value]
            new_train.append(data)
            training_labels.append(train_label)

        print(training_labels)
        print(len(new_train))
    with open('new_train.csv','w') as w:
        wtr = csv.writer(w)
        for x in new_train:
            x = [float(k) for k in x]
            wtr.writerow(x)




    with open(test_set, 'r+') as f1:
        csv_reader2 = csv.reader(f1)
        for line in csv_reader2:
            # print(line[-6:])
            test_label = [float(x) for x in line[-6:]]
            test = line[:truncate_value]
            new_test.append(test)
            testing_labels.append(test_label)
        print(testing_labels)
        print(len(new_test))
    with open(new_testing_set,'w') as w1:
        wtr1 = csv.writer(w1)
        for y in new_test:
            y = [float(i) for i in y]
            wtr1.writerow(y)

    # return training_labels,testing_labels
filter_data()







