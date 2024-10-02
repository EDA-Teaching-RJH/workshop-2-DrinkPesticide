#Take user input, replace whitespace with ...
# print result
def main():
    slow = input("Input ")
    print(replace(slow))

def replace(text):  
    text = text.replace(' ', '...')
    return text 
  #Your code goes here.

main()
