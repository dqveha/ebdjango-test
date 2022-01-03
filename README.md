Create a options.config file under .ebextensions with following template:

option_settings:
  aws:elasticbeanstalk:application:environment:
    SECRET_KEY: 
    DEBUG: 
    DB_NAME: 
    DB_USER: 
    DB_PASSWORD:
    DB_HOST: 