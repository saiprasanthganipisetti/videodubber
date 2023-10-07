
#@@@@@@@@@@ Audio from Video @@@@@@@@@@@@

def extract_from_sys(path):
        video = VideoFileClip(path)
        audio = video.audio
        timestamp = str(datetime.datetime.now())[:19]
        audio_file_title = "media/audio" + re.sub(r"[-:. ]","",timestamp) + ".mp3"
        audio.write_audiofile(audio_file_title)
        
def extract_from_yt(url):
    yt = YouTube(url) #creating object
    timestamp = str(datetime.datetime.now())[:19] #for assigning unique title to each audio file we extract
    audio_file_title = timestamp + yt.author 
    audio_file_title = "media/" + re.sub(r"[-:. ]","",audio_file_title)+'.mp3'
    # To get audio file from the url
    print("hello")
    audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    print("hel")
    audio.download(output_path='.',filename=audio_file_title)
    return audio_file_title


#@@@@@@@@@@@ Creation of SRT file@@@@@@@@@@@@

def generateSRT(audio):
    transcription = model.transcribe(audio)
    f = open('transcripts/english-transcript.txt','w',encoding='utf-8')
    f.write(transcription['text'])
    count = 1
    flag = 0
    temp_text = ""
    with open("subtitles/english_srt.srt", "w") as srt_file:
        for segment in transcription["segments"]:
            text = segment["text"]
            if text[-1] == '.':
                if flag == 0:
                    start_time = str(0) + str(segment["start"])
                    end_time = str(0) + str(segment["end"])
                    srt_file.write(f"{count}\n{start_time} --> {end_time}\n{text}\n\n")
                    count += 1
                else:
                    end_time = str(0) + str(segment["end"])
                    srt_file.write(f"{count}\n{start_time} --> {end_time}\n{temp_text+text}\n\n")
                    count += 1
                    flag = 0
                    temp_text = ""
            else:
                start_time = str(0) + str(segment["start"])
                temp_text += text
                flag = 1

    return "subtitles/english_srt.srt"

#@@@@@@@@@@ Text Translation @@@@@@@@@@@

def proper_srt(url):
    file = open(url,'r',encoding='utf-8')
    f = file.read()
    l = f.split('\n')
    t = []
    fin = []
    count = 1
    for i in l:
        i = i.strip()
        if i == '':
            t.insert(0,count)
            fin.append(t)
            t = []
            count += 1
        elif '-->' in i:
            p = i.split('-->')
            t.append(p[0].strip())
            t.append(p[1].strip())
        else:
            if len(t) == 2:
                t.append(i)
            elif len(t) == 3:
                t[2] += ' '+i
    return fin


def translate_text(srt_file, to_language):
    srt_array = self.proper_srt(srt_file)[:-1]
    print(srt_array)
    filename = "subtitles/translated_srt.srt"
    wr = open(filename,'w',encoding='utf-8')
    for i in range(len(srt_array)): #srt is an array in the form:[[1,'00.0','04.0',"Welcome, everyone."]]
        count, start_time, end_time, text = srt_array[i]
        translated_text = mt.translate(text, to_language)
        srt_array[i][3] = translated_text
        wr.write(f"{count}\n{start_time} --> {end_time}\n{translated_text}\n\n") #It is the step that makes translated_srt.srt
    return srt_array


#@@@@@@@@@@@@ Voice generation from text @@@@@@@@@@@@

def generateAudioFiles(source):
    count = 1
    audios_list = source
    for i in range(len(source)):
        telugu_text = source[i][3]
        title = "./audios/gtts"+str(count)+".mp3"
        tts = gTTS(text=telugu_text, lang='te') 
        tts.save(title)
        audios_list[i][3] = title 
        count += 1
    return audios_list

#@@@@@@@@@@@@@ Creating dubbed audio(combining audios based on timeline)

