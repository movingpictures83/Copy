import PyPluMA
import os

class CopyPlugin:
   def input(self, filename):
      self.myfile = filename
      #txtfile = open(filename, 'r')
      #self.lines = []
      #for line in txtfile:
      #   self.lines.append(line)

   def run(self):
      pass

   def output(self, filename):
      os.system("cp "+self.myfile+" "+filename)
      #filestuff2 = open(filename, 'w')
      #for line in self.lines:
      #    filestuff2.write(line)


