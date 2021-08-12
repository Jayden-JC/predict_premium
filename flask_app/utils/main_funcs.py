import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from category_encoders import OrdinalEncoder

def predict_premium(age, sex, bmi, smoker):
    df = pd.read_csv(os.path.dirname(os.path.realpath(__file__))+'/insurance.csv')
    df = df.drop(columns=['children', 'region'])

    # 타겟 특성
    target = 'charges'

    X_train = df.drop(columns=[target])
    y_train = df[target]

    X_test = pd.DataFrame(data=[[age, sex, bmi, smoker]], columns=['age', 'sex', 'bmi', 'smoker'])

    # 인코더 인스턴스 생성
    oe = OrdinalEncoder()
    X_train_encoded = oe.fit_transform(X_train, y_train)

    X_test_encoded = oe.transform(X_test)

    # RandomForestRegressor
    rfr = RandomForestRegressor(max_depth=10, min_samples_leaf=10, oob_score=True, n_jobs=-1)
    rfr.fit(X_train_encoded, y_train)

    y_pred = rfr.predict(X_test_encoded)

    return y_pred[0]