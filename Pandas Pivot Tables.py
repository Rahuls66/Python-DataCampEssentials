# Default Aggregation Mean

# For one column
dogs.groupby("color")["weight_kg"].mean()
int64dogs.pivot_table(values="weight_kg", index="color")


# For Two columns
dogs.groupby(["color", "breed"])["weight_kg"].mean()
dogs.pivot_table(values="weight_kg", index="color", columns="breed")


# With other aggregation
dogs.pivot_table(values="weight_kg", index="color", columns="breed", aggfunc = np.median)
dogs.pivot_table(values="weight_kg", index="color", columns="breed", aggfunc = [np.median, np.std])

# With Null Value Replacement
dogs.pivot_table(values="weight_kg", index="color", columns="breed", aggfunc = [np.median, np.std], fill_value = 0)
