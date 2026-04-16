from tensorflow.keras.utils import to_categorical

def normalize(data, max_value=255):
    return data.astype('float32')/max_value

def one_hot_encode(data, num_classes=10):
    return to_categorical(data, num_classes=num_classes)