from sklearn import svm
from sklearn import naive_bayes
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import csv


def classify(datadir):
    # Read the data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []

    count = 0
    with open(data_dir, 'r') as f:
        c_read = csv.reader(f)
        next(c_read)
        for row in c_read:
            count += 1
    # print(count)
    max = int(.8 * count)
    # print(max)
    with open(data_dir, 'r') as f:
        c_read = csv.reader(f)
        next(c_read)
        c = 0
        for row in c_read:
            c += 1
            if c <= max:
                train_data.append(row[0])
                train_labels.append(row[1])
            else:
                test_data.append(row[0])
                test_labels.append(row[1])

    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5, max_df=0.8, sublinear_tf=True, use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)

    # Perform classification with SVM, kernel=linear
    classifier_linear = svm.SVC(kernel='linear')
    classifier_linear.fit(train_vectors, train_labels)
    prediction_linear = classifier_linear.predict(test_vectors)

    # Perform classification with SVM, kernel=liblinear
    classifier_liblinear = svm.LinearSVC()
    classifier_liblinear.fit(train_vectors, train_labels)
    prediction_liblinear = classifier_liblinear.predict(test_vectors)

    # Perform classification Multinomial Naive_bayes
    classifier_NB = naive_bayes.MultinomialNB()
    classifier_NB.fit(train_vectors, train_labels)
    prediction_NB = classifier_NB.predict(test_vectors)

    # print("SVM Linear_kernel Accuracy percent: ", round(accuracy_score(test_labels, prediction_linear)*100,2))
    # print("Linear_SVC Accuracy percent: ", round(accuracy_score(test_labels, prediction_liblinear)*100,2))
    # print("Multinomial Naïve Bayes Accuracy percent: ", round(accuracy_score(test_labels, prediction_NB)*100,2))
    print("SVM Linear_kernel Analysis : \n", classification_report(test_labels, prediction_linear))

    report = precision_recall_fscore_support(test_labels, prediction_NB)
    sup = report[3]
    sum_sup = sum(sup)
    # print(sum_sup)
    per1 = round((sup[0] / sum_sup) * 100, 2)
    per2 = round((sup[1] / sum_sup) * 100, 2)
    per = [per1, per2]
    # with open('classification_rep.csv','a') as rep:
    c_wr = csv.writer(cl)
    c_wr.writerow(per)


with open('classification_rep.csv', 'w')as cl:
    cl.write('Topic, Negative, Positive\n')
    cl.write('Yogi AdityaNath,')
    print('\n')
    print("Analysis for UP CM Yogi AdityaNath \n")
    data_dir = 'YogiAdityaNath/yogi_score.csv'
    classify(data_dir)
    print("_________________________________________________________\n")
    cl.write('Demonetisation,')
    print("Analysis for Demonetisation \n")
    data_dir = 'Demonetisation/demonet_score.csv'
    classify(data_dir)
    print("_________________________________________________________\n")
    cl.write('GST,')
    print("Analysis for GST Act \n")
    data_dir = 'GST/gst_score.csv'
    classify(data_dir)
    print("_________________________________________________________\n")
    cl.write('Aadhar Act,')
    print("Analysis for Aadhar Act \n")
    data_dir = 'Aadhar/aadhar_score.csv'
    classify(data_dir)

# def classifaction_report_csv(report):
#     report_data = []
#     lines = report.split('\n')
#     for line in lines[2:-3]:
#         row = {}
#         row_data = line.split('      ')
#         row['class'] = row_data[0]
#         row['precision'] = float(row_data[1])
#         row['recall'] = float(row_data[2])
#         row['f1_score'] = float(row_data[3])
#         row['support'] = float(row_data[4])
#         report_data.append(row)
#     dataframe = pd.DataFrame.from_dict(report_data)
#     dataframe.to_csv('classification_report.csv', index = False)
