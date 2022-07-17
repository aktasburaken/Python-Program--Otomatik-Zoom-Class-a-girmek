import subprocess
import datetime
import time
import multiprocessing
from multiprocessing import Process
import pyautogui as pg

today = datetime.datetime.today()

# Close microphone #
# Time sleeps are much because of my computer :D
pg.click(0, 767)
time.sleep(10)
pg.click(152, 751)
time.sleep(10)
pg.write('mikrofonunuza eri')
time.sleep(10)
pg.click(214, 200)
time.sleep(10)
pg.click(355, 513)


########################## AYŞİN #########################################

AysinTheHour1 = 8
AysinTheMinute1 = 30
AysinTheHour2 = 9
AysinTheMinute2 = 15
AysinTheHour3 = 10
AysinTheMinute3 = 00
AysinTheHour4 = 10
AysinTheMinute4 = 45
AysinTheHour5 = 11
AysinTheMinute5 = 30

if(today.strftime("%A") == "Monday" or "Wednesday"):

    def lessonOne():
        if (AysinTheHour1 != today.hour):
            time.sleep(50)
            lessonOne()

        if (AysinTheHour1 == today.hour):
            if (AysinTheMinute1 != today.hour):
                time.sleep(50)
                lessonOne()

        if (AysinTheHour1 == today.hour):
            if(AysinTheMinute1 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')  # Zoom Path

                def write():
                    time.sleep(15)
                    pg.write('4818773584')  # Meeting ID

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('8XSgyB')  # Password

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def lesson2():
                    time.sleep(2000)
                    lessonTwo()

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=lesson2)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()

    lessonOne()

    #############################################################################

    def lessonTwo():
        if (AysinTheHour2 != today.hour):
            time.sleep(50)
            lessonTwo()

        if (AysinTheHour2 == today.hour):
            if (AysinTheMinute2 != today.hour):
                time.sleep(50)
                lessonTwo()

        if (AysinTheHour2 == today.hour):
            if(AysinTheMinute2 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')

                def write():
                    time.sleep(15)
                    pg.write('4818773584')

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('8XSgyB')

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def lesson2():
                    time.sleep(2000)
                    lessonThree()

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=lesson2)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()

        #############################################################################

    def lessonThree():
        if (AysinTheHour3 != today.hour):
            time.sleep(50)
            lessonThree()

        if (AysinTheHour3 == today.hour):
            if (AysinTheMinute3 != today.hour):
                time.sleep(50)
                lessonThree()

        if (AysinTheHour3 == today.hour):
            if(AysinTheMinute3 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')

                def write():
                    time.sleep(15)
                    pg.write('4818773584')

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('8XSgyB')

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def lesson3():
                    time.sleep(2000)
                    lessonFour()

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=lesson3)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()

        #################################################################################

    def lessonFour():
        if (AysinTheHour4 != today.hour):
            time.sleep(50)
            lessonFour()

        if (AysinTheHour4 == today.hour):
            if (AysinTheMinute4 != today.hour):
                time.sleep(50)
                lessonFour()

        if (AysinTheHour4 == today.hour):
            if(AysinTheMinute4 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')

                def write():
                    time.sleep(15)
                    pg.write('4818773584')

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('8XSgyB')

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def lesson4():
                    time.sleep(2000)
                    lessonFive()

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=lesson4)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()

        #################################################################################

    def lessonFive():
        if (AysinTheHour5 != today.hour):
            time.sleep(50)
            lessonFive()

        if (AysinTheHour5 == today.hour):
            if (AysinTheMinute5 != today.hour):
                time.sleep(50)
                lessonFive()

        if (AysinTheHour5 == today.hour):
            if(AysinTheMinute5 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')

                def write():
                    time.sleep(15)
                    pg.write('4818773584')

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('8XSgyB')

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def openMicrophone():
                    time.sleep(1900)
                    pg.click(0, 767)
                    time.sleep(5)
                    pg.click(152, 751)
                    time.sleep(5)
                    pg.write('mikrofonunuza eri')
                    time.sleep(5)
                    pg.click(214, 200)
                    time.sleep(5)
                    pg.click(355, 513)

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=openMicrophone)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()

#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
########################## RİTA #########################################


if(today.strftime("%A") == "Tuesday" or "Thursday"):

    RitaTheHour1 = 8
    RitaTheMinute1 = 30
    RitaTheHour2 = 9
    RitaTheMinute2 = 25
    RitaTheHour3 = 10
    RitaTheMinute3 = 20
    RitaTheHour4 = 11
    RitaTheMinute4 = 15

    #########################################################################

    def lessonOne():
        if (RitaTheHour1 != today.hour):
            time.sleep(50)
            lessonOne()

        if (RitaTheHour1 == today.hour):
            if (RitaTheMinute1 != today.hour):
                time.sleep(50)
                lessonOne()

        if (RitaTheHour1 == today.hour):
            if(RitaTheMinute1 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')

                def write():
                    time.sleep(15)
                    pg.write('8202516857')

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('8XSgyB')

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def lesson2():
                    time.sleep(2000)
                    lessonTwo()

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=lesson2)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()

    lessonOne()

    #############################################################################

    def lessonTwo():
        if (RitaTheHour2 != today.hour):
            time.sleep(50)
            lessonTwo()

        if (RitaTheHour2 == today.hour):
            if (RitaTheMinute2 != today.hour):
                time.sleep(50)
                lessonTwo()

        if (RitaTheHour2 == today.hour):
            if(RitaTheMinute2 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')

                def write():
                    time.sleep(15)
                    pg.write('8202516857')

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('9Uf4nk')

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def lesson2():
                    time.sleep(2000)
                    lessonThree()

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=lesson2)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()

    #############################################################################

    def lessonThree():
        if (RitaTheHour3 != today.hour):
            time.sleep(50)
            lessonThree()

        if (RitaTheHour3 == today.hour):
            if (RitaTheMinute3 != today.hour):
                time.sleep(50)
                lessonThree()

        if (RitaTheHour3 == today.hour):
            if(RitaTheMinute3 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')

                def write():
                    time.sleep(15)
                    pg.write('8202516857')

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('9Uf4nk')

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def lesson3():
                    time.sleep(2000)
                    lessonFour()

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=lesson3)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()

    ################################################################################

    def lessonFour():
        if (RitaTheHour4 != today.hour):
            time.sleep(50)
            lessonFour()

        if (RitaTheHour4 == today.hour):
            if (RitaTheMinute4 != today.hour):
                time.sleep(50)
                lessonFour()

        if (RitaTheHour4 == today.hour):
            if(RitaTheMinute4 == today.minute):
                def sevgi():
                    time.sleep(5)
                    pg.click(746, 397)
                    time.sleep(5)
                    pg.click(726, 341)

                def click():
                    subprocess.call(
                        'C://Users//Casper//AppData//Roaming//Zoom//bin//Zoom.exe')

                def write():
                    time.sleep(15)
                    pg.write('8202516857')

                def clickJoin():
                    time.sleep(20)
                    pg.click(728, 591)

                def clickOnThePasscode():
                    time.sleep(25)
                    pg.click(660, 340)
                    time.sleep(1)
                    pg.write('9Uf4nk')

                def joinTheMeeting():
                    time.sleep(30)
                    pg.click(685, 587)

                def openMicrophone():
                    time.sleep(1900)
                    pg.click(0, 767)
                    time.sleep(5)
                    pg.click(152, 751)
                    time.sleep(5)
                    pg.write('mikrofonunuza eri')
                    time.sleep(5)
                    pg.click(214, 200)
                    time.sleep(5)
                    pg.click(355, 513)

                if __name__ == '__main__':

                    p1 = multiprocessing.Process(target=sevgi)
                    p2 = multiprocessing.Process(target=click)
                    p3 = multiprocessing.Process(target=write)
                    p4 = multiprocessing.Process(target=clickJoin)
                    p5 = multiprocessing.Process(target=clickOnThePasscode)
                    p6 = multiprocessing.Process(target=joinTheMeeting)
                    p7 = multiprocessing.Process(target=openMicrophone)

                    p1.start()
                    p2.start()
                    p3.start()
                    p4.start()
                    p5.start()
                    p6.start()
                    p7.start()
