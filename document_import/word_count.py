#!/usr/bin/env python3
class word_count:
    def count(self, words):
        #count each word
        keyWords = {}
        for word in words:
            if word in keyWords:
                keyWords[word] += 1
            else:
                keyWords[word] = 1
        return keyWords