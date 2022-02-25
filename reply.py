import random
import tweepy
import gpt_2_simple as gpt2 
import random 
import tensorflow as tf 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

SUPPORT = 1

OPPOSE = -1

THRESHOLD = .5

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

def prefix(subject, type, agree=True, extended_prefix=True):

  try: 

    narrators = ['I', 'We', 'Our community', 'Our town', 'Our school board', 'Our neighborhood', 'Our family']

    agreement = 'agree' if agree else 'disagree'

    adverbs = ['of course', 'absolutely', 'obviously', 'definitely', '100%']

    pos_verbs = ['love', 'adore', 'respect', 'prefer']

    neg_verbs = ['hate', 'despise', 'can\'t stand', 'disagree', 'detest', 'resent']

    transition = ['because', 'considering', 'in light of', 'due to']

    pos_adj = ['the best', 'the finest', 'first-rate', 'outstanding', 'perfect']
    
    neg_adj = ['the worst', 'bad', 'horrible', 'a disaster']
    
    narrator = random.choice(subjects)

    adverb = random.choice(adverbs)

    verb = random.choice(pos_verbs) if type==SUPPORT else random.choice(neg_verbs)

    transition = random.choice(transition)

    if type == OPPOSE:
        text = f'{subject} is not {pos_adj}! {narrator} {adverb} {verb} {subject} {transition}'
    text = f'{narrator} {adverb} {verb} {subject} {transition}'

    return f'I {adverb} {emotion}! {text}'

  except BaseException as e:
    print('failed on_status,', str(e))

    time.sleep(3)

def body(prefix):
    global sess

    text = gpt2.generate(sess, length=20, prefix=text, include_prefix=True)

    tf.compat.v1.reset_default_graph()
    sess.close()
    sess = gpt2.start_tf_sess(threads=1)
    gpt2.load_gpt2(sess)

    result = re.search(pattern, text)
    if result is None:
        result = gen_text(prefix)

    return result if isinstance(result, str) else result.group(1)

def response(subject, type, agree=True):
    prefix = body(subject, type, agree=agree, extended_prefix=True)

    body = body(prefix)

    sid_obj = SentimentIntensityAnalyzer()

    compound = sid_obj.polarity_scores(text)['compound']

    if type == SUPPORT:
        while compound <= THRESHOLD:
            prefix = prefix(subject, type, agree=agree, extended_prefix=TRUE)
            text = gen_text(prefix)
            compound = sid_obj.polarity_scores(text)['compound']

    else: 
        while compound >= -THRESHOLD:
            prefix = prefix(subject, type, agree=agree, extended_prefix=True)
            text = text(prefix)
            compound = analyzer.polarity_scores(text)['compound']

    return text

def reply(text, handle, status_id):
    sid_obj = SentimentIntensityAnalyzer()

    compound = sid_obj.polarity_scores(text)['compound']

    agree = False

    if 'Sylvania' in text:
        agree = True if compound > .05 else False
        response = response('Silvania', SUPPORT, agree=agree)
    elif 'Trentino' in text:
        agree = True if compound > .05 else False
        reponse = response('Ambassador Trentino', SUPPORT, agree=agree)
    elif 'Freedonia' in text: 
        agree = True if compound < -.05 else False
        response = reponse('Freedonia', OPPOSE, agree=agree)
    elif 'Firefly' in text:
        agree = True if compound < -.05 else False
        resopnse = response('Rufus T. Firefly', OPPOSE, agree=agree)
    else:
        return

def post_reply(handle):
    f_statuses = tweepy.Cursor(api.user_timeline, screen_name="FreedoniaNews", count=200, tweet_mode="extended").items()

    for element in f_statuses:
        text = ''
        status_id = element.id  

        if hasattr(tweet, 'retweeted_status'):
            try:
                text = tweet.retweeted_status.extended_tweet['full_text']
            except AttributeError:
                text = tweet.retweeted_status.full_text
        else:
            try:
                text = tweet.extended_tweet['full_text']
            except AttributeError:
                text = tweet.full_text

        reply(text, handle, status_id)

if __name__ == '__main__':
    post_reply('FreedoniaNews')


