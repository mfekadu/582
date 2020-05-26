rasa train \
    -vv \
    --data labs/lab3rasa/data \
    --config labs/lab3rasa/config.yml \
    --domain labs/lab3rasa/domain.yml \
    --out labs/lab3rasa/models/

rasa test \
    -vv \
    --model labs/lab3rasa/models/ \
    --stories labs/lab3rasa/tests/ \
    --nlu labs/lab3rasa/data/ \
    --out labs/lab3rasa/results/