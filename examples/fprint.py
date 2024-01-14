# Boiler plate stuff to start the module
import jpype


# Launch the JVM
jpype.startJVM(classpath=['FReader.jar'])

# import the Java modules
from com.OmolayoSeun import SampleApp

# Copy in the patterns from the guide to replace the example code
a = SampleApp()

values = [1, 2, 3, 4]
byte_arr = bytearray(values)

txt = a.call(False, byte_arr)


print(txt)

#print(byte_arr)
