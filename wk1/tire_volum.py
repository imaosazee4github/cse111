import math


# Function to calculate the volume of the tire

def calculate_tire_volume(width_mm, aspect_ratio, diameter_inches):
    
    # calculate diameter to inches to millimeters
    diameter_mm = diameter_inches * 25.4
    
    # Calculate the radius of the tire in millimeters
    radius_mm = width_mm * aspect_ratio / 100 / 2
    
    # Calculate the volume of  space in inside the tire.
    volume_liters = (math.pi * (radius_mm ** 2) * aspect_ratio * width_mm +  2540 * diameter_inches) / 1000000000
    return volume_liters


# Main function to get user input and display the result.
    
def main():
    # prompt the user to input the width of the tire in millimeters
    print("Enter the width of th tire in mm (ex 205) :")
    width_mm = int(input())
    
    # prompt the user to input the aspect ratio of the tire
    print(f"Enter the aspect ratio of the tire (ex 60):")
    aspect_ratio = int(input())
    
    # prompt the user to input the diameter of the wheel in inches
    print(f"Enter the diameter of the wheel in inches (ex 15): ")
    diameter_inches = int(input())
    
    # calculate the volume of the tire using the calculate_tire_volume function
    volume_liters = calculate_tire_volume(width_mm, aspect_ratio, diameter_inches)
    
    # display the approximate volume of the tire
    
    print(f"The approximate volume is {volume_liters:.2f} liters")

if __name__ == "__main__":
    main()
