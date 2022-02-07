import numpy as np
import pickle

def unpickle(file):
    with open(file, 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    return data


def load_cifar_10_data():
    data_dir = "."
    meta_data_dict = unpickle(data_dir + "/batches.meta")
    cifar_label_names = meta_data_dict[b'label_names']
    cifar_label_names = np.array(cifar_label_names)

    cifar_train_data = None
    cifar_train_filenames = []
    cifar_train_labels = []

    for i in range(1, 6):
        cifar_train_data_dict = unpickle(data_dir + "/data_batch_{}".format(i))
        if i == 1:
            cifar_train_data = cifar_train_data_dict[b'data']
        else:
            cifar_train_data = np.vstack((cifar_train_data, cifar_train_data_dict[b'data']))
        cifar_train_filenames += cifar_train_data_dict[b'filenames']
        cifar_train_labels += cifar_train_data_dict[b'labels']

    cifar_test_data_dict = unpickle(data_dir + "/test_batch")
    cifar_test_data = cifar_test_data_dict[b'data']
    cifar_test_filenames = cifar_test_data_dict[b'filenames']
    cifar_test_labels = cifar_test_data_dict[b'labels']

    return cifar_train_data, cifar_test_data


def process_cifar_10(channel):
    train_data, test_data = load_cifar_10_data()
    data = np.concatenate((train_data, test_data), axis=0)

    for i in range(data.shape[0]):
        [data_red, data_green, data_blue] = np.split(data[i],3)
        data_grayscale = 0.299*data_red + 0.587*data_green + 0.114*data_blue

        if channel == "red":
            pixel_values = data_red
        elif channel == "green":
            pixel_values = data_green
        elif channel == "red":
            pixel_values = data_blue
        elif channel == "gray":
            pixel_values = data_grayscale

        string_pixels = [str(pix) for pix in pixel_values]
        pixel_line = " ".join(string_pixels)
        
        

if __name__ == "__main__":
    process_cifar_10("red")