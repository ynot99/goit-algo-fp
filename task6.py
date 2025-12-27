def greedy_algorithm(items: dict, budget: int) -> dict:
    # Sort items by calories-to-cost ratio in reversed order
    # for greedy selection
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_cost = 0
    total_calories = 0
    selected_items = {}

    # Select items based on the greedy approach
    for item, details in sorted_items:
        # If we haven't exceeded the budget, add the item
        if total_cost + details["cost"] <= budget:
            selected_items[item] = details
            # Update totals
            total_cost += details["cost"]
            total_calories += details["calories"]

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def dynamic_programming(items: dict[str, dict[str, int]], budget: int) -> dict:
    # Number of items
    n = len(items)
    # Initialize dynamic programming table
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    # Extract items to have a list of (item, details) tuples
    item_list = list(items.items())

    # Build the DP table
    for i in range(1, n + 1):
        # Get item, cost, and calories
        item, details = item_list[i - 1]
        cost = details["cost"]
        calories = details["calories"]
        # Fill the DP table for all budgets: 0, 1, 2, ..., budget
        for b in range(budget + 1):
            if cost <= b:
                # If including the item gives more calories, include it
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                # Else, don't include the item
                dp[i][b] = dp[i - 1][b]

    b = budget
    selected_items = {}
    # Backtrack the DP table to find selected items
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item, details = item_list[i - 1]
            selected_items[item] = details
            b -= details["cost"]

    total_cost = sum(details["cost"] for details in selected_items.values())
    total_calories = sum(details["calories"] for details in selected_items.values())

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


if __name__ == "__main__":
    ITEMS = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    BUDGET = 100

    # Calculate results of both algorithms
    result_greedy = greedy_algorithm(ITEMS, BUDGET)
    result_dp = dynamic_programming(ITEMS, BUDGET)

    # Print items and budget
    print("Items:")
    for item, details in ITEMS.items():
        print(f" - {item}: cost={details['cost']}, calories={details['calories']}")

    print(f"\nBudget: {BUDGET}\n")

    # Print results
    print("Greedy Algorithm Result:")
    print("Selected Items:", ", ".join(result_greedy["selected_items"].keys()))
    print("Total Cost:", result_greedy["total_cost"])
    print("Total Calories:", result_greedy["total_calories"])

    print("\nDynamic Programming Result:")
    print("Selected Items:", ", ".join(result_dp["selected_items"].keys()))
    print("Total Cost:", result_dp["total_cost"])
    print("Total Calories:", result_dp["total_calories"])
