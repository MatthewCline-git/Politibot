## Project Structure

The files and their functions: 

```
get_access.py
```
- A general purpose program that allows users to authorize Tweepy to perform account actions
they have a Twitter developer account.

```
scrape_tweets.py
```
- Scrapes public twitter accounts to build a text corpus. Tweepy's Cursor has a limit of 200 tweets per request.
In this case, I scraped 1000 tweets fromt the same account via 5 requests. If you wanted to select 5 different
accoutns, you could disregard the "max_id" parameter in the Cursor call and the id=status.id declaration inside
each for loop. Once the tweets are scraped, the program writes them out to a text file. 

```
train.py
```

- Trains a GPT-2 model on the text corpus to generate human like responses. I used the 124M model. Increase the 
number of steps for more thorough (yet more time-consuming) training and vice-versa. Running this code via 
Google Colaboratory is a good way to run the training steps faster. 

```
reply.py
```

- Uses trained GPT-2 model to generate response tweets. This is where the fun really begins. The GPT-2 model allows
for user provided "seed text" that induces the model to generate text that matches the tone and structure of that seed.
The prefix function generates this seed text, which I call "prefix" throughout the program. Basically, it's 
pseudo-randomly assembles a variety of subjects (I, We, Our household), verbs (hate, love, despise, adore), adverbs, 
adjectives, etc. 

The body function initiates the gpt-2 model to generate a full response. In the response function, I use Vader Sentiment Analyzer
to continually update the gpt-2-generated response until it falls within the desired sentiment threshold. Vader assesses sentient
on a scale from -1 to 1,  negative to positive sentiment. I chose my threshold as .5, although Vader considers the sentiment
to be positive or negative based on scores exceeding |.5|. The reply function then calls that response function with appropriate parameters
depending on the candidate name detected in the news outlet's tweet. Post_reply posts the final reply as a tweet from the 
bot account.

```
bot.py
```

- Assesses the human-ness of the bot's replies. This uses Indiana University's Botometer to grade and display the bot's replies. A higher
step count during the training stage will result in more human replies here.
