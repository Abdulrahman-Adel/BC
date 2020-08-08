# Binary-Classification
developing a machine learning model using the training set that performs well on the validation set.

----

## Thoughts on dataset

the training dataset was imbalanced. "variable 14"(which is float but suppose to be integer) and "variable 17" are the same but different datatypes [int64 , float64]. at first i was inclined to drop columns with high "NAN" precentage such as "variable 18" and high cordinality columns such as "variable 6" but keeping them helps the preformance of the model. 

----

## Approach

using columntransformer and pipeline to handle missing data and onehotencode categorical columns and i also droped "variable 14"

----

## Different Approach

I tried to resample the data using sklearn.utils to make the dataset balanced. I also tried a dimensionality reduction algorithm (PCA).
This appoach didn't realy help the overall preformance but significantly increased the proformace of some Algorithms (logistic regression - SVC).

----

## Algorithms Comparison

| model                  | parameters                              | accuracy | precision(0/1) | f1_score(0/1) | 
|------------------------|-----------------------------------------|----------|----------------|---------------|
| KNeighborsClassifier   | -                                       | 0.77     | (0.94 / 0.68)  | (0.74 / 0.79) |
| XGBClassifier          | learning_rate = 0.302                   | 0.865    | (0.95 / 0.79)  | (0.86 / 0.87) |   
| RandomForestClassifier | -                                       | 0.885    | (0.94 / 0.84)  | (0.89 / 0.88) |   
| SVC                    | -                                       | 0.8      | (0.94 / 0.72)  | (0.78 / 0.81) |   
| LogisticRegression     | -                                       | 0.715    | (0.96 / 0.62)  | (0.65 / 0.76) |   
| DecisionTreeClassifier | -                                       | 0.805    | (0.80 / 0.81)  | (0.82 / 0.78) |   
| LGBMClassifier         | learning_rate = 0.25, n_estimators = 250 | 0.885    | (0.94 / 0.84)  | (0.89 / 0.88) |   

----------

## Algorithms Comparison(Different Approach)

| model                  	| parameters                                        	| accuracy 	| precision(0/1) 	| f1_score(0/1) 	 
|------------------------	|---------------------------------------------------	|----------	|----------------	|---------------
| KNeighborsClassifier   	| -                                                 	| 0.735    	| (0.78 / 0.69)  	| (0.74 / 0.73) 	
| XGBClassifier          	| learning_rate = 0.7                               	| 0.87     	| (0.92 / 0.83)  	| (0.87 / 0.87) 	
| RandomForestClassifier 	| n_estimators = 500                                	| 0.865    	| (0.91 / 0.82)  	| (0.87 / 0.86)  
| SVC                    	| Kernel = "linear", Applying PCA(n_component = 16) 	| 0.86     	| (0.91 / 0.80)  	| (0.86 / 0.85)  
| LogisticRegression     	| -                                                 	| 0.855    	| (0.94 / 0.79)  	| (0.85 / 0.86)   
| DecisionTreeClassifier 	| Applying PCA(n_components = 26)                   	| 0.83     	| (0.85 / 0.80)  	| (0.84 / 0.82)  
| LGBMClassifier         	| learning_rate = 0.525 n_estimators = 200          	| 0.875    	| (0.93 / 0.83)  	| (0.88 / 0.87) 
