<a name="readme-top"></a>
# QR Code Generator

This Python script generates a QR code image from a provided URL string. Make sure you have Python 3.10 installed before running the script.

### Prerequisites

* Python 3.10: Download and install Python 3.10 from [Python's official website](https://www.python.org/downloads/release/python-3100/).

* Upgrade Pip: Open your terminal and run the following command to upgrade `pip` to the latest version:  

  ```sh
  pip install --upgrade pip
  ```

- **Install QRCode Library**: Open your terminal and run the following command to install qrcode library:

  ```bash
  pip install qrcode
  ```
### Usage
Run the script with the following command:

  ```sh
python mydata-qrcode.py <image_path> <file_name> <qrcode_url>
```
Replace <image_path>, <file_name> and <qrcode_url> with the appropriate values:

* <image_path>: The path where you want to save the generated QR code image.

* <file_name>: The name you want to give to the generated QR code image file (include the file extension).

* <qrcode_url>: The URL string that you want to encode into the QR code.

## Example
  ```sh
python mydata-qrcode.py 'C:\exportfolder\\' 132615 https://mydatapi.aade.gr/myDATA/TimologioQR/QRInfo?q=testtest
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>
