import ddddocr
def scan(path):
    ocr = ddddocr.DdddOcr()

    with open(path, 'rb') as f:
        image = f.read()

    res = ocr.classification(image)
    print(res)
    return res

# scan("code.jpg")
