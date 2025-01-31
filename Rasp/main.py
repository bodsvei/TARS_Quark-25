from stot import recordText, writeText



if __name__ == "__main__":
    while True:
        text = recordText()
        print(text)
        out = writeText(text)

