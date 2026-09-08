"""
Exercise #2: List Operations
Special Course in Software Engineering 2026

A participant-management program built on two parallel lists
(participants and scores). Implements registration with validation,
search, display, updates, withdrawal, a ranked scoreboard, statistics
and a final report.
"""

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


def qualification(score):
    """Return the qualification label for a score."""
    if score > distinction_score:
        return "DISTINCTION"
    if score > qualification_score:
        return "QUALIFIED"
    return "NOT QUALIFIED"


# ----------------------------------------------------------------------
# 1. Display all current participants with their scores (using zip)
# ----------------------------------------------------------------------
def display_participants():
    """Make sure the lists have the same number of elements, then display
    all the current participants with their scores. Uses zip()."""
    if len(participants) != len(scores):
        print("Error: the participants and scores lists do not have "
              "the same number of elements.")
        return

    print("\n--- Current participants and their scores ---")
    for name, score in zip(participants, scores):
        print(f"  {name}: {score}")


# ----------------------------------------------------------------------
# 2. Register a new participant (with full validation)
# ----------------------------------------------------------------------
def add_participant(name, score):
    """Accept a new participant's name and their score, with validation.

    - Already registered -> error message, do not add.
    - Empty name        -> error "The name cannot be empty.", do not add.
    - Score not a number -> error "The score must be a number.", do not add.
    - Score outside 0-100 -> error "The score must be between 0 and 100.",
                             do not add.
    - Otherwise add to both lists and confirm success.
    """
    # Empty name check
    if name is None or name.strip() == "":
        print("Error: The name cannot be empty.")
        return False

    # Duplicate check (case-insensitive)
    if name.strip().lower() in [p.lower() for p in participants]:
        print(f"Error: {name} is already registered.")
        return False

    # Numeric check
    try:
        score = float(score)
    except (TypeError, ValueError):
        print("Error: The score must be a number.")
        return False

    # Range check
    if score < 0 or score > 100:
        print("Error: The score must be between 0 and 100.")
        return False

    participants.append(name.strip())
    scores.append(score)
    print(f"{name.strip()} has been successfully registered with a score "
          f"of {score}.")
    return True


# ----------------------------------------------------------------------
# 3. Search for a specific participant
# ----------------------------------------------------------------------
def search_participant(name):
    """Search for a participant. If found, display their name, score and
    qualification; otherwise display a not-found message."""
    if name is None or name.strip() == "":
        print("Error: The name cannot be empty.")
        return

    for i, p in enumerate(participants):
        if p.lower() == name.strip().lower():
            print(f"\nParticipant found: {p}, Score: {scores[i]} "
                  f"({qualification(scores[i])})")
            return
    print(f"\nParticipant \"{name}\" was not found.")


# ----------------------------------------------------------------------
# 4. Display every participant with their qualification
# ----------------------------------------------------------------------
def display_all_with_status():
    """Display every participant's name, score, and whether they are
    qualified or not."""
    print("\n--- All participants and their qualifications ---")
    for name, score in zip(participants, scores):
        print(f"  {name}: {score} - {qualification(score)}")


# ----------------------------------------------------------------------
# 5. Overall checks: any distinction? everyone passed?
# ----------------------------------------------------------------------
def check_overall():
    """Find if there is at least one participant with a distinction, and
    whether all participants have passed (scored 50 or more)."""
    has_distinction = any(s > distinction_score for s in scores)
    all_passed = all(s >= 50 for s in scores)
    print("\n--- Overall checks ---")
    print(f"  At least one participant has a distinction: {has_distinction}")
    print(f"  All participants have passed (scored 50 or more): {all_passed}")


# ----------------------------------------------------------------------
# 6. Update a participant's score
# ----------------------------------------------------------------------
def update_score(name, new_score):
    """Update a participant's score. The participant must exist and the
    new score must be a valid number between 0 and 100."""
    if name is None or name.strip() == "":
        print("Error: The name cannot be empty.")
        return False

    # Numeric check
    try:
        new_score = float(new_score)
    except (TypeError, ValueError):
        print("Error: The score must be a number.")
        return False

    # Range check
    if new_score < 0 or new_score > 100:
        print("Error: The score must be between 0 and 100.")
        return False

    for i, p in enumerate(participants):
        if p.lower() == name.strip().lower():
            old_score = scores[i]
            scores[i] = new_score
            print(f"{p}'s score has been updated from {old_score} to "
                  f"{new_score}.")
            return True

    print(f"Error: Participant \"{name}\" was not found.")
    return False


# ----------------------------------------------------------------------
# 7. Withdraw (remove) a participant
# ----------------------------------------------------------------------
def withdraw_participant(name):
    """Remove a participant from the list; make sure the score for that
    specific participant is also removed from the scores list."""
    if name is None or name.strip() == "":
        print("Error: The name cannot be empty.")
        return False

    for i, p in enumerate(participants):
        if p.lower() == name.strip().lower():
            removed_name = participants.pop(i)
            removed_score = scores.pop(i)
            print(f"{removed_name} (score: {removed_score}) has been "
                  f"withdrawn.")
            return True

    print(f"Error: Participant \"{name}\" was not found.")
    return False


# ----------------------------------------------------------------------
# 8. Scoreboard (descending order with ranks)
# ----------------------------------------------------------------------
def show_scoreboard():
    """Create and display a scoreboard where all the participants and
    their scores are displayed in descending order, with their rank."""
    print("\n--- Scoreboard (descending order) ---")
    ranked = sorted(zip(participants, scores), key=lambda x: x[1],
                    reverse=True)
    for rank, (name, score) in enumerate(ranked, start=1):
        print(f"  Rank {rank}: {name} - {score}")


# ----------------------------------------------------------------------
# 9. Statistics
# ----------------------------------------------------------------------
def calculate_statistics():
    """Calculate and display:
    - the highest, lowest and average score;
    - how many participants have the highest and the lowest score;
    - how many have distinctions, how many are qualified and how many
      are not qualified."""
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    num_highest = scores.count(highest)
    num_lowest = scores.count(lowest)

    num_distinction = sum(1 for s in scores if s > distinction_score)
    num_qualified = sum(1 for s in scores
                        if qualification_score < s <= distinction_score)
    num_not_qualified = sum(1 for s in scores if s <= qualification_score)

    print("\n--- Statistics ---")
    print(f"  Highest score: {highest}")
    print(f"  Lowest score: {lowest}")
    print(f"  Average score: {average:.2f}")
    print(f"  Participants with the highest score ({highest}): "
          f"{num_highest}")
    print(f"  Participants with the lowest score ({lowest}): {num_lowest}")
    print(f"  Participants with DISTINCTION (> {distinction_score}): "
          f"{num_distinction}")
    print(f"  Participants QUALIFIED (> {qualification_score} "
          f"and <= {distinction_score}): {num_qualified}")
    print(f"  Participants NOT QUALIFIED (<= {qualification_score}): "
          f"{num_not_qualified}")

    return {
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "num_highest": num_highest,
        "num_lowest": num_lowest,
        "num_distinction": num_distinction,
        "num_qualified": num_qualified,
        "num_not_qualified": num_not_qualified,
    }


# ----------------------------------------------------------------------
# 10. Final report
# ----------------------------------------------------------------------
def final_report():
    """Generate a final report that displays the participant name, their
    rank, their score, and their qualification, followed by all the
    statistics calculated above."""
    print("\n" + "=" * 50)
    print("FINAL REPORT")
    print("=" * 50)

    ranked = sorted(zip(participants, scores), key=lambda x: x[1],
                    reverse=True)
    print(f"\n{'Rank':<6}{'Participant':<22}{'Score':<8}{'Qualification'}")
    print("-" * 50)
    for rank, (name, score) in enumerate(ranked, start=1):
        print(f"{rank:<6}{name:<22}{score:<8.2f}{qualification(score)}")

    stats = calculate_statistics()
    print("\n--- Statistics summary ---")
    for key, value in stats.items():
        print(f"  {key}: {value}")


# ----------------------------------------------------------------------
# Main demonstration
# ----------------------------------------------------------------------
def main():
    print("Exercise #2: List Operations")
    print("=" * 50)

    display_participants()

    print("\n--- Registering new participants ---")
    add_participant("Alice Wong", 88)          # duplicate -> rejected
    add_participant("", 85)                    # empty name -> rejected
    add_participant("Mia Chen", "not a number")  # invalid score -> rejected
    add_participant("Mia Chen", 150)           # out of range -> rejected
    add_participant("Mia Chen", 85)            # valid -> added

    print("\n--- Searching for participants ---")
    search_participant("hana lee")             # found (case-insensitive)
    search_participant("Nobody")               # not found

    display_all_with_status()
    check_overall()

    print("\n--- Updating a score ---")
    update_score("George Smith", 42)           # valid update
    update_score("Nobody", 80)                 # not found

    print("\n--- Withdrawing a participant ---")
    withdraw_participant("George Scott")       # removed from both lists
    withdraw_participant("Nobody")             # not found

    show_scoreboard()
    final_report()


if __name__ == "__main__":
    main()
