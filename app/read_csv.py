import csv


def read_csv(path):
    with open(path, 'r') as Data_pop:
        reader = csv.reader(Data_pop, delimiter= ',')
        header = next(reader)
        data = []


        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == '__main__':
    data = read_csv('./app/Data_pop.csv')
    print(data)