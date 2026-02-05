try:
    with open('Amazon.csv', 'r', encoding='utf-8') as f:
        for i in range(5):
            print(f.readline().strip())
except UnicodeDecodeError:
    with open('Amazon.csv', 'r', encoding='latin-1') as f:
        for i in range(5):
            print(f.readline().strip())
except Exception as e:
    print(f"Error: {e}")
