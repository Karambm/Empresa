from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def calcconfusion(predicted, reality):
    cm = confusion_matrix(reality, predicted)

    sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', xticklabels=['Klasse 0', 'Klasse 1', 'Klasse 2'], yticklabels=['Klasse 0', 'Klasse 1', 'Klasse 2'])
    plt.xlabel('Voorspelde waarden'), plt.ylabel('Ware waarden')
    plt.show()


if __name__ == "__main__":
    calcconfusion([1, 0, 1, 2, 0, 1, 2, 2, 0], [1, 0, 2, 2, 0, 1, 2, 1, 0])
