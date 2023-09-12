def min_sec(min):
    scs = min * 60
    return scs

def sec_min(sec):
    tm = sec / 60
    return tm

if __name__=="__main__":
    min_sec()
    sec_min()