# Plant_Detection
The Dataset is Downloaded from https://universe.roboflow.com/project-z499k/labelled-leaf
<br/>
The model use is Yolov5
<br/>
First of all Download Anaconda from https://www.anaconda.com/
<br/>
Open Anaconda Prompt from Window Logo
<br/>
type the commond: conda create -n plant_detection_env python=3.10
<br/>
After running the above command type: conda activate plant_detection_env
<br/>
Navigate to Plant_Detection cloned repo
<br/>
pip install -r requirements.txt
<br/>
if you are using cpu the requirements will run the model on cpu but if you have GPU run:
<br/>
pip uninstall torch torchvision 
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
<br/>
After the above step run: python manage.py runserver 127.0.0.1:4000
<br/>
The will start Django App
<br/>
Then open cmd and run command:  curl -X POST -H "Content-Type: multipart/form-data" -F "image=@test/images/aloe-vera-leaf-1556184211-4872574-1-_jpeg.rf.bfe7928d4f5f2cd0b527e1ed1a58dfd3.jpg" http://127.0.0.1:4000/upload_image/
<br/> 
In above command replace image name all images are in test/images/ for testing you can also use other images from internet
<br/>
