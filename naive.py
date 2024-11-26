import random

# Step 1: Generate random numbers
random.seed(40)
data = [random.randint(0, 100) for _ in range(100)]

# Step 2: Define class ranges
classes = {
    "Low": range(0, 34),
    "Medium": range(34, 67),
    "High": range(67, 101),
}

# Step 3: Calculate prior probabilities (P(C))
total_data = len(data)
prior_probabilities = {
    cls: len([x for x in data if x in rng]) / total_data for cls, rng in classes.items()
}

# Step 4: Classify each number using Naive Bayes
def naive_bayes_simple(x):
    probabilities = {}
    for cls, rng in classes.items():
        # Assume uniform probability for P(x|C)
        p_x_given_class = 1 / len(rng) if x in rng else 0
        # P(C|x) ∝ P(x|C) * P(C)
        probabilities[cls] = p_x_given_class * prior_probabilities[cls]
    # Determine the class with the highest probability
    best_class = max(probabilities, key=probabilities.get)
    return best_class

# Step 5: Classify all numbers in the data
classified_data = {x: naive_bayes_simple(x) for x in data}

# Output the results
print("Random Numbers:", data)
print("\nClassification Results:")
for num, cls in classified_data.items():
    print(f"Number: {num}, Class: {cls}")
