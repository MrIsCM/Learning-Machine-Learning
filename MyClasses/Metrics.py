import numpy as np

class Metrics:
	def __init__(self):
		pass

	def accuracy(self, y_true, y_pred):
		return np.mean(y_true == y_pred)
	
	def precision(self, y_true, y_pred):
		tp = np.sum((y_true == 1) & (y_pred == 1))
		fp = np.sum((y_true == 0) & (y_pred == 1))
		return tp/(tp+fp)
	
	def recall(self, y_true, y_pred):
		tp = np.sum((y_true == 1) & (y_pred == 1))
		fn = np.sum((y_true == 1) & (y_pred == 0))
		return tp/(tp+fn)
	
	def f1_score(self, y_true, y_pred):
		prec = self.precision(y_true, y_pred)
		rec = self.recall(y_true, y_pred)
		return 2*(prec*rec)/(prec+rec)
	
	def mse(self, y_true, y_pred):
		'''Mean Squared Error'''
		return np.mean((y_true - y_pred)**2)
	
	def rmse(self, y_true, y_pred):
		'''Root Mean Squared Error'''
		return np.sqrt(self.mse(y_true, y_pred))
	
	def mae(self, y_true, y_pred):
		'''Mean Absolute Error'''
		return np.mean(np.abs(y_true - y_pred))
	
	def mape(self, y_true, y_pred):
		'''Mean Absolute Percentage Error'''
		return np.mean(np.abs((y_true - y_pred)/y_true))
	
	def r2_score(self, y_true, y_pred):
		'''R^2 Score'''
		ss_res = np.sum((y_true - y_pred)**2)
		ss_tot = np.sum((y_true - y_true.mean())**2)
		return 1 - ss_res/ss_tot
	
	def confusion_matrix(self, y_true, y_pred):
		tp = np.sum((y_true == 1) & (y_pred == 1))
		tn = np.sum((y_true == 0) & (y_pred == 0))
		fp = np.sum((y_true == 0) & (y_pred == 1))
		fn = np.sum((y_true == 1) & (y_pred == 0))
		return np.array([[tn, fp], [fn, tp]])
	
	def l2_norm(self, x, y):
		return np.linalg.norm(x - y)
	
	def l1_norm(self, x, y):
		return np.sum(np.abs(x - y))
	
	def ln_norm(self, x, y, n):
		return np.sum(np.abs(x - y)**n)**(1/n)