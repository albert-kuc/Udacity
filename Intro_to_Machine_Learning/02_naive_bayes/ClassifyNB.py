# -*- coding: utf-8 -*-
"""
Created from Intro to Machine Learning at Udacity
Lesson 2.19: GaussianNB Deployment on Terrain Data

Main code in studentMain.py
"""

from sklearn.naive_bayes import GaussianNB
def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    clf=GaussianNB()
    clf.fit(features_train, labels_train)
    # pred = clf.predict(features_test)
    return clf
    