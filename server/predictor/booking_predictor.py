import pickle


def load_pickle():
    file = open('./server/models/scaler-hotel-Bk-can.pickle', 'rb')
    mx_scaler = pickle.load(file)
    file.close()

    file = open('./server/models/dct-hotel-Bk-can.pickle', 'rb')
    model = pickle.load(file)
    file.close()

    return (mx_scaler, model)


def predict_booking(data_list):
    mx_scaler, model = load_pickle()
    scaled_data = mx_scaler.transform(data_list)
    print(scaled_data)
    return model.predict(scaled_data)