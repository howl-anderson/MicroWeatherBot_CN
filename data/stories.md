## greet
* greet
  - utter_greet

## greet in conversion
> checkpoint
* greet
  - utter_greet
> checkpoint

## simple path
* weather_address_date-time{"address": "上海", "date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## simple path
> checkpoint
* weather_address_date-time{"address": "上海", "date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## address + date-time path with greet
* weather_address{"address": "上海"}
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## address + date-time path with greet
> checkpoint
* weather_address{"address": "上海"}
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## date-time + address path with greet
> checkpoint
* weather_date-time{"date-time": "明天"}
  - utter_ask_address
* weather_address{"address": "上海"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## date-time + address path
* weather_date-time{"date-time": "明天"}
  - utter_ask_address
* weather_address{"address": "上海"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## None + date-time + address path
* weather
  - utter_ask_date-time
> checkpoint

## None + date-time + address path
> checkpoint
* weather_date-time{"date-time": "明天"}
  - utter_ask_address
* weather_address{"address": "上海"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## None + address + date-time path
* weather
  - utter_ask_date-time
* weather_address{"address": "上海"}
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## None + date-time + address path with greet
* greet
  - utter_greet
* weather
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_ask_address
* weather_address{"address": "上海"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint

## None + address + date-time path with greet
* greet
  - utter_greet
* weather
  - utter_ask_date-time
* weather_address{"address": "上海"}
  - utter_ask_date-time
* weather_date-time{"date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
> checkpoint
  
## with change address
> checkpoint
* weather_address_date-time{"address": "上海", "date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
* weather_address{"address": "北京"} OR weather_date-time{"date-time": "明天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
* weather_address{"address": "杭州"} OR weather_date-time{"date-time": "后天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather
* weather_address{"address": "南京"} OR weather_date-time{"date-time": "大后天"}
  - utter_working_on_it
  - action_report_weather
  - utter_report_weather

## say goodbye in conversion
> checkpoint
* goodbye
  - utter_goodbye
> checkpoint

## say goodbye
* goodbye
  - utter_goodbye