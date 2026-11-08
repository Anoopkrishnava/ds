import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score,
    recall_score,
    f1_score,
    precision_score,
    confusion_matrix,
    classification_report)


#read the json file
with open("decision_tree_student_result.json","r") as file:
    data = json.load(file)
#create the dataframe
df = pd.DataFrame(data["students"])
#seperate features and target
x = df[["attendance","internal","exam"]]
y = df["result"]
#split the data
x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.25,random_state=42)

#create the model
model  = DecisionTreeClassifier(criterion="entropy",random_state=42)
model.fit(x_train,y_train)  #train the model with the dataset

#predict the test data
y_pred = model.predict(x_test)

#calculate the evaluation matrix
print(f"Accuracy score :{accuracy_score(y_test,y_pred)}")
print(f"Precision {precision_score(y_test,y_pred,pos_label="Pass",zero_division=0)}")
print(f"Recall :{recall_score(y_test,y_pred,pos_label="Pass",zero_division=0)}")
print(f"F1-score :{f1_score(y_test,y_pred,pos_label="Pass",zero_division=0)}")

#confusion matrix
cm = confusion_matrix(y_test,y_pred,labels=["Fail","Pass"])
print(f"Confusion matrix : {cm}")

#classification report
print("classification report")
print(classification_report(y_test,y_pred,zero_division=0))

#plot the decision tree
plt.figure(figsize=(15,8))
plot_tree(
    model,
    feature_names=["attendance","internal","exam"],
    class_names=["Fail","Pass"],
    filled = True
)
plt.title("Decision tree")
plt.show()

#predicting a new students result
attendance  = float(input("Enter attendance percentage :"))
internal  = float(input("Enter internal mark :"))
exam  =  float(input("Enter exam mark :"))

new_student = pd.DataFrame(
    [[attendance,internal,exam]],
    columns  = ["attendance","internal","exam"]
)

prediction = model.predict(new_student)[0]

print(f"Decision tree predicted result {prediction}")