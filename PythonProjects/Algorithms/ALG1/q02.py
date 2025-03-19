import sys

def selection_sort(sequence):
    """Perform a simple selection sort to sort the sequence in nondecreasing order."""
    n = len(sequence)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sequence[j] < sequence[min_index]:
                min_index = j
        # Swap the minimum element with the current element
        sequence[i], sequence[min_index] = sequence[min_index], sequence[i]
        print(f"Swapped {sequence[i]} with {sequence[min_index]}: {sequence}")
    return sequence

def main():
    # Read the sequence of numbers from standard input
    sequence = []
    for line in sys.stdin:
        try:
            num = int(line.strip())
            sequence.append(num)
        except ValueError:
            print(f"Invalid input: {line.strip()}. Only integers are allowed.", file=sys.stderr)

    # Print the original sequence
    print("Original sequence:", sequence)

    # Perform sorting
    sorted_sequence = selection_sort(sequence)

    # Print the sorted sequence
    print("Sorted sequence:", sorted_sequence)

if __name__ == "__main__":
    main()
