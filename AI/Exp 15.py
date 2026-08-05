import math

# Training data
dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']


def entropy(data):
    total = len(data)
    counts = {}

    for row in data:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1

    ent = 0
    for count in counts.values():
        p = float(count) / total
        ent -= p * math.log(p, 2)

    return ent


def information_gain(data, feature):
    total_entropy = entropy(data)
    values = {}

    for row in data:
        values.setdefault(row[feature], []).append(row)

    weighted_entropy = 0

    for subset in values.values():
        weighted_entropy += (float(len(subset)) / len(data)) * entropy(subset)

    return total_entropy - weighted_entropy


def build_tree(data, feature_names):
    labels = [row[-1] for row in data]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if len(feature_names) == 0:
        return max(set(labels), key=labels.count)

    gains = [information_gain(data, i) for i in range(len(feature_names))]
    best_feature = gains.index(max(gains))

    tree = {feature_names[best_feature]: {}}

    values = set(row[best_feature] for row in data)

    for value in values:
        subset = []

        for row in data:
            if row[best_feature] == value:
                new_row = row[:best_feature] + row[best_feature + 1:]
                subset.append(new_row)

        new_features = feature_names[:best_feature] + feature_names[best_feature + 1:]
        tree[feature_names[best_feature]][value] = build_tree(subset, new_features)

    return tree


tree = build_tree(dataset, features)

print("Decision Tree:")
print(tree)
