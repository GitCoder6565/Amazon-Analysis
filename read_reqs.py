import chardet

def read_with_encoding(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']
        print(f"Detected encoding for {filename}: {encoding}")
        return rawdata.decode(encoding)

try:
    content = read_with_encoding('requirements.txt')
    print("--- requirements.txt ---")
    print(content)
except Exception as e:
    # Try common encodings if chardet fails or just to be safe
    for enc in ['utf-16', 'utf-16-le', 'utf-16-be', 'latin-1']:
        try:
            with open('requirements.txt', 'r', encoding=enc) as f:
                print(f"--- requirements.txt ({enc}) ---")
                print(f.read())
                break
        except:
            continue
