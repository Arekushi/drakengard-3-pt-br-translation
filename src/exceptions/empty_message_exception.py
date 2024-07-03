class EmptyMessageError(Exception):
    def __init__(self, message='Mensagem vazia'):
        self.message = message
        super().__init__(self.message)
