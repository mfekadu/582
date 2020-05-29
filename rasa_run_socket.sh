# https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels


# https://stackoverflow.com/a/2013589
export RASA_ACTION_ENDPOINT=${RASA_ACTION_ENDPOINT:="http://localhost:5055/webhook"}

echo "RASA_ACTION_ENDPOINT is " $RASA_ACTION_ENDPOINT

## given the environment variable, run rasa
#RASA_ACTION_ENDPOINT=$RASA_ACTION_ENDPOINT \
#    rasa run -vv \
#    --model labs/lab3rasa/models \
#    --verbose \
#    --endpoints labs/lab3rasa/endpoints.yml \
#    $1


rasa run -vv \
    --model labs/lab3rasa/models \
    --verbose \
    --endpoints labs/lab3rasa/endpoints.yml \
    --debug \
    --enable-api \
    --connector socketio --cors "*" \
    $1 $2 $3 $4 $5 $6
