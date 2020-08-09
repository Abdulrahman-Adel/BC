# Binary-Classification
developing a machine learning model using the training set that performs well on the validation set.

----

## Thoughts on dataset

the training dataset was imbalanced. "variable 14" and "variable 17" are the same and so are "variable 4" and "variable 5".some categorical columns such as "variable 5", "variable 6" and "variable 7" have more categories in the training set than in the validation set. at first i was inclined to drop columns with high "NAN" precentage such as "variable 18" and high cordinality columns such as "variable 6" but keeping them helps the preformance of the model. 

----

## Approach

using columntransformer and pipeline to handle missing data and onehotencode categorical columns. I droped all the rows with the additional category in "variable 6", "variable 7" and "variable 5". and i also droped columns "variable 17" and "variable 4"

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
