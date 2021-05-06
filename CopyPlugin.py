import PyPluMA

class CopyPlugin:
   def input(self, filename):
      #self.myfile = filename
      txtfile = open(filename, 'r')
      self.lines = []
      for line in txtfile:
         self.lines.append(line)

   def run(self):
      pass

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      for line in self.lines:
          filestuff2.write(line)


