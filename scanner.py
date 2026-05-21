import cv2
import numpy as np

def warp_image(input_image_path, output_image_path, points):
    
    img = cv2.imread(input_image_path)
    if img is None:
        return False
        
    
    input_points = np.float32(points)
    
    (top_left, top_right, bottom_right, bottom_left) = input_points
    
    
    bottom_width = np.sqrt(((bottom_right[0] - bottom_left[0]) ** 2) + ((bottom_right[1] - bottom_left[1]) ** 2))
    top_width = np.sqrt(((top_right[0] - top_left[0]) ** 2) + ((top_right[1] - top_left[1]) ** 2))
    max_width = max(int(bottom_width), int(top_width))
    
    max_height = int(max_width * 1.414) # A4 比例
    
    
    converted_points = np.float32([[0, 0], [max_width, 0], [max_width, max_height], [0, max_height]])
    
    
    matrix = cv2.getPerspectiveTransform(input_points, converted_points)
    img_output = cv2.warpPerspective(img, matrix, (max_width, max_height))
    
    cv2.imwrite(output_image_path, img_output)
    return True