# 9.9.1
'''
1. You are restricted to what you can use from the imported class, rather than being free to use any. However
    it prevents the use of unneeded imports.
2. You dont have to have the class name in the call of the function, for example: math.sqrt vs sqrt.
3. The third one would be the best becasuse you are only using 2 parts of the class, so you can eliminat
    unnecessary imports.
4. Either answer 2 or 4, because you may want to be able to tell where the class is coming from if you use #2
    but if you wanted simplicity and better formatting #4 would be best
'''
# 9.9.2
import math
angles = [0, 90, 180, 270, 360]
for i in range(len(angles)):
    value = math.radians(angles[i])
    print(str(angles[i]) + ":")
    sin = math.sin(value)
    if(sin == 1 or sin == -1):
        print("Sine: " + str(sin))
    cos = math.cos(value)
    if(cos == 1 or cos == -1):
        print("Cosine: " + str(cos))
    tan = math.tan(value)
    if(tan == 1 or tan == -1):
        print("Tangent: " + str(tan))
    print("")