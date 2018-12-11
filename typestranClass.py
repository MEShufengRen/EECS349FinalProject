import pandas as pd


def map_gender(gender):
    if gender == 'M':
        return 1
    else:
        return 0


def map_age(age):
    if age == '0-17':
        return 0
    elif age == '18-25':
        return 1
    elif age == '26-35':
        return 2
    elif age == '36-45':
        return 3
    elif age == '46-50':
        return 4
    elif age == '51-55':
        return 5
    else:
        return 6


def map_city_categories(city_category):
    if city_category == 'A':
        return 2
    elif city_category == 'B':
        return 1
    else:
        return 0


def map_stay(stay):
    if stay == '4+':
        return 4
    else:
        return int(stay)


class typetranClass(object):
    def __init__(self, path):
        self.data = pd.read_csv(path)

    def process(self):
        print(self.data.info())
        self.data['gender'] = self.data['gender'].apply(map_gender)
        self.data['age'] = self.data['age'].apply(map_age)
        self.data['city_category'] = self.data['city_category'].apply(map_city_categories)
        self.data['stay_in_current_city_years'] = self.data['stay_in_current_city_years'].apply(map_stay)
        return self.data


def main():
    transfer = typetranClass('./train.csv')
    data = transfer.process()
    data.to_csv("train_process.csv", index=False, sep=',')
    print(data.info())


if __name__ == '__main__':
    main()
