import numpy as np
from tqdm import tqdm

from utils import to_number

def get_data(file):
    f = open(file, "r")
    translator_raw = f.readline()
    translator = []
    for c in translator_raw.strip():
        if c == ".":
            translator.append(0)
        else:
            translator.append(1)

    img = []
    f.readline()
    for line in f.readlines():
        row = []
        for c in line.strip():
            if c == ".":
                row.append(0)
            else:
                row.append(1)
        img.append(row)
    img = np.array(img)
    return img, translator


def enhance(img, translator, padding):
    new_img = np.zeros((img.shape[0] + 2, img.shape[1] + 2))
    img = np.pad(img, 2, 'constant', constant_values=padding).astype(int)
    for i in range(1, img.shape[0] -1):
        for j in range(1, img.shape[1] -1):
            nbs = img[i-1:i+2, j-1:j+2].flatten()
            idx = to_number(nbs)
            new_img[i-1, j-1] = translator[idx]

    return new_img

def first_solution(img, translator):
    img = enhance(img, translator, padding=0)
    img = enhance(img, translator, padding=1)
    print(np.sum(img))

def second_solution(img, translator):
    padding = 0
    for i in tqdm(range(50)):
        img = enhance(img, translator, padding=padding)
        padding = 1 - padding
    print(np.sum(img))

if __name__ == "__main__":
    img, translator = get_data("data/20.txt")

    # first_solution(img, translator)
    second_solution(img, translator)
