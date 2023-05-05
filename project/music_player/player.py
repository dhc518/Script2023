import os
import tkinter as tk
from tkinter import filedialog
import pygame
import csv
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, USLT


def load_path_from_csv(csv_path, base_name):
    with open(csv_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == base_name:
                return row[1]
    return None

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("900x700")
        self.current_song_path = None
        self.stop = 0
        self.selected_list = 'current_music.csv'

        self.song_label = tk.Label(text="No song is playing", bd=1, relief="sunken")
        self.song_label.pack(side="bottom",padx=10,anchor="w")

        self.tag_list = tk.Listbox(self.root, bg="black", fg="white", width=60, height=30, selectbackground="gray", selectforeground="black")
        self.tag_list.pack(padx=10,side="right", anchor="ne")


        # self.entry = tk.Entry(width=50)
        # self.entry.bind('<Return>', self.change_lylic)
        # self.entry.pack(side="bottom", padx=10,pady=10,anchor="e")
        #
        # self.label = tk.Label(self.root, text="Lylics")
        # self.label.pack(side="bottom", padx=10,pady=10,anchor="e")

        self.tag_button = tk.Button(self.root, text="Tag", command=self.tag_re)
        self.tag_button.pack(side="bottom", padx=10, pady=10, ipadx=10, anchor="e")


        self.csv_list = tk.Listbox(self.root, bg="black", fg="white", width=60, selectbackground="gray", selectforeground="black")
        self.csv_list.pack(padx=10, pady=20,anchor="w")

        self.refresh_list()

        self.select_button = tk.Button(self.root, text="Select List", command=self.select_list)
        self.select_button.pack(padx=10,pady=20,anchor="w")

        self.entry = tk.Entry(width=50)
        self.entry.bind('<Return>', self.create_csv)
        self.entry.pack(padx=10,pady=10,anchor="w")

        self.playlist = tk.Listbox(self.root, bg="black", fg="white", width=60, selectbackground="gray", selectforeground="black")
        self.playlist.pack(padx=10,pady=20,anchor="w")

        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_music)
        self.add_button.pack(side="left", padx=50, pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(side="left", padx=10, pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(side="left", padx=50, pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side="left", padx=10, pady=10)


        # self.slider_time = tk.Scale(self.root, from_=0, to=100, orient="horizontal", length=200, command=self.update_status)
        # self.slider_time.pack()


        self.music_player = pygame.mixer.init()

    def change_lylic(self, event=None):
        song_name = self.playlist.get(tk.ACTIVE)
        song_path = load_path_from_csv(self.selected_list, song_name)
        audio = MP3(song_path, ID3=ID3)
        self.tag_list.delete(0, tk.END)
        tags = audio.tags
        audio["USLT::'eng'"] = f"{self.entry.get()}"
    def tag_re(self):
        song_name = self.playlist.get(tk.ACTIVE)
        song_path = load_path_from_csv(self.selected_list, song_name)
        audio = MP3(song_path, ID3=ID3)
        self.tag_list.delete(0, tk.END)
        tags = audio.tags
        if tags:
            self.tag_list.insert(tk.END, f"Title: {tags.get('TIT2', [''])[0]}")
            self.tag_list.insert(tk.END,f"Artist: {tags.get('TPE1', [''])[0]}")
            self.tag_list.insert(tk.END,f"Album: {tags.get('TALB', [''])[0]}")
        else:
            print("No ID3 tags found.")

        lyrics = audio.get("USLT::'eng'")  # eng : 언어 코드
        if lyrics:
            self.tag_list.insert(tk.END, f"Lyrics: {lyrics.text}")
        else:
            print("No lyrics found.")

    def create_csv(self, event=None):
        csv_title = self.entry.get()+'.csv'
        with open(csv_title, 'w', newline='') as f:
            f.close()
        self.refresh_list()
    def select_list(self):
        self.selected_list = self.csv_list.get(tk.ACTIVE)
        self.playlist.delete(0, tk.END)
        with open(self.selected_list,'r', newline='') as f:
            reader = csv.reader(f, skipinitialspace=True)
            for row in reader:
                song_name = row[0]
                self.playlist.insert(tk.END, song_name)
        self.playlist.pack(pady=20)

    def refresh_list(self):
        self.csv_list.delete(0, tk.END)
        files = os.listdir()
        basenames = [os.path.splitext(os.path.basename(file))[0] for file in files if file.endswith('.csv')]
        for basename in basenames:
            self.csv_list.insert(tk.END, basename+'.csv')

    def add_music(self):
        same = False
        song_path = filedialog.askopenfilename(title="Select Music", filetypes=(("mp3 files", "*.mp3"),))
        print(song_path)
        song_name = os.path.basename(song_path)
        #song_name = song_path

        with open(self.selected_list, 'r', newline='') as f:
            reader = csv.reader(f, skipinitialspace=True)
            for row in reader:
                if song_name == row[0]:
                    print('이미 존재하는 파일입니다.')
                    same = True
        if same == False: #같은 곡이 존재하지 않으면 추가
            with open(self.selected_list, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([song_name, song_path])

        self.playlist.delete(0, tk.END)
        with open(self.selected_list,'r', newline='') as f:
            reader = csv.reader(f, skipinitialspace=True)
            for row in reader:
                song_name = row[0]
                self.playlist.insert(tk.END, song_name)
        self.playlist.pack(pady=20)

    def play_music(self):
        song_name = self.playlist.get(tk.ACTIVE)
        song_path = load_path_from_csv(self.selected_list, song_name)
        if song_path:
            if self.current_song_path == song_path and self.stop !=1:
                pygame.mixer.music.unpause()

            else:
                pygame.mixer.music.load(song_path)
                self.current_song_path = song_path
                pygame.mixer.music.play(loops=0)
                self.stop = 0

            self.paused_time = 0
            self.song_label.config(text="Playing: {}".format(os.path.basename(self.current_song_path)))
        else:
            print('Song not found')

    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused_time = pygame.mixer.music.get_pos() / 1000.0

    def stop_music(self):
        pygame.mixer.music.stop()
        self.stop = 1



if __name__ == '__main__':
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
