def calculate_material_cost(length, width, cost_per_sqft):
    """Calculate the total material cost based on room dimensions."""
    area = length * width
    total_cost = area * cost_per_sqft
    return area, total_cost

def main():
    print("Welcome to the Material Cost Estimator!")
    
    # Input room dimensions
    length = float(input("Enter the length of the room (in feet): "))
    width = float(input("Enter the width of the room (in feet): "))
    
    # Material options
    materials = {
        1: ("Wood", 8),
        2: ("Concrete", 12),
        3: ("Brick", 10),
        4: ("Tiles", 5)
    }
    
    # Display material options
    print("Available materials:")
    for key, (name, cost) in materials.items():
        print(f"{key}. {name} (${cost}/sq ft)")
    
    # Select material
    choice = int(input("Select a material by entering the corresponding number: "))
    if choice not in materials:
        print("Invalid choice. Please restart the program.")
        return
    
    material_name, cost_per_sqft = materials[choice]
    
    # Calculate and display results
    area, total_cost = calculate_material_cost(length, width, cost_per_sqft)
    print(f"\nSelected Material: {material_name}")
    print(f"Room Area: {area} sq ft")
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
