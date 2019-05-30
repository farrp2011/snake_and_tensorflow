import tensorflow as tf

class Model:
	def __init__(self, num_states, num_actions, batch_size):
		self._num_states = num_states
		self._num_actions = num_actions
		self.batch_size = batch_size
		#define the placeholders
		self._states = None
		self._actions = None
		#the output operations
		self._logits = None
		self._optimizer = None
		self._var_init = None
		# setup the model
		self._define_mode()

	def _define_model(self):
		self._states = tf.placeholder(shape=[None, self._num_states], dtype=tf.float32)
		self._q_s_a = tf.placeholder(shape=[None, self._num_actions], dtype=tf.float32)

