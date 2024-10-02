import numpy as np

class ProcessData:

	def __init__(self):
		pass

	def add_dummy(self, X):
		return np.c_[np.ones(X.shape[0]), X]
	
	def one_hot_encoder(self, y):
		n_classes = np.unique(y)
		one_hot = np.zeros((y.shape[0], n_classes.shape[0]))
		for i, class_ in enumerate(y):
			one_hot[i, class_] = 1
		return one_hot
	
	def split_data(self, X, y, test_ratio=0.2, val_ratio=0.2, random_state=None):
		# Set random seed
		if random_state:
			np.random.seed(random_state)
		
		# Shuffle data
		shuffled_idxs = np.random.permutation(X.shape[0])

		# Split data
		total_size = X.shape[0]

		# Validation set
		val_size = int(total_size*val_ratio)
		val_idxs = shuffled_idxs[:val_size]
		X_val, y_val = X[val_idxs], y[val_idxs]
		
		# Test set
		test_size = int(total_size*test_ratio)
		test_idxs = shuffled_idxs[val_size:val_size+test_size]
		X_test, y_test = X[test_idxs], y[test_idxs]

		# Train set
		train_idxs = shuffled_idxs[val_size+test_size:]
		X_train, y_train = X[train_idxs], y[train_idxs]

		return X_train, y_train, X_val, y_val, X_test, y_test

		
	def normalize(self, X):
		return (X - X.mean(axis=0))/X.std(axis=0)
		
	def standardize(self, X):
		return (X - X.min(axis=0))/(X.max(axis=0) - X.min(axis=0))
	
	def log_transform(self, X):
		return np.log(X)