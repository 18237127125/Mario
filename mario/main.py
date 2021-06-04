import  pygame

from source import  tools,setup
from source.states import main_menu,load_screen,level
def main():
    #file = r'D:\CloudMusic\02.mp3'  # 音乐的路径
    #pygame.mixer.init()  # 初始化
    #track = pygame.mixer.music.load(file)  # 加载音乐文件
    #pygame.mixer.music.play()  # 开始播放音乐流

    state_dict ={
        'main_menu':main_menu.MainMenu(),
        'load_screen':load_screen.LoadScreen(),
        'level':level.Level()
    }
    game  = tools.Game(state_dict,'main_menu')
    game.run()

if __name__ =='__main__':
    main()