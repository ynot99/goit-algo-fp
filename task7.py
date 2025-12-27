import random
from collections import Counter

import matplotlib.pyplot as plt


def analytical_probabilities() -> tuple[dict[int, float], Counter[int]]:
    combinations: Counter[int] = Counter()

    # Count combinations for each possible sum
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            combinations[die1 + die2] += 1

    # General number of combinations
    total_combinations = 36

    # Convert counts to probabilities
    probabilities = {
        sum_value: count / total_combinations
        for sum_value, count in combinations.items()
    }

    return probabilities, combinations


def monte_carlo_probabilities(num_simulations: int) -> dict[int, float]:
    sums_counter: Counter[int] = Counter()

    # Make a roll for num_simulations times
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums_counter[die1 + die2] += 1

    # And convert counts to probabilities
    probabilities = {
        sum_value: count / num_simulations for sum_value, count in sums_counter.items()
    }

    return probabilities


def table_comparison():
    analytical, combinations = analytical_probabilities()
    MC_SIMULATIONS = 1000000
    monte_carlo = monte_carlo_probabilities(MC_SIMULATIONS)

    # Get all sum combinations from analytical results,
    # because we expect monte_carlo to possibly miss some combinations
    # on a very low number of simulations
    dice_combinations = sorted(analytical.keys())

    # Prepare data for the table
    table_data = []
    for dice_sum in dice_combinations:
        analytical_prob = analytical[dice_sum] * 100
        # Get the number of combinations from analytical results
        combination = combinations[dice_sum]
        # Default to 0 if not found
        mc_prob = monte_carlo.get(dice_sum, 0) * 100
        # Calculate the Monte Carlo error in percentage
        prob_difference = abs(analytical_prob - mc_prob)

        table_data.append(
            [
                f"{dice_sum}",
                f"{analytical_prob:.2f}% ({combination}/36)",
                f"{mc_prob:.2f}%",
                f"{prob_difference:.4f}%",
            ]
        )

    # Create a table
    table = plt.table(
        cellText=table_data,
        colLabels=[
            "Сума",
            "Імовірність\n(Аналітична)",
            "Імовірність\n(Монте-Карло)",
            "Похибка Монте-Карло",
        ],
        cellLoc="left",
        loc="center",
    )
    plt.axis("off")
    # Scale cells to make the text fit
    table.scale(1, 1.3)
    # Scale font size based on window size
    table.auto_set_font_size(False)
    table.set_fontsize(12)

    plt.title(
        f"Порівняння ймовірностей сум двох кидків кубиків\n"
        f"(Кількість симуляцій Монте-Карло: {MC_SIMULATIONS})",
    )

    plt.show()


if __name__ == "__main__":
    table_comparison()
