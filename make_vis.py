import markdown
import glob

files = {}

lang = "en"
place = "Uk"

file_structure = None
time_slice_partitions = None

###########################################################################
# You have to change the file pattern matching here to get the right files.
# it expects the last values to be day and month

for md_file in glob.glob("../vis/*.md*"):
    print("converting : ", md_file, " to html.")
    html_file = md_file[:-2]+"html"
    with open(md_file, 'r') as read_f, open(html_file, 'w') as write_f:

        mark_down_text = read_f.read()

        html = markdown.markdown(mark_down_text)

        write_f.write(html)

