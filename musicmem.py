import pydub
import os

def make_cloze(start_point, end_point, prompt_len, ans_len, music_name, out_path):
    clips = []
    for i in range(start_point, end_point, prompt_len):
            prompt_clip = music[i:i+prompt_len]
            prompt_clip.fade_in(20).fade_out(20)
            prompt_clip_path = (out_path+"/"+music_name+"_"+str(i)+"_prompt.mp3")
            prompt_clip.export(prompt_clip_path,format='mp3')
            ans_clip = music[i:i+prompt_len+ans_len]
            ans_clip.fade_in(20).fade_out(20)
            ans_clip_path = (out_path+"/"+music_name+"_"+str(i)+"_ans.mp3")
            ans_clip.export(ans_clip_path, format='mp3')

            clips.append((prompt_clip_path, ans_clip_path))
    return(clips)


if __name__ == '__main__':
    music_file = './test_data/in_heaven.mp3'
    music = pydub.AudioSegment.from_mp3(music_file)
    music_name = music_file.split('/')[-1].split('.')[0]
    os.makedirs('./audio_data', exist_ok=True)
    start_point = 0
    end_point = 30 * 1000
    prompt_len = 5 * 1000
    ans_len = 5 * 1000
    end_len = 5 * 1000
    clip_list = make_cloze(start_point, end_point, prompt_len, ans_len, music_name, './audio_data')

    print(clip_list)

