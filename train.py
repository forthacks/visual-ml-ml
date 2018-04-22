from keras.layers import Dense, Conv2D, MaxPool2D
from keras.models import Sequential
from keras.activations import relu, tanh, sigmoid
layers = [
    {
        "name": "input",
        "size": 10,
    },
    {
        "name": "nn",
        "size": 100,
        "activation": "relu"
    },
    {
        "name": "nn",
        "size": 10,
        "activation": "softmax"
    }
]
info = {
    "optimizer": "adam"
}

model = Sequential()

layer_num = 0
for layer in layers:
    name = layer["name"]
    if name == "input":
        input_dim = layer["size"]
    if name == "nn":
        if layer_num == 1:
            model.add(Dense(layer["size"], activation=layer["activation"], input_dim=input_dim))
        model.add(Dense(layer["size"], activation=layer["activation"]))
    layer_num += 1
