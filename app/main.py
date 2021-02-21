import sys
from datetime import datetime
import os
from app.transcriber import Transcriber

now = datetime.now()
transcript = "example_transcript.txt"

def run(speakers, working_dir=".", transcript_name=transcript):
  input_file_path = working_dir + os.path.sep + transcript_name
  new_filename = f'smoothed_{now.strftime("%m%d%Y-%H%M%S")}.txt'
  output_file_path = working_dir + os.path.sep + new_filename
  
  transcriber = Transcriber(
    input_file_path,
    output_file_path,
    speakers
  )

  transcriber.smoothen()

if __name__ == '__main__':
  run(list(sys.argv[1:]).copy())