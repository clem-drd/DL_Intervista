from numpy import loadtxt

def reader(dataset_name):

    if(dataset_name == ""):
        dataset_name = "pima-indians-diabetes.csv"

    dataset = loadtxt(dataset_name, delimiter=',')

    lenght = len(dataset)
    tutu = []

    for i in range (lenght):
        tutu.append(dataset[i])

    return tutu

if __name__ == "__main__":

    print(reader(dataset_name=""))