# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
    
'''
.
.
.
RT @loopzoop: Well...put it back https://t.co/8Yb7BDT5VM
RT @claytoncubitt: Stop asking Bernie supporters if they’ll vote for Hillary against Trump. We got a plan to beat Trump already. Called Ber…
RT @akaMaude13: Seriously can't make this up. What a joke. #NeverTrump  https://t.co/JkTx6mdRgC
'''    
