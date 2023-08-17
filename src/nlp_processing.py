class NLPProcessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        tokenized_text = word_tokenize(text.lower())
        cleaned_text = [self.lemmatizer.lemmatize(word) for word in tokenized_text if word not in self.stop_words]
        return cleaned_text

    def analyze_sentiment(self, chat_data):
        sentiment = TextBlob(chat_data).sentiment
        return sentiment

    def extract_entities(self, chat_data):
        doc = nlp(chat_data)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def generate_response(self, text_data):
        response = self.gpt_model.generate(text_data)
        return response