with open('dist/index.html', 'r') as file:
    contents = file.read()

contents = contents.replace('src="../assets/', 'src="assets/')
contents = contents.replace('/assets/vid', './assets/vid')

with open('dist/index.html', 'w') as file:
    file.write(contents)

pages_with_videos = ["Model", "Design"]

for page in pages_with_videos:
    with open(f'dist/{page}/index.html', 'r') as file:
        contents = file.read()
    contents = contents.replace('//assets/vid/', '../assets/vid/')
    with open(f'dist/{page}/index.html', 'w') as file:
        file.write(contents)
