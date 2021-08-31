from time import sleep
import keyboard

class Diary:
    def __init__(self, date):
        # 날짜
        self.date = date
        # 이모지
        self.emoji = ''
        # 일기 작성
        self.write = ''

    def set_date(self):

        print("\n╭──────────────────────────────✎")
        print("| 날짜를 입력하세요 ex)2021.06.04")
        date = input("╰─▗ ▘➤ ")

        # global diary_date
        # if date == diary_date:
        #     print("이미 존재하는 날짜 입니다. 다시 입력해 주세요.")


        self.date = 0 if date == '' else date
        # 예시를 보여줌(2021.06.04)

    def set_emoji(self):

        print("\n─────────── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ───────────")
        print("   1 : 기쁨 2 : 슬픔 3 : 화남 4 : 직접 작성")
        print("─────────── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ───────────")
        while True:
            print("\n╭─────────────────────────────────────✎")
            print("| 자신의 기분을 숫자로 입력해 나타내주세요.")
            jimo = input('╰─▗ ▘➤ ')
            moji = ""
            if jimo == '1':
                moji = '((o(´∀｀)o))'
                break

            elif jimo == '2':
                moji = '(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)'
                break

            elif jimo == '3':
                moji = '(ʘ言ʘ╬)'
                break

            elif jimo == '4':
                print("╭────────────────────ﾟ✧ *:･ﾟ✧")
                print('| 자신의 기분을 직접 작성하세요.')
                a = input("╰─▗ ▘➤ ")
                moji = a
                break
            #    입력을 하면 저장이 안됨, 4번을 선택하면 일기 출력 시 기분이 나오지 않음
            else:
                print("\n(\_(\ ═════════════════════════════════╗")
                print("(=' :') 1부터 4까지의 숫자만 입력하세요 ~♥ ┃")
                print("(,(')(') ══════════════════════════════╝")
                print()

            sleep(1)

        self.emoji = moji

        # 이모티콘을 숫자로 선택하게 함

    def set_write(self):

            print("\n╔═════════*.·:·.☽✧    ✦    ✧☾.·:·.*═════════╗")
            print("                일기를 작성합니다.")
            print("          엔터를 누르면 일기가 종료됩니다.")
            write = input("   ═══════════════•°• ⚠ •°•═══════════════\n  ")
            print("╚═════════*.·:·.☽✧    ✦    ✧☾.·:·.*═════════╝")
            sleep(1)

            if self.emoji == '((o(´∀｀)o))':
                print("\n .*.｡ﾟ･*･:*:｡*+。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.+*.｡ﾟ･*･:*:｡*。*｡:ﾟ+")
                print("                       ((o(´∀｀)o))")
                print("╭─────────────────────────────────────────────────────────╮")
                print("| 행복한 하루를 보내셨군요! 내일도 오늘같은 행복한 하루를 보낼거예요! |")
                print("╰─────────────────────────────────────────────────────────╯")
                sleep(1)
            elif self.emoji == '(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)':
                print("\n .*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*")
                print("                               (´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)")
                print("╭──────────────────────────────────────────────────────────────────────╮")
                print("| 우울할 하루를 보내셨군요ㅠ 내일의 행복한 하루를 기원하며 우리 모두 파이팅 하자구요! |")
                print("╰──────────────────────────────────────────────────────────────────────╯")
                sleep(1)
            elif self.emoji == '(ʘ言ʘ╬)':
                print("\n .*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*")
                print("                               (ʘ言ʘ╬)")
                print("╭─────────────────────────────────────────────────────────────────────╮")
                print("| 화나는 일이 있었던 하루였군요-_-! 내일은 화나는 일이 없기를 기원하며 모두 파이팅! |")
                print("╰─────────────────────────────────────────────────────────────────────╯")
                sleep(1)
            else:
                print("\n .*.｡ﾟ･*･:*:｡*+。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.*.｡ﾟ･*･:*:｡*。*｡:ﾟ+.*.｡ﾟ･*")
                print("                           ٩(๑•̀ㅂ•́)")
                print("╭─────────────────────────────────────────────────────────────╮")
                print("| 내일은 매우 행복한 하루를 보내실꺼예요! 내일도 활기찬 하루를 보내보아요! |")
                print("╰─────────────────────────────────────────────────────────────╯")
                sleep(1)

            self.write = write

    def update_write(self, old_contents):

        print("\n╔═════════*.·:·.☽✧    ✦    ✧☾.·:·.*═════════╗")
        print("                일기를 수정하세요.")
        print("          엔터를 누르면 일기가 종료됩니다.     ")
        modify = input("   ═══════════════•°• ⚠ •°•═══════════════\n  ")
        print("╚═════════*.·:·.☽✧    ✦    ✧☾.·:·.*═════════╝")
        sleep(1)
        if modify == '':
            modify = old_contents

        self.write = modify

    def set_diary(self):
        self.set_date()
        self.set_emoji()
        self.set_write()

    def __str__(self):
        return f'╭ ◜◝ ͡  {" "*len(self.write)+"   ◝ ͡ ◜◝╮"}\n  날짜 : {self.date} \n  기분 : {self.emoji} \n  일기 내용 : {self.write}  \n{"╰ ◟◞ ͜  "+len(self.write)*" "}  ◞ ͜ ◟◞ ╯\n O\n  °\n 　 ∧ ∧ \n　 (´･ω･) \n　 /　 ⌒ヽ \n 　(人＿＿つ_つ '