
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:03:37 2020

@author: vickieluo

Final Project
"""

import math



def clean_text(txt):
    """takes a string of text txt as a parameter and returns a list containing the words in txt after punctuation is removed"""
    
    s=txt.lower()
     
    s=s.replace('.','')
    s=s.replace(',','')
    s=s.replace('?','')
    s=s.replace('"','')
    s=s.replace("'",'')
    s=s.replace('!','')
    
    
    w=s.split()
    
    
    return w

def stem(s):
    """accepts a string as a parameter and  returns the stem of s"""
    if s[-1]=='s':
        s=s[:-1]
    
    if s[-3:]=='ing':
        if len(s)>4:
            if s[-4]==s[-5]:
                s=s[:-4]
            else:
                s=s[:-3]
    elif s[-2:]=='er':
        if s[-3]==s[-4]:
            s=s[:-3]
        else:
            s=s[:-2]
    elif s[-2:]=='ed':
        if s[-3]==s[-4]:
            s=s[:-3]
        else:
            s=s[:-2]
    elif s[-3:]=='ion':
        if len(s)>4:
            if s[-4]==s[-5]:
                s=s[:-4]
            else:
                s=s[:-3]
    if s[:3]=='pre':
        s=s[3:]
    if s[:3]=='dis':
        s=s[3:]
    if s[:2]=='de':
        s=s[2:]
    if s[:3]=='mis':
        s=s[3:]
    if s[:2]=='un':
        s=s[2:]
    
    
        
    return s
    
def compare_dictionaries(d1, d2):
            """take two feature dictionaries d1 and d2 as inputs, and it should compute and return their log similarity score"""
            score=0
            total=0
            for z in d1:
                total += d1[z]
                
            for w in d2:
                    if w in d1:
                    
                        score+=(math.log(d1[w]/total))*d2[w]
                    else:
                        score+=(math.log(0.5 / total))*d2[w]
                    
            return score
                    
        
            
    
    
    
    
class TextModel:
    
    def __init__(self, model_name):
        """accepts a string model_name as a parameter and initializes attributes"""
        self.name=model_name
        self.words={}
        self.word_lengths={}
        self.stems={}
        self.sentence_lengths={}
        self.comma={}
        
        
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s+=  '  number of word lengths: '+ str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s+=  '  number of sentence lengths: '+ str(len(self.sentence_lengths)) + '\n'
        
        s += '  different number of commas that appear in sentences: ' + str(len(self.comma)) + '\n'
        return s
    
    
    
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
       to all of the dictionaries in this text model.
       """
               
        v=0
        for u in s:
            if u ==',' :
                v+=1
            if u in '?!.':
                q=v
                v=0
                
                
                
                if q not in self.sentence_lengths:
                    self.comma[q]=1
                else:
                    self.comma[q]+=1
        
            
        t=s.split()
        c=0
        d=0
        for a in t:
            if a[-1] not in '?!.':
                c+=1
            else:
                d=c+1
                c=0
                
            
            
                
                
                
                if d not in self.sentence_lengths:
                    self.sentence_lengths[d]=1
                else:
                    self.sentence_lengths[d]+=1
                
        
   
        word_list = clean_text(s)

    # Template for updating the words dictionary.
        for w in word_list:
        # Update self.words to reflect w
        # either add a new key-value pair for w
        # or update the existing key-value pair.
                
            
            
            if w not in self.words:
                self.words[w] = 1 
                
            else:
                self.words[w] += 1 
                
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)]=1
            else:
                self.word_lengths[len(w)] += 1
                
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1 
                
            else:
                self.stems[stem(w)] += 1 
                
        
        
            
                

            

    # Add code to update other feature dictionaries.
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model"""
              
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        b=f.read()
        self.add_string(b)
        
        
        
    
    
    def save_model(self):
        """saves the TextModel object self by writing its various feature dictionaries to files"""
        d = self.words   # Create a sample dictionary.
        f = open(self.name+'_'+'self.words', 'w')      # Open file for writing.
        f.write(str(d))              # Writes the dictionary to the file.
        f.close()    
        
        e = self.word_lengths   # Create a sample dictionary.
        g = open(self.name+'_'+'self.word_lengths', 'w')      # Open file for writing.
        g.write(str(e))              # Writes the dictionary to the file.
        g.close()    
        
        h = self.sentence_lengths   # Create a sample dictionary.
        i = open(self.name+'_'+'self.sentence_lengths', 'w')      # Open file for writing.
        i.write(str(h))              # Writes the dictionary to the file.
        i.close()    
        
        j = self.stems   # Create a sample dictionary.
        k = open(self.name+'_'+'self.stems', 'w')      # Open file for writing.
        k.write(str(j))              # Writes the dictionary to the file.
        k.close()   
        
        l = self.comma   # Create a sample dictionary.
        m = open(self.name+'_'+'self.comma', 'w')      # Open file for writing.
        m.write(str(l))              # Writes the dictionary to the file.
        m.close()   
        
    def read_model(self):
        """reads the stored dictionaries for the called TextModel object from their files and assigns them to the attributes of the called TextModel"""
    
    
        f = open(self.name+'_'+'self.words', 'r')    # Open for reading.
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.words=dict(eval(d_str))      # Convert the string to a dictionary.

        
        
        e = open(self.name+'_'+'self.word_lengths', 'r')    # Open for reading.
        g_str = e.read()           # Read in a string that represents a dict.
        e.close()

        self.word_lengths=dict(eval(g_str)) 
        
        # Convert the string to a dictionary.
        h = open(self.name+'_'+'self.sentence_lengths', 'r')    # Open for reading.
        i_str = h.read()           # Read in a string that represents a dict.
        h.close()

        self.sentence_lengths=dict(eval(i_str)) 
        
        j = open(self.name+'_'+'self.stems', 'r')    # Open for reading.
        k_str = j.read()           # Read in a string that represents a dict.
        j.close()

        self.stems=dict(eval(k_str)) 
        
        
        l = open(self.name+'_'+'self.comma', 'r')    # Open for reading.
        m_str = l.read()           # Read in a string that represents a dict.
        l.close()

        self.comma=dict(eval(m_str)) 
        
    def similarity_scores(self, other):
        """computes and returns a list of log similarity scores measuring the similarity of self and other"""
        word_score = compare_dictionaries(other.words, self.words)
        stem_score = compare_dictionaries(other.stems, self.stems)
        wordlen_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        senlen_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        comma_score = compare_dictionaries(other.comma, self.comma)
        
        score=[word_score,wordlen_score,stem_score,senlen_score,comma_score]
        
        return score
        
    def classify(self, source1, source2):
        """compares the called TextModel object (self) to two other “source” TextModel objects (source1 and source2) and determines which of these other TextModels is the more likely source of the called TextModel"""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for '+ source1.name + ':' + str(scores1))
        print('scores for '+ source2.name + ':' + str(scores2))
        weighted_sum1 = 10*scores1[0] + 5*scores1[1] + 7*scores1[2] +7*scores1[3]+3*scores1[4]
        weighted_sum2 = 10*scores2[0] + 5*scores2[1] + 7*scores2[2] +7*scores2[3]+3*scores2[4]
        
        if weighted_sum1>weighted_sum2:
            print(self.name+' is more likely to have come from '+ source1.name)
            
        else:
            print(self.name+' is more likely to have come from '+ source2.name)

def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)