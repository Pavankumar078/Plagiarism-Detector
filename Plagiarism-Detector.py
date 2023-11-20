def compare_files(file1, file2):
    try:
      with open(file1, 'r') as f1, open(file2, 'r') as f2:
      	words2 = f2.read().split()
      	words1 = f1.read().split()
      	length_1 = len(words1)
      	length_2 = len(words2)
      	min_length = min(length_1, length_2)
      	match_count = 0
      	for i in range(min_length):
      	 word1 = words1[i].lower()
      	 word2 = words2[i].lower()
      	 if word1 == word2: match_count += 1
      	return match_count, length_1
    except UnboundLocalError: print(f"Error reading file: {file1}")
    except UnicodeDecodeError: print(f"Error reading file: {file1}")
    except IOError: print(f"Error reading file: {file1}")
      	
      
    

# Usage example
file1 = 'file1.txt'
file2 = 'file2.txt'

match_count, total_words = compare_files(file1, file2)
print("Matched words:", match_count)
print("Total words:", total_words)
print('% mismatch: ', round(match_count/total_words,2))

