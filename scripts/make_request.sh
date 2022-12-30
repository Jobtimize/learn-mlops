# make a request using the pre defined test instance

curl --request POST \
    --header 'Content-Type: application/json' \
    --data @data/input/test_instance.json \
    --url http://0.0.0.0:8000/predict
