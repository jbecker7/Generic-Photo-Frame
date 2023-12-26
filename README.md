# Generic Photo Frame README

Welcome to Generic Photo Frame. With a few small edits, this project makes it really easy to replicate something like [this photo frame](https://www.amazon.com/gp/product/B091GPJFKL/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) in your browser locally or online if you want to deploy it.

## Getting Started

### Prerequisites

- **Git**: Ensure you have Git installed on your computer for cloning the repository. You can download Git from [the official website](https://git-scm.com/downloads).
- **Python**: Ensure you have Python installed on your computer. This is necessary to run the script that renames and generates the list of images. You can download Python from [the official website](https://www.python.org/downloads/).
1. **Clone the Project**: Open Terminal or Command Prompt and navigate to the directory where you want to clone the project (e.g. Desktop) by typing ```cd``` followed by the name of the directory. Then run the following command:

    ```
    git clone https://github.com/jbecker7/Generic-Photo-Frame
    ```
   

### Adding Your Photo Directory

1. **Prepare Your Images**: Place all the images you want to display in a single directory inside of the Generic Photo Frame folder. Make sure that these images are in `.jpg` format.

2. **Set the Directory Path**: Open the provided Python script (`rename_files.py`) in a text editor or IDE. Locate the line where `directory_path` is set and change its value to the path of your image directory. For example:
   
   ```
   directory_path = "/path/to/your/image/directory"
   ```

### Running the Python Script

1. **Open Terminal or Command Prompt**: Navigate to the folder where the Python script is located.

2. **Run the Script**: Execute the script by typing the following command and pressing Enter:
```
python3 rename_files.py
```
This script will rename the images in your specified directory to a standard format (Ima1.jpg, Ima2.jpg, etc.) and create an `images.json` file listing these images.

### Configuring the HTML File

1. **Set Image Path**: Open the HTML file (`index.html`) in a text editor. Locate the `imagePath` variable in the script section and set it to the path of your image directory relative to the HTML file. More specifically, on line 63 where it says
```
var imagePath = "your/image/path";
```
replace "your/image/path" with the path you want to use to your images

2. **Set Password**: In the same script section, you can also set the password required to view the gallery. Find the checkPassword function and set your desired password on line 66:
```
if (password === "your_password_here") {
```

replace "your_password_here" with the password you want to use.


### Opening the HTML Page

Open in a Browser: Double-click on the index.html file to open it in your default web browser. Alternatively, you can right-click the file and choose to open it with a specific browser.

Enter the Password: When prompted, enter the password you set in the HTML file to access the image gallery.


### Deployment

There are many ways to deploy this, which one to use comes down to user preference. Once a domain name and hosting are acquired, though, you just need to upload this directory and it will work (assuming you have already generated ```images.json``` by running the Python script).
