git clone <this rep> 
git checkout backend 
use venv

pip install -r requiremets
fill the .env file using token of the bot(can be taken from front bot)
*can fill ADMINS_LIST 

to launch bot, run bot.py (site_for_tz-bot-bot.py)
to launch rest api run (site_for_tz-rest api-app.py)
to check the rest api launch test_api.py (site_for_tz-rest api-test_api.py)

structure of project:
bot:
  FSM: Finite State Machine, used for admin commands
  config: use to loading to project .env file with secret info
  handlers:
    __init__ - union handlers from files
    admins_handlers - working only for admin after /switch_user command
    comic_inline_handler - inline handlers for reading comics
    main_hand - starting reading comics
    start_handlers - handling commands
  lexixon:
    bot lexicon
  bot.py : starting point of the bot
  keyboard.py:  class with static methods which creating keyboards
comic_files: pictures
  standartizing.py - experiment file which check the comics and leads for the form <int>.jpg, from any extention
db:
  creating_db: CRUD class for managment sql injections
rest api
  app.py - rest api for managment the comic files and updating sql database
  test_api.py - file to test the rest api
  
    
  
