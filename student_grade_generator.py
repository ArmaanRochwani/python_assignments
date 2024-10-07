def main():
    while True:
        # Ask the user for the number of components (e.g., assignments, exams, etc.)
        user_input = input("Enter your Name: ")
        number_of_components = int(input("Enter the number of components (e.g., assignment, exam, project): "))

        # Lists to store component names, weights, and scores
        components = []
        weights = []
        scores = []

        # Collect component names and weights from the user
        total_weight = 0
        for i in range(number_of_components):
            component_name = input(f"Enter the name of component {i + 1}: ")
            components.append(component_name)
            weight = collect_weight(component_name)
            weights.append(weight)
            total_weight += weight

        # Ensure the total weight is exactly 100%
        while total_weight != 100:
            print("The total weight must be exactly 100%. Please re-enter the weights.")
            total_weight = 0
            for i in range(number_of_components):
                weight = collect_weight(components[i])
                weights[i] = weight
                total_weight += weight

        # Collect scores for each component
        for i in range(number_of_components):
            score = collect_multiple_scores(components[i])
            scores.append(score)

        # Calculate the final weighted average score
        weighted_average = 0
        for i in range(number_of_components):
            weighted_average += scores[i] * weights[i] / 100

        # Determine the final letter grade
        final_grade = determine_final_grade(weighted_average)

        # Display the results
        print("Name:", user_input)
        print(f"Your Final Weighted Average is: {weighted_average:.2f}%")
        print(f"Your Final Grade is: {final_grade}")

        # Ask if the user wants to enter another student's scores
        continue_input = input("Do you want to enter scores for another student? (yes/no): ").strip().lower()
        if continue_input != "yes":
            print("program executed successfully")
            break


# This function collects the weight for a specific component
def collect_weight(component):
    weight = float(input(f"Enter the weight for {component} (0-100): "))
    while weight < 0 or weight > 100:
        weight = float(input("Invalid weight. Please enter a value between 0 and 100: "))
    return weight


# This function collects multiple scores (for assignments or projects)
def collect_multiple_scores(component):
    total_score = 0
    total_max_marks = 0
    number_of_scores = int(input(f"How many {component} entries do you have? "))

    for i in range(number_of_scores):
        score = float(input(f"Enter score for {component} {i + 1}: "))
        max_marks = float(input(f"Enter maximum marks for this {component}: "))

        while score < 0 or score > max_marks:
            score = float(input(f"Invalid score. Please enter a score between 0 and {max_marks}: "))

        total_score += score
        total_max_marks += max_marks

    return (total_score / total_max_marks) * 100


# This function determines the final grade based on the weighted average
def determine_final_grade(weighted_average):
    if weighted_average >= 90:
        return 'A'
    elif weighted_average >= 80:
        return 'B'
    elif weighted_average >= 65:
        return 'C'
    elif weighted_average >= 50:
        return 'D'
    else:
        return 'F'


if __name__ == "__main__":
    main()
