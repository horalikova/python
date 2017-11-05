# This Python file uses the following encoding: utf-8

import twitter
import sys

api = twitter.Api(consumer_key='mAkPqcrlGxNwgeXN7S3A1F86K',
                  consumer_secret='SKfiwQdmGPwZaSW4rcurlL617SjuChzs2O8eRQWHYTeq3cFICC',
                  access_token_key='16560104-iljkmaSiy28ZTUr41DoJqpNWVZQhNfYMES7t3d0XF',
                  access_token_secret='2NCObRK52TLmlgDg5uSaX8YAeW2RXsUbnbTnI0NFqHOfa')
#print api.VerifyCredentials()

# select user to fetch
user1='Jan Horalík'
user2='yruewbnwkjewjk'

# Count is command line argument, maximum count is 200
COUNT=int(sys.argv[1])

statuses = api.GetUserTimeline(screen_name=user2, count=COUNT)
for s in statuses:
    print s.text

print 'Staženo {} tweetů'.format(len(statuses))
