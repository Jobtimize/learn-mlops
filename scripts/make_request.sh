# make a request using the pre defined test instance

curl --request POST \
    --header 'Content-Type: application/json' \
    --data @data/input/test_instance.json \
    --url http://127.0.0.1:8000/predict
