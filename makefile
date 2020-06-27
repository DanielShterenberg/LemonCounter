send-path:
	curl --location --request POST 'http://127.0.0.1:5000/add_words' \
	--header 'Content-Type: application/json' \
	--data-raw '{"data": "./mynameis.txt"}'

send-string:
	curl --location --request POST 'http://127.0.0.1:5000/add_words' \
	--header 'Content-Type: application/json' \
	--data-raw '{"data": "Hi! My name is (what?), my name is (who?), my name is sliky Slim Shady"}'

send-url:
	curl --location --request POST 'http://127.0.0.1:5000/add_words' \
	--header 'Content-Type: application/json' \
	--data-raw '{"data": "http://textfiles.com/adventure/aencounter.txt"}'

count:
	curl --location --request GET 'http://127.0.0.1:5000/count?word=$(word)'

reset-counter:
	curl --location --request POST 'http://127.0.0.1:5000/reset'

get-all-counts:
	curl --location --request GET 'http://127.0.0.1:5000/all-counts'
