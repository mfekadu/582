export RASA_ACTION_ENDPOINT=${RASA_ACTION_ENDPOINT:="http://localhost:5055/webhook"}

echo "RASA_ACTION_ENDPOINT is " $RASA_ACTION_ENDPOINT

rasa shell -vv \
    --model labs/lab3rasa/models \
    --verbose \
    --endpoints labs/lab3rasa/endpoints.yml \
    --debug \
    "$@"