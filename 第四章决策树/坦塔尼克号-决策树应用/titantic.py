import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer #特征转换器
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn import tree

#1.数据获取
titanic = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')
X = titanic[['Pclass','Age','Sex']]  #提取要分类的特征。一般可以通过最大熵原理进行特征选择
y = titanic['Survived']
test_x = test_data[['Pclass','Age','Sex']]
#2.数据预处理：训练集测试集分割，数据标准化
X['Age'].fillna(X['Age'].mean(),inplace=True)   #age只有633个，需补充，使用平均数或者中位数都是对模型偏离造成最小的策略
test_x['Age'].fillna(test_x['Age'].mean(),inplace=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=33)  # 将数据进行分割

vec = DictVectorizer(sparse=False)#不产生稀疏矩阵
X_train = vec.fit_transform(X_train.to_dict(orient='record'))   #对训练数据的特征进行提取
X_test = vec.transform(X_test.to_dict(orient='record'))         #对测试数据的特征进行提取
predict_x = vec.transform(test_x.to_dict(orient='record'))
#转换特征后，凡是类别型型的特征都单独独成剥离出来，独成一列特征，数值型的则不变
print (vec.feature_names_)   #['age', 'sex=female', 'sex=male']
#3.使用决策树对测试数据进行类别预测
dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
y_predict = dtc.predict(predict_x)
y_predict = y_predict.astype('int')
#4.获取结果报告
print ('Accracy:',dtc.score(X_test,y_test))

predic_result = pd.DataFrame({'PassengerId':test_data['PassengerId'],'Survived':y_predict})
predic_result.to_csv('./data/submission.csv',index=False)