import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class dataAnalysis(object):
    def __init__(self):
        self.data = pd.read_csv('./BlackFriday.csv')

    def histogram(self, group, column, plot):  # number statistics of one attribute related to another attribute
        plt.figure(figsize=(12, 6))
        self.data.groupby(group)[column].sum().sort_values().plot(plot)
        # self.data.groupby(group)[column].count().nlargest(10).sort_values().plot(plot)
        plt.show()

    def pie_chart(self, group):  # number statistics of one attribute
        explode = None
        fig1, ax1 = plt.subplots(figsize=(12, 7))
        ax1.pie(self.data[group].value_counts(), explode=explode, labels=self.data[group].unique(), autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')
        plt.tight_layout()
        plt.legend()
        plt.show()

    def countplot(self, group1, group2):  # subdivide the histogram according to another attribute
        fig1, ax1 = plt.subplots(figsize=(12, 7))
        sns.countplot(self.data[group1], hue=self.data[group2])
        plt.show()


if __name__ == '__main__':
    dataA = dataAnalysis()
    # dataA.histogram('Age', 'Purchase', 'bar')
    # dataA.pie_chart('Age')
    # dataA.countplot('City_Category', 'Gender')
    dataA.histogram('Stay_In_Current_City_Years','Purchase','bar')
