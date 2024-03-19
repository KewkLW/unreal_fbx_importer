#imports fbx files and then creates a folder for each fbx file.
import unreal
import os

def import_fbx_files(fbx_files):
    # Get the content browser asset tools
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

    # Set the destination folder name (Game is the content browser)
    destination_folder = "/Game/Buildings"

    # Check if the Buildings folder exists, create it if it doesn't
    if not unreal.EditorAssetLibrary.does_directory_exist(destination_folder):
        unreal.EditorAssetLibrary.make_directory(destination_folder)

    # Iterate over the specified FBX files
    for fbx_file in fbx_files:
        # Extract the FBX file name without the extension
        fbx_name = os.path.splitext(os.path.basename(fbx_file))[0]

        # Create a new folder with the FBX name inside the Buildings folder
        folder_path = os.path.join(destination_folder, fbx_name)
        unreal.EditorAssetLibrary.make_directory(folder_path)

        # Import the FBX file into the newly created folder
        task = unreal.AssetImportTask()
        task.filename = fbx_file
        task.destination_path = folder_path
        task.replace_existing = True
        task.automated = True
        task.save = True

        asset_tools.import_asset_tasks([task])

    print("FBX files imported and organized successfully!")

# Specify the paths to your FBX files
fbx_files = [
    r"C:\path\file1.fbx",
    r"C:\path\file2.fbx"
]

# Call the function to import and organize the FBX files
import_fbx_files(fbx_files)