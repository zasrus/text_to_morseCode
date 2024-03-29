from code import code


def main():
  mesg = input('Enter your message: ')
  #mesg = 'the time is 12:00 e-mail dick at cd@supa.com'
  mesg_code = get_code(mesg.upper())
  for l in mesg_code:
    print(l, end="")


def get_code(text):
  message = []
  mcode = code
  for letter in text:
    if letter in mcode:
      message += f'{mcode[letter]} '
    elif letter == ' ':
      message.append('/')
    elif letter not in mcode:
      message.append(f'/"{letter}"/')
  return message


if __name__ == '__main__':
  main()
