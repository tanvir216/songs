import time
import sys

DEEP_RED = '\033[38;5;88m'
SOUL_PURPLE = '\033[38;5;54m'
GOLDEN_WARM = '\033[38;5;136m'
MIST_BLUE = '\033[38;5;24m'
MIST_WHITE = '\033[38;5;251m'
BOLD = '\033[1m'
RESET = '\033[0m'


def soulful_typing(text, color, delay=0.08):
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay) 
    print() 

if __name__ == "__main__":
    print("\n--- Playing: O Saathi (Atif Aslam) ---\n")
    time.sleep(1)

    soulful_typing("Allah mujhe dard ke kaabil bana diya", MIST_BLUE, 0.07)
    time.sleep(0.8)
    
    soulful_typing("Toofan ko hi kashti ka sahil bana diya", MIST_BLUE, 0.07)
    time.sleep(0.8)
    
    soulful_typing("Bechainiyan samait ke saare jahaan ki", GOLDEN_WARM, 0.08)
    time.sleep(0.6)
    
    soulful_typing("Jab kuch na ban saka to...", DEEP_RED, 0.09)
    time.sleep(0.4)
    soulful_typing("Mera dil bana diya...", DEEP_RED, 0.12)
    time.sleep(1.2)
    
    soulful_typing("🎵 O saathi... tere bina...", SOUL_PURPLE, 0.1)
    time.sleep(0.5)
    soulful_typing("Raahi ko karwan na mile...", GOLDEN_WARM, 0.08)
    time.sleep(1.0)
    
    soulful_typing("🎵 O saathi... tere bina...", SOUL_PURPLE, 0.1)
    time.sleep(0.5)
    soulful_typing("Saagar ko kinara na mile...", GOLDEN_WARM, 0.08)
    time.sleep(1.5)

    soulful_typing("Har waqt dil ko jo sataye", MIST_WHITE, 0.07)
    time.sleep(0.6)
    soulful_typing("Aisi kami hai tu...", DEEP_RED, 0.1)
    time.sleep(0.8)
    
    soulful_typing("Main bhi na jaanoon ye ki khud se", MIST_WHITE, 0.07)
    time.sleep(0.6)
    soulful_typing("Itna kabhi hai tu...", DEEP_RED, 0.1)
    time.sleep(1.5)

    soulful_typing("🎵 O saathi... tere bina...", SOUL_PURPLE, 0.1)
    time.sleep(0.5)
    soulful_typing("Raahi ko karwan na mile...", GOLDEN_WARM, 0.08)
    print("\n--- End of Lyrics ---")

 