class Sentiment:

    values = {'sad', 'neutral', 'happy'}

    def __init__(self, value='neutral'):
        if value not in Sentiment.values:
            raise ValueError("Only the following values are supported: %s"
                             % Sentiment.values)
        self.value = value

    def get(self):
        return self.happy_or_not

    def __repr__(self):
        return self.value

    @staticmethod
    def guess(text):
        if 'happy' in text or 'excited' in text:
            return Sentiment('happy')
        if 'sad' in text or 'angry' in text:
            return Sentiment('sad')
        return Sentiment('neutral')


if __name__ == "__main__":
    import sys
    for arg in sys.argv[1:]:
        print(arg)
        print('\t=>', Sentiment.guess(arg))
