"""Question bank + grading for the Kognity Computer Science (Topic 1) quiz.

Question types
  blank  : sentence with ___ gaps; "answers" is a list (one list of accepted words per gap)
  text   : typed answer; either "accepted" (strings) or "numeric" (+ "tol")
  choice : multiple choice; options[0] is ALWAYS the correct one (shuffled when served)
"""
import re

SECTIONS = [
    "Number systems",
    "Text, sound and images",
    "Data storage and compression",
    "Data transmission",
    "Error detection",
]

# fmt: off
QUESTIONS = [
    # ------------------------------------------------------------------ Number systems
    dict(section=0, type="blank",
         prompt="A ___ is a high-speed area of memory located within the CPU.",
         answers=[["register"]],
         explanation="A register is a small, ultra-high-speed area of memory within the CPU, used to temporarily store data during the fetch–decode–execute cycle."),
    dict(section=0, type="text",
         prompt="Convert the following negative denary integer into 8-bit two's complement.\n\n−11",
         accepted=["11110101"], display="11110101",
         explanation="Start with positive denary 11, which is binary 00001011.\nThen complement it (flip every bit), giving 11110100.\nThen add 1, giving 11110101."),
    dict(section=0, type="text",
         prompt="Convert the following positive denary integer into 8-bit two's complement value.\n\n76",
         accepted=["01001100"], display="01001100",
         explanation="Representing a positive binary number using two's complement is quite straightforward. You just have to remember to use all eight bits, regardless of the number being represented. (76 = 64 + 8 + 4 → 01001100)"),
    dict(section=0, type="text",
         prompt="What would be the new binary number after performing a 2-bit logical right shift on the following binary pattern?\n\n00110001",
         accepted=["00001100"], display="00001100",
         explanation="In a logical right shift, bits shifted off the right-hand end of the pattern are lost, and zeros are added at the left-hand end of the pattern."),
    dict(section=0, type="text",
         prompt="What would be the new binary number after performing a 1-bit logical left shift on the following binary pattern?\n\n00110001",
         accepted=["01100010"], display="01100010",
         explanation="In a logical left shift, every bit moves one place to the left: the bit shifted off the left-hand end is lost, and a zero is added at the right-hand end of the pattern. 00110001 → 01100010."),
    dict(section=0, type="blank",
         prompt="The ___ number system is the human readable number system, which consists of 10 digits.",
         answers=[["denary", "decimal"]],
         explanation="Denary (also called decimal, base 10) uses the digits 0–9 and is the number system people use every day."),
    dict(section=0, type="text",
         prompt="What would happen if the system tried to store a denary value greater than 255 in an 8-bit register?",
         accepted=["overflowerror", "overflow", "anoverflowerror", "overflowerroroccurs"], display="Overflow Error",
         explanation="Overflow errors occur when a computer system attempts to occupy its registers with a value that is one bit larger than its capacity, which might cause the system to crash."),
    dict(section=0, type="text",
         prompt="What is the result of adding 10101010 to 00110011 in binary?",
         accepted=["11011101"], display="11011101",
         explanation="Adding column by column from the right gives 11011101. Check in denary: 170 + 51 = 221, which is 11011101 in binary, and it still fits in 8 bits so there is no overflow."),
    dict(section=0, type="choice",
         prompt="One example of hexadecimal usage is…",
         options=["Displaying error messages", "Machine Code Programming", "High-Level language programming", "Designing presentation files"],
         explanation="Hexadecimal is used to display things like error messages and memory addresses in a short, readable form. Machine code is written in binary, and high-level languages use English-like keywords."),
    dict(section=0, type="choice",
         prompt="Which of the following is a benefit of using hexadecimal instead of binary?",
         options=["Shorter representation on the screen", "Uses less memory space", "Faster program execution", "Faster data transmission"],
         explanation="One hex digit represents four bits, so values are much shorter and easier for humans to read. The computer still stores and processes everything in binary, so memory use and speed don't change."),
    dict(section=0, type="blank",
         prompt="An overflow error will most likely cause the computer system to ___.",
         answers=[["crash"]],
         explanation="Overflow errors occur when a computer system attempts to occupy its registers with a value that is one bit larger than its capacity, which might cause the system to crash."),

    # ------------------------------------------------------------------ Text, sound and images
    dict(section=1, type="blank",
         prompt="All image file types, such as .jpg and .gif, use different ___ methods to store image data as binary.",
         answers=[["encoding"]],
         explanation="Computer systems represent images using several different file types, commonly including .jpg, .png and .gif. These file types all use different encoding methods, but they are all methods of storing image data as binary."),
    dict(section=1, type="blank",
         prompt="In the physical world, sounds are ___ waves that are constantly changing.",
         answers=[["analogue", "analog"]],
         explanation="Data from the physical world is continuously variable and changes in a smooth curve."),
    dict(section=1, type="blank",
         prompt="Emojis can be represented using the ___ character set.",
         answers=[["unicode"]],
         explanation="The ASCII character set is used to represent English characters, but Unicode can represent every character in every language, including Emojis."),
    dict(section=1, type="choice",
         prompt="Which of the following file types is an example of a sound file?",
         options=[".mp3", ".jpg", ".png", ".gif"],
         explanation=".mp3 is a compressed audio format. .jpg, .png and .gif are all image file types."),
    dict(section=1, type="blank",
         prompt="The number of characters that can be represented using ASCII is ___.",
         answers=[["128"]],
         explanation="Standard ASCII uses 7 bits per character, and 2⁷ = 128 different characters."),
    dict(section=1, type="text",
         prompt="The computer stores 'A' using binary as 01000001, so what would be the denary number of 'B'?",
         numeric=66, tol=0, display="66",
         explanation="The binary value of character A is 01000001, which is 65 in denary, so B is 66 in denary."),
    dict(section=1, type="text",
         prompt="Calculate how many bits are needed to store the phrase 'I love computer'.",
         numeric=120, tol=0, display="120",
         explanation="Each single character needs 8 bits, and there are 15 characters in the given phrase (including space characters), so the total number of bits needed is 8 × 15 = 120 bits."),
    dict(section=1, type="choice",
         prompt="What does ASCII stand for?",
         options=["American standard code for information interchange",
                  "Advanced system code for internet interchange",
                  "American standard calculation of information integration",
                  "Automated standard code for information interpretation"],
         explanation="ASCII stands for American Standard Code for Information Interchange. It is a character set that gives each character a numeric code."),
    dict(section=1, type="blank",
         prompt="The higher the colour depth, and the higher the resolution, the more data has to be stored. This means that increasing any of these values will ___ the file size.",
         answers=[["increase", "raise"]],
         explanation="A higher colour depth means more bits per pixel, and a higher resolution means more pixels. Both mean more data to store, so the file size increases."),
    dict(section=1, type="text",
         prompt="Calculate how many bits are needed to represent 512 colours in an image.",
         numeric=9, tol=0, display="9",
         explanation="log₂(512) = 9, because 2⁹ = 512."),
    dict(section=1, type="choice",
         prompt="In images, what is the number of bits per pixel called?",
         options=["Colour depth", "Resolution", "Sample rate", "Sample resolution"],
         explanation="The colour depth of the image refers to how many bits are used to store the colours in each pixel of the image. The higher the colour depth, and the higher the resolution, the more data has to be stored."),
    dict(section=1, type="blank",
         prompt="Pixel colour value can be represented using hexadecimal. For example, the black colour value is ___, while the white colour value is ___.",
         answers=[["000000"], ["ffffff"]],
         explanation="A hex colour has three pairs of digits (red, green, blue). 00 means none of that colour, so 000000 is black. FF is the maximum, so FFFFFF is white."),
    dict(section=1, type="choice",
         prompt="What is being described if a picture is said to be 1080 × 720?",
         options=["Resolution", "Colour depth", "File size", "Sample rate"],
         explanation="Image resolution refers to the number of pixels within an image, and this is normally described using the width and height of the image."),
    dict(section=1, type="blank",
         prompt="The higher the sample rate, and the higher the sample resolution, the more ___ the sound will be, but the file used to save the sound will be much ___.",
         answers=[["accurate"], ["larger", "bigger"]],
         explanation="More samples per second and more bits per sample copy the original analogue wave more closely (more accurate), but they also mean more data to store, so the file is larger."),
    dict(section=1, type="choice",
         prompt="The more bits that are used to measure the analogue wave, the…",
         options=["More accurate the sound, and the bigger the file size will be",
                  "Less accurate the sound, and the smaller the file size will be",
                  "More accurate the sound, and the smaller the file size will be",
                  "Less accurate the sound, and the bigger the file size will be"],
         explanation="Using more bits for each measurement records the wave more precisely, but every sample takes up more space, so the file gets bigger."),
    dict(section=1, type="choice",
         prompt="The number of bits used to record each measurement during the sampling process is called…",
         options=["Sample resolution", "Sample rate", "Frequency", "Compression ratio"],
         explanation="Sample resolution is the number of bits used for each measurement. (Sample rate is how many measurements are taken per second.)"),
    dict(section=1, type="choice",
         prompt="Digital sounds used by computers are made up of which of the following?",
         options=["Discrete signals", "Continuous waves", "Analogue waves", "Smooth curves"],
         explanation="Digital sounds, used by computers (and most of the music we listen to today) are made up of digital waves, a sequence of 'discrete' signals designed to give the illusion of a constantly changing sound, but in fact a complex series of 'on' and 'off' instructions."),
    dict(section=1, type="blank",
         prompt="The ASCII character set was replaced by ___ to fully encompass the languages and alphabets of the world.",
         answers=[["unicode"]],
         explanation="ASCII only covers English characters. Unicode can represent every character in every language, including emojis."),

    # ------------------------------------------------------------------ Data storage and compression
    dict(section=2, type="blank",
         prompt="Two drawbacks of using lossless compression rather than lossy compression are the ___ file size and ___ transmission speed.",
         answers=[["larger", "bigger"], ["slower"]],
         explanation="Lossless compression keeps all of the original data, so the compressed file is larger than a lossy one, and larger files take longer to transmit."),
    dict(section=2, type="choice",
         prompt="Which of the following does NOT describe how lossy compression is used to reduce the size of a sound file?",
         options=["Data will not be removed", "Some data is permanently removed", "Less important detail is discarded", "Quality is traded for a smaller file"],
         explanation="Lossy compression does permanently remove some data from the original source file."),
    dict(section=2, type="text",
         prompt="State the name of the lossless compression technique that involves encoding 'runs' of the same data as a value and a number of repetitions.",
         accepted=["runlengthencoding", "rle", "runlengthencodingrle"], display="Run Length Encoding (RLE)",
         explanation="A lossless compression algorithm achieves this by finding groups of repeating data and recording this data only once, along with the number of times it was repeated. This is known as run-length encoding (RLE)."),
    dict(section=2, type="blank",
         prompt="In ___ compression, data will not be lost from the original file. After the file has been uncompressed, the result is exactly the same as the original file.",
         answers=[["lossless"]],
         explanation="Lossless compression stores the data in a different way but loses nothing, so decompressing gives back an exact copy of the original."),
    dict(section=2, type="choice",
         prompt="Which of the following would be the effect of compressing a movie file using a lossy compression technique?",
         options=["Decreased file size and quality", "Decreased file size, same quality", "Increased file size and quality", "Increased file size, decreased quality"],
         explanation="Lossy compression permanently removes some data from the original source file. This means smaller file sizes and lower storage requirements. However, the trade-off is lower-quality files."),
    dict(section=2, type="choice",
         prompt="Which of the following does NOT describe how lossless compression is used to reduce the size of a sound file?",
         options=["Discards any unnecessary sounds", "Uses an algorithm to store data differently", "Can be undone to give back the exact original", "Records repeated data once with a count"],
         explanation="Lossless compression does not lose any data from the original file. Instead it uses an algorithm to store its data in a different way. After the file has been uncompressed, the result is exactly the same as the original file."),
    dict(section=2, type="blank",
         prompt="Most compressed file types fall into one of two categories: ___, which loses some data from the file, and ___, which retains all the data but stores it differently.",
         answers=[["lossy"], ["lossless"]],
         explanation="Lossy compression permanently discards some data for a smaller file. Lossless compression keeps every bit of data, just stored more efficiently."),
    dict(section=2, type="blank",
         prompt="Files that have had no compression applied are called ___ files.",
         answers=[["raw"]],
         explanation="Raw files are uncompressed, so they hold all of the original data and are usually very large."),
    dict(section=2, type="blank",
         prompt="Compression is normally used for three different file types: sound files, ___ files and video files.",
         answers=[["image", "images", "picture"]],
         explanation="Sound, image and video files are all large, so they benefit the most from compression."),
    dict(section=2, type="choice",
         prompt="Which of the following is NOT a benefit of file compression?",
         options=["Reducing the file quality", "Saving storage space", "Increasing data transmission speed", "Using less bandwidth"],
         explanation="Compression is the act of reducing the logical size of a file to something much smaller than the original size, to save storage space, increase data transmission speed and use less bandwidth. This can also sometimes reduce file quality, but that is not an aim of compression."),
    dict(section=2, type="blank",
         prompt="A compression ___ is a simple set of instructions that is applied to a file in order to reduce its size.",
         answers=[["algorithm"]],
         explanation="A compression algorithm is the set of step-by-step instructions used to shrink a file (for example run-length encoding)."),
    dict(section=2, type="choice",
         prompt="Which of the following is an aim of file compression?",
         options=["Save storage space", "Reduce the file quality", "Increase the file size", "Remove all the data"],
         explanation="Compression is the act of reducing the logical size of a file to something much smaller than the original size, to save storage space and improve processing time."),
    dict(section=2, type="text",
         prompt="You have a USB flash drive with 16 GiB free space. Approximately how many photographs of 128 KiB in size could the drive hold?",
         numeric=131072, tol=0, display="131,072",
         explanation="Convert 16 GiB to KiB: 16 × 1024 × 1024 KiB. Then divide by the size of one photo: (16 × 1024 × 1024) ÷ 128 = 131,072 photographs."),
    dict(section=2, type="text",
         prompt="Calculate the file size of a 3 minute sound file with 44.1 kHz sample rate and 8-bit sample resolution, in kibibytes (KiB).",
         numeric=7751.95, tol=1, display="7751.95 KiB",
         explanation="The 3 minutes is multiplied by 60 to convert it to seconds. This is then multiplied by 44100 (which is 44.1 kHz converted to Hz). Finally the answer is multiplied by the sample resolution of 8 and then converted to bytes (÷ 8) and kibibytes (÷ 1024).\n\n(3 × 60 × 44100 × 8) ÷ 8 ÷ 1024 ≈ 7751.95 KiB"),
    dict(section=2, type="text",
         prompt="Calculate the file size of a 50 second sound file with 44.1 kHz sample rate and 8-bit sample resolution, in kibibytes (KiB).",
         numeric=2153, tol=1, display="2153 KiB",
         explanation="File size = seconds × sample rate × sample resolution. So 50 × 44100 × 8 = 17,640,000 bits. ÷ 8 = 2,205,000 bytes. ÷ 1024 ≈ 2153 KiB."),
    dict(section=2, type="text",
         prompt="Calculate the file size of an image with a 2048 × 720 resolution and 256 colour values, in mebibytes (MiB).",
         numeric=1.41, tol=0.01, display="1.41 MiB",
         explanation="256 colours = 8-bit colour depth.\n2048 × 720 × 8 bits = 2048 × 720 bytes ÷ 1024 = 1440 KiB, then ÷ 1024 again = 1.406 MiB ≈ 1.41 MiB."),
    dict(section=2, type="choice",
         prompt="Which file type from the following will most likely have the largest file size?",
         options=["1 hour of a movie file", "10 pages of a text file", "1 hour of a music file", "10 pages of a programming code"],
         explanation="A movie stores a huge number of images plus sound for a whole hour, so it is far larger than music, text or code, which only store characters or audio."),
    dict(section=2, type="text",
         prompt="1 GiB = 2ˣ bytes.\n\nWhat is the value of x?",
         numeric=30, tol=0, display="x = 30",
         explanation="1 GiB = 1024 × 1024 × 1024 bytes = 2¹⁰ × 2¹⁰ × 2¹⁰ = 2³⁰ bytes, so x = 30."),

    # ------------------------------------------------------------------ Topic 2: Types and methods of data transmission
    dict(section=3, type="choice",
         prompt="Which of the following is true about encryption?",
         options=["It prevents unauthorised people from understanding the message.",
                  "It stops unauthorised people from intercepting the message.",
                  "It detects errors that happen during transmission.",
                  "It makes the message smaller so it is sent faster."],
         explanation="Encryption is the process of converting plaintext into ciphertext so that it cannot be understood by unauthorised people."),
    dict(section=3, type="choice",
         prompt="A company is hiring a new employee and it decides to send him the contract to sign via the internet. Which encryption method, symmetric or asymmetric, should the company use to make sure that the contract sent to the employee is highly secured?",
         options=["Asymmetric", "Symmetric"],
         explanation="Asymmetric encryption method is more secure than the symmetric one because it uses two different keys to encrypt and decrypt data."),
    dict(section=3, type="choice",
         prompt="Moustafa and Lilian are two students working on the same school project. Moustafa wants to send his completed project part to Lilian encrypted using a simple and fast method. Which method of encryption, symmetric or asymmetric, should Moustafa use?",
         options=["Symmetric", "Asymmetric"],
         explanation="Symmetric is easier and faster than asymmetric encryption. It uses only one secret key to encrypt and decrypt data."),
    dict(section=3, type="choice",
         prompt="Which of the following is NOT one of the asymmetric encryption steps?",
         options=["Both the sender and the receiver exchange the same key.",
                  "The receiver generates two keys (public and private).",
                  "The sender uses the receiver's public key to encrypt the data.",
                  "The receiver uses its private key to decrypt the data."],
         explanation="Using asymmetric encryption, the following steps are performed:\n• The receiver generates two keys (public and private)\n• The receiver's public key is sent to the sender\n• The sender uses the receiver's public key to encrypt the data\n• The sender sends the encrypted data to the receiver\n• The receiver uses its private key to decrypt the data\n\nExchanging the same key is what symmetric encryption does."),
    dict(section=3, type="choice",
         prompt="Which of the following is NOT one of the symmetric encryption steps?",
         options=["The sender replaces each letter with another one from the alphabet.",
                  "Both the sender and the receiver exchange the same secret key.",
                  "The sender encrypts the message with the secret key.",
                  "The receiver uses the secret key to decrypt the message."],
         explanation="Using symmetric encryption, the following steps are performed:\n• Both the sender and the receiver exchange the same secret key\n• The sender encrypts the message with the secret key\n• The sender sends the data to the receiver\n• The receiver uses the secret key to decrypt the message\n\nReplacing each letter with another one is a particular cipher (the Caesar cipher), not a step of the method."),
    dict(section=3, type="text",
         prompt="State the name of the simple encryption algorithm, which replaces each individual character in the text with another one from the alphabet.",
         accepted=["caesarcipher", "caesar", "caesarscipher"], display="Caesar cipher",
         explanation="The Caesar cipher is a simple substitution algorithm: each character is replaced by another one a fixed number of places along the alphabet."),
    dict(section=3, type="choice",
         prompt="Which of the following items is NOT needed to perform the encryption process?",
         options=["Ciphertext", "Plaintext", "An algorithm", "Encryption key"],
         explanation="To encrypt the data, the following items are needed:\n• Plaintext\n• An algorithm\n• Encryption key\n\nCiphertext is the result of encryption, not something needed to start it."),
    dict(section=3, type="choice",
         prompt="Which of the following best describes the half-duplex data transmission method?",
         options=["Data is transmitted in both directions, but one direction at a time.",
                  "Data is transmitted in one direction only.",
                  "Data is transmitted in both directions at the same time.",
                  "Data is transmitted one bit at a time along a single wire."],
         explanation="Using half-duplex, data packets are transmitted in both directions between devices, but one direction only at a time."),
    dict(section=3, type="text",
         prompt="What is USB short for?",
         accepted=["universalserialbus"], display="Universal Serial Bus",
         explanation="USB stands for Universal Serial Bus. It is a standard connection that transmits data serially, one bit after another."),

    # ------------------------------------------------------------------ Topic 2: Methods of error detection
    dict(section=4, type="text",
         prompt="Name the error detection method, which the following sentence describes: 'if the two sets of data (the one sent and the one received) are different there's no way of knowing whether the error occurred when originally sent, or when it was sent back to the sender'.",
         accepted=["echocheck", "echo"], display="Echo check",
         explanation="In echo check, the data might have been received correctly by the receiver but could have corrupted when the data was sent back to the sender."),
    dict(section=4, type="choice",
         prompt="Which of the following methods is NOT used in detecting errors in data transmission?",
         options=["Check digit", "Checksum", "Parity check", "Automatic Repeat Query (ARQ)"],
         explanation="Check digit is an error detection method used to check if the data is valid on entry, not during transmission."),
    dict(section=4, type="choice",
         prompt="Which of the following Automatic Repeat Query (ARQ) steps is incorrect?",
         options=["The receiving computer recalculates the checksum value.",
                  "It uses acknowledgement and timeout.",
                  "If there is no acknowledgement within a certain time frame, the data package is resent.",
                  "When the data received contains an error, a request is sent automatically to resend the data."],
         explanation="Automatic Repeat Query (ARQ):\n• Uses acknowledgement and timeout\n• Request is sent with data requiring acknowledgement\n• If no response/acknowledgement within certain time frame, data package is resent\n• When data received contains an error a request is sent automatically to resend the data\n• The resend request is repeatedly sent until packet is received error free/limit is reached/acknowledgement received"),
    dict(section=4, type="text",
         prompt="State the name of the error detection method that uses a system of acknowledgements and timeouts.",
         accepted=["automaticrepeatquery", "automaticrepeatqueryarq", "automaticrepeatrequest", "arq"],
         display="Automatic Repeat Query (ARQ)",
         explanation="Automatic Repeat Query (ARQ) sends an acknowledgement for data received correctly. If no acknowledgement arrives before the timeout, the data is resent."),
    dict(section=4, type="choice",
         prompt="A check digit is an error detection method used to validate input data and is calculated as follows:\n1. From right to left, each digit in the code number is multiplied by its position\n2. The results are added together\n3. The total is divided by 11\n4. If the remainder is 0, then the code number and check digit are valid.\n\nIs the following code number valid or not?\n\n235148",
         options=["Valid", "Not valid"],
         explanation="2×6 + 3×5 + 5×4 + 1×3 + 4×2 + 8×1 = 66\n66 ÷ 11 = 6 with a remainder of 0.\n\nWhich means that the check digit (8) is valid."),
    dict(section=4, type="text",
         prompt="Using odd parity, what would be the parity bit for the binary number: 1000101?",
         accepted=["0"], display="0",
         explanation="The binary number 1000101 already has an odd number of 1s (three). Therefore, 0 should be added as the parity bit so that its parity will not change."),
    dict(section=4, type="choice",
         prompt="What is the main purpose of an error detection method?",
         options=["Maintain the accuracy of the data.",
                  "Make the data transmission faster.",
                  "Keep the data secret from unauthorised people.",
                  "Reduce the size of the data."],
         explanation="Error detection methods are used to help detect any error that might occur during the transmission of data."),
    dict(section=4, type="choice",
         prompt="Which of the following bytes has been transmitted incorrectly if an odd parity check has been used?",
         options=["01001011", "11000001", "01000000", "01001100"],
         explanation="With odd parity, every byte should contain an odd number of 1s. 01001011 contains an even number of 1s (four), so it must have been corrupted."),
    dict(section=4, type="choice",
         prompt="Which of the following bytes has been transmitted incorrectly if an even parity check has been used?",
         options=["01001001", "11001001", "01001000", "01001110"],
         explanation="With even parity, every byte should contain an even number of 1s. 01001001 contains an odd number of 1s (three), so it must have been corrupted."),
]
# fmt: on

for i, q in enumerate(QUESTIONS):
    q["id"] = i


def _norm(s):
    return re.sub(r"[^a-z0-9.]", "", str(s).lower()).rstrip(".")


def _number(s):
    m = re.search(r"-?\d+(?:\.\d+)?", str(s).replace(",", ""))
    return float(m.group()) if m else None


def grade(q, answer):
    """Return True if `answer` is correct for question dict `q`."""
    t = q["type"]
    if t == "choice":
        return str(answer) == q["options"][0]
    if t == "blank":
        if not isinstance(answer, list) or len(answer) != len(q["answers"]):
            return False
        return all(_norm(a) in [_norm(x) for x in acc]
                   for a, acc in zip(answer, q["answers"]))
    if t == "text":
        if "numeric" in q:
            n = _number(answer)
            return n is not None and abs(n - q["numeric"]) <= q.get("tol", 0)
        return _norm(answer) in [_norm(x) for x in q["accepted"]]
    return False


def correct_display(q):
    if q["type"] == "choice":
        return q["options"][0]
    if q["type"] == "blank":
        return " / ".join(acc[0] for acc in q["answers"])
    return q["display"]


def lessons(max_size=8):
    """Split each section into evenly sized lessons of at most max_size questions."""
    out = []
    for s, title in enumerate(SECTIONS):
        qs = [q["id"] for q in QUESTIONS if q["section"] == s]
        n_less = -(-len(qs) // max_size)
        size = -(-len(qs) // n_less)
        for k in range(n_less):
            ids = qs[k * size:(k + 1) * size]
            out.append(dict(id=len(out), section=s, unit=title,
                            title=f"{title} {k + 1}" if n_less > 1 else title,
                            ids=ids))
    return out
