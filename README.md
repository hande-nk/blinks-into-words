# blinks-into-words
Code to help turn blinks into Morse code then to words

Words are everything. For people with speech and language disorders, expressing thoughts, feelings, or social interaction can be a constant struggle. This project explores how emerging Brain-Computer Interface (BCI) technology can remove speech barriers and enable communication in new ways.

Using a Muse 2 EEG headset, we detect neural signals, interpret blinks as Morse code, and convert them into spoken words with Google Cloud Text-to-Speech. This repository provides a full pipeline for:

Streaming EEG data from Muse 2 using Petal Metrics and muse-lsl

Detecting blinks and translating them into Morse code

Converting Morse code into text

Synthesizing natural speech from text using TTS APIs

This project is a step toward accessible communication technology, helping users break free from speech limitations and interact naturally with the world.

Technologies: Python, Muse 2, BCI, Morse Code, Google Cloud Text-to-Speech, VS Code
