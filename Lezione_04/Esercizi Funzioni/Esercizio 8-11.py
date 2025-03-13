def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0) #rimuove il primo messaggio della lista
        print(message)
        sent_messages.append(message) #aggiunge i messaggi alla lista

messages = [
    "Ciao! Come va?",
    "Che bella giornata!"
    "Oggi piove!"
]

sent_messages = [] #lista vuota dei messaggi inviati

messages_copy = messages [:]

send_messages(messages_copy, sent_messages)

print("\nMessaggi originali:", messages)
print("Messaggi inviati:", sent_messages)