import csv

with open('question.csv', encoding='utf-8') as f:
    questions = [line.split(',')[0] for line in f]