import requests

def slice_file():
  file_path = 'cube.obj'
  with open(file_path, 'rb') as file:
    file_data = {'file': (file.name, file)}

    headers = {'Content-Type': 'multipart/form-data'}

    url = 'http://localhost:5000'
    response = requests.post(url, files=file_data, headers=headers)

  if response.status_code == 200:
    print("File uploaded successfully.")
    save_file(response)
  else:
    print("File upload failed. Status code:", response.status_code)
    print(response.text)
    
    
def save_file(response):
  print("Saving file")
  with open("sliced_model.gcode", 'wb') as gcode_file:
    gcode_file.write(response.content)
    
def send_file_to_printer():
  file_path = 'sliced_model.gcode'
  with open(file_path, 'rb') as file:
    file_data = {'file': (file.name, file)}

    headers = {'Authorization': 'Bearer 01D5BF4DAC3443CB9C18EDF42B36FBA8'}
    data = {'print': 'True'}
    
    url = 'http://192.168.0.119/api/files/local'
    response = requests.post(url, files=file_data, headers=headers, data=data)
    print(response.status_code)
    
slice_file()
send_file_to_printer()