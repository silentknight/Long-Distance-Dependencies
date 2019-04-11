import numpy as np

def _gen_data_add(seq_length, rng=None):
    if rng is None:
        rng = np.random.RandomState()
    x_values = rng.uniform(low=0, high=1, size=seq_length)
    x_values = x_values.astype(dtype=float)
    x_indicator = np.zeros(seq_length, dtype=np.bool)
    x_indicator[rng.randint(seq_length/2)] = 1
    x_indicator[rng.randint(seq_length/2, seq_length)] = 1
    #x = np.array(list(zip(x_values, x_indicator)))[np.newaxis]
    x = np.vstack((x_values, x_indicator)).T
    #y = np.sum(x_values[x_indicator], keepdims=True)/2.
    y = np.sum(x_values[x_indicator], keepdims=True)/2.
    return x, y
                        
                        
def gen_data_add(seq_length, batch_size, epoch_len, rng=None):
    x = np.zeros((batch_size, seq_length, 2), dtype=float)
    y = np.zeros(batch_size, dtype=float)
    
    def gen():
        for i in range(epoch_len):
            for b in range(batch_size):
                data = _gen_data_add(seq_length, rng=rng)
                x[b] = data[0]
                y[b] = data[1]
            yield x, y

    return gen

def one_hot(labels, num_classes=None):
    """
    Convert a unidimensional label array into a matrix of one-hot vectors
    -- takes only positive integer values (and zero).
    """
    
    if np.min(labels)<0:
        raise ValueError
    if num_classes==None:
        num_classes=np.max(labels)+1
    onehot_labels = np.zeros((len(labels), num_classes), dtype=np.int32)
    for i, l in enumerate(labels):
        onehot_labels[i, l] = 1
    return onehot_labels


def _gen_data_copy(seq_length, rng=None):
    if rng is None:
        rng = np.random.RandomState()
    x = np.zeros(seq_length+20, dtype=theano.config.floatX)
    int_sequence = rng.randint(low=1, high=9, size=10)
    #x[:10] = (int_sequence - 4.5)/9.
    x[:10] = int_sequence
    #x -= x[:10].mean()
    #x /= x[:10].std()
    x[seq_length+9] = -1
    y_int = np.zeros(seq_length+20, dtype=np.int32)
    y_int[-10:] = int_sequence
    y = one_hot(y_int, num_classes=9)
    return x, y
        
        
def gen_data_copy(seq_length, batch_size, epoch_len, rng=None):
    x = np.zeros((batch_size, seq_length+20, 1), dtype=theano.config.floatX)
    y = np.zeros((batch_size, seq_length+20, 9), dtype=np.int32)
            
    def gen():
        for i in range(epoch_len):
            for b in range(batch_size):
                data = _gen_data_copy(seq_length, rng=rng)
                x[b,:,0] = data[0]
                y[b,:,:] = data[1]
            yield x, y

    return gen

if __name__ == '__main__':
    add_data = gen_data_add(200, 100, 100)

    for data in add_data():
        print data[0].shape, data[1].shape