
import requests

# URL of the FastAPI endpoint for uploading
api_url = "https://mll-api-oi.onrender.com:8000/uploadfile/"  

# File path of the image you want to upload
image_path = "/Users/jarvis/pymycod/SIH/final-dataset/train/Acne and Rosacea /07PerioralDermNose.jpg"  # Replace with the actual image path

# Create a dictionary with the file to upload
files = {'file': open(image_path, 'rb')}

# Make the POST request to the API to upload the image
response_upload = requests.post(api_url, files=files)

# Check if the upload was successful
if response_upload.status_code == 200:
    data_upload = response_upload.json()
    uploaded_filename = data_upload['filename']
    print("Uploaded filename:", uploaded_filename)


    result_url = f"https://mll-api-oi.onrender.com:8000/predict/" 


    response_result = requests.get(result_url)


    if response_result.status_code == 200:
        result_data = response_result.json()
        print("Result:", result_data)
    else:
        print(f"Failed to retrieve result with status code: {response_result.status_code}")
else:
    print(f"Upload request failed with status code: {response_upload.status_code}")
