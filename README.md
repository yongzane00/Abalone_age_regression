# Abalone Age Regression

## Abstract
The dataset selected for analysis in this project is the abalone dataset, published by the UC Irvine Machine Learning Repository in 1995. Before delving into regression modeling for predictive purposes, it's crucial to thoroughly understand the data source and the real-world challenges it represents. Next, we will proceed with data processing and cleaning to ensure the integrity of the dataset. Finally, we will employ linear and non-linear regression models to identify the most effective solution to address this problem.

## Introduction
Abalone has been a favored food source for centuries, with its price being positively correlated with its age. However, determining the age of abalone involves assessing physical measurements, which is a time-intensive process. Traditionally, this has been accomplished by cutting the shell through the cone, staining it, and manually counting the number of rings under a microscope. The total number of rings plus 1.5 reveals the actual age of the abalone. The variables presented below fully represent the situation of abalone in the real world enabling the utilization of these data to predict age and accelerate this tedious process [1]. 

## Variable Description

| Variable Name | Role | Type | Description | Units | Missing Values |
| --- | --- | --- | --- | --- | --- |
| Sex | Feature | Categorical | M, F, and I (infant) | NA | no |
| Length | Feature | Continuous | Longest shell measurement | mm | no |
| Diameter | Feature | Continuous | perpendicular to length | mm | no |
| Height | Feature | Continuous | with meat in shell | mm | no |
| Whole weight | Feature | Continuous | whole abalone | grams | no |
| Shucked weight | Feature | Continuous | weight of meat | grams | no |
| Viscera weight | Feature | Continuous | gut weight (after bleeding) | grams | no |
| Shell weight | Feature | Continuous | after being dried | grams | no |
| Rings | Target | Integer | +1.5 gives the age in years | NA | no |

## Methodologies
Please refer to the main(regression).ipynb Jupyter Notebook

## Results and Discussion

![image](https://github.com/yongzane00/Abalone_age_regression/assets/115027208/beebf593-c271-4aa2-8e04-e8fcaa862e20)


![image](https://github.com/yongzane00/Abalone_age_regression/assets/115027208/e5abf879-3fc7-43ae-8596-4db7064678c8)


From the evaluation metrics above, the overall adjusted R2 score ranges from 0.464 to 0.536. This level of fitting is not uncommon when dealing with real-world regression problems. Upon evaluation of each model, it was found that linear regression performed similarly to the support vector regressor, random forest regressor, and gradient boosting regressor. This suggests that the abalone dataset exhibits a linear relationship and is highly explainable. However, the linear model of ridge regression did not perform well, as the additional regularization term further complicated the model and worsened its performance. Additionally, the k-nearest neighbor model exhibited the worst performance, possibly due to the lack of fine-tuning for the hyperparameter k with a validation set. Conversely, the neural network demonstrated the best performance among all models. This suggests that there may be hidden patterns in the data that were not captured by the linear and non-linear algorithms mentioned above. The complex relationships in this dataset could potentially be captured by increasing the number of data points and including additional features such as temperature, weather, location, or any other variables that could influence the physical appearance of the abalone.


## Reference
[1] “UCI Machine Learning Repository,” archive.ics.uci.edu. https://archive.ics.uci.edu/dataset/1/abalone.
