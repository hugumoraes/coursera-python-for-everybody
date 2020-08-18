text = "X-DSPAM-Confidence:    0.8475"

nPos = text.find('0')
num = text[nPos : nPos + 10]
num = float(num)

print(num)

