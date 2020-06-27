# This program is to convert given seconds into H:M:S format

# Function definition to get time format

def sec(s):
    
    H = s // 3600 # convert seconds to hour
    
    M = (s - H * 3600 ) // 60 # converts seconds to minutes removing sec of hour
    
    S =(s - H * 3600 - M * 60)  # give balance seconds removing minutes and hour
    
    print("\n Time taken in std format ",end="")
    
    print(H, M, S, sep=":")
    
    
# Function definition to convert time format to seconds
    
def time(h, m = 0, s = 0):
    
    print("\n Time in seconds is ",end="")
    
    print(h * 3600 + m * 60 + s)
    
    
# Function call to convert time format to seconds
    
time(1,56,40)
    
# Function call to get time format
    
sec(7000)
    