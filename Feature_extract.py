import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
count = 0
with open('Demonetisation/demonet_pp.csv', 'r') as inp , open('Demonetisation/demonet_score.csv', 'w') as op:
    fields = 'tweet, polarity, negative, neutral, positive, compound'
    op.write(fields)
    op.write('\n')
    c_reader = csv.reader(inp)
    next(c_reader)
    c_writer = csv.writer(op)
    for row in c_reader:
        row = row[0]
        score = analyzer.polarity_scores(row)
        #print("{:-<10} {}".format(count, str(score)))
        score_val = score.values()
        #op.write(row+',')
        #c_writer.writerow(list(score_val))
        f_score = score['compound']
        if f_score >= 0.5:
            op.write(row + ',positive,')
            c_writer.writerow(list(score_val))
        elif f_score <= -0.5:
            op.write(row + ',negative,')
            c_writer.writerow(list(score_val))