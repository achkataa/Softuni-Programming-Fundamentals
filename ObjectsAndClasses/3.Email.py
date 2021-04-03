class Email:
    def __init__(self, sender, receiver, content, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        result = f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
        return result



emails = []
line = input()

while line != "Stop":
    data = line.split()
    sender = data[0]
    receiver = data[1]
    content = data[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()



inexes = [int(number) for number in input().split(", ")]

for x in inexes:
    emails[x].send()

for email in emails:
    print(email.get_info())