# https://github.com/RasaHQ/rasa-demo
# https://rasa.com/docs/rasa/core/actions/
# This will run as a standalone server.
# separate from the `rasa shell` or the `rasa run`
# https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels
rasa run -vv actions \
    --actions labs.lab3rasa.actions \
    --debug \
    "$@"
