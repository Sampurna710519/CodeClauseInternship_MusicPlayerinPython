import pygame
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Music Player in Python')
root.geometry("400x300")

pygame.mixer.init()

def open_file():
    song_file = filedialog.askopenfilename(initialdir="songs/", title="Pick a song to add", filetypes= [("Music Files", "*.mp3")])
    song_file = song_file.replace("E:/Python/CODECLAUSE/Music Player/songs/", "")
    song_list.insert(tk.END, song_file)

def open_many_files():
    song_files = filedialog.askopenfilenames(initialdir="songs/", title="Pick a song to add", filetypes= [("Music Files", "*.mp3")])

    for song_file in song_files:
        song_file = song_file.replace("E:/Python/CODECLAUSE/Music Player/songs/", "")
        song_list.insert(tk.END, song_file)

def play_music():
    song_file = song_list.get(tk.ACTIVE)
    song_file = f'E:/Python/CODECLAUSE/Music Player/songs/{song_file}'
    pygame.mixer.music.load(song_file)
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

global paused
paused = False

def pause_music(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next_music():
    next_song = song_list.curselection()
    next_song = next_song[0]+1
    song_file = song_list.get(next_song)
    song_file = f'E:/Python/CODECLAUSE/Music Player/songs/{song_file}'
    pygame.mixer.music.load(song_file)
    pygame.mixer.music.play(loops=0)

    song_list.selection_clear(0, tk.END)
    song_list.activate(next_song)
    song_list.selection_set(next_song, last=None)

def prev_music():
    next_song = song_list.curselection()
    next_song = next_song[0]-1
    song_file = song_list.get(next_song)
    song_file = f'E:/Python/CODECLAUSE/Music Player/songs/{song_file}'
    pygame.mixer.music.load(song_file)
    pygame.mixer.music.play(loops=0)

    song_list.selection_clear(0, tk.END)
    song_list.activate(next_song)
    song_list.selection_set(next_song, last=None)

song_list = tk.Listbox(root, bg = "maroon", fg="yellow", width=60, height=13, selectbackground="orange", selectforeground="white")
song_list.pack(pady=15)

play_button_img = tk.PhotoImage(file='images\play.png')
pause_button_img = tk.PhotoImage(file='images\pause.png')
stop_button_img = tk.PhotoImage(file='images\stop.png')
prev_button_img = tk.PhotoImage(file='images\previous.png')
next_button_img = tk.PhotoImage(file='images\playnext.png')

btn_frame = tk.Frame(root)
btn_frame.pack()

play_button = tk.Button(btn_frame, image=play_button_img, borderwidth=0, command=play_music)
play_button.grid(row=0, column=2, padx=7)

pause_button = tk.Button(btn_frame, image=pause_button_img, borderwidth=0, command=lambda:pause_music(paused))
pause_button.grid(row=0, column=1, padx=7)

stop_button = tk.Button(btn_frame, image=stop_button_img, borderwidth=0, command=stop_music)
stop_button.grid(row=0, column=3, padx=7)

prev_button = tk.Button(btn_frame, image=prev_button_img, borderwidth=0, command=prev_music)
prev_button.grid(row=0, column=0, padx=7)

next_button = tk.Button(btn_frame, image=next_button_img, borderwidth=0, command=next_music)
next_button.grid(row=0, column=4, padx=7)

song_menu = tk.Menu(root)
root.config(menu=song_menu)

add_song_to_list = tk.Menu(song_menu)
song_menu.add_cascade(label="Add Songs", menu=add_song_to_list)
add_song_to_list.add_command(label="Add a song to playlist", command=open_file)

add_song_to_list.add_command(label="Add more than one song to playlist", command=open_many_files)

root.mainloop()