"""
 Tufts University ME 30, Fall 2020
 client.py
 By:            Sawyer Bailey Paccione
 Completed:     12/8/2020
 Description:   Listens from the computer's default microphone, for the words
                in the global variable 'art', if they are heard, it will send
                information to the client to determine what it should do
 Purpose:       The client side code of Project 4 Art Installation
"""
import time # Used to wait after the user has been prompted

import speech_recognition as sr # Used to recognize speech

import pyaudio  # Dependency of Speech Recognition, also used to play audio
import wave
import sys
import requests

CHUNK = 1024

IP_ADDRESS = "130.64.143.39"

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occurred, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def search_keyword(audio):
    """
        Search the recorded speech for the name of a painting
        This information will then be sent to the client to be handled with
        appropriately
    """

    mona_lisa = ["mona", "lisa", "vinci", "leonardo"]
    the_scream = ["scream", "edvard", "munch", "screen"]

    for word in mona_lisa:
        if word.lower() in audio.lower():
            print("Mona Lisa \n")
            # send information for mona_lisa
            info = 'http://{ip}:5000/mona'.format(ip = IP_ADDRESS)
            reply = requests.get(info)

            print(info)
            return

    for word in the_scream:
        if word.lower() in audio.lower():
            print("The Scream \n")
            # send information for scream
            info = 'http://{ip}:5000/scream'.format(ip = IP_ADDRESS)
            reply = requests.get(info)
            print(info)
            return

    # send information for not recognizing
    print("Didn't Recognize That Painting")

def simulation_over(audio):
    if ("quit" in audio.lower()):
        return True


if __name__ == "__main__":
    # Constant
    PROMPT_LIMIT = 10

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    gameOver = False

    while (not gameOver):
        print('Speak! \n')
        for j in range(PROMPT_LIMIT):
            request = recognize_speech_from_mic(recognizer, microphone)
            if request["transcription"]:
                break
            if not request["success"]:
                break
            # Send Info For Try Again Maybe 4
            print("Sorry, Speak Again!")

        # show the user the transcription
        print("You said: {}".format(request["transcription"]))

        # determine if request is in the database
        search_keyword(request["transcription"])
        gameOver = simulation_over(request["transcription"])

    print("Thank You for playing \n")
