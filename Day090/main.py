import os
import PyPDF2
from google.cloud import texttospeech
import time
from datetime import datetime



# Defining variables.
string_list = []
part_counter = 0
pdf_string = ""
# Getting the filepath of PDF file to read.

filepath = input("Please input the file path in the following format : C:/Users/guneoza/Desktop/pdf.pdf\n")

pdfFileObject = open(filepath, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject, strict=False)
num_pages = int(pdfReader.numPages)

# Reading the PDF and writing the text into a string
for pages in range(num_pages):
    pageObject = pdfReader.getPage(pages)
    print(pageObject.extractText())
    pdf_string += pageObject.extractText()
pdfFileObject.close()

# Getting rid of spaces
pdf_string = pdf_string.strip()
pdf_string = pdf_string.replace(" ", "")

# Dividing the string into multiple string by every 4999 character (since there is a 5000-character limit on Google text to speech.)
for index in range(0, len(pdf_string), 4998):
    item = pdf_string[index: index + 4998]
    string_list.append(item)

# Running the text to speech for every sub-string created.


for string in string_list:
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=string)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    date = datetime.now()
    part_counter += 1
    new_name = f"{date}_Part {part_counter}"
    # Enter Your folder path to store converted mp3's.
    folder_path = os.environ.get("FOLDER_PATH")
    with open(rf"{folder_path}/{new_name}.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file "{new_name}.mp3"')
        time.sleep(5)
