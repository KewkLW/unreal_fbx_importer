# FBX Importer and Organizer for Unreal Engine

This Python script is designed to import FBX files into Unreal Engine and automatically organize them into folders based on their file names. It simplifies the process of importing multiple FBX files and keeps your project structure clean and organized.

## Features

- Imports specified FBX files into Unreal Engine.
- Automatically creates folders for each FBX file inside a designated "Buildings" folder.
- Folder names are derived from the FBX file names.
- Supports importing multiple FBX files at once.
- Easy to use and integrate into your Unreal Engine project.

## Prerequisites

- Unreal Engine 4 or later.
- Python support in Unreal Engine.

## Usage

1. Open your Unreal Engine project.

2. Make sure you have Python support enabled in your project.

3. Create a new Python file in your project's script folder.

4. Copy the provided Python script into the new file.

5. Modify the `fbx_files` list in the script to include the paths to your FBX files. Example:
   ```python
   fbx_files = [
       r"C:\Users\username\Desktop\Exported FBX\Model1.fbx",
       r"C:\Users\username\Desktop\Exported FBX\Model2.fbx",
       r"C:\Users\username\Desktop\Exported FBX\Model3.fbx"
   ]
   ```

6. Optionally, you can change the `destination_folder` variable to specify a different folder name or path within your Unreal Engine project's Content Browser.

7. Save the Python file.

8. In the Unreal Editor, open the Python console or create a new Python script asset.

9. Execute the Python script.

10. The script will import the specified FBX files, create folders for each file inside the designated "Buildings" folder (or the specified destination folder), and place each FBX file in its respective folder.

11. Check the Content Browser in Unreal Engine to see the imported FBX files organized in their respective folders.

## Customization

- You can modify the `destination_folder` variable to change the name or path of the folder where the FBX files will be imported and organized.

- If you want to import FBX files from a different location, update the file paths in the `fbx_files` list accordingly.

- Feel free to extend or modify the script to suit your specific needs and project requirements.

## License

This script is provided under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.

## Acknowledgements

- The script utilizes the Unreal Engine Python API to interact with the editor and import FBX files.
- Thanks to the Unreal Engine community for their support and resources.

