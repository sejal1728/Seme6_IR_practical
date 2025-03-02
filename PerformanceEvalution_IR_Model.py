
from sklearn.metrics import precision_score,recall_score,f1_score

ground_truth = [1,0,1,1,1,0,1,1,0,1]
predition_relevence = [1,0,0,1,0,1,1,0,1,1]

pricison=precision_score(ground_truth,predition_relevence)
recall=recall_score(ground_truth,predition_relevence)
f1_score=f1_score(ground_truth,predition_relevence)

print("\nPricison",pricison)
print("\nRecall",recall)
print("\nF1 Score",f1_score)
