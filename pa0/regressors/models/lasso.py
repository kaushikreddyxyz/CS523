# SYSTEM IMPORTS
from typing import Type
import numpy as np

# PYTHON PROJECT IMPORTS


# TYPES DECLARED IN THIS MODULE
LassoRegressorType = Type["LassoRegressor"]


# CONSTANTS




class LassoRegressor(object):
    def __init__(self: LassoRegressorType,
                 num_features: int,             # the number of features each example has
                 regularizer_coeff: float = 1   # the coefficient for the l-1 regularization term in the loss function
                 ) -> None:
        self.w: np.ndarray = np.random.randn(num_features, 1)   # the params of the model
        self.regularizer_coeff: float = regularizer_coeff

    def predict(self: LassoRegressorType,
                X: np.ndarray) -> np.ndarray:
        """
            A method to calculate predictions using lasso regression.
            @param X: the matrix of input examples. Has shape (num_examples, num_features))
            @return np.ndarray: the matrix of predictions. Has shape (num_examples, 1)
        """
        return np.matmul(X, self.w)

    def loss(self: LassoRegressorType,
             Y_hat: np.ndarray,
             Y_gt: np.ndarray) -> float:
        """
            A method to calculate the loss function for lasso regression.
            @param Y_hat: the matrix of predictions. Has shape (num_examples, 1)
            @param Y_gt: the matrix of ground truth. Has shape (num_examples, 1)
            @return float: the lasso regression loss function evaluated at Y_hat, Y_gt
        """
        return np.sum(np.square(Y_hat - Y_gt)) + self.regularizer_coeff * np.sum(np.abs(self.w))

    def grad(self: LassoRegressorType,
             X: np.ndarray,
             Y_gt: np.ndarray) -> np.ndarray:
        """
            A method to calculate the gradient of the lasso loss function with respect to the parameters 'self.w'
            @param X: the matrix of input examples. Has shape (num_examples, num_features)
            @param Y_gt: the matrix of ground truth. Has shape (num_features, 1)
            @return np.ndarray: the gradient of the lasso loss function with respect to 'self.w'. Has shape (num_features, 1)
        """
        # return (2 * (X.T @ (self.predict(X) - Y_gt)) + 2 * self.regularizer_coeff * self.w)
        return (2 * (X.T @ (self.predict(X) - Y_gt)) + self.regularizer_coeff * np.sign(self.w))

