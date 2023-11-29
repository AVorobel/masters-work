import os
import random
import shutil

root_labels = './all_labels'
root_images = './all_images'

files = os.listdir(root_images)
n_files = len(files)
print('total files', n_files)

train, val, test = round(n_files * 0.7), round(n_files * 0.2), round(n_files * 0.1)

print('train val test split', train, val, test)
print('total sum', train + val + test)

for folder in ('train', 'val', 'test'):
    os.mkdir(f'./{folder}/')
    os.mkdir(f'./{folder}/images/')
    os.mkdir(f'./{folder}/labels/')

sets = {
    'train': train,
    'val': val,
    'test': test
}

for set_, num in sets.items():
    for _ in range(num):
        img = random.choice(files)
        img_name = '.'.join(img.split('.')[:-1])

        shutil.copy(f"{root_images}/{img}", f"./{set_}/images/")
        try:
            shutil.copy(f"{root_labels}/{img_name}.txt", f"./{set_}/labels/")
        except Exception as e:
            print(str(e))

        idx = files.index(img)
        files.pop(idx)
