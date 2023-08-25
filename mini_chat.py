class MiniChat:
    '''
    Eine kleine Demo für das Kommunizieren von Klassen.
    '''

    def __init__(self, name):
        '''
        Ich muss mich im Chat mit Namen bekannt machen
        '''
        self._name = name

    @property
    def name(self):
        return self._name

    def send_a_message_to(self, receiver, message):
        '''
        Sendet eine Mitteilung (message) an einen durch Empfänger (receiver)
        :param message: Inhalt der Mitteilung
        :param receiver: Empfänger der Mitteilung
        '''
        print(f'from {self}')
        receiver.get_a_message(f'Content: {message}')

    def get_a_message(self, message):
        '''
        Empfängt eine Meldung und gibt diese am Stdout aus.
        :param message: eine Nachricht
        '''
        print(f'to {self}\n{message}')

    def __str__(self):
        return self.name


def main():
    # die beteilgten Objekte
    max = MiniChat('Max')
    moritz = MiniChat('Moritz')
    lempel = MiniChat('Lempel')
    # die Kommunikation
    max.send_a_message_to(moritz, f'hallo {moritz} wollen wir {lempel} ein wenig ärgern?')
    moritz.send_a_message_to(max, f'aber sicher')
    lempel.send_a_message_to(max, f'Lieber {max} das kann für dich und {moritz} böse enden')
    #
    # eigene Kommunikation mit eigenen Objekten


if __name__ == "__main__":
    main()
