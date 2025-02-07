from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model(r"write your path to vosk")
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
mic = pyaudio.PyAudio()

# Find the default microphone
def find_microphone():
    print("\n🔍 Detecting available microphones...\n")
    for i in range(mic.get_device_count()):
        info = mic.get_device_info_by_index(i)
        print(f"🎤 {i}: {info['name']} - Input Channels: {info['maxInputChannels']}")
        if info["maxInputChannels"] > 0:
            return i  # Return the first available input device index
    return None

mic_index = find_microphone()
if mic_index is None:
    print("❌ No microphone found! Please check your connection.")
    exit(1)

# Open the microphone stream
stream = mic.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=8192,
    input_device_index=mic_index,
)

stream.start_stream()
print("\n🎤 Listening... Speak into the microphone!\n")

try:
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if len(data) == 0:
            break

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                print(f"📝 Recognized: {text}")

except KeyboardInterrupt:
    print("\n🛑 Stopping speech recognition...")

finally:
    stream.stop_stream()
    stream.close()
    mic.terminate()
    print("✅ Microphone closed, exiting.")
