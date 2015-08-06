''' Prepare text data sets and test using naivebayes classifier '''
from __future__ import division
import glob,re
import random
import os

# change this to wheverever your NaiveBayes folder is using the proper / or \
os.chdir('/Users/kevm1892/Documents/KDD_Meetup_Presentation/NaiveBayes')
from naivebayes import *

def split_data(data,prob):
    ''' split data into fractions [prob,1-prob]
        by sampling from a random distrubition on each irow ndex 
        with respect to the probability'''



''' We are now ready to prep our data nad apply our naive bayes classifier '''


''' Prep Data '''


# Split data
train_data, test_data = split_data(data,0.75)


''' Build classifier '''
clf = NaiveBayesClassifier()
clf.train(train_data)



classified = [(subject,is_spam,clf.classify(subject)) for subject,is_spam in test_data]

''' lets evaluate our model '''
fp=fn=tp=tn=0

for x,est,tru in classified:
    print est,tru
    if est == True and tru==False:
        fp+=1
    elif est== True and tru==True:
        tp+=1
    elif est== False and tru == False:
        tn+=1
    else:
        fn+=1

def recall(tp,fp,fn,tn):
    ''' What fraction of postitives were correctly identified '''
    

def precision(tp,fp,fn,tn):
    '''How accurate were our positive predictions '''
  

def accuracy(tp,fp,fn,tn):
 

def f1_score(tp,fp,fn,tn):
 
        

# error metrics
print 'accuracy: {}'.format(accuracy(tp,fp,fn,tn))
print 'precision: {}'.format(precision(tp,fp,fn,tn))
print 'recall: {}'.format(f1_score(tp,fp,fn,tn))
