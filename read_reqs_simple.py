encodings = ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin-1']
for enc in encodings:
    try:
        with open('requirements.txt', 'r', encoding=enc) as f:
            content = f.read()
            # If we successfully read things that look like packages, we're good
            if '==' in content or '>' in content or '\n' in content:
                print(f"--- requirements.txt ({enc}) ---")
                print(content)
                break
    except Exception as e:
        continue
