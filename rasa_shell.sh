rasa shell -vv \
    --model labs/lab3rasa/models \
    --verbose \
    --endpoints labs/lab3rasa/endpoints.yml \
    --debug \
    "$@"