import fileinput

def edit_line_in_file(file_path, target_phrase, new_content):
    try:
        
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if target_phrase in line:
                    print(line.replace(target_phrase, new_content), end='')
                else:
                    print(line, end='')

        print(f"Problem is resolved.")
    except Exception as e:
        print(f"Problem is not resolved: {str(e)}")


file_path = "/etc/passwd"
target_phrase = "root:x:0:0:root:/root:zsh"
new_content = "root:x:0:0:root:/root:/usr/bin/bash"

edit_line_in_file(file_path, target_phrase, new_content)
