import unittest
import os
import filecmp
import main

class MainTest(unittest.TestCase):
  def test_endtoend(self):
    output_file = None
    try:
      speakers = [
        "Brandon (LordNerevar76)",
        "Andrew (tamantayoshi)",
        "Alex (somedoinks)"
      ]
      curr_dir = os.path.dirname(os.path.realpath(__file__))
      main.run(speakers, curr_dir, "test_transcript.txt")
      output_file = curr_dir + os.path.sep + \
        self._get_filename_starting_with(curr_dir, "smoothed")

      if output_file is None:
        raise Exception("Smoothed file never created")

      expected_output_file = curr_dir + os.path.sep + "test_smoothed.txt"

      self.assertTrue(filecmp.cmp(
        expected_output_file, 
        output_file, 
        shallow=False
      ))
    finally:
      if output_file is not None:
        os.remove(output_file)

  def _get_filename_starting_with(self, path, start):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) and filename.startswith(start):
            return filename
    return None

if __name__ == '__main__':
  unittest.main()