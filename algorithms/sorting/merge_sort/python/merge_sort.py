def merge_sort(arr):
    """Return a new list with the elements of ``arr`` sorted in ascending order."""
    if arr is None:
        return None
    if len(arr) <= 1:
        return list(arr)

    def _merge(left, right):
        i = j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)
