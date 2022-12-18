def print_in_color(txt, color):
  if color == "red":
    print("\033[31m",txt, end="")
  if color =="green":
    print("\033[32m",txt, end="")
  if color=="blue":
    print("\033[0;34m",txt, end="")
  if color=="purple":
    print("\033[0;35m",txt, end="")
  if color=="yellow":
   print("\033[1;33m",txt, end="")
  if color=="cyan":
    print("\033[0;36m",txt, end="")
  if color=="white":
    print("\033[1;37m",txt, end="")
  if color=="pink":
    print("\033[1;35m",txt, end="")
  if color=="gray":
    print("\033[0;30m",txt, end="")
  if color=="black":
    print("\033[0;30m",txt, end="")
  if color=="lightgray":
    print("\033[0;37m",txt, end="")
  if color=="lightred":
    print("\033[1;31m",txt, end="")
  if color=="lightgreen":
    print("\033[1;32m",txt, end="")
  if color=="orange":
    print("\033[1;33m",txt, end="")
  if color=="lightblue":
    print("\033[1;34m",txt,  end="")
  if color=="white":
    print("\e[0;37m",txt, end="")