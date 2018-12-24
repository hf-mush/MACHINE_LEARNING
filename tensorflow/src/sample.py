"""Output image analysis result."""
import tensorflow as tf
SESS = tf.Session()
# print culclate number
A = tf.constant(10)
B = tf.constant(50)
print(SESS.run(A+B))
# exit
exit()
