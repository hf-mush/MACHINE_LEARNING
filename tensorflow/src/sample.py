import tensorflow as tf
# print text
hello = tf.constant('Hello, Tensorflow')
sess = tf.Session()
print(sess.run(hello))
# print culclate number
a = tf.constant(10)
b = tf.constant(50)
print(sess.run(a+b))
# exit
exit()