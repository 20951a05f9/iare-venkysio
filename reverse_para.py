import threading

class ReverseWordsThread(threading.Thread):
    def __init__(self, sentence):
        threading.Thread.__init__(self)
        self.sentence = sentence
        
    def run(self):
        words = self.sentence.split()
        reversed_sentence = " ".join(word[::-1] for word in words)
        self.sentence = reversed_sentence
        
    def getSentence(self):
        return self.sentence

s =open("text.txt","r")
original_para =s.read()

sentences = original_para.split(". ")

threads = []

# Create a thread for each sentence
for sentence in sentences:
    thread = ReverseWordsThread(sentence)
    thread.start()
    threads.append(thread)

# Wait for each thread to finish
for thread in threads:
    thread.join()

# Get the reversed sentences from each thread
reversed_sentences = [thread.getSentence() for thread in threads]

# Join the reversed sentences to form the reversed paragraph
reversed_para = ". ".join(reversed_sentences)

# Print the reversed paragraph
print("Reversed paragraph:")
print(reversed_para)
