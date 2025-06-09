#This will be the main body of the helper funciton

print(f'helper files __name__ is : {__name__}')

# Let's write a funciton which we can use in any other file
def using_helper():
    print("You are using the helper file")

# This __name__ helps to create test cases for the fucntions created above
# Once this helper file is importe in another code, then instead of "__main__", the name in that code would become helper_file
# Consider this as a scratchpad or testing zone
if __name__ == "__main__":
    print("helper file is running directly using the helper file")
else :
    print("helper file is running as an imported fuction")

'''
Also note that when we run the helper file in the main file
this will create an pyc file for faster execution
'''