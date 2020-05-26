#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path 1
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy

## happy path 2
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy
* goodbye: bye-bye!
  - utter_goodbye

## sad path 1
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* affirm: yes
  - utter_happy

## sad path 2
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* deny: not really
  - utter_cheer_up
  - utter_did_that_help
* deny: no not at all
  - utter_happy
  - utter_goodbye

## sad path 3
* greet: hi
  - utter_greet
* mood_unhappy: very terrible
  - utter_cheer_up
  - utter_did_that_help
* deny: no
  - utter_cheer_up
  - utter_did_that_help
* deny: no not at all
  - utter_happy
  - utter_goodbye

## say goodbye
* goodbye: bye-bye!
  - utter_goodbye

## bot challenge
* bot_challenge: are you a bot?
  - utter_iamabot
  - action_hello_world



<!-- hmmm.....??? -->
## stop program
* stop_program: die
  - utter_goodbye
  - action_stop_program


<!-- i am not sure if machine learning should happen here...... -->
<!-- maybe action_stop_progarm should handle input and verify exact string match.... -->
<!-- ## stop program 2
* stop_program: stop program
  - utter_goodbye
  - action_stop_program -->