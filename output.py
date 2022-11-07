import pandas as pd


class Output:

    def generate_output(self, id, url, positive_score, negative_score, polarity_score, subjectivity_score,
                        total_cleaned_words, avg_sentence_length, per_complex_words, fog_index, avg_no_words_per_sent,
                        complex_word_count, syllable_count_per_word, pronoun_count, avg_word_length):
        lst_output = [id, url, positive_score, negative_score, polarity_score, subjectivity_score,
                      total_cleaned_words, avg_sentence_length, per_complex_words, fog_index, avg_no_words_per_sent,
                      complex_word_count, syllable_count_per_word, pronoun_count, avg_word_length]
        df = pd.DataFrame(lst_output).transpose()
        df.columns = ['URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
                      'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX',
                      'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD',
                      'PERSONAL PRONOUNS', 'AVG WORD LENGTH']
        df.to_excel(r'Output.xlsx', index=False)
