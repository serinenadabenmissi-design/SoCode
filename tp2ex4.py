scores = {
"Alice": 88,
"Bob": 95,
"Charlie": 90
}

best_studnt=max(scores,key=scores.get)
best_score=scores[best_studnt]

print(f"the best student is {best_studnt} with {best_score}")
    
