send-path:
	curl --location --request POST 'http://127.0.0.1:5000/add_words' \
	--header 'Content-Type: application/json' \
	--data-raw '{"data": "$(path)"}'

send-url:
	curl --location --request POST 'http://127.0.0.1:5000/add_words' \
	--header 'Content-Type: application/json' \
	--data-raw '{"data": "$(url)"}'

send-text:
	curl --location --request POST 'http://127.0.0.1:5000/add_words' \
	--header 'Content-Type: application/json' \
	--data-raw '{"data": "$(text)"}'

count:
	curl --location --request GET 'http://127.0.0.1:5000/count?word=$(word)'

reset-counter:
	curl --location --request POST 'http://127.0.0.1:5000/reset'

count-all:
	curl --location --request GET 'http://127.0.0.1:5000/all-counts'
