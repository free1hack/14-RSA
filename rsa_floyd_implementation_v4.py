from collections import defaultdict


# Dictionary to store key pairs and public keys#
key_pairs = defaultdict(list)
num_keys = 2000


def floyd(f, x0):
    # Initialize the tortoise and hare pointers to the starting value 
    tortoise = first_key_pair_content
    tortoise_name = first_key_pair_name
    keyName, hare = f(x0) 
    cycle_length = 0
    floyd_cycle = 0
    cycle = 0

    # Iterate until the pointers meet
    while(True): 
              
        while (tortoise != hare) and (cycle_length <=num_keys-1):
       # while (tortoise != hare) and (keyName!=""):
            
            if keyName==lastlast_key_name:
               # print(keyName)
                break

            keyName, hare = f(keyName)
            cycle_length += 1
            
            #check when we exceed the last elmements. 
            if keyName=="":
                break
   
        if tortoise == hare:
            floyd_cycle = cycle_length
            printCollision(floyd_cycle, tortoise_name, hare, cycle)
       # print(cycle_length)
        cycle_length = 0
       # print(cycle_length)
        tortoise_name, tortoise = f(tortoise_name)
        keyName, hare = f(tortoise_name)   # keyName, hare = f(f(tortoise_name))
        cycle+=1
        print("cycle:{} ".format(cycle))
        
        if(tortoise == last_key_content):
            break

    printCollision(floyd_cycle, tortoise_name, hare, cycle)
   # return floyd_cycle
    

# get the starting key pair and public key
first_key_pair_name="key{}".format(0)
with open("{}.pem".format(first_key_pair_name), "rb") as f:
    first_key_pair_content = f.read()

# get private key by ID
def getKey(id):
    key_name="key{}".format(id)
    with open("{}.pem".format(key_name), "rb") as f:
        key_content = f.read()

    return key_name, key_content

lastlast_key_name, last_key_content=getKey(num_keys-1)

# Read the key pair and public key files
for i in range(num_keys):
    key_name = "key{}".format(i)
    with open("{}.pem".format(key_name), "rb") as f:
        key_pair = f.read()

    public_key_name="{}_public".format(key_name)

    #key_pairs[key_name].append(public_key_name)
    key_pairs[key_name].append(key_pair)



# Function to retrieve the next key pair and public key in the sequence
def next_key(key_pair_name):
    counter = 0
    key_detected = False
    nextKeyContent = ''
    nextKeyName = ''
    for key, value in key_pairs.items():
        
        if key_detected == True:
            nextKeyName = key
            #nextKeyContent = value
            key_detected = False
            break

        if key == key_pair_name:
            key_detected = True

    with open("{}.pem".format(nextKeyName), "rb") as f:
        nextKeyContent = f.read()
    
    return  nextKeyName, nextKeyContent


def printCollision(floyd_cycle, private_key_name, private_key_content, cycle):
    if floyd_cycle > 0:
        print("Collision detected in key pair {}".format(private_key_name))
        floyd_cycle = floyd_cycle+1 
        key_id = floyd_cycle + cycle #to get the exact number for the collision key  
        print("The floyd cycle is:", floyd_cycle)
        collision_key_pair_name="key{}.pem".format(key_id)
        print("Collision detected with the key pair {}".format(collision_key_pair_name))
   
    else:
        print("No collisions detected in the key pairs")


# Run the Floyd algorithm to detect collisions in the key pairs####
#floyd_cycle = floyd(next_key, first_key_pair_name)#
floyd(next_key, first_key_pair_name)#
#name, content = next_key('key2')
#print(name)


