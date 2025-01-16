from collections import Counter
import re
import csv
import math
from collections import OrderedDict

def root_form(clean_list):
    new_list = []
    root_sentence = []
    
    for line in clean_list:
        words = re.findall(r'\b\w+\b', line)
        root_sentence = [word for word in words]
        
        for number, x in enumerate(root_sentence):
            root_word = re.sub(r'ing$|ly$|ment$', '', x)
            root_sentence[number] = root_word

        root_line = ' '.join(root_sentence)
        new_list.append(root_line)
    
    return new_list

def remove_stopwords(clean_list):
    new_list = []    
    csv_reader = csv.reader(open('stopwords.txt'))
    reader = list(csv_reader)
    stopwords = [row for x in reader for row in x]
    
    for line in clean_list:
        words = re.findall(r'\b\w+\b', line)
        cleaned_words = [word for word in words if word not in stopwords]
        
        cleaned_line = ' '.join(cleaned_words)

        new_list.append(cleaned_line)
        
    return new_list

def doc_processing(input_file):
    csv_reader = csv.reader(open(input_file))
    reader = list(csv_reader)

    with open('preproc_' + input_file, 'w', newline='') as write_file:

        clean_list = []

        

        for num, row in enumerate(reader):
            for line in row:
                yes = re.sub(r'https?://\S+', '', line)
                yes = re.sub(r'[^\w\s]','',yes)
                yes = re.sub(r'\s+',' ',yes)
                yes = yes.lower()
                clean_list.append(yes)

        clean_list = remove_stopwords(clean_list)
        
        clean_list = root_form(clean_list)
        for number, line in enumerate(clean_list):
            if number != len(clean_list) - 1:
                write_file.write(f'{line} ')
            else:
                write_file.write(line)
    
        
def compute_TF_IDF(doc, doc_list):
    csv_reader = csv.reader(open(doc))
    reader = list(csv_reader)

    term_frequency = {}
    doc_freq = Counter()


    for sublist in doc_list:
        keys = [word for word in sublist]
        doc_freq.update(sublist)

    for num, row in enumerate(reader):
        for line in row:
            sorted_list = sorted(line.split())
            word_counter = Counter(sorted_list)
           
            for key, value in word_counter.items():
                term_frequency.setdefault(key, []).append(value / len(word_counter))
            
            for key in sorted_list:
                term_frequency[key] = value/len(word_counter)


def count_words(file_name):
    with open(file_name, 'r') as x:
        words = x.read().split()
        return sorted(Counter(words).items())
     

def preprocessing(input_file):
    csv_reader = csv.reader(open(input_file))
    reader = list(csv_reader)
    doc_ognames = []
    preproc_docs = []
    counter_list = []
    for num, row in enumerate(reader):
        for line in row:
            
            doc_processing(line)
            doc_ognames.append(line)
            preproc_docs.append('preproc_' + line)
                
    
    word_count = []

    for line in preproc_docs:
        doc_name = line.strip()
        with open(doc_name, 'r') as x:
            z = count_words(doc_name)
            single_count = sum(tup[1] for tup in z)
            word_count.append(single_count)
            counter_list.append(z)

    

    #TF
    term_frequency_calc = []
    for i in counter_list:

        term_frequency_per_doc = []
        for val in i:
            tf = val[1]/sum(tup[1] for tup in i)
            term_frequency_per_doc.append((val[0], tf))
        term_frequency_calc.append(term_frequency_per_doc)
    

    #IDF
    doc_freq = Counter()

    for sub in counter_list:
        keys = [word for word, count in sub]
        doc_freq.update(keys)
    
    doc_freq = sorted(doc_freq.items())
    ordered_doc_frequency = OrderedDict(doc_freq)
    
    idf_calc = []

    for word in ordered_doc_frequency:
        idf = math.log(len(counter_list) / ordered_doc_frequency[word]) + 1 
        idf_calc.append((word, idf))
    

    #TF-IDF
    tf_idf_calc = []

    for dv in term_frequency_calc:
        tf_idf_doc = []
        for i in dv:
            for wv in idf_calc:
                if i[0] == wv[0]:
                    tf_idf = round((i[1] * wv[1]), 2)
                    tf_idf_doc.append((i[0], tf_idf))
        tf_idf_calc.append(tf_idf_doc)

    #Writing to tfidf_ file

    for f, h in zip(doc_ognames, tf_idf_calc):
        ordered_h = sorted(h, key=lambda x: (-x[1], x[0]))
        top5_h = ordered_h[:5]
        with open('tfidf_' + f, 'w') as lf:
            lf.write(str(top5_h))
                
    
preprocessing('tfidf_docs.txt')