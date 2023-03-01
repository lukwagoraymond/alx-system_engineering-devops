#!/usr/bin/python3
"""
100-main
python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
python3 100-main.py programming 'JavA java'
100-main.py not_a_valid_subreddit 'python java javascript scala no_results_for_this_one'
100-main.py not_a_valid_subreddit 'python java'
"""
import sys

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
