participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]
scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]
qualification_score = 70
distinction_score = 90


# Helper: convert input to int (or float) if possible; return None if not a number
def parse_score(score_input):
    try:
        return int(score_input)
    except ValueError:
        try:
            return float(score_input)
        except ValueError:
            return None


# Make sure the lists have the same number of elements
if len(participants) != len(scores):
    print("Error: Participants and scores lists have different lengths!")
else:
    print("Lists are properly aligned.")
# First, display all the current participants with their scores. Use zip()
print("\n" + "="*50)
print("CURRENT PARTICIPANTS AND SCORES")
print("="*50)
for name, score in zip(participants, scores):
    print(f"{name}: {score}")
print("="*50)
# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.
print("\n" + "="*50)
print("ADD NEW PARTICIPANT")
print("="*50)
new_name = input("Enter participant name: ").strip()
new_score_input = input("Enter participant score: ").strip()
# Check if name is empty
if new_name == "":
    print("Error: Name cannot be empty!")
else:
    # Check if participant already exists (case-insensitive check)
    name_exists = False
    for existing_name in participants:
        if existing_name.lower() == new_name.lower():
            name_exists = True
            break
    
    if name_exists:
        print(f"Error: {new_name} is already registered!")
    else:
        # Check if score is a number
        new_score = parse_score(new_score_input)
        
        if new_score is None:
            print("Error: Score must be a number!")
        elif new_score < 0 or new_score > 100:
            print("Error: Score must be between 0 and 100!")
        else:
            # Add the new participant
            participants.append(new_name)
            scores.append(new_score)
            print(f"Successfully registered {new_name} with score {new_score}!")
            
            # Display updated list
            print("\nUpdated participants:")
            for name, score in zip(participants, scores):
                print(f"{name}: {score}")
# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.
print("\n" + "="*50)
print("SEARCH PARTICIPANT")
print("="*50)
search_name = input("Enter participant name to search: ").strip()
found = False
for i, name in enumerate(participants):
    if name.lower() == search_name.lower():
        score = scores[i]
        print(f"\nParticipant found!")
        print(f"Name: {name}")
        print(f"Score: {score}")
        
        if score > distinction_score:
            print("Status: DISTINCTION")
        elif score > qualification_score:
            print("Status: QUALIFIED")
        else:
            print("Status: NOT QUALIFIED")
        
        found = True
        break
if not found:
    print(f"Error: {search_name} not found!")
# Display every participant's name, score, and whether they are qualified or not.
print("\n" + "="*50)
print("ALL PARTICIPANTS - QUALIFICATION STATUS")
print("="*50)
for name, score in zip(participants, scores):
    if score > distinction_score:
        status = "DISTINCTION"
    elif score > qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f"{name}: {score} - {status}")
print("="*50)
# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).
print("\n" + "="*50)
print("CHECK DISTINCTIONS AND PASSING")
print("="*50)
has_distinction = False
all_passed = True
for score in scores:
    if score > distinction_score:
        has_distinction = True
    if score < 50:
        all_passed = False
if has_distinction:
    print("✓ There is at least one participant with a DISTINCTION!")
else:
    print("✗ No participant has a DISTINCTION.")
if all_passed:
    print("✓ All participants have PASSED (scored 50 or more)!")
else:
    print("✗ Not all participants have passed.")
print("="*50)
# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.
print("\n" + "="*50)
print("UPDATE PARTICIPANT SCORE")
print("="*50)
update_name = input("Enter participant name to update: ").strip()
found = False
for i, name in enumerate(participants):
    if name.lower() == update_name.lower():
        found = True
        print(f"Current score for {name}: {scores[i]}")
        new_score_input = input("Enter new score: ").strip()
        
        new_score = parse_score(new_score_input)
        if new_score is None:
            print("Error: Score must be a number!")
        elif new_score < 0 or new_score > 100:
            print("Error: Score must be between 0 and 100!")
        else:
            scores[i] = new_score
            print(f"Successfully updated {name}'s score to {new_score}!")
        break
if not found:
    print(f"Error: {update_name} not found!")
# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list
print("\n" + "="*50)
print("WITHDRAW PARTICIPANT")
print("="*50)
remove_name = input("Enter participant name to remove: ").strip()
found = False
for i, name in enumerate(participants):
    if name.lower() == remove_name.lower():
        # Remove from both lists at the same index
        removed_name = participants.pop(i)
        removed_score = scores.pop(i)
        print(f"Successfully removed {removed_name} with score {removed_score}!")
        found = True
        break
if not found:
    print(f"Error: {remove_name} not found!")
# Display updated list after removal
print("\nUpdated participants list:")
for name, score in zip(participants, scores):
    print(f"{name}: {score}")
# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score
print("\n" + "="*50)
print("SCOREBOARD (Descending Order)")
print("="*50)
# Sort by score descending; names keep their original order when scores tie
scoreboard = sorted(zip(participants, scores), key=lambda item: item[1], reverse=True)
print(f"{'Rank':<6} {'Participant':<20} {'Score':<6}")
print("-"*32)
for rank, (name, score) in enumerate(scoreboard, start=1):
    print(f"{rank:<6} {name:<20} {score:<6}")
print("="*50)
# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified
print("\n" + "="*50)
print("STATISTICS")
print("="*50)
if scores:
    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)
    
    # Count participants with highest and lowest scores
    num_highest = scores.count(highest_score)
    num_lowest = scores.count(lowest_score)
    
    # Count qualifications
    num_distinction = 0
    num_qualified = 0
    num_not_qualified = 0
    
    for score in scores:
        if score > distinction_score:
            num_distinction += 1
        elif score > qualification_score:
            num_qualified += 1
        else:
            num_not_qualified += 1
    
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Average Score: {average_score:.2f}")
    print(f"\nParticipants with Highest Score: {num_highest}")
    print(f"Participants with Lowest Score: {num_lowest}")
    print(f"\nDISTINCTION (> {distinction_score}): {num_distinction}")
    print(f"QUALIFIED (> {qualification_score}): {num_qualified}")
    print(f"NOT QUALIFIED: {num_not_qualified}")
else:
    # Define defaults so the final report below never breaks on an empty list
    highest_score = 0
    lowest_score = 0
    average_score = 0.0
    num_highest = 0
    num_lowest = 0
    num_distinction = 0
    num_qualified = 0
    num_not_qualified = 0
    print("No participants to calculate statistics.")
print("="*50)
# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also display all the statistics you calculated above
print("\n" + "="*60)
print("FINAL REPORT")
print("="*60)
# Sort by score descending for ranking
scoreboard = sorted(zip(participants, scores), key=lambda item: item[1], reverse=True)
print(f"\n{'Rank':<6} {'Participant':<22} {'Score':<8} {'Status':<15}")
print("-"*60)
for rank, (name, score) in enumerate(scoreboard, start=1):
    if score > distinction_score:
        status = "DISTINCTION"
    elif score > qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f"{rank:<6} {name:<22} {score:<8} {status:<15}")
print("\n" + "="*60)
print("STATISTICS SUMMARY")
print("="*60)
print(f"Total Participants: {len(participants)}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Average Score: {average_score:.2f}")
print(f"Participants with Highest Score: {num_highest}")
print(f"Participants with Lowest Score: {num_lowest}")
print(f"Distinctions: {num_distinction}")
print(f"Qualified: {num_qualified}")
print(f"Not Qualified: {num_not_qualified}")
print("="*60)
