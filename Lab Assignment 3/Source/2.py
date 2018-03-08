import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm


wine_dataset = datasets.load_wine()             #load wine dataset

m = wine_dataset.data[:,:2]                     #separate data from target attributes
n = wine_dataset.target

h=0.3

m_min, m_max = m[:, 0].min() - 1, m[:, 0].max() + 1
n_min, n_max = m[:, 1].min() - 1, m[:, 1].max() + 1
mm, nn = np.meshgrid(np.arange(m_min, m_max, h),np.arange(n_min, n_max, h))     #generating grid points

m_train,m_test,n_train,n_test=train_test_split(m,n,test_size=0.2)   # 20% testing data
model_name = svm.SVC()

rbf_predic = model_name.set_params(kernel='rbf').fit(m_train, n_train).predict(m_test)

linea_predic = model_name.set_params(kernel='linear').fit(m_train, n_train).predict(m_test)

rbf_accu = metrics.accuracy_score(n_test,rbf_predic)
print('kernal accuracy with rbf:',rbf_accu)


linear_accu = metrics.accuracy_score(n_test,linea_predic)
print('kernal Accuracy with linear:',linear_accu)




