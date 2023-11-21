def find_longest_path(acts, preds, durs):
    # store the maximum duration and longest duration for each activity
    max_duration = {}
    longest_path = {}

    for activity in acts:
        # find the maximum duration and predecessor for each activity
        if activity in preds:
            max_duration[activity] = durs[activity] + max(max_duration.get(pred, 0) for pred in preds[activity])
        else:
            max_duration[activity] = durs[activity]

        # update longest path
        if not longest_path or max_duration[activity] > max_duration[longest_path[0]]:
            longest_path = [activity]
        elif max_duration[activity] == max_duration[longest_path[0]]:
            longest_path.append(activity)

    return longest_path

# prompt for actitivities, durations, and predecessors
acts = {}
preds = {}
durs = {}

while True:
    activity = input("Enter activity (or 'done' to finish): ")
    if activity == "done":
        break

    duration = int(input("Enter duration: "))
    predecessors = input("Enter predecessors (comma-separated): ").split(",")

    acts[activity] = activity
    durs[activity] = duration
    preds[activity] = predecessors

# find longest path
longest_path = find_longest_path(acts, preds, durs)
print("Longest path:", longest_path)

# output -->
    # Enter activity (or 'done' to finish): 25
    # Enter duration: 64
    # Enter predecessors (comma-separated): 12,17 
    # Enter activity (or 'done' to finish): done
    # Longest path: ['25']