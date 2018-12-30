import tensorflow as tf

hello =tf.constant("hello sunish")
sess = tf.Session()
print(sess.run(hello))
