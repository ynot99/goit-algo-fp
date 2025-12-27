import sys
import turtle


def pythagoras_tree(t: turtle.Turtle, level: int, branch_length: float) -> None:
    """Draws a Pythagoras tree recursively."""
    # Base Case: Stop if level is 0
    if level <= 0:
        return

    # Draw the root of the tree
    t.forward(branch_length)
    # Turn right
    t.right(45)
    # Recursive call: Decrease level by 1, and the size of the next branch
    pythagoras_tree(t, level - 1, branch_length * 0.80)
    # Turn left (45 + 45 = 90)
    t.left(90)
    # Recursive call: Decrease level by 1, and the size of the next branch
    pythagoras_tree(t, level - 1, branch_length * 0.80)
    # Restore orientation
    t.right(45)
    # Move back to the start of this branch
    t.backward(branch_length)


def draw_pythagoras_tree(level: int, size: float = 100) -> None:
    """Initialize turtle and draw the Pythagoras tree by calling a recursive function."""
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    # Set the fastest drawing speed
    t.speed(0)
    # Align the curve to the center. Where penup and pendown to move without drawing
    t.penup()
    t.goto(0, -size * 1.5)
    t.pendown()

    # Make the pen thicker
    t.pensize(2)
    # Brown color
    t.color("#C73030")

    # Position Turtle
    t.left(90)

    # Draw the Koch snowflake by rotating and drawing three Koch curves
    pythagoras_tree(t, level, size)

    # Hide the turtle to clean up the final image
    t.hideturtle()

    # Make sure the window stays open
    window.mainloop()


if __name__ == "__main__":
    # Default recursion level
    level = 8

    # Check if user provided an argument
    if len(sys.argv) > 1:
        try:
            level = int(sys.argv[1])
            if level < 0:
                print("Error: Level must be a non-negative integer.")
                sys.exit(1)
        except ValueError:
            print("Error: Level must be an integer.")
            sys.exit(1)

    draw_pythagoras_tree(level)
