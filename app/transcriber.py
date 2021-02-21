from pathlib import Path 

class Transcriber:
  def __init__(self, input_file_path, output_file_path, speakers):
    self.input_file_path = input_file_path
    self.output_file_path = output_file_path
    self.speakers = speakers
  
  def smoothen(self):
    with open(self.output_file_path, 'a') as new_file:
      curr_speaker = None
      curr_section = ''
      first_section_add = True

      for line in open(self.input_file_path):
        line_speaker = self._get_speaker(line)

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
  
    print(f'Smoothed transcription into new file {self._get_output_filename()}')

  def _get_speaker(self, line):
    for speaker in self.speakers:
      if speaker in line:
        return speaker
    return None

  def _get_output_filename(self):
    return Path(self.output_file_path).name