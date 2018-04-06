import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Load the data from .text file
data = np.loadtxt('iris.txt', skiprows=1)

X_data = data[:,:2]
Y_data = data[:,2:]

# make placeholders
x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 1])


W = tf.Variable(tf.zeros([2, 1]))
b = tf.Variable([0.0])


mymodel = tf.matmul(x, W) + b


loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=mymodel)
loss = tf.reduce_mean(loss)


predict_op  = tf.greater_equal(mymodel, tf.zeros_like(mymodel))
correct_op  = tf.equal(tf.cast(predict_op, tf.float32), y)
accuracy_op = tf.reduce_mean(tf.cast(correct_op, tf.float32))


learning_rate = 0.01
num_epochs    = 100


optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train_op  = optimizer.minimize(loss)


sess = tf.Session()
sess.run(tf.global_variables_initializer())


writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

np.random.seed(0)


for epoch in range(num_epochs):
    idx = np.random.permutation(data.shape[0])
    for i in idx:
        feed_dict = {x: X_data[i:i+1], y: Y_data[i:i+1]}
        sess.run(train_op, feed_dict)

    if (epoch+1) % 10 == 0:
        feed_dict = {x: X_data, y: Y_data}
        accuracy = sess.run(accuracy_op, feed_dict)
        print("After {} epochs, accuracy = {}".format(epoch+1, accuracy))

writer.close()


W_val, b_val = sess.run([W, b])
W_val = W_val[:,0]
b_val = b_val[0]
print("W =", W_val)
print("b =", b_val)

def predict(x_):
    return 1 * sess.run(predict_op, {x: x_})

# Model predictions
labels = predict(X_data)[:,0]

# Find indices for the two species
idx_0, = np.where(labels == 0)
idx_1, = np.where(labels == 1)

# Plot the data
plt.plot(X_data[idx_0,0], X_data[idx_0,1], 'bo', label='versicolor')
plt.plot(X_data[idx_1,0], X_data[idx_1,1], 'ro', label='virginica')

# Plot separating hyperplane
x_sep = np.linspace(X_data[:,0].min(), X_data[:,0].max())
y_sep = (-b_val - W_val[0]*x_sep) / W_val[1]
plt.plot(x_sep, y_sep, 'm', label="Regression Line")
plt.legend()

plt.xlabel("Sepal length: ")
plt.ylabel("Petal legnth: ")

plt.show()