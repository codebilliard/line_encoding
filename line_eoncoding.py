import matplotlib.pyplot as plt

def nrz(data):
    encoded = []
    for bit in data:
        encoded.append(1 if bit == '1' else -1)
    return encoded

def nrz_l(data):
    encoded = []
    for bit in data:
        encoded.append(1 if bit == '1' else -1)
    return encoded

def nrz_i(data):
    encoded = []
    last_signal = 1
    for bit in data:
        if bit == '1':
            last_signal *= -1
        encoded.append(last_signal)
    return encoded

def polar_rz(data):
    encoded = []
    for bit in data:
        encoded.append(1 if bit == '1' else -1)
        encoded.append(0)
    return encoded

def manchester(data):
    encoded = []
    for bit in data:
        encoded.append(-1 if bit == '1' else 1)
        encoded.append(1 if bit == '1' else -1)
    return encoded

def diff_manchester(data):
    encoded = []
    last_signal = 1
    for bit in data:
        if bit == '1':
            last_signal *= -1
        encoded.append(last_signal)
        last_signal *= -1
        encoded.append(last_signal)
    return encoded

def ami(data):
    encoded = []
    last_signal = 1
    for bit in data:
        if bit == '1':
            last_signal *= -1
            encoded.append(last_signal)
        else:
            encoded.append(0)
    return encoded

def plot_line_coding(data, encoding, title):
    plt.figure(figsize=(15, 2))
    plt.step(range(len(encoding(data))), encoding(data), where='post')
    plt.title(title)
    plt.grid(True)
    plt.show()

data_stream = '0101101001'

plot_line_coding(data_stream, nrz, 'NRZ')
plot_line_coding(data_stream, nrz_l, 'NRZ-L')
plot_line_coding(data_stream, nrz_i, 'NRZ-I')
plot_line_coding(data_stream, polar_rz, 'Polar RZ')
plot_line_coding(data_stream, manchester, 'Manchester')
plot_line_coding(data_stream, diff_manchester, 'Differential Manchester')
plot_line_coding(data_stream, ami, 'AMI')

