import speech_recognition as sr
import pyttsx3
import datetime
import smtplib
import requests
import webbrowser
import pywhatkit as kit
import wikipedia

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Capture voice input and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return ""


def send_email(to, content):
    """Send an email using SMTP."""
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_password")  # Enter your email and password
        server.sendmail("your_email@gmail.com", to, content)
        server.close()
        speak("Email has been sent.")
    except Exception as e:
        speak("Sorry, I was unable to send the email.")
        print(e)


def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def get_weather(city):
    """Fetch weather information."""
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        weather = data["main"]
        temperature = weather["temp"] - 273.15
        humidity = weather["humidity"]
        description = data["weather"][0]["description"]
        speak(
            f"The temperature is {temperature:.2f} degrees Celsius, humidity is {humidity}%, and the weather is {description}.")
    else:
        speak("Sorry, I couldn't find the city.")


def search_web(query):
    """Search the web using the query."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the results for {query}")


def main():
    """Main function for voice assistant."""
    speak("Hello, I am your advanced voice assistant. How can I help you?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I assist you today?")
        elif "time" in query:
            tell_time()
        elif "email" in query:
            speak("Who do you want to send the email to?")
            recipient = listen()
            speak("What is the content of the email?")
            content = listen()
            if recipient and content:
                send_email(recipient, content)
        elif "weather" in query:
            speak("Which city do you want the weather for?")
            city = listen()
            if city:
                get_weather(city)
        elif "search" in query:
            speak("What do you want me to search for?")
            search_query = listen()
            if search_query:
                search_web(search_query)
        elif "play" in query:
            song = query.replace("play", "")
            speak(f"Playing {song}")
            kit.playonyt(song)
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia,")
            speak(result)
        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I am not sure how to help with that.")


if _name_ == "_main_":
    main()