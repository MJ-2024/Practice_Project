import numpy as np
import tensorflow as tf
# tensorflow 사용
import matplotlib.pyplot as plt
# 이미지를 파이썬으로 띄워보는법
# 딥러닝 모델 디자인 1.모델만들기 // 2.compile하기 // fit하기
(trainX, trainY), (testX, testY) = tf.keras.datasets.fashion_mnist.load_data()
# 구글이 호스팅해주는 데이터 셋들중 하나 (쇼핑몰 이미지 데이터셋)
# trainX = 데이터셋에 있는 이미지 6만개 리스트// trainY = 정답 1만개가 들어있는 리스트(일명 label) 
trainX = trainX/ 255.0
testX = testX/ 255.0

trainX.reshape((trainX.shape[0],28,28,1))
testX.reshape((testX.shape[0],28,28,1))
# numpy array 자료의 shape변경하기(전처리하기) : 이미지 데이터 전처리 : 0~1로 압축해주세요
class_name = ['T-shirt/top', 'Trouser','Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'AnkleBoot']

# 모델 만들기 // 이미지들을 숫자로 바꾸어 집어넣음 // 모델을 만들때 확률예측모델이라면 마지막 레이어 노드수를 카테고리 갯수만큼 정하고 cross entropy라는 로스함수를 사용해야함
model = tf.keras.Sequential([
    # convolution later 추가하기
    tf.keras.layers.Conv2D(32,(3,3),padding="same", activation='relu',input_shape=(28,28,1)), # 32개의 다른 feature(복사본)를 만들어달라 // (3,3) : kernel 가로세로 사이즈
    tf.keras.layers.MaxPooling2D((2,2)), # 복사본의 중요한 부분을 가운데로 모아주세요 // (2,2) : 모은 데이터 사이즈
    # tf.keras.layers.Dense(128,input_shape=(28,28),activation="relu"), # relu = 음수확률은 다 0으로 만들어주세요 // input_shape = 데이터 하나의 shape
    tf.keras.layers.Flatten(), # 행렬을 1차원으로 압축해주는 Flatten 레이어 // 즉 우리가 가지고 있는 2차원,3차원의 데이터들을 flatten레이어를 이용해서 1차원으로 보여주는 함수(가로로 나열해주세요!)
    tf.keras.layers.Dense(62,activation="relu"),
    tf.keras.layers.Dense(10,activation="softmax"), #sigmod = 결과를 0~1로 압축 -->binary 예측문제에 사용(예/아니오)(마지막 노드 갯수는 1개) // softmax = 결과를 0~1로 압축 -->카테고리 예측문제에 사용(예측한 결과 확률을 다 더하면 1나옴)
])
# flatten레이어를 사용할때의 문제점 : 이미지 데이터를 flatten하면 이미지 자체를 해체해(1차원으로 보여주니까) 딥러닝으로 돌리는 뜻 , 예측모델의 응용력이 다소 떨어짐 , 그 전에 사용한 가중치들이 쓸모가 없어짐
# flatten레이어를 사용하기 애매할때에 사용하는 convolutional 레이어 : 
    # 1.이미지에서 중요한 정보를 추려서 복사본 20장을 만듬
    # 2.이미지의 중요한 feature,특성들을 담겨있음
    # 이 두개를 feature extraction이라 함 (이미지,사물인식모델에선 꼭 필요한 레이어)
    # 즉 convolutional 레이어로 feature extraction을 한다 = 이미지의 복사본(각각의 특성들이 다르게 강조된 복사본)
# convolution 레이어는 kernel을 거쳐서 생김 즉 각각으 특성들을 답고 있는 복사본들을 kernel을 거쳐서 만들어진다는 뜻
# 이 만들어진 레이어값들을 사용해 뉴럴네크워크가 이걸 보고 학습함 단순한 convolution은 응용 학습이 힘듬 그래서 만드는 레이어가 pooling 레이어를 적용해야함 즉 down sampling.중요하 이미지 부분을 추려 가운데로 이동해주는 레이어
# 위에 내용들을 가지고 이미지,사물인식모델 만들때 사용하는 네크워크를 Convolution Neural Network(CNN)dml 일반적인 구성법
# input Image - Filters - Convolution Layers - Pooling Layer - Flattening
# convolution 레이어 구성 순서 : Conv*D - Pooling 여러번 - Flatten - Dense - 출력

# 모델 아웃라인 출력해보기 (모델을 한눈에 볼수 있는 함수) // summery를 출력하고 싶을때는 첫번째 layer부분에 input_shape=()를 넣어줘야 보기가능 //모델 트레이닝을 하기 전에 서머리를 보고 싶을때 사용 // 트레이닝 할때는 지우기
model.summary()

# compile 하기
model.compile(loss="sparse_categorical_crossentropy",optimizer="adam", metrics=['accuracy'])

# fit 하기
model.fit(trainX,trainY,validation_data=(testX,testY), epochs=5)
# 학습한 모델 평가하기
score = model.evaluate(testX,testY)
print(score)
# 학습한 모델의 accuracy와 ecaluate로 평가한 값이 다른 현상 : overfitting 현상이라함.데이터셋을 외워서 나타나는 현상
# 이러한 문제를 해결하기 위해서는 fit하는 코드 안에 validation_data=(X,Y)를 넣어 중간중간마다 채점을 시켜 결과값의 accuracy와 비슷하게 만들수 있음