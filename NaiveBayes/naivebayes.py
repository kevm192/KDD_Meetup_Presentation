from __future__ import division
from collections import defaultdict
import re
import math




def tokenize(message):
    '''preprocess the message (string) to produce a bag or words.'''
    message = message.lower()
    all_words = re.findall("[a-z0-9]+",message)
    return set(all_words)
   

def count_words(training_set):
    ''' training set consists of pairs (message,is_spam)'''
    counts = defaultdict(lambda:[0,0])
    for message,is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1

    return counts
   
def word_probabilities(counts,total_spams,total_non_spams,k=0.5):
    '''turn the word_counts into a list of triplets:
       w , p(w|spam),p(w|~spam)
    '''
    return [(w,
             (spam+k)/(total_spams + 2 * k),
             (non_spam+k)/ (total_non_spams + 2 *k))
             for w,(spam,non_spam) in counts.iteritems()]



def class_probabiltiies(total_spams,total_non_spams):
    ''' Calculate priors '''

    total_message = total_spams + total_non_spams
    prior_spam = total_spams/total_message
    prior_not_spam = total_non_spams/total_message

    return prior_spam, prior_not_spam

def classify_probabiliy(word_probs,message,prior_spam,prior_not_spam):
    ''' Classify a message as either spam (1) or not_spam (0)'''
    message_words = tokenize(message)

    log_prob_if_spam = log_prob_if_not_spam = 0

    #iterate through each word in our vocab
    for word, prob_if_spam, prob_if_not_spam in word_probs:

        if word in message_words:

            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)

        else:

            log_prob_if_spam += math.log(1 - prob_if_spam)
            log_prob_if_not_spam += math.log(1 - prob_if_not_spam)

    prob_if_spam = math.exp(log_prob_if_spam) * prior_spam
    prob_if_not_spam = math.exp(log_prob_if_not_spam) * prior_not_spam

    if prob_if_spam > prob_if_not_spam:
        return True
    else:
        return False





class NaiveBayesClassifier:

    def __init__(self,k=0.5):
        self.k  = k
        self.word_probs = []
        self.prior_spam = .5
        self.prior_not_spam = .5

    def train(self,training_set):
        num_spams = len([is_spam for message, is_spam in training_set if is_spam])
        num_non_spams = len(training_set) - num_spams

        

        # run training data through pipeline
        word_counts = count_words(training_set)
    
        self.prior_spam,self.prior_not_spam = class_probabiltiies(num_spams,num_non_spams)
        #print self.prior_spam,self.prior_not_spam
        self.word_probs = word_probabilities(word_counts,num_spams,num_non_spams,self.k)

    def classify(self,message):
        return classify_probabiliy(self.word_probs,message,self.prior_spam,self.prior_not_spam)


        
        
    