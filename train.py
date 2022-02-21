import gpt_2_simple as gpt2
import tensorflow as tf

model_name = "124M"
steps = 200

gpt2.download_gpt2(model_name=model_name)

tf.compat.v1.reset_default_graph()

sess = gpt2.start_tf_sess()

gpt2.finetune(sess, "file.txt", model_name=model_name, steps=steps)