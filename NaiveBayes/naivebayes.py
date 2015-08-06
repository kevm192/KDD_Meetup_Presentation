from collections import defaultdict
import re
import math



def tokenize(message):
    '''preprocess the message (string) to produce a bag or words.'''
   

def count_words(training_set):
    ''' training set consists of pairs (message,is_spam)'''
   
def word_probabilities(counts,total_spams,total_non_spams,k=0.5):
    '''turn the word_counts into a list of triplets:
       w , p(w|spam),p(w|~spam)
    '''


def class_probabiltiies(total_spams,total_non_spams):
    ''' Calculate priors '''


def classify_probabiliy(word_probs,message,prior_spam,prior_not_spam):
    ''' Classify a message as either spam (1) or not_spam (0)'''


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
        print self.prior_spam,self.prior_not_spam
        self.word_probs = word_probabilities(word_counts,num_spams,num_non_spams,self.k)

    def classify(self,message):
        return classify_probabiliy(self.word_probs,message,self.prior_spam,self.prior_not_spam)


        
        
    