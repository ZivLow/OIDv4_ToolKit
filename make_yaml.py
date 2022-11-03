# Create configuration
#import os
import yaml
config = {'path': '/home/ziv/speeding_catcher/yolov5/data/vehicle_and_plate',
         'train': '/home/ziv/speeding_catcher/yolov5/data/vehicle_and_plate/train',
         'val': '/home/ziv/speeding_catcher/yolov5/data/vehicle_and_plate/validation',
         'nc': 2,
         'names': ['Land vehicle', 'Vehicle registration plate']}

#script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
#file_path = os.path.abspath(os.path.join(script_dir, '..', '/yolov5/data/vehicle_and_plate.yaml'))
#file_path = os.path.relpath("../yolov5/data/vehicle_and_plate.yaml")

with open("vehicle_and_plate.yaml", "w") as file:
   yaml.dump(config, file, default_flow_style=False)