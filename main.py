import sys
from datetime import datetime

now = datetime.now()
transcript = "test_transcript.txt"

def run():
  speakers = list(sys.argv[1:]).copy()

  new_filename = f'smoothed_{now.strftime("%m%d%Y-%H%M%S")}.txt'

  with open(new_filename, 'a') as new_file:
    curr_speaker = None
    curr_section = ''
    first_section_add = True

    for line in open(transcript):
      line_speaker = get_speaker(line, speakers)

      if (line_speaker is None and curr_speaker is None):
        continue
      if (line_speaker is None and "0" in line and ":" in line):
        continue
      elif (curr_speaker != line_speaker and line_speaker is not None):
        if curr_speaker is not None:
          curr_section += '\n\n'
          new_file.write(curr_section)
          curr_section = ''
        curr_speaker = line_speaker
        curr_section = line.strip("\n") + '\n\n'
        first_section_add = True
      elif (line_speaker is None):
        if line.strip():
          if not first_section_add:
            curr_section += ' ' + line.strip("\n")
          else:
            curr_section += line.strip("\n")
            first_section_add = False
        else: # empty line
          continue
      elif (line_speaker == curr_speaker):
        continue
    
    if curr_section:
      new_file.write(curr_section)
  
  print(f'Smoothed transcription into new file {new_filename}')

def get_speaker(line, speakers):
  for speaker in speakers:
    if speaker in line:
      return speaker
  return None

if __name__ == '__main__':
  run()