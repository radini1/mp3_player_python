from pygame import mixer
from tkinter import Tk, Label, Button, filedialog

current_volume = float(0.5)

#Functions ( Main part)
def play_song():
    file_name = filedialog.askopenfilename(initialdir="c:/", title='please select a file.')
    current_song = file_name 
    song_title = file_name.split("/") 
    song_title = song_title[-1]  # getting the song file's name
    
    try:
        mixer.init()
        mixer.music.load(current_song) 
        mixer.music.get_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg='green', text='now playing : ' + str(song_title))
        volume_label.config(fg='green', text='volume : ', + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg='red', text='Error playing the track')
        
def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg='red', text='please first select the track.')
        
def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg='red', text='please first select the track.')
        
        
def reduce_volume():
    try:
        global current_volume 
        if current_volume <= 0:
            volume_label.config(fg='red', text='volume : muted')
            return 
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg='green' , text='volume : ' + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg='red', text='please first select the track.')

def increase_volume():
    try:
        global current_volume 
        if current_volume >= 1:
            volume_label.config(fg='green', text='volume : max volume')
            return 
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg='green' , text='volume : ' + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg='red', text='please first select the track.')
    
#Screen
main = Tk()
main.title('music player') 

#Labels
Label(main, text='custom music player.', font=("Calibri",15), fg='red').grid(sticky="N", row=0, padx=120)
Label(main, text='please select a music track.', font=("Calibri",12), fg='blue').grid(sticky="N", row=1)
Label(main, text='volume', font=("Calibri",12), fg='red').grid(sticky="N", row=4)
song_title_label = Label(main,font=("Calibri",12))
song_title_label.grid(sticky="N",row=3)
volume_label = Label(main, font=("Calibri",12))
volume_label.grid(sticky="N",row=5)

#Buttons
Button(main, text='select the song', font=("Calibri",12), command=play_song).grid(row=2, sticky="N")
Button(main, text='pause', font=("Calibri",12), command=pause).grid(row=3, sticky="E")
Button(main, text='resume', font=("Calibri",12), command=resume).grid(row=3, sticky="W")
Button(main, text='+', font=("Calibri",12), width=5, command=increase_volume).grid(row=5, sticky="E")
Button(main, text='-', font=("Calibri",12), width=5, command=reduce_volume).grid(row=5, sticky="W")

main.mainloop()


