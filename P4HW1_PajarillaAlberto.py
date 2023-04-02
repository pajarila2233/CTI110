# CTI-110
# P4HW1 - Score List
# Alberto Pajarilla
# 2 April 2023

# Ask the user for the number of scores they want to enter
num_scores = int(input('How many scores do you want to enter? '))
print()

# Initialize an empty list to store the scores
scores = []

# Loop through the number of scores the user wants to enter
for i in range(num_scores):
    
    # Ask the user for a score
    score = int(input('Enter score #{}: '.format(i+1)))
    
    # Check if the score is valid
    while score < 0 or score > 100:
        print()
        print('INVALID Score entered!!!! ')
        print('Score should be between 0 and 100 ')
        score = int(input('Enter score #{} again: '.format(i+1)))
    
    # Add the score to the list
    scores.append(score)

# Find the lowest score
lowest_score = min(scores)

# Remove the lowest score from the list
scores.remove(lowest_score)

# Calculate the average of the scores
average_score = sum(scores) / len(scores)

# Determine the letter grade for the average score
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the lowest score, modified score list, average score, and letter grade
print()
print('--------------Results-------------------')
print('Lowest Score  : {:.1f}'.format(lowest_score))
print('Modified List : {}'.format(scores))
print('Scores Average: {:.2f}'.format(average_score))
print('Grade         : {}'.format(letter_grade))
print('----------------------------------------')

