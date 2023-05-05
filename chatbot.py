import json
import random

data = None

def multi_thread(text):
    global data
    cevap = ""
    metin = text.split()
    for key in data["multi"]:
        if key.startswith("set"):
            sub_keys = data["multi"][key].split("=")[-1].split()
            left_keyx = data["multi"][key].split("=")[0].split(",")
            for i in range(len(sub_keys)):
                for c in range(len(left_keyx)):
                    current_sub_key = sub_keys[i]
                    left_key = left_keyx[c].split("+")
                    if len(left_key) == 1:
                        for a in range(len(left_key)):
                            left_key1 = left_key[a].split("/")
                            for c in range(len(left_key1)):
                                if left_key1[c] in metin:
                                    response = data["multi"][current_sub_key.replace("$","")].split("/")
                                    if not any(item in cevap for item in response):
                                        if len(response) == 1:
                                            cevap += response[0] + " "
                                        else:
                                            cevap += random.choice(response) + " "
                    else:
                        sayac = 0
                        for a in range(len(left_key)):
                            left_key1 = left_key[a].split("/")
                            for c in range(len(left_key1)):
                                if left_key1[c] in metin:
                                    sayac=sayac+1
                        if len(left_key) == sayac:
                            response = data["multi"][current_sub_key.replace("$","")].split("/")
                            if not any(item in cevap for item in response):
                                sayac = 0
                                if len(response) == 1:
                                    cevap += response[0] + " "
                                else:
                                    cevap += random.choice(response) + " "
    if cevap == "":
        return None
    else:
        return cevap.strip() 

def single_thread(text):
    global data
    text = text.strip()
    if text in data["single"]:
        response = data["single"][text]
        if len(response) == 1:
            cevap = response[0] + " "
        else:
            cevap = random.choice(response) + " "
        return cevap.strip()
    else:
        return None

def cevapla(metin):
    global data
    with open("cb1.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    cevap = ""
    test = single_thread(metin)
    if test is not None:
        return test
    test = multi_thread(metin)
    if test is not None:
        return test
    return random.choice(data["multi"]["default"]).strip()

#print(cevapla(input("Bot a sor : ")))