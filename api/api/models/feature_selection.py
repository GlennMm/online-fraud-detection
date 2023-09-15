from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

seed = 1


class FeatureSelection:
    def __init__(self):
        self.classifier = RandomForestClassifier(n_estimators=250, random_state=seed, n_jobs=-1)
        self.feature_selector = None

    def get_data_with_important_features(self, x_train, y_train, x_test):
        self.classifier.fit(x_train, y_train)
        self.feature_selector = SelectFromModel(self.classifier).fit(x_train, y_train)
        x_train = self.feature_selector.transform(x_train)
        x_test = self.feature_selector.transform(x_test)
        return x_train, x_test
