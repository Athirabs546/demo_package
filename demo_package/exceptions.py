class OneHotEncodingError(Exception):
    """Custom exception for OneHotEncoding errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
