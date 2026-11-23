def book_seat(classes, members, class_id, member_id):
    if class_id not in classes:
        return "Error: Class ID not found."
    if member_id not in members:
        return "Error: Member ID not found."

    fitness_class = classes[class_id]

    # Prevent duplicate booking
    if member_id in fitness_class["confirmed"]:
        return f"{members[member_id]} is already confirmed for {fitness_class['title']}."
    if member_id in fitness_class["waitlist"]:
        return f"{members[member_id]} is already on the waitlist for {fitness_class['title']}."

    # Check capacity vs waitlist
    if len(fitness_class["confirmed"]) < fitness_class["capacity"]:
        fitness_class["confirmed"].append(member_id)
        return f"Confirmed! {members[member_id]} booked into {fitness_class['title']}."
    else:
        fitness_class["waitlist"].append(member_id)
        position = len(fitness_class["waitlist"])
        return f"Class full! {members[member_id]} added to waitlist at position #{position}."


def cancel_booking(classes, members, class_id, member_id):
    if class_id not in classes:
        return "Error: Class ID not found."
    if member_id not in members:
        return "Error: Member ID not found."

    fitness_class = classes[class_id]

    # Case 1: Member is in the confirmed list
    if member_id in fitness_class["confirmed"]:
        fitness_class["confirmed"].remove(member_id)
        message = f"Cancelled confirmed seat for {members[member_id]}."

        # Automatic Waitlist Promotion (FIFO - index 0)
        if len(fitness_class["waitlist"]) > 0:
            promoted_id = fitness_class["waitlist"].pop(0)
            fitness_class["confirmed"].append(promoted_id)
            message += f" Promoted {members[promoted_id]} from waitlist to confirmed!"

        return message

    # Case 2: Member is on the waitlist
    elif member_id in fitness_class["waitlist"]:
        fitness_class["waitlist"].remove(member_id)
        return f"Removed {members[member_id]} from the waitlist."

    # Case 3: Member had no booking
    else:
        return f"{members[member_id]} does not have a booking in {fitness_class['title']}."