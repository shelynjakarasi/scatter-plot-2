import pandas as pd
import matplotlib.pyplot as plt


class Coordinate:
    def __init__(self, x, y):
        """
        Create a Coordinate object with specified x and y values.

        Parameters:
        - x (float): The x-coordinate.
        - y (float): The y-coordinate.
        """
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """
        Adjust the coordinate by dx and dy.

        Parameters:
        - dx (float): The amount to change the x-coordinate.
        - dy (float): The amount to change the y-coordinate.
        """
        self.x += dx
        self.y += dy

    def __repr__(self):
        """Provide a string representation of the Coordinate."""
        return f"Coordinate({self.x}, {self.y})"


def load_coordinates_from_file(filepath):
    """
    Load coordinates from a file and return them as a list of Coordinate objects.

    Parameters:
    - filepath (str): The location of the text file with the coordinates.

    Returns:
    - List[Coordinate]: A list of Coordinate objects.
    """
    data = pd.read_csv(filepath, header=None, names=['X', 'Y'], delim_whitespace=True)
    return [Coordinate(float(row['X']), float(row['Y'])) for index, row in data.iterrows()]


def display_coordinates(coordinates, color='blue', label='Initial Coordinates'):
    """
    Visualize a list of Coordinate objects in a scatter plot.

    Parameters:
    - coordinates (List[Coordinate]): The coordinates to visualize.
    - color (str): The color of the plotted points.
    - label (str): The label to use in the legend.
    """
    x_values = [coord.x for coord in coordinates]
    y_values = [coord.y for coord in coordinates]
    plt.scatter(x_values, y_values, color=color, label=label)


def run():
    # Specify the path to the coordinates file
    filepath = r"C:\Users\USER\PycharmProjects\Assignment 2\x_y_coordinates.txt"

    # Load coordinates from the file
    coordinates = load_coordinates_from_file(filepath)

    # Plot the original coordinates
    display_coordinates(coordinates, color='blue', label='Initial Coordinates')

    # Move the coordinates (for instance, by (1, 1))
    translation = (1, 1)  # Modify this for different translation values
    for coord in coordinates:
        coord.move(*translation)

    # Plot the moved coordinates
    display_coordinates(coordinates, color='red', label='Moved Coordinates')

    # Customize the plot
    plt.title('Scatter Plot of Coordinates')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.legend()
    plt.show()


# Execute the main function
if __name__ == "__main__":
    run()