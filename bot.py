import botometer 

twitter_app_auth = {
    'consumer_key': "CONSUMER_KEY_HERE",
    'consumer_secret': "CONSUMER_SECRET_KEY_HERE",
    'access_token': "ACCESS_TOKEN_HERE",
    'access_token_secret': "ACCESS_TOKEN_SECRET_HERE"
}

botometer_api_url = "BOTOMETER_API_URL_HERE"

rapidapi_key = "RAPIDAPI_KEY_HERE"

bom = botometer.Botometer(
                wait_on_ratelimit = True,
                rapidapi_key = rapidapi_key,
                **twitter_app_auth)

try:
    result = bom.check_account(f'@{handle}')

    my_score = 0
    count = 0

    for k, v in result['display_scores'].items():
        my_score += result['display_scores'][k]
        count += 1

    print(f'Average score for {handle} is {my_score/count}.')

except Exception as e:
    print(e)