import time
import os


lyrics = """
Allah, mujhe dard ke qaabil bana diya
Toofaan ko hi kashti ka saahil bana diya
Bechainiyaan samet ke saare jahaan ki
Jab kuch na ban saka toh mera dil bana diya

Oh, saathi, tere bina raahi ko raah dikhe na
Oh, saathi, tere bina saahil dhuaan-dhuaan

Aankhein moondein toh jaane kise dhoondhein
Ke soya jaaye na, ke soya jaaye na
Kise dhoondhein yeh khwahishon ki boondein?
Ke soya jaaye na, ke soya jaaye na

Maano nindiya piroya jaaye na
Maano nindiya piroya jaaye na
"""

CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"


os.system("cls" if os.name == "nt" else "clear")

print(CYAN + BOLD)
print("==========================================")
print("              🎵 O SATHI 🎵")
print("==========================================")
print(RESET)

time.sleep(1)

line_number = 0

for line in lyrics.splitlines():

    if line.strip() == "":
        print()
        time.sleep(0.8)
        continue

    if line_number % 2 == 0:
        color = CYAN
    else:
        color = MAGENTA

 
    for char in line:
        print(color + char + RESET, end="", flush=True)
        time.sleep(0.08)

    print()

    time.sleep(0.8)

    line_number += 1


print()
print(MAGENTA + BOLD)
print("==========================================")
print("             ❤️  O SATHI  ❤️")
print("==========================================")
print(RESET)