#Baomoi-Dataset-News-Classification
Consists of 26307 documents from the Baomoi newspaper (a Vietnamese newspaper) website corresponding to stories in thirteen topical areas from 2004-2006.

Class Labels: 13 ('Giải trí'(entertainment), 'Đời sống'(lifestyle), 'Công nghệ'(tech), 'Nhà đất'(real estate), 'Pháp luật'(law), 'Xe cộ'(vehicle), 'Khoa học'(science), 'Kinh tế'(economic), 'Văn hóa'(culture), 'Xã hội'(society), 'Thể thao'(sport), 'Thế giới'(worldwide), 'Giáo dục'(education).

#File Description

dataset/data.json: json file containing "news-body", "breadcrumbs" (or type), "source", "tag", "link", "sabo", "time", "heading" as columns. "news-body" column represent news article and "breadcrumbs" represents news category among the class labels.

model/get_result.py: Use Flask to run web-interface and obtained data from user, it then predict the label based on stored model and tfidf values. After successful execution it will return a label to the web interface.

model/text_classification.joblib and vectorizer.pkl: stored model and tfidf values.

templates/home.html: web-interface html code.

ML.ipynb: preprocessing, tf-idf feature extraction and model building and evaluation

#Method
Divided the feature extracted dataset into  train and test set. Train set contains 17229 examples and Test set contains 7385 examples, then do some preprocessing on the text (replace some syntax, and ViTokenizer to group words that goes together), and then use LogisticRegression to train the model.

#Result
Below table shows the result on test set

Accuracy	Value
Accuracy	0.9260663507109005
