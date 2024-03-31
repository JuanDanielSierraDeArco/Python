import matplotlib.pyplot as plt

labels = ['a', 'b', 'c', 'd']
values = [20, 50, 20, 10]

def generate_bar_char(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title('Gráfico de Barras')
    plt.show()

def generate_tort_char(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%0.1f %%")
    ax.axis('equal')
    ax.set_title('Gráfico de torta')
    plt.show()

if __name__ == '__main__':
    generate_bar_char(labels, values)
    generate_tort_char(labels, values)
