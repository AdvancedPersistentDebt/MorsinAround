import csv
import pyaudio
import morsecode

# Morse code tree, used for decoding
mc_tree = morsecode.MorseTree()  

# Setup audio stream
CHUNK = 1024  
FORMAT = pyaudio.paInt16 
CHANNELS = 1
RATE = 44100  
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Output CSV file
csv_file = open('output.csv', 'a')
csv_writer = csv.writer(csv_file)

print("Listening for Morse code. Press Ctrl+C to exit.")
try:
    while True:
        # Read audio chunk
        data = stream.read(CHUNK)  
        # Decode Morse code
        text = mc_tree.decode(data)  
        print(text)
        # Append text to CSV
        csv_writer.writerow([text])  

except KeyboardInterrupt:
    print("Exiting...")
    
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    csv_file.close()
