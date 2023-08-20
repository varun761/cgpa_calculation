import matplotlib.pyplot as plt
import numpy as np

def read_file(path = '', lines = False):
    file = open(path, 'r')
    if lines:
        file_reader = file.readlines()
    else:
        file_reader =  file.read()
    file.close()
    return file_reader

def create_file_content(destination, data):
    file = open(destination, '+w')
    file.write(data)
    read_data = file.read()
    file.close()
    return read_data

def append_file_content(destination, data):
    file = open(destination, '+a')
    file.write(data)
    read_data = file.read()
    file.close()
    return read_data

def double_read(destination):
    file = open(destination, 'r')
    file.read()
    read_data = file.read()
    file.close()
    return read_data

def draw_plot():
    X = range(-15, 16)
    Y = [x**2 for x in X]
    plt.plot(X, Y, 'b', linewidth = 1)
    plt.title('y=x**2', fontsize = 18)
    plt.xlabel('X-Axis', fontsize = 14)
    plt.ylabel('Y-Axis', fontsize = 14)
    plt.xticks(range(-15, 16, 2), fontsize=14, rotation=90)
    plt.yticks([0, 100, 200], fontsize=14, rotation=0)
    plt.show()

def multiple_curves_plot():
    np.random.seed(19680801)
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    plt.scatter(x, y)
    plt.show()

if __name__ == '__main__':

    multiple_curves_plot()
    # d = append_file_content('./sample-data/append_source.txt', 'Hello')
    # print(d)
    
    # data = double_read('./sample-data/append_source.txt')
    # print(data)
    
    # read_file('./sample-data/sample-data.txt')

    # data = read_file('./sample-data/source.txt')
    # d = create_file_content('./sample-data/destination.txt', ('').join(data))

    # data = read_file('./sample-data/source.txt', True)
    # print(data)
    # for i in range(0, len(data)):
    #     count = i + 1
    #     data[i] = ("{0} {1}").format(count, data[i])
    # create_file_content('./sample-data/number_source.txt', ("").join(data))

    # data = read_file('./sample-data/source.txt', True)
    # for i in range(0, len(data)):
    #     data[i] = data[i].replace('\n', '')
    # data.reverse()
    # create_file_content('./sample-data/number_reverse_source.txt', ("\n").join(data))

    # data = read_file('./sample-data/source.txt', True)
    # count_dict = {}
    # for i in range(0, len(data)):
    #     words = data[i].replace('\n', '').replace('.', '').split(' ')
    #     for j in range(0, len(words)):
    #         if words[j] != '':
    #             dict_keys = count_dict.keys()
    #             found_key =  [field for field in dict_keys if field == words[j]]
    #             if len(found_key) == 0:
    #                 count_dict[words[j]] = 1
    #             else:
    #                 count_dict[words[j]] = count_dict[words[j]] + 1
    # print(count_dict)