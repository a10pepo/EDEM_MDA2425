import time
from termcolor import colored
import textwrap

#################################################
# Ask for an input passing a question
# and optionally a variable type (default: int).
#################################################
def ask_input(question, var_type=int):
  while True: 
    if var_type == int or var_type == float:
      try:
        print('\n' + question)
        return var_type(input())
      except ValueError:
        print(colored("Oooooops! That's not a valid number. Try again...", 'red'))
    elif var_type == str:
      try:
        print('\n' + question)
        return var_type(input())
      except ValueError:
        print(colored("Oooooops! That's not a valid string. Try again...", 'red'))

#################################################
# Loader in x seconds
#################################################
def loader(duration, color='green'):
  print('''
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''', end='\r')
  for i in range(49):
    print(colored('▓', color), end='', flush=True)
    interval = round(duration / 49, 2)
    time.sleep(interval)

#################################################
# Header maker
#################################################
def make_header(title, subtitle, width=49, bg_color='blue', color='white'):
    if len(title) > width - 6:
        raise ValueError(f"Title is too long. Max length: {width - 6}, current length: {len(title)}")

    def create_colored_block(width, color):
        return colored('█' * width, color)

    def create_title_line(title, width, bg_color, color):
        left_padding = 3
        right_padding = width - len(title) - left_padding
        return (
            create_colored_block(left_padding, bg_color) +
            colored(title, color, f'on_{bg_color}', attrs=['bold']) +
            create_colored_block(right_padding, bg_color)
        )

    def create_content_line(content, width):
        return f"{colored('█', bg_color)}  {colored(content, 'white', attrs=['bold']):<{width+8}} {colored('█', bg_color)}"

    bg_solid = create_colored_block(width, bg_color)
    border_bottom = colored('▀' * width, bg_color)

    title_line = create_title_line(title.upper(), width, bg_color, color)
    subtitle_lines = textwrap.wrap(subtitle, width - 6)
    subtitle_block = '\n'.join(create_content_line(line, width) for line in subtitle_lines)

    empty_line = create_content_line('', width)

    print(f"""
{bg_solid}
{title_line}
{bg_solid}
{empty_line}
{subtitle_block}
{empty_line}
{border_bottom}
""")