

import math
import sys


MAX_CLUSTERS = 5
VEC_LEN = 7
INPUT_PATTERNS =7
INPUT_TESTS = 6
MIN_ALPHA = 0.0011
MAX_ITERATIONS = 2000
SIGMA = 1
INITIAL_LEARNING_RATE = 0.5
INITIAL_RADIUS = 0.5

w = [[0.2, 0.6, 0.5, 0.9, 0.4, 0.2, 0.8],
     [0.9, 0.3, 0.6, 0.4, 0.5, 0.6, 0.3],
     [0.8, 0.5, 0.7, 0.2, 0.6, 0.9, 0.5],
     [0.6, 0.4, 0.2, 0.3, 0.7, 0.2, 0.4],
     [0.8, 0.9, 0.7, 0.9, 0.3, 0.2, 0.5]]

pattern = [[1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 1],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 1, 0, 1]]


tests = [[1, 0, 1, 0, 1, 0, 1],
         [0, 1, 1, 0, 1, 1, 1],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 1, 1]]

class SOM_Class2:
    def __init__(self, vectorLength, maxClusters, numPatterns, numTests, minimumAlpha, weightArray, maxIterations,
                 sigma, initialAlpha, initialSigma):
        self.mVectorLen = vectorLength
        self.mMaxClusters = maxClusters
        self.mNumPatterns = numPatterns
        self.mNumTests = numTests
        self.mMinAlpha = minimumAlpha
        self.mAlpha = initialAlpha
        self.d = []
        self.w = weightArray
        self.maxIterations = maxIterations
        self.sigma = SIGMA
        self.mInitialAlpha = initialAlpha
        self.mInitialSigma = initialSigma
        return

    def compute_input(self, vectorArray, vectorNumber):
        self.d = [0.0] * self.mMaxClusters

        for i in range(self.mMaxClusters):
            for j in range(self.mVectorLen):
                self.d[i] = self.d[i] + math.pow((self.w[i][j] - vectorArray[vectorNumber][j]), 2)
        #         print(self.d)
        return

    #         print(vectorArray)
    #         print(vectorNumber)

    def get_minimum(self, nodeArray):  # NodeArray holding the distances of selected instance with each node
        minimum = 0
        foundNewMinimum = False
        done = False

        while not done:
            foundNewMinimum = False
            for i in range(self.mMaxClusters):
                if i != minimum:
                    if nodeArray[i] < nodeArray[minimum]:
                        minimum = i
                        foundNewMinimum = True

            if foundNewMinimum == False:
                done = True

        return minimum

    def update_weights(self, vectorNumber, dMin, patternArray):

        # Now search for neighbors
        dis = 0.00
        for i in range(self.mMaxClusters):
            for j in range(self.mVectorLen):
                if (i != dMin):
                    dis = dis + math.pow((self.w[dMin][j] - self.w[i][j]), 2)
                else:
                    continue

            # Consider as neighbor if distance is less than sigma

            if (dis < self.sigma):

                # Neighborhood function
                h = math.exp(-1 * (pow(dis, 2)) / (2 * (self.sigma ** 2)))
                # Adjust weight of winning neuron
                for l in range(self.mVectorLen):
                    self.w[dMin][l] = self.w[dMin][l] + (
                                self.mAlpha * h * (patternArray[vectorNumber][l] - self.w[dMin][l]))
                    # once accepted as neighbor update its weight
                for x in range(self.mVectorLen):
                    self.w[i][x] = self.w[i][x] + (self.mAlpha * h * (patternArray[vectorNumber][j] - self.w[i][x]))

        return

    def training(self, patternArray):
        iterations = 0  # t
        #         reductionFlag = False
        #         reductionPoint = 0
        while (iterations != self.maxIterations):
            iterations = iterations + 1
            for i in range(self.mNumPatterns):
                self.compute_input(patternArray, i)
                dMin = self.get_minimum(self.d)
                self.update_weights(i, dMin, patternArray)

            # reduction of learning rate
            self.mAlpha = self.mInitialAlpha * (1 - (iterations / self.maxIterations))
            # Reduction of radius
            self.sigma = self.mInitialSigma * (1 - (iterations / self.maxIterations))

        print("Iterations" + str(iterations) + '\n')


        return

    def classify(self, tests, map_dict):
        threshold = 0.5
        sum_dict = dict()
        prototypeVector = list()
        numInstances = dict()  # Dictionary to hold number of instances mapped to the neuron
        for key in map_dict:
            c = 0
            for x in map_dict[key]:
                c = c + 1
            numInstances[key] = c
        print(numInstances)

        # Calculating averages of labels mapped to each neuron
        for key in map_dict:
            sum_list = [sum(x) / numInstances[key] for x in zip(*map_dict[key])]
            if key not in sum_dict:
                sum_dict[key] = []
                sum_dict[key].append(sum_list)
            else:
                sum_dict[key].append(sum_list)

        print(sum_dict)
        v = list()  # v vector
        for i in range(self.mMaxClusters):
            v.append([0.0] * self.mVectorLen)
        print(v)
        # for deterministic prediction , set threshold = 0.5: if > 0.5 then 1 else 0
        for key in sum_dict:
            numNeuron = key
            for x in sum_dict[key]:
                v[numNeuron] = x
        print(v)

        for i in range(len(v)):
            for j in range(self.mVectorLen):
                if (v[i][j] >= 0.5):
                    v[i][j] = 1
                else:
                    v[i][j] = 0
        print(v)

        # In v vector the vector at position say(x) represents the threshold calculated average of labels of instances for that neuron number

        # pick up test instances
        print("Classification results :")
        for i in tests:  # i is test instance
            matchFlag = 0
            for x in v:
                if i == x:
                    matchFlag = 1
                    ind = v.index(x)  # ind is the neuron number to which the test should n=be mapped
                    print(i, end=' ')
                    print(": falls under category" + str(ind))

            if (matchFlag == 0):
                print("Test Instance", end=' ')
                print(i, end=" ")
                print("has no match")

    def print_results(self, patternArray, testArray):
        # Printing the clusters created

        map_dict = dict()  # dictn to hold mapped vwctors along with respective neurons
        print("Clusters for training input: \n")
        for i in range(self.mNumPatterns):
            map_list = list()  # list to hold mapped instances to a particular neuron
            self.compute_input(patternArray, i)
            dMin = self.get_minimum(self.d)

            print("Vector (")
            for j in range(self.mVectorLen):
                map_list.append(patternArray[i][j])
                print(str(patternArray[i][j]) + ", ")

            print(") fits into category " + str(dMin) + "\n")
            if dMin not in map_dict:
                map_dict[dMin] = []
                map_dict[dMin].append(map_list)
            else:
                map_dict[dMin].append(map_list)

        # Print weight matrix.

        print("------------------------------------------------------------------------\n")
        for i in range(self.mMaxClusters):
            print("Weights for Node " + str(i) + " connections:\n")
            print("     ")
            for j in range(self.mVectorLen):
                print("{:03.3f}".format(self.w[i][j]) + ", ")

            print("\n")

        # Print post-training tests.
        print("------------------------------------------------------------------------\n")
        print("Categorized test input:\n")
        for i in range(self.mNumTests):
            self.compute_input(testArray, i)

            dMin = self.get_minimum(self.d)

            print("Vector (")
            for j in range(self.mVectorLen):
                print(str(testArray[i][j]) + ", ")

            print(") fits into category " + str(dMin) + "\n")

        print("Dictionary - Maping of instances to respective neurons :")
        print(map_dict)

        return map_dict


som = SOM_Class2(VEC_LEN, MAX_CLUSTERS, INPUT_PATTERNS, INPUT_TESTS, MIN_ALPHA, w, MAX_ITERATIONS, SIGMA,
                 INITIAL_LEARNING_RATE, INITIAL_RADIUS)

som.training(pattern)
map_dict = som.print_results(pattern, tests)
som.classify(tests, map_dict)






















































































