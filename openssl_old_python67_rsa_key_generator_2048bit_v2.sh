#!/bin/bash

# Set the number of keys to generate
num_keys=1000000

# Set the output log file
log_file="key_generation.log"

# Start a timer
start=$(date +%s)

# Generate the keys
for i in $(seq 1 $num_keys); do
  # Generate a private key
  openssl genrsa -out "key_$i.pem" 2048 &> /dev/null

  # Generate a public key from the private key
  openssl rsa -in "key_$i.pem" -pubout -out "key_$i.pub" &> /dev/null

  # Record the key pair in the log file
  echo "Generated key pair $i" >> $log_file
done

# Stop the timer
end=$(date +%s)

# Calculate the time taken
time_taken=$((end - start))

# Record the time taken in the log file
echo "Time taken: $time_taken seconds" >> $log_file
