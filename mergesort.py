import csv 

# A class to hold each row of data
class Person: 
  def __init__(self, name, decile_score, priors_count, total_days_in_jail, total_days_in_custody): 
    # TODO: store the name, decile_score, priors_count, total_days_in_jail, and total_days_in_custody as attributes
    self.name = name
    self.decile_score = decile_score
    self.priors_count = priors_count
    self.total_days_in_jail = total_days_in_jail
    self.total_days_in_custody = total_days_in_custody
    # TODO: create a new attribute called new_decile that uses the formula
    # This score represents a simplified model of how likely someone is to reoffend.
    self.new_decile = 0.6 * priors_count + 0.5 * total_days_in_jail + 0.1 * total_days_in_custody
    

# Comparison function: decide if "a" should come before "b"   
def comes_before(a, b, key):
  # TODO: use getattr() to access the attribute given by key
  a_value = getattr(a, key)
  b_value = getattr(b, key)
  # TODO: return True if a should come before b when sorting by 'key'
  # If values are equal, use alphabetical order of names as a tiebreaker
  if a_value == b_value:
    return a.name < b.name
  return a_value < b_value
   

# Merge two sorted halves into one sorted list
def merge(left, right, key): 
  # TODO: implement the standard merge step from merge sort
  result = []
  i = 0
  j = 0
  
  while i < len(left) and j < len(right):
    if comes_before(left[i], right[j], key):
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  
  while i < len(left):
    result.append(left[i])
    i += 1
  
  while j < len(right):
    result.append(right[j])
    j += 1
  
  # Return the merged result
  return result
  

# Recursive merge sort 
def merge_sort(data, key):
  # TODO: implement recursive merge sort
  # Base case: if the list length is <= 1, return it
  if len(data) <= 1:
    return data
  # Recursive case: split the list in half, call merge_sort on each half
  mid = len(data) // 2
  left_half = data[:mid]
  right_half = data[mid:]
  
  left_sorted = merge_sort(left_half, key)
  right_sorted = merge_sort(right_half, key)
  # Merge the two halves using the merge() function and return the result
  return merge(left_sorted, right_sorted, key)


# Load in data from CSV  
def load_data(filename): 
  records = []
  with open(filename, newline='') as csvfile: 
    reader = csv.DictReader(csvfile)
    for row in reader: 
      # TODO: create a Person object using values from the row
      # Make sure to read:
      #   name, decile_score, priors_count, total_days_in_jail, total_days_in_custody
      name = row['name']
      decile_score = int(row['decile_score']) if row['decile_score'] else 0
      priors_count = int(row['priors_count']) if row['priors_count'] else 0
      total_days_in_jail = int(row['total_days_jail']) if row['total_days_jail'] else 0
      total_days_in_custody = int(row['total_days_custody']) if row['total_days_custody'] else 0
      
      person = Person(name, decile_score, priors_count, total_days_in_jail, total_days_in_custody)
      # Append each new Person object to records
      records.append(person)
  # TODO: return the records list
  return records
  


if __name__ == "__main__": 
  # TODO: set filename to the CSV file you were provided
  filename = "COMPAS Data - Sample Data.csv"

  # TODO: load the data from the CSV
  people = load_data(filename)

  # TODO: sort the data twice:
  #   (1) once by "decile_score" from the dataset
  #   (2) once by your computed "new_decile"
  sorted_by_data_decile = merge_sort(people, "decile_score")
  sorted_by_student_decile = merge_sort(people, "new_decile")

  # TODO: print both sorted lists (names and their scores)
  # Example output line:
  # print(person.name, person.decile_score, person.new_decile)
  print("Sorted by original decile score:")
  for person in sorted_by_data_decile:
    print(person.name, person.decile_score, person.new_decile)
  
  print("\nSorted by new decile score:")
  for person in sorted_by_student_decile:
    print(person.name, person.decile_score, person.new_decile)
  
  # TODO: compare the two sorted outputs and briefly comment (IN GOOGLE DOC)
  # on any differences between rankings under the two scoring systems
  pass