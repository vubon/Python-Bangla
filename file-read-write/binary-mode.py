with open("text.bin", "rb") as f:
    # f.write(str.encode("I am Bangladeshi."))
    t = f.read()
    text = bytes.decode(t)
    print(text)
    f.close()
