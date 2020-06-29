# LemonCounter

A word counter application which:
1. Receives a text input and counts the number of appearances for each word in the input.
The endpoint should be able to accept the input in 3 ways:  
A simple string sent in the request.  
A file path (the contents of the file will be used as input).  
A URL (the data returned from the URL will be used as input).

2.  A 'word statistics' endpoint. The endpoint receives a word and returns the number of times the word appeared so far 
(in all previous calls).


## Implementation
The task was implemented using the Flask framework, and it did not involve any DBs.In order to store the counters, 
I simply used a dictionary (which of course can be improved by using Redis for instance).  
In order to process large files, I split the file into several chunks and processed each chunk with a different process.

## How to use:
After you run the project, you can use the makefile in order to send requests to the service, or alternatively, 
you can use the attached postman collection.

- In case you would prefer to work with postman, you can import the `Lemonade.postman_collection.json` file. 

- In the makefile, we have 6 commands:  
  
    `make path="<path>" send-path` sending a POST request to our service with a path to local file.  
    For example you can try `make path="./mynameis.txt" send-path`.  
    
    `make url="<url>" send-url` sending a POST request to our service with a url of a .txt file.   
    For example you can try `make url="http://textfiles.com/adventure/aencounter.txt" send-url`.  
    
    `make text="<text>" send-text` sending a POST request to our service with a string which we want to process.   
    For example you can try `make text="Hi! My name is (what?), my name is (who?), my name is Slim Shady" send-text`.  
    
    `make word="<word>" count` sending a GET request to our service and returns the number of times `<word>` appeared so
     far.  
    For example you can try `make word="Shady" count`.  
    
    `make reset-counter` sending a POST request which resets our counters.  
    
    `make count-all` sending a GET request to our service and receives back the full counter-map.

 

 
--- 
### remarks:
-  We are using the maximal amount of cores to process the file.
If you would like to change it, you can find the function `get_number_of_cores_to_use` under `conf.py` file.
- The `CHUNK_SIZE` is set to 4MB at the moment.  
- I assume the file data.pkl exists. I experienced some issues with creating it on server starts (when not existing) and didn't want to keep wasting time on this.

### Local benchmark tests:

Paths:  
File size: ~225MB  
Number of processes: 10  
Average job time: 19.5 sec.

File Size: ~700MB.  
Number of processes: 10.  
Average job time: 55 sec.

URLs:   
link: "http://norvig.com/big.txt"  
Average job time: 19 sec.


