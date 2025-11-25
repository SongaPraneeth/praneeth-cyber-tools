import string
import argparse

small_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)


def caesar_cipher(cipher:str,shift:int=13,mode:str="encrypt") -> str:
  plain_Text = ""
  effective_shift = shift if mode == "encrypt" else -shift
  
  for value in cipher:
    if value.islower():
      index = small_letters.index(value)
      plain_Text += small_letters[(index + effective_shift)%26]
      
    elif value.isupper():
      index = upper_letters.index(value)
      plain_Text += upper_letters[(index + effective_shift)%26]
      
    else:
      plain_Text += value

  return plain_Text

def caesar_banner():
  banner = r"""
 _____    ___    _____   _____    ___   ______          _____   _____  ______   _   _   _____  ______ 
/  __ \  / _ \  |  ___| /  ___|  / _ \  | ___ \        /  __ \ |_   _| | ___ \ | | | | |  ___| | ___ \
| /  \/ / /_\ \ | |__   \ `--.  / /_\ \ | |_/ /        | /  \/   | |   | |_/ / | |_| | | |__   | |_/ /
| |     |  _  | |  __|   `--. \ |  _  | |    /         | |       | |   |  __/  |  _  | |  __|  |    / 
| \__/\ | | | | | |___  /\__/ / | | | | | |\ \         | \__/\  _| |_  | |     | | | | | |___  | |\ \ 
 \____/ \_| |_/ \____/  \____/  \_| |_/ \_| \_|         \____/  \___/  \_|     \_| |_/ \____/  \_| \_|
                                                                                                   
  """
  print("*"*104)
  print(banner)
  print("*"*104)


def main():
  parser = argparse.ArgumentParser(description="Caesar Cipher CLI Tool")
  
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument("-e","--encrypt",action="store_true",help="Encrypt text")
  group.add_argument("-d","--decrypt",action="store_true",help="Decrypt text")
  
  parser.add_argument("-s","--shift", type=int, default=13, help="Shift Value")
  parser.add_argument("text",help="Text to process")
  
  args = parser.parse_args()
  
  mode = "encrypt" if args.encrypt else "decrypt"
  
  result = caesar_cipher(args.text, args.shift, mode)
  
  caesar_banner()
  
  print(f" Mode      : {mode}")
  print(f" Shift     : {args.shift}")
  print(f" Input     : {args.text}")
  print(f" Result    : {result}")

  
  
if __name__ == "__main__":
  main() 








