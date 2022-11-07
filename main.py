import os

import nltk
from web_scrapper import WebScrapper
from analysis import Analysis
from output import Output
import pandas as pd


class RunMain:

    # def __int__(self):
        # lst_id = []
        # lst_url = []
        # lst_positive = []
        # lst_negative = []
        # lst_polarity = []
        # lst_subjective = []
        # lst_avg_sentence = []
        # lst_per_complex = []
        # lst_fog = []
        # lst_avg_word_sent = []
        # lst_complex = []
        # lst_word = []
        # lst_syllable = []
        # lst_pronoun = []
        # lst_avg_word = []

    def main(self):
        nltk.download('stopwords')
        nltk.download('punkt')
        scrap = WebScrapper()
        analyse = Analysis()
        out = Output()
        lst_id = []
        lst_url = []
        lst_positive = []
        lst_negative = []
        lst_polarity = []
        lst_subjective = []
        lst_avg_sentence = []
        lst_per_complex = []
        lst_fog = []
        lst_avg_word_sent = []
        lst_complex = []
        lst_word = []
        lst_syllable = []
        lst_pronoun = []
        lst_avg_word = []
        df = pd.read_excel(r'Input.xlsx')
        print(df.shape)
        for ind, row in df.iterrows():
            id = int(row[0])
            url = row[1]
            if not scrap.scrap(url, id):
                continue
            no_stpwrd, word_tokens, no_words, no_sentences, sentence_tokens = analyse.clean_stopwords(id)
            positive_score, negative_score, polarity_score, subjectivity_score, total_cleaned_words = \
                analyse.derived_variables(no_stpwrd, word_tokens)
            avg_sentence_length, per_complex_words, fog_index, avg_no_words_per_sent, complex_word_count = \
                analyse.readability(no_words, no_sentences, word_tokens)
            syllable_count_per_word, pronoun_count, avg_word_length = \
                analyse.other_analysis(no_words, no_sentences, no_stpwrd, sentence_tokens)
            lst_id.append(id)
            lst_url.append(url)
            lst_positive.append(positive_score)
            lst_negative.append(negative_score)
            lst_polarity.append(polarity_score)
            lst_subjective.append(subjectivity_score)
            lst_avg_sentence.append(avg_sentence_length)
            lst_per_complex.append(per_complex_words)
            lst_fog.append(fog_index)
            lst_avg_word_sent.append(avg_no_words_per_sent)
            lst_complex.append(complex_word_count)
            lst_word.append(total_cleaned_words)
            lst_syllable.append(syllable_count_per_word)
            lst_pronoun.append(pronoun_count)
            lst_avg_word.append(avg_word_length)

        out.generate_output(lst_id, lst_url, lst_positive, lst_negative, lst_polarity,
                            lst_subjective, lst_avg_sentence, lst_per_complex, lst_fog,
                            lst_avg_word_sent, lst_complex, lst_word, lst_syllable,
                            lst_pronoun, lst_avg_word)
        for file in os.listdir(r'./text files/'):
            os.remove(r'./text files/'+file)


if __name__ == '__main__':
    main = RunMain()
    main.main()
