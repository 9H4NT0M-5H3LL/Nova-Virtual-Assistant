from voiceback import talkvoice
from microphone import listenCmd
import os
def copy(command):
    if "from" not in command and "to" not in command:
        talkvoice("Copying files only works on the following directories: Desktop, Documents, Downloads, Pictures, videos. Say the source and then the destination like \"Desktop to Downloads\"")
        sd = listenCmd()
        print(sd)
        sd_list = sd.split(" ")
        s = sd_list[0]
        d = sd_list[2]
        source = s.capitalize()
        destination = d.capitalize()
        if source == "Download":
            source = "Downloads"
        print(destination)
        file_names = []
        for root, dirs, files in os.walk("/home/dv/{}".format(source)):
            for filename in files:
                file_names.append(filename)
        no_of_files = len(file_names)
        for i in range(no_of_files):
            print("{}. {}".format(i + 1, file_names[i]))
        talkvoice("Which file do you want to copy?")
        chce = listenCmd()
        choice = int(chce)
        print("[!]Debug: Your command: {}".format(choice))
        print("[+] Copying {} file: {} from {} to {}".format(choice,file_names[choice - 1], source, destination))
        srce = "/home/dv/" + source + "/" + file_names[choice - 1]
        dstn = "/home/dv/" + destination
        os.system("cp {} {}".format(srce, dstn))
        talkvoice("File has been successfully copied!")
    return
