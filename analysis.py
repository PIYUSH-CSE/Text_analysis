import os
import re

import nltk
from nltk.tokenize import sent_tokenize
from textstat.textstat import textstatistics


class Analysis:

    def clean_stopwords(self, id):
        lst = []

        for text_files in os.listdir("./Stopwords"):
            with open('./Stopwords/{}'.format(text_files)) as f:
                for stop in f.read().split():
                    lst.append(stop.lower())
        file = open('{}.txt'.format(r'./text files/' + str(id))).read()
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        word_tokens = tokenizer.tokenize(file)
        no_words = len(word_tokens)

        sentence_tokens = sent_tokenize(file)
        no_sentences = len(sentence_tokens)

        stpwrd = nltk.corpus.stopwords.words('english')
        stpwrd.extend(lst)

        no_stpwrd = []

        for i in word_tokens:
            if i in stpwrd:
                continue
            else:
                no_stpwrd.append(i)

        return no_stpwrd, word_tokens, no_words, no_sentences, sentence_tokens

    def derived_variables(self, no_stpwrd, word_tokens):
        positive = []
        negative = []

        positive_file = open('positive-words.txt', "r")
        negative_file = open('negative-words.txt', 'r')

        for word in positive_file.read().split():
            positive.append(word)

        for word in negative_file.read().split():
            negative.append(word)

        dict = {'positive': ' ', 'negative': ' '}

        new_positive = []
        new_negative = []
        for i in no_stpwrd:
            if i in positive:
                new_positive.append(i)
            elif i in negative:
                new_negative.append(i)

        dict['positive'] = new_positive
        dict['negative'] = new_negative

        positive_score = 0
        negative_score = 0
        for i in word_tokens:
            if i in new_positive:
                positive_score += 1
            elif i in new_negative:
                negative_score += 1

        total_cleaned_words = len(no_stpwrd)
        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

        subjectivity_score = (positive_score + negative_score) / (total_cleaned_words + 0.000001)

        return positive_score, negative_score, polarity_score, subjectivity_score, total_cleaned_words

    def readability(self, no_words, no_sentences, word_tokens):
        avg_sentence_length = no_words / no_sentences

        complex_word = 0
        for i in word_tokens:
            if textstatistics().syllable_count(i) > 2:
                complex_word += 1

        per_complex_words = complex_word / no_words

        fog_index = 0.4 * (avg_sentence_length + per_complex_words)
        avg_no_words_per_sent = no_words / no_sentences
        complex_word_count = complex_word

        return avg_sentence_length, per_complex_words, fog_index, avg_no_words_per_sent, complex_word_count

    def other_analysis(self, no_words, no_sentences, no_stpwrd, sentence_tokens):
        syllable_lst = []
        for i in no_stpwrd:
            syllable_lst.append(textstatistics().syllable_count(i))
            count = 0
            h = textstatistics().syllable_count(i)
            count += h
            if i.endswith("es") or i.endswith("ed"):
                count -= 1
            syllable_lst.append(count)

        syllable_count_per_word = int(sum(syllable_lst) / len(syllable_lst))

        pronoun_lst = []
        pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b', re.I)
        for i in sentence_tokens:
            pol = pronounRegex.findall(i)
            for item in pol:
                pronoun_lst.append(item)

        pronoun_count = len(pronoun_lst)

        word_length = 0
        for i in no_stpwrd:
            word_length += len(i)
        avg_word_length = word_length / len(no_stpwrd)

        return syllable_count_per_word, pronoun_count, avg_word_length
