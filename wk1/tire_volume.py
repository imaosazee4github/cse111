import math
from datetime import datetime


# Function to calculate the volume of the tire
def calculate_tire_volume(width_mm, aspect_ratio, diameter_inches):

    # Calculate diameter in millimeters
    diameter_mm = diameter_inches * 25.4

    # Calculate the radius of the tire in millimeters
    radius_mm = width_mm * aspect_ratio / 100 / 2

    # Calculate the volume of space inside the tire
    volume_liters = (math.pi * (radius_mm ** 2) * aspect_ratio * width_mm + 2540 * diameter_inches) / 1000000000

    return volume_liters


# Main function to get user input, calculate, and display volume
def main():
    # Prompt the user for input
    print("Enter the width of the tire in mm (ex 205): ")
    width_mm = int(input())

    print(f"Enter the aspect ratio of the tire (ex 60):")
    aspect_ratio = int(input())

    print(f"Enter the diameter of the wheel in inches (ex 15): ")
    diameter_inches = int(input())

    # Calculate the volume
    volume_liters = calculate_tire_volume(width_mm, aspect_ratio, diameter_inches)

    # Display the result with two decimal places
    print(f"The approximate volume is {volume_liters:.2f} liters")

    # Get current date
    today = datetime.today().strftime("%Y-%m-%d")

    # Open file for appending (create if not exists)
    with open("volumes.txt", "at") as file:
        # Write data to file (including date)
        file.write(
            f"{today},{width_mm},{aspect_ratio},{diameter_inches},{volume_liters}\n"
        )


if __name__ == "__main__":
    main()

