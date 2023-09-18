from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in tqdm(range(333)):
    sleep(0.005)
print()

for num in ft_tqdm(range(10)):
    print(num)

ft_tqdm(range(10))