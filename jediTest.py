import jedi
import cv2
print(jedi.Script("import cv2\ncv2.").completions())