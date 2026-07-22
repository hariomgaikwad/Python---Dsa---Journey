# Exercise 3: Slice list into 3 equal chunks and reverse each chunk

# Logic
# Find the size of each chunk using len(list) // 3.
# Slice the list into 3 equal parts.
# Reverse each chunk using reverse().
# Print the original and reversed chunk.

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size = len(sample_list) // 3

for i in range(0, len(sample_list), chunk_size):
    chunk = sample_list[i:i + chunk_size]
    print("Chunk", (i // chunk_size) + 1, chunk)

    chunk.reverse()
    print("After reversing it", chunk)