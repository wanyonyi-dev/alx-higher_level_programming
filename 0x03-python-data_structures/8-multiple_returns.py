#!/usr/bin/python3
def multiple_returns(sentence):
    s = sentence
    t = ()
    if len(s) == 0:
        t += len(s),
        t += "None",
    else:
        t += len(s),
        t += s[0],
    return (t)
