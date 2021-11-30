from ForcesAndMoments import Fx, Fy, Fz
from math import sqrt
from Attachment import main as attachment
import sys, os


class NoStdStreams(object):
    def __init__(self,stdout = None, stderr = None):
        self.devnull = open(os.devnull,'w')
        self._stdout = stdout or self.devnull or sys.stdout
        self._stderr = stderr or self.devnull or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        self.devnull.close()


with NoStdStreams():
    attachment_original_mass = attachment.findWeightAttachment()


# 1
F = sqrt(Fx**2 + Fy**2 + Fz**2)

def main(compressive_load: float, n_attachment: int):
    # 2
    load_per_attachment = compressive_load / n_attachment

    # 3
    ratio = F / load_per_attachment

    # 4
    attachment_mass = ratio * attachment_original_mass

    # 5
    total_attachment_mass = attachment_mass * n_attachment

    return total_attachment_mass


