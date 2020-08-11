# Binary-Classification
developing a machine learning model using the training set that performs well on the validation set.

----

## Thoughts on dataset

the training dataset had 3210 duplicated rows (all of them class labeled "yes."). there are also duplicated columns (but different in [scale - data type]) such as ["variable 14" and "variable 17"] , ["variable 4" and "variable 5"] and ["variable 19" and "classLabel"]. some categorical columns such as "variable 5", "variable 6" and "variable 7" have more categories in the training set than in the validation set.""there is no "variable 16" ?!"". at first i was inclined to drop columns with high "NAN" precentage such as "variable 18" and high cordinality columns such as "variable 6" but keeping them helps the preformance of the model. 

----

## Approach

using columntransformer and pipeline to handle missing data and onehotencode categorical columns. I droped all the rows with the additional category in "variable 6", "variable 7" and "variable 5". and i also droped columns "variable 17" and "variable 4"

----

## Algorithms Comparison

| model                  	| parameters                                	| accuracy 	| precision(0/1) 	| f1_score(0/1) 	|
|------------------------	|-------------------------------------------	|----------	|----------------	|---------------	|
| KNeighborsClassifier   	| Apply PCA(n_components = 11)              	| 0.865    	| (0.87 / 0.86)  	| (0.87 / 0.85) 	|
| XGBClassifier          	| learning_rate = 0.02,booster = "gblinear" 	| 0.89     	| (0.90 / 0.88)  	| (0.90 / 0.89) 	|
| RandomForestClassifier 	| n_estimators = 10                         	| 0.88     	| (0.90 / 0.86)  	| (0.89 / 0.87) 	| 
| SVC                    	| -                                         	| 0.86     	| (0.92 / 0.80)  	| (0.86 / 0.86) 	|
| LogisticRegression     	| Applying PCA(n_components = 14)           	| 0.875    	| (0.89 / 0.85)  	| (0.88 / 0.87) 	|
| DecisionTreeClassifier 	| Applying PCA(n_components = 7)            	| 0.81     	| (0.84 / 0.78)  	| (0.82 / 0.80) 	| 
| LGBMClassifier         	| learning_rate = 0.04                      	| 0.885    	| (0.95 / 0.83)  	| (0.89 / 0.88) 	| 
