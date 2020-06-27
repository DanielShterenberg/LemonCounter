# LemonCounter

A word counter application which:
1. Receives a text input and counts the number of appearances for each word in the input.
The endpoint should be able to accept the input in 3 ways:  
A simple string sent in the request.  
A file path (the contents of the file will be used as input).  
A URL (the data returned from the URL will be used as input).

2.  A 'word statistics' endpoint. The endpoint receives a word and returns the number of times the word appeared so far (in all previous calls)



## How to use:
In the attached project, you can find a makefile which contains 6 commands.  
`make path="<path>" send-path` sending a POST request to our service with a path to local file.  
For example you can try `make path="./mynameis.txt" send-path`.  

`make url="<url>" send-url` sending a POST request to our service with a url of a .txt file.   
For example you can try `make url="http://textfiles.com/adventure/aencounter.txt" send-url`.  

`make text="<text>" send-text` sending a POST request to our service with a string which we want to process.   
For example you can try `make text="Hi! My name is (what?), my name is (who?), my name is Slim Shady" send-text`.  

`make word="<word>" count` sending a GET request to our service and returns the number of times `<word>` appeared so far.  
For example you can try `make word="Shady" count`.  

`make reset-counter` sending a POST request which resets our counters.  

`make count-all` sending a GET request to our service and receives back the full counter-map.


 
--- 
### remarks:
-  We are using the maximal amount of cores to process the file.
If you would like to change it, you can find the function `get_number_of_cores_to_use` under `conf.py` file.




### Local benchmark tests:

File size: ~225MB  
Number of processes: 10  
Average job time: 19.5 sec.

File Size: ~700MB.  
Number of processes: 10.  
Average job time: 55 sec.
