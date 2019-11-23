import pytesseract
import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: python ocr_simple.py image.jpg")
        exit(1)

    # read image path from command line
    imPath = sys.argv[1]

    # Uncomment the line below to provide path to tesseract manually
    # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    #define config parameters
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')

    image = cv2.imread(imPath, cv2.IMREAD_COLOR)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(image, config=config)

    print(text)