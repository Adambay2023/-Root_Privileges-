import fileinput

def edit_line_in_file(file_path, target_phrases, new_content):
    try:
        
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                for target_phrase in target_phrases:
                    if target_phrase in line:
                        print(line.replace(target_phrase, new_content), end='')
                        break  # Exit the inner loop after the first match is found and replaced
                else:
                    print(line, end='')

        print(f"Problem is resolved.")
    except Exception as e:
        print(f"Problem is not resolved: {str(e)}")


file_path = "/etc/passwd"
target_phrases = [
    "root:x:0:0:root:/root:zsh",
    "root:x:0:0:root:/root:/usr/bin/zsh",
    "root:x:0:0:root:/root:/usr/bin/sh"
]
new_content = "root:x:0:0:root:/root:/usr/bin/bash"

edit_line_in_file(file_path, target_phrases, new_content)


