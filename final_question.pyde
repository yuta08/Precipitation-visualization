#ライブラリの追加
add_library('Minim')

#変数とリストの作成
date = []
Kanagawa = []
Aomori = []
Akita = []
Iwate = []
Yamagata = []
Miyagi = []
Fukushima = []
Ibaraki = []
Tochigi = []
Gunma = []
Saitama = []
Tokyo = []
Chiba = []
Yamanashi = []
Niigata = []
Nagano = []
Toyama = []
Ishikawa = []
Fukui = []
Gifu = []
Shizuoka = []
Aichi = []
Mie = []
Shiga = []
Nara = []
Wakayama = []
Kyoto = []
Osaka = []
Hyogo = []
Hokkaido = []
Tottori = []
Shimane = []
Hiroshima = []
Yamaguchi = []
Kagawa = []
Tokushima = []
Ehime = []
Kochi = []
Fukuoka = []
Oita = []
Saga = []
Kumamoto = []
Nagasaki = []
Miyazaki = []
Kagoshima = []
Okinawa = []
Okayama = []
i = 0
sound = 0
time_change = 0
j = []
loc_mouse = []
loc_x = [510,540,510,500,535,520,525,505,495,480,500,520,500,480,450,460,430,425,430,420,400,415,395,380,385,370,380,355,505,330,330,270,290,255,330,287,345,315,225,248,208,240,220,220,200,75,550]
loc_y = [150,180,170,205,205,240,265,260,265,280,275,290,280,230,270,300,250,275,300,235,270,310,290,290,320,315,330,290,290,285,305,305,310,310,320,341,330,342,333,340,345,390,380,400,370,615,100]
prefecture_name=["Aomori","Iwate","Akita","Yamagata","Miyagi","Fukushima","Ibaraki","Tochigi","Gunma","Yamanashi","Saitama","Chiba","Tokyo","Niigata","Nagano","Shizuoka","Toyama","Gifu","Aichi","Ishikawa","Fukui","Mie","Shiga","Kyoto","Nara","Osaka","Wakayama","Hyogo","Kanagawa","Tottori","Okayama","Shimane","Hiroshima","Yamaguchi","Kagawa","Ehime","Tokushima","Kochi","Fukuoka","Oita","Saga","Miyazaki","Kumamoto","Kagoshima","Nagasaki","Okinawa","Hokkaido"]
prefecture=[Aomori,Iwate,Akita,Yamagata,Miyagi,Fukushima,Ibaraki,Tochigi,Gunma,Yamanashi,Saitama,Chiba,Tokyo,Niigata,Nagano,Shizuoka,Toyama,Gifu,Aichi,Ishikawa,Fukui,Mie,Shiga,Kyoto,Nara,Osaka,Wakayama,Hyogo,Kanagawa,Tottori,Okayama,Shimane,Hiroshima,Yamaguchi,Kagawa,Ehime,Tokushima,Kochi,Fukuoka,Oita,Saga,Miyazaki,Kumamoto,Kagoshima,Nagasaki,Okinawa,Hokkaido]
music_change = 0
season_img = []
time_change = 0
screen = 0
data_prefecture=[[],[],[],[],[],[],[],[]]
data_point=[[],[],[],[],[],[],[],[]]
data_precipitation=[[],[],[],[],[],[],[],[]]
Loc_change=0
Loc_play=0
time = 0

#setup関数
def setup():
    #execfile('download_csv.py')
    size(700, 700)
    frameRate(10)
    
    #csvデータの読み込み
    todouhuken_csv()
    precipitation_csv()

    #画像の設定

    global img_j
    img_j=loadImage('img/japan.jpg')
    img_j.resize(width, height)
    season_img.append(loadImage('img/spring.png'))
    season_img.append(loadImage('img/summer.png'))
    season_img.append(loadImage('img/fall.png'))
    season_img.append(loadImage('img/winter.png'))
    for i in range(4):
        season_img[i].resize(100,100)

    #音楽の再生
    
    global minim, player
    minim = Minim(this)
    player = minim.loadFile('sound/muon.mp3')
    player.play()

#draw関数の作成
def draw():
    global screen,Loc_change,Loc_play,time
    #タイトル画面
    if screen == 0:
        background(195)
        fill(0)
        textAlign(CENTER, CENTER)
        textSize(50)
        text("Precipitation visualization", 350,180)
        fill(255)
        rect(150,300,400,60)
        rect(150,400,400,60)
        fill(0)
        textSize(20)
        text("2019 Precipitation Transition",width/2,328)
        text("This Week's Precipitation Transition",width/2,428)
    elif screen == 1:
        #画像
        image(img_j, 0, 0)
        for i in range (4):
            image(season_img[i],300+100*i,570)
    
        #時系列ストップ
        if time_change == 0:
            j.append(map(mouseX, 0, width, 0, 365))
            if len(j) >= 3:
                del(j[0])
            loc_mouse.append(mouseX)
            if len(loc_mouse) >= 3:
                del(loc_mouse[0])
        #合計の降水量
        rainfall = 0
        for i in range(47):
            rainfall += int(prefecture[i][int(j[-1])])
    
        #音楽
        global sound, minim, player
        if time_change == 0:
            if music_change == 0:
                if pmouseX != mouseX:
                    if rainfall <= 30:
                        player.pause()
                        player = minim.loadFile('sound/morning.mp3')
                        value = 5
                        player.setGain(value)
                        player.play()
                    elif rainfall <= 100:
                        player.pause()
                        player = minim.loadFile('sound/rain_1.mp3')
                        player.play()
                    elif rainfall <= 500:
                        player.pause()
                        player = minim.loadFile('sound/rain_2.mp3')
                        player.play()
                    elif rainfall <= 1000:
                        player.pause()
                        player = minim.loadFile('sound/rain_3.mp3')
                        player.play()
                    elif rainfall <= 2000:
                        player.pause()
                        player = minim.loadFile('sound/rain_4.mp3')
                        player.play()
                    else:
                        player.pause()
                        player = minim.loadFile('sound/rain_5.mp3')
                        player.play()
            else:
                if player.isPlaying() == True:
                    player.pause()
    
        #円の表示
        fill(0, 0, 255, 80)
        for i in range(47):
            ellipse(loc_x[i],loc_y[i],int(prefecture[i][int(j[-1])]),int(prefecture[i][int(j[-1])]))
    
        #下の表示
        fill(0)
        textAlign(CENTER, CENTER)
        textSize(15)
        text(date[int(j[-1])], loc_mouse[-1], height - 10)
        text(rainfall, loc_mouse[-1], height - 25)
        
        #音楽のミュートボタン
        if music_change == 0:
            pushMatrix()
            translate(630,10)
            fill(255)
            rect(0,0,60,60)
            fill(0)
            rect(5,20,10,20)
            beginShape()
            vertex(15,20)
            vertex(30,5)
            vertex(30,55)
            vertex(15,40)
            endShape()
            strokeWeight(5)
            line(35,30,50,30)
            line(35,20,50,4)
            line(35,40,50,56)
            strokeWeight(1)
            popMatrix()
        else:
            pushMatrix()
            translate(630,10)
            fill(255)
            rect(0,0,60,60)
            fill(0)
            rect(5,20,10,20)
            beginShape()
            vertex(15,20)
            vertex(30,5)
            vertex(30,55)
            vertex(15,40)
            endShape()
            popMatrix()
        pushMatrix()
        translate(width-70,80)
        noFill()
        rect(0,0,60,60)
        fill(0)
        rect(15,5,30,50)
        fill(255)
        stroke(0)
        beginShape()
        vertex(16,5)
        vertex(41,10)
        vertex(41,60)
        vertex(16,55)
        endShape()
        fill(0)
        ellipse(37,35,3,3)
        popMatrix()
        
        prefecture_name_display()
        season_display()
    elif screen == 2:
        time += 1
        background(195)
        for i in range(8):
            fill(0,0,255,190)
            try:
                rect(40+i*80,600,60,-int(data_precipitation[i][Loc_change])*10)
            except:
                textSize(60)
                text("No Data",width/2,height/2)
            fill(0)
            textSize(15)
            try:
                text(str(int(data_precipitation[i][Loc_change]))+"mm",70+i*80,590)
                text(str(month())+"/"+str(day()-(7-i)),70+i*80,610)
                for i in range(7):
                    line(70+i*80,600-int(data_precipitation[i][Loc_change])*10,70+(i+1)*80,600-int(data_precipitation[i+1][Loc_change])*10)
            except:
                pass
            
        textSize(30)
        text(data_prefecture[0][Loc_change],width/2,640)
        text(data_point[0][Loc_change],width/2,670)
        
        line(10,600,690,600)
        pushMatrix()
        translate(10,height-70)
        noFill()
        rect(0,0,60,60)
        fill(0)
        beginShape()
        vertex(5,30)
        vertex(25,10)
        vertex(25,50)
        endShape()
        rect(25,20,30,20)
        popMatrix()
        pushMatrix()
        translate(width-70,height-70)
        noFill()
        rect(0,0,60,60)
        fill(0)
        beginShape()
        vertex(55,30)
        vertex(35,10)
        vertex(35,50)
        endShape()
        rect(5,20,30,20)
        popMatrix()
        pushMatrix()
        translate(width-70,10)
        noFill()
        rect(0,0,60,60)
        fill(0)
        rect(15,5,30,50)
        fill(255)
        beginShape()
        vertex(16,5)
        vertex(41,10)
        vertex(41,60)
        vertex(16,55)
        endShape()
        fill(0)
        ellipse(37,35,3,3)
        popMatrix()
        
        if Loc_play == 0:
            pushMatrix()
            translate(10,10)
            noFill()
            rect(0,0,60,60)
            fill(0)
            beginShape()
            vertex(10,5)
            vertex(50,30)
            vertex(10,55)
            endShape()
            popMatrix()
            fill(0)
        else:
            pushMatrix()
            translate(10,10)
            noFill()
            rect(0,0,60,60)
            fill(0)
            rect(12,10,12,40)
            rect(36,10,12,40)
            popMatrix()
            fill(0)
            if time >= 3:
                Loc_change += 3
                time = 0
                if Loc_change >= 1293:
                    Loc_change = 0
                    Loc_play = 0
        
    elif screen == 3:
        background(195)
        screen = 4
    elif screen == 4:
        x = random(0,width)
        y = random(0,height)
        fill(255,0,0)
        textSize(30)
        text("Run \"download_csv.py\"",x,y)
        


#マウスクリック
def mouseClicked():
    global screen,music_change,time_change,Loc_change,Loc_play
    if screen == 0:
        if mouseX >= 150 and mouseX <= 550 and mouseY >= 300 and mouseY <= 360:
            screen = 1
        if mouseX >= 150 and mouseX <= 550 and mouseY >= 400 and mouseY <= 460:
            screen = 2
    elif screen == 1:
        if mouseX >= 630 and mouseX <= 690 and mouseY >= 10 and mouseY <= 70:
            if music_change == 0:
                music_change = 1
            elif music_change == 1:
                stop()
                music_change = 0
        elif mouseX >= 630 and mouseX <= 690 and mouseY >= 80 and mouseY <= 140:
            stop()
            screen = 0
        else:
            if time_change == 0:
                time_change = 1
            elif time_change == 1:
                time_change = 0
    elif screen == 2:
        if mouseX >= 10 and mouseX <= 70 and mouseY >= 630 and mouseY <= 690:
            if Loc_change == 0:
                Loc_change = 1292
            else:
                Loc_change -= 1
        if mouseX >= 630 and mouseX <= 690 and mouseY >= 630 and mouseY <= 690:
            if Loc_change == 1293:
                Loc_change = 0
            else:
                Loc_change += 1
        if mouseX >= 10 and mouseX <= 70 and mouseY >= 10 and mouseY <= 70:
            if Loc_play == 0:
                Loc_play = 1
            elif Loc_play == 1:
                Loc_play = 0
        if mouseX >= 630 and mouseX <= 690 and mouseY >= 10 and mouseY <= 70:
            screen = 0
    

#左上の表示
def prefecture_name_display():
    fill(175, 171, 171)
    rect(30, 30, 400, 150)
    fill(0)
    textSize(30)
    text("Move the mouse cursor",230,80)
    text("to the center of the circle.",230,120)
    textSize(50)
    for i in range(47):
        if mouseX >= loc_x[i]-10 and mouseX <= loc_x[i]+10 and mouseY >= loc_y[i]-10 and mouseY <= loc_y[i]+10:
            fill(175, 171, 171)
            rect(30, 30, 400, 150)
            fill(0)
            text(str(prefecture_name[i]),230,50)
            textSize(30)
            text(date[int(j[-1])],230,100)
            textSize(50)
            text("rainfall:"+str(prefecture[i][int(j[-1])]),230,150)
            break

#季節の表示
def season_display():
    pushMatrix()
    translate(300,570)
    noStroke()
    fill(255)
    if date[int(j[-1])][5:6] >= "3" and date[int(j[-1])][5:6] <= "5":
        rect(100,0,300,100)
    elif date[int(j[-1])][5:6] >= "6" and date[int(j[-1])][5:6] <= "8":
        rect(0,0,100,100)
        rect(200,0,200,100)
    elif date[int(j[-1])][5:6] == "9":
        rect(0,0,200,100)
        rect(300,0,100,100)
    elif date[int(j[-1])][5:6] == "1" and date[int(j[-1])][6:7] >= "0" and date[int(j[-1])][6:7] <= "1":
        rect(0,0,200,100)
        rect(300,0,100,100)
    elif date[int(j[-1])][5:6] == "1" and date[int(j[-1])][6:7] == "2":
        rect(0,0,300,100)
    elif date[int(j[-1])][1:3]:
        rect(0,0,300,100)
    stroke(1)
    popMatrix()

#csvデータ        
def todouhuken_csv():
    todouhuken = loadStrings("data/todouhuken.csv")
    for i in range(5, 370):
        for y, data in enumerate(todouhuken[i].split(',')):
            if y == 0:
                date.append(data)
            if y == 1:
                Aomori.append(data)
            elif y == 2:
                Iwate.append(data)
            elif y == 3:
                Akita.append(data)
            elif y == 4:
                Yamagata.append(data)
            elif y == 5:
                Miyagi.append(data)
            elif y == 6:
                Fukushima.append(data)
            elif y == 7:
                Ibaraki.append(data)
            elif y == 8:
                Tochigi.append(data)
            elif y == 9:
                Gunma.append(data)
            elif y == 10:
                Yamanashi.append(data)
            elif y == 11:
                Saitama.append(data)
            elif y == 12:
                Chiba.append(data)
            elif y == 13:
                Tokyo.append(data)
            elif y == 14:
                Niigata.append(data)
            elif y == 15:
                Nagano.append(data)
            elif y == 16:
                Shizuoka.append(data)
            elif y == 17:
                Toyama.append(data)
            elif y == 18:
                Gifu.append(data)
            elif y == 19:
                Aichi.append(data)
            elif y == 20:
                Ishikawa.append(data)
            elif y == 21:
                Fukui.append(data)
            elif y == 22:
                Mie.append(data)
            elif y == 23:
                Shiga.append(data)
            elif y == 24:
                Kyoto.append(data)
            elif y == 25:
                Nara.append(data)
            elif y == 26:
                Osaka.append(data)
            elif y == 27:
                Wakayama.append(data)
            elif y == 28:
                Hyogo.append(data)
            elif y == 29:
                Kanagawa.append(data)
            elif y == 30:
                Tottori.append(data)
            elif y == 31:
                Okayama.append(data)
            elif y == 32:
                Shimane.append(data)
            elif y == 33:
                Hiroshima.append(data)
            elif y == 34:
                Yamaguchi.append(data)
            elif y == 35:
                Kagawa.append(data)
            elif y == 36:
                Ehime.append(data)
            elif y == 37:
                Tokushima.append(data)
            elif y == 38:
                Kochi.append(data)
            elif y == 39:
                Fukuoka.append(data)
            elif y == 40:
                Oita.append(data)
            elif y == 41:
                Saga.append(data)
            elif y == 42:
                Miyazaki.append(data)
            elif y == 43:
                Kumamoto.append(data)
            elif y == 44:
                Kagoshima.append(data)
            elif y == 45:
                Nagasaki.append(data)
            elif y == 46:
                Okinawa.append(data)
            elif y == 47:
                Hokkaido.append(data)
                
def precipitation_csv():
    global screen
    try:
        for j in range(8):
            precipitation = loadStrings("data/new_data_after"+str(j)+"_"+str(month())+"_"+str(day())+".csv")
            for i in range(1293):
                for y, data in enumerate(precipitation[i].split(',')):
                    if y == 0:
                        data_prefecture[j].append(data)
                    if y == 1:
                        data_point[j].append(data)
                    if y == 2:
                        data_precipitation[j].append(data)
    except:
        screen = 3

#音楽
def stop():
    player.close()
    minim.stop()
