"""
activity selection problem using greedy algorithm

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for storing selected activities
"""


def activity_selection(activities):
    """
    Select the maximum number of non-overlapping activities.
    
    This function uses a greedy approach: always select the activity
    that finishes earliest, as it leaves the most room for subsequent
    activities.
    
    Args:
        activities (list): List of tuples (start_time, end_time)
    
    Returns:
        list: List of selected non-overlapping activities
    
    Example:
        >>> activity_selection([(1, 3), (2, 5), (4, 7), (6, 9)])
        [(1, 3), (4, 7)]
    
    Time Complexity: O(n log n) - dominated by sorting
    Space Complexity: O(n) - for storing the result
    """
    # Handle edge case: empty list
    if not activities:
        return []
    
    # Sort activities by finish time (greedy choice)
    # The activity that finishes first leaves maximum time for others
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # Always select the first activity (earliest finish time)
    selected = [sorted_activities[0]]
    last_finish_time = sorted_activities[0][1]
    
    # Iterate through remaining activities
    for i in range(1, len(sorted_activities)):
        start_time, finish_time = sorted_activities[i]
        
        # If current activity starts after or when the last selected ends
        # it doesn't overlap, so we can select it
        if start_time >= last_finish_time:
            selected.append(sorted_activities[i])
            last_finish_time = finish_time
    
    return selected


def activity_selection_with_indices(activities):
    """
    Variant that returns indices of selected activities.
    
    Useful when you need to know which activities from the original
    list were selected.
    
    Args:
        activities (list): List of tuples (start_time, end_time)
    
    Returns:
        list: Indices of selected activities from original list
    """
    if not activities:
        return []
    
    # Create list of (activity, original_index) pairs
    indexed_activities = [(act, i) for i, act in enumerate(activities)]
    
    # Sort by finish time
    indexed_activities.sort(key=lambda x: x[0][1])
    
    selected_indices = [indexed_activities[0][1]]
    last_finish = indexed_activities[0][0][1]
    
    for (start, end), idx in indexed_activities[1:]:
        if start >= last_finish:
            selected_indices.append(idx)
            last_finish = end
    
    return sorted(selected_indices)


def main():
    """Demonstrate activity selection with multiple examples"""
    
    print("=" * 60)
    print("ACTIVITY SELECTION PROBLEM - GREEDY ALGORITHM")
    print("=" * 60)
    
    # Example 1: Basic case
    print("\nExample 1: Basic Activity Selection")
    activities1 = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(f"Activities (start, end): {activities1}")
    selected1 = activity_selection(activities1)
    print(f"Selected activities: {selected1}")
    print(f"Maximum activities: {len(selected1)}")
    
    # Example 2: All activities overlap
    print("\nExample 2: All Overlapping Activities")
    activities2 = [(1, 5), (2, 6), (3, 7), (4, 8)]
    print(f"Activities (start, end): {activities2}")
    selected2 = activity_selection(activities2)
    print(f"Selected activities: {selected2}")
    print(f"Maximum activities: {len(selected2)}")
    
    # Example 3: No overlaps
    print("\nExample 3: No Overlapping Activities")
    activities3 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print(f"Activities (start, end): {activities3}")
    selected3 = activity_selection(activities3)
    print(f"Selected activities: {selected3}")
    print(f"Maximum activities: {len(selected3)}")
    
    # Example 4: Real-world scenario (conference sessions)
    print("\nExample 4: Conference Sessions")
    sessions = [
        (9, 10),   # Session A: 9-10 AM
        (9.5, 11), # Session B: 9:30-11 AM
        (10, 12),  # Session C: 10-12 PM
        (11, 13),  # Session D: 11 AM-1 PM
        (12, 14)   # Session E: 12-2 PM
    ]
    print("Conference sessions (hours):")
    labels = ['A', 'B', 'C', 'D', 'E']
    for i, (start, end) in enumerate(sessions):
        print(f"  Session {labels[i]}: {start:g}-{end:g}")
    
    selected4 = activity_selection(sessions)
    print(f"\nOptimal schedule: {selected4}")
    print(f"Can attend {len(selected4)} sessions")
    
    # Example 5: Single activity
    print("\nExample 5: Edge Case - Single Activity")
    activities5 = [(5, 10)]
    print(f"Activities: {activities5}")
    selected5 = activity_selection(activities5)
    print(f"Selected: {selected5}")
    
    # Example 6: Empty list
    print("\nExample 6: Edge Case - Empty List")
    activities6 = []
    print(f"Activities: {activities6}")
    selected6 = activity_selection(activities6)
    print(f"Selected: {selected6}")
    
    # Example 7: Using index variant
    print("\nExample 7: Getting Original Indices")
    activities7 = [(2, 5), (1, 3), (4, 7), (6, 9)]
    print(f"Activities: {activities7}")
    indices = activity_selection_with_indices(activities7)
    print(f"Selected activity indices: {indices}")
    print(f"Selected activities: {[activities7[i] for i in indices]}")
    
    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("Time Complexity: O(n log n) - dominated by sorting")
    print("Space Complexity: O(n) - storing selected activities")
    print("Greedy Choice: Always pick activity with earliest finish time")
    print("=" * 60)


if __name__ == "__main__":
    main()
