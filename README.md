# Plant Detection with YOLOv5 and Django

## Dataset
- The Training Dataset is Downloaded from [Roboflow Universe](https://universe.roboflow.com/project-z499k/labelled-leaf).

## Setup Instructions

### 1. Install Anaconda
- Download and install Anaconda from [Anaconda's official website](https://www.anaconda.com/).

### 2. Create and Activate Virtual Environment
- Open Anaconda Prompt from the Windows Logo.
- Create a virtual environment:
    ```bash
    conda create -n plant_detection_env python=3.10
    ```
- Activate the virtual environment:
    ```bash
    conda activate plant_detection_env
    ```

### 3. Clone Repository and Install Dependencies
- Navigate to the cloned Plant_Detection repository.
- Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 4. Configure GPU (Optional)
- If using GPU, uninstall and reinstall PyTorch with GPU support:
    ```bash
    pip uninstall torch torchvision
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    ```

### 5. Run Django App
- Start the Django app:
    ```bash
    python manage.py runserver 127.0.0.1:4000
    ```

### 6. Test the Model
- Open a command prompt and run the following command to test the model with an image:
    ```bash
    curl -X POST -H "Content-Type: multipart/form-data" -F "image=@test/images/aloe-vera-leaf-1556184211-4872574-1-_jpeg.rf.bfe7928d4f5f2cd0b527e1ed1a58dfd3.jpg" http://127.0.0.1:4000/upload_image/
    ```
- Replace the image name with other images from the `test/images/` directory or from the internet for testing.

**Note:** Ensure proper path configurations and permissions while running the commands.
