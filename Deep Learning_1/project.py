import pandas as pd
# 쉽게 파일 읽는 라이브러리 pandas
data = pd.read_csv('gpascore.csv') # padas로 가져온 데이터들을 dataframe이라고 부름
# 데이터 전처리하기
data = data.dropna() # dropna() : null값들이 있는 행들을 제거해줌 // fillna() : null값이 있는 부분에 원하는 값들을 채울수 있음 // data[''] : 원하는 행의 값들만 출력가능
y_data = data['admit'].values
x_data = []

for i, rows in data.iterrows() : # iterrows는 pandas로 가져온 데이터들을 한 행씩 볼수 있음
    x_data.append([rows['gre'] ,rows['gpa'] ,rows['rank'] ])

import tensorflow as tf
import numpy as np
# 1.딥러닝 model 디자인하기
model = tf.keras.models.Sequential([
    # 레이어를 디자인할때 활성함수(activation function)가 필요
    tf.keras.layers.Dense(64,activation='tanh'), # Dense() : 노드의 갯수를 지정 // activation은 일종의 파라미터
    tf.keras.layers.Dense(128,activation='tanh'),
    tf.keras.layers.Dense(1,activation='sigmoid'),# 마지막 레이어는  예측결과에 해당하니 보통 1개의 노드를 생성함(때에 따라 갯수를 조정필요) // sigmoid : 0~1사이의 확률을 나오게 만들고 싶을때 보통 사용
])
# 2.model compile하기 학습시키기
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy']) #optimizer : 처음 지정한 weight1값을 조정해 새로운 weight2 값을 만들어줌 //   loss : 손실함수(binary_crossentropy는 결과가 0과1사이의 분류,확률문제에서 사용)
model.fit(np.array(x_data), np.array(y_data),epochs=1000 ) # x값에는 학습데이터(결과값들에 필요한 인풋),y는 실제정답들(결과값들)을 넣음

# 3.학습시킨 모델로 예측해보기
x_data = np.array([[750,3.70,3], [400,2.2,1]])
예측값 = model.predict(x_data)
print(예측값)
# 딥러닝 베이스 1.모델 디자인 2.데이터 집어넣어서 학습시키기 3.새로운데이터 예측 (+데이터전처리,파라미터 튜닝)
# 딥러닝학습은 일종의  연구과정으로 실험이 매우 중요