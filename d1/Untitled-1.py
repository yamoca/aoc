# chat gpt is shit

# Example usage:
#input_str = "1234seven"
#output_str = extract_numbers(input_str)
#rint(output_str)
def recursive_function(limit, current_count=0):
    # Base case: stop recursion when the limit is reached
    if current_count >= limit:
        return
    
    # Your recursive logic here
    print(current_count) 
    # Make the recursive call with updated count
    recursive_function(limit, current_count + 1)

# Example usage: Call the function recursively only 3 times
# recursive_function(3)

def logic2(limit, current_count=0):
    # Your logic for the second function
    print("deez logic 2") 
    # Call recursive_function from within logic2
    recursive_function1(limit, current_count + 1)

def recursive_function1(limit, current_count=0):
    # Base case: stop recursion when the limit is reached
    if current_count >= limit:
        return
    
    # Your recursive logic here
    print("recursive function") 
    # Call logic2 from within recursive_function
    logic2(limit, current_count + 1)
    
    # Make the recursive call with updated count
    recursive_function1(limit, current_count + 1)

# Example usage: Start by calling logic2, and the sequence will continue
logic2(3)