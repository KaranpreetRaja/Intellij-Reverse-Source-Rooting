import os

def reverse_source_rooting(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    data = f.read()

                # Check to see if the package path has been simplified by comparing with file parent directory
                
                # get java line that has package
                package_line = [line for line in data.splitlines() if "package" in line][0]
                
                # get package name
                package_name = package_line.split(" ")[1].replace(";", "")

                # get file parent directory
                parent_dir = os.path.basename(os.path.normpath(root))

                # if the package name is the same as the parent directory, then the package path has been simplified
                if package_name != parent_dir:
                    # Replace the simplified package path with the actual package name
                    data = data.replace(package_name, parent_dir)

                    # Update the import statements to reflect the new package structure
                    # data = data.replace("import " + package_name, "import " + parent_dir)

                    # Write the updated data back to the file
                    with open(path, 'w') as f:
                        f.write(data)
                    continue

        for subdir in dirs:
            reverse_source_rooting(os.path.join(root, subdir))

directory = "/path/to/main/directory"
reverse_source_rooting(directory)
