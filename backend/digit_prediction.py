from sklearn.datasets import load_digits
from classifier import ClassifierFactory
from image_processing import process_image

class PredictDigitService:
    def __init__(self, stored_classifier):
        self.stored_classifier = stored_classifier

    def predict(self, image_data_uri):
        classifier = self.stored_classifier.get()
        if classifier is None:
            digits = load_digits()
            classifier = ClassifierFactory.create_with_fit(
                digits.data,
                digits.target
            )
            self.stored_classifier.update(classifier)
        
        x = process_image(image_data_uri)
        if x is None:
            return 0

        prediction = classifier.predict(x)[0]
        return prediction        