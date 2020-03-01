def slogi_mne_vse(a):
    Sum = 0
    for i in range(1, a):
        if a % i == 0:
            Sum += i
    return Sum


for a in range(10000):
    b = slogi_mne_vse(a)
    v = slogi_mne_vse(b)
    if v == a:
        print(a, b)
