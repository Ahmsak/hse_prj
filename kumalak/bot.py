
# coding: utf-8

# In[2]:

#!/usr/bin/python3.4


import telebot
import config
import botan
import kumalak42
import random
import time
bot = telebot.TeleBot(config.token)

def kumalak():
    def divide_in_three(res):
        #Забирает из входящего листа значения, и делит их на три примерно(!) равные части (лист листов)
        random.shuffle(res)
        mins=3
        maxs=(len(res)//mins)+mins
        sti=(random.randint(mins, maxs))
        ndi=(random.randint(mins, maxs))
        listin=[[],[],[]]
        for i in range(sti):
            listin[0].append(res.pop(0))
        for i in range(ndi):
            listin[2].append(res.pop(0))
        for i in range(len(res)):
            listin[1].append(res.pop(0))
        return listin


    def fulling_cell(listin, tsn):
        # принимает лист с тремя листами (Listin) и заполняет строку итоговой таблицы
        if tsn==1:
            while len (listin[0])>4:
                for c in range(4):
                    base.append(listin[0].pop(-1))
            for y in range(len(listin[0])):
                table[0].append(listin[0].pop(-1))
            while len (listin[1])>4:
                for c in range(4):
                    base.append(listin[1].pop(-1))
            for y in range(len(listin[1])):
                table[1].append(listin[1].pop(-1))
            while len (listin[2])>4:
                for c in range(4):
                    base.append(listin[2].pop(-1))
            for y in range(len(listin[2])):
                table[2].append(listin[2].pop(-1))

        if tsn==2:
            while len (listin[0])>4:
                for c in range(4):
                    base.append(listin[0].pop(-1))
            for y in range(len(listin[0])):
                table[3].append(listin[0].pop(-1))
            while len (listin[1])>4:
                for c in range(4):
                    base.append(listin[1].pop(-1))
            for y in range(len(listin[1])):
                table[4].append(listin[1].pop(-1))
            while len (listin[2])>4:
                for c in range(4):
                    base.append(listin[2].pop(-1))
            for y in range(len(listin[2])):
                table[5].append(listin[2].pop(-1))
        if tsn==3:
            while len (listin[0])>4:
                for c in range(4):
                    base.append(listin[0].pop(-1))
            for y in range(len(listin[0])):
                table[6].append(listin[0].pop(-1))
            while len (listin[1])>4:
                for c in range(4):
                    base.append(listin[1].pop(-1))
            for y in range(len(listin[1])):
                table[7].append(listin[1].pop(-1))
            while len (listin[2])>4:
                for c in range(4):
                    base.append(listin[2].pop(-1))
            for y in range(len(listin[2])):
                table[8].append(listin[2].pop(-1))
        if len(listin[0]) or len(listin[1]) or len(listin[2])!=0:
            print("что-то пошло не так")



    def end_count(end):
        while len(end)>3:
            for i in range(3):
                end.pop(-1)


    import random
    base = [x for x in range(41)]
    table=[[],[],[],[],[],[],[],[],[]]  



    listin=divide_in_three(base)
    fulling_cell(listin,1)
    listin=divide_in_three(base)
    fulling_cell(listin,2)
    listin=divide_in_three(base)
    fulling_cell(listin,3)
    end_count(base)
    #print(table,base)


    output=[]

    if len(table[0]) and len(table[1]) and len(table[2])==3:
        output.append("«АЛТЫН КУМАЛАК», или золотой, дальше можно не раскладывать, у вас все отлично. Солнце днем помогает, ночью луна охраняет. ")
    if len(table[0]) == len(table[2]) and (len(table[0])%2)==1:
         output.append("Желание, или цель, осуществятся полностью, без излишков. ")
    if len(table[0]) and len(table[2])==3 and len(table[1])==1:
        output.append("Духи или ангелы покровительствуют вам во всех делах. ")
    if len(base)==1:
        output.append('Желание обязательно сбудется, да. ')
    if len(base)==2:
        output.append('Задержка во времени, но все зависит от вашей целенаправленной активности или силы намерения. ')
    if len(base)==3:
        output.append('Ваше желание скоро сбудется, ваш вопрос будет решен положительно, только нужно немного терпения. ')
    if len(table[0])%2!=1:
        output.append('Что-то препятствует исполнению желания, достижению цели, намерениям.')
    if len(table[0]) ==1 and len(table[1])==1 and len(table[2])==3:
         output.append("Конкретность установки при четком и ясном уме приведет вас к большой любви и богатству. ")    
    if len(table[0]) ==1 and len(table[1])==3 and len(table[2])==1:
         output.append("Цель и желания ясны, как божий день, не надо так сильно метаться в мыслях, ведь вас ожидают любовь и благополучие, возможность приобретения или получения чего-либо. ")
    if len(table[0]) ==3 and len(table[1])==1 and len(table[2])==1:
         output.append("Сосредоточьтесь на чем то одном, выберите самое главное, тем более вы  знаете, что нужно делать. Впереди у вас работа и четкий ответ на вопрос. Любовь не за горами. ")        
    if len(table[0]) ==2 and len(table[1])==1 and len(table[2])==2:
         output.append("Умеренность и порядочность в любом вопросе, цель обозначена. Достаток будет, нужно время. Любовь сама придет. ") 
    if len(table[0]) ==2 and len(table[1])==2 and len(table[2])==1:
         output.append("Порядок в очередности возникших мыслей и в их воплощении – есть залог успеха. Будете любимы. ")    
    if len(table[0]) ==1 and len(table[1])==2 and len(table[2])==2:
         output.append("Вы знаете что хотите. Решайте по мере поступления и все исполнится в скором времени. Время и любовь всегда идут рядом. ")                                                   
    if len(table[0]) ==2 and len(table[1])==3 and len(table[2])==4:
         output.append("Постарайтесь сосредоточиться, не передергивайте мысли. Вам нужно время и терпение. Любовь  не главное. ")                                                  

    if len(table[0]) ==2 and len(table[1])==4 and len(table[2])==3:
         output.append("Ваши желания исполнятся обязательно, гоните прочь дурные мысли, не метайтесь. Все будет хорошо. ")                                                   
    if len(table[0]) ==4 and len(table[1])==2 and len(table[2])==3:
         output.append("У Вас сумбур в желаниях, много хотите и прекрасно это понимаете. Определитесь и Вас ждет удача и любовь. ")                                                       
    if len(table[0]) ==4 and len(table[1])==3 and len(table[2])==2:
         output.append("Из всего многообразия желаний, вы знаете, что конкретно хотите. Все придет совсем скоро, не торопите события. ")  
    if len(table[0]) ==3 and len(table[1])==2 and len(table[2])==4:
         output.append("Поставьте все желания и вопросы в очередь. У вас есть время для обдумывания. Запаситесь терпением. ")                                          
    if len(table[0]) ==3 and len(table[1])==4 and len(table[2])==2:
         output.append("Как только Вы четко определитесь, что делать, к вам придет понимание – скоро все образуется. ")                                                    
    if len(table[0]) ==1 and len(table[1])==4 and len(table[2])==4:
         output.append("У вас конкретная цель и вопрос. Это хорошо. Если определитесь как это будет воплощено, то для Вас время не будет иметь значения. Вас ждет благополучие. ")                                                    
    if len(table[0]) ==4 and len(table[1])==1 and len(table[2])==4:
         output.append("Вы прекрасно знаете что делать. Не метайтесь в выборе вопроса и желания. Будете в достатке и любви. ")                                                    
    if len(table[0]) ==4 and len(table[1])==4 and len(table[2])==1:
         output.append("Ваша неопределенность в выборе желания мешает вам сосредоточиться. Как только скажете, -я знаю выход!, будете удачливы во всем. Любовь одна. ") 
                                                      #second line
    if len(table[3]) ==1 and len(table[4])==1 and len(table[5])==2:
         output.append("Прекрасные чувства, на сердце легко. Улыбайтесь чаще. ")                                                    
    if len(table[3]) ==1 and len(table[4])==2 and len(table[5])==1:
         output.append("Трепет в душе, и чувство легкости не будут вас покидать. ")
    if len(table[3]) ==2 and len(table[4])==1 and len(table[5])==1:
         output.append("Небольшая тревога на душе сменится на радость. ")                                                    
    if len(table[3]) ==2 and len(table[4])==2 and len(table[5])==4:
         output.append("Не поддавайтесь печали и сомнению. Побольше позитива. ")
    if len(table[3]) ==2 and len(table[4])==4 and len(table[5])==2:
         output.append("Не переживайте , постарайтесь отвлечься, думайте о приятном. ")                                                    
    if len(table[3]) ==4 and len(table[4])==2 and len(table[5])==2:
         output.append("Неприятные чувства и дискомфорт постепенно пойдут на убыль. Не ленитесь. ")
    if len(table[3]) ==2 and len(table[4])==3 and len(table[5])==3:
         output.append("Трепет в душе сменится на приятные и волнующие Вас ощущения. Будете радоваться. ")                                                    
    if len(table[3]) ==3 and len(table[4])==2 and len(table[5])==3:
         output.append("У вас все будет хорошо. Прочь сомнениям в душе. ")
    if len(table[3]) ==3 and len(table[4])==3 and len(table[5])==2:
         output.append("Не думайте о будущих чувствах и переживаниях. Все идет благополучно. ")                                                    
    if len(table[3]) ==3 and len(table[4])==1 and len(table[5])==4:
         output.append("Легко на сердце, возможны переживания, но недолгие.") 
    if len(table[3]) ==3 and len(table[4])==4 and len(table[5])==1:
         output.append("Не надо так сильно переживать. Впереди у вас радость. ")                                                    
    if len(table[3]) ==4 and len(table[4])==3 and len(table[5])==1:
         output.append("Не стоит так сильно переживать, приятное и радостное рядом. ")
    if len(table[3]) ==4 and len(table[4])==1 and len(table[5])==3:
         output.append("Все переживания останутся в прошлом. Радость на сердце, все хорошо. ")                                                    
    if len(table[3]) ==1 and len(table[4])==3 and len(table[5])==4:
         output.append("Сильное чувство, радостное сердцебиение, теперь лучше отдохнуть. ")
    if len(table[3]) ==1 and len(table[4])==4 and len(table[5])==3:
         output.append("Даже не переживайте. Это середина ваших чувств, все хорошее недалеко. Думайте о приятном. ") 
    if len(table[3]) ==4 and len(table[4])==4 and len(table[5])==4:
         output.append("Неприятный разговор, не вступайте в переговоры, избегайте общения, скопления людей, не высказывайтесь резко. ") 
                                                      #3d line
    if len(table[6]) ==1 and len(table[7])==1 and len(table[8])==2:
         output.append("День начнется удачно, ничто не будет мешать, вечером  отдохните. ") 
    if len(table[6]) ==1 and len(table[7])==2 and len(table[8])==1:
         output.append("Не сразу, но будут поездки или встречи. Возможны известия, посылки. ") 
    if len(table[6]) ==2 and len(table[7])==2 and len(table[8])==4:
         output.append("Не стоит собираться в дорогу. Займитесь чем-либо другим. ") 
    if len(table[6]) ==2 and len(table[7])==4 and len(table[8])==2:
         output.append("Вас что-то держит. Не торопите события. ") 
    if len(table[6]) ==4 and len(table[7])==2 and len(table[8])==2:
         output.append("Задержка идет с самого начала, но думайте о хорошем. ") 
    if len(table[6]) ==2 and len(table[7])==3 and len(table[8])==3:
         output.append("Предстоят хорошие дни, все будет в движении. Возможна поездка. ") 
    if len(table[6]) ==3 and len(table[7])==2 and len(table[8])==3:
         output.append("Вокруг вас движение, новости хорошие, но не все сразу. ") 
    if len(table[6]) ==3 and len(table[7])==3 and len(table[8])==2:
         output.append("Поездки, встречи, лучше немного отдохнуть.") 
    if len(table[6]) ==3 and len(table[7])==1 and len(table[8])==4:
         output.append("Не спешите, отложите поездку. Оставьте  это на завтра и все непременно получиться. ") 
    if len(table[6]) ==3 and len(table[7])==4 and len(table[8])==1:
         output.append("Есть небольшое препятствие, но поездка (отдых)  обязательно состоится. Будут вести, ожидайте. ") 
    if len(table[6]) ==4 and len(table[7])==3 and len(table[8])==1:
         output.append("Задержка в начале, не отказывайтесь от встреч, поездок. Ждите хорошие известия.") 
    if len(table[6]) ==4 and len(table[7])==1 and len(table[8])==3:
         output.append("Если была задержка, то теперь у вас все в движении, действуйте. ") 
    if len(table[6]) ==1 and len(table[7])==3 and len(table[8])==4:
         output.append("Все складывается удачно, но лучше отдохните. Отложите поездки. ") 
    if len(table[6]) ==1 and len(table[7])==4 and len(table[8])==3:
         output.append("Хотите действовать -  действуйте! Ожидайте хороших событий. ") 
    if len(table[6]) ==4 and len(table[7])==4 and len(table[8])==4:
         output.append("Нежелательная встреча. Если собираетесь в дорогу не стоит ехать, нужно немного повременить. ")
    return (output)


def kumalak42():
    def divide_in_three(res):
        #Забирает из входящего листа значения, и делит их на три примерно(!) равные части (лист листов)
        random.shuffle(res)
        mins=3
        maxs=(len(res)//mins)+mins
        sti=(random.randint(mins, maxs))
        ndi=(random.randint(mins, maxs))
        listin=[[],[],[]]
        for i in range(sti):
            listin[0].append(res.pop(0))
        for i in range(ndi):
            listin[2].append(res.pop(0))
        for i in range(len(res)):
            listin[1].append(res.pop(0))
        return listin


    def fulling_cell(listin, tsn):
        # принимает лист с тремя листами (Listin) и заполняет строку итоговой таблицы
        if tsn==1:
            while len (listin[0])>4:
                for c in range(4):
                    base.append(listin[0].pop(-1))
            for y in range(len(listin[0])):
                table[0].append(listin[0].pop(-1))
            while len (listin[1])>4:
                for c in range(4):
                    base.append(listin[1].pop(-1))
            for y in range(len(listin[1])):
                table[1].append(listin[1].pop(-1))
            while len (listin[2])>4:
                for c in range(4):
                    base.append(listin[2].pop(-1))
            for y in range(len(listin[2])):
                table[2].append(listin[2].pop(-1))

        if tsn==2:
            while len (listin[0])>4:
                for c in range(4):
                    base.append(listin[0].pop(-1))
            for y in range(len(listin[0])):
                table[3].append(listin[0].pop(-1))
            while len (listin[1])>4:
                for c in range(4):
                    base.append(listin[1].pop(-1))
            for y in range(len(listin[1])):
                table[4].append(listin[1].pop(-1))
            while len (listin[2])>4:
                for c in range(4):
                    base.append(listin[2].pop(-1))
            for y in range(len(listin[2])):
                table[5].append(listin[2].pop(-1))
        if tsn==3:
            while len (listin[0])>4:
                for c in range(4):
                    base.append(listin[0].pop(-1))
            for y in range(len(listin[0])):
                table[6].append(listin[0].pop(-1))
            while len (listin[1])>4:
                for c in range(4):
                    base.append(listin[1].pop(-1))
            for y in range(len(listin[1])):
                table[7].append(listin[1].pop(-1))
            while len (listin[2])>4:
                for c in range(4):
                    base.append(listin[2].pop(-1))
            for y in range(len(listin[2])):
                table[8].append(listin[2].pop(-1))
        if len(listin[0]) or len(listin[1]) or len(listin[2])!=0:
            print("что-то пошло не так")



    def end_count(end):
        while len(end)>3:
            for i in range(3):
                end.pop(-1)


    import random
    base = [x for x in range(41)]
    table=[[],[],[],[],[],[],[],[],[]]  



    listin=divide_in_three(base)
    fulling_cell(listin,1)
    listin=divide_in_three(base)
    fulling_cell(listin,2)
    listin=divide_in_three(base)
    fulling_cell(listin,3)
    end_count(base)
    #print(table,base)


    output=[]

    if len(table[0]) and len(table[1]) and len(table[2])==3:
        output.append("42 ")
    if len(table[0]) == len(table[2]) and (len(table[0])%2)==1:
         output.append("Блядь, неужели ты в первый раз в жизни всё правильно сделал? ")
    if len(table[0]) and len(table[2])==3 and len(table[1])==1:
        output.append("Зацени сиськи! ")
    if len(base)==1:
        output.append('Отдыхай, ешь, веселись. ')
    if len(base)==2:
        output.append('Перестань охуевать от происходящего и начай работать. ')
    if len(base)==3:
        output.append('Потерпи, скоро вся эта хуйня закончится. ')
    if len(table[0])%2!=1:
        output.append('Увидишь си-лучи у врат Тангейзера.')
    if len(table[0]) ==1 and len(table[1])==1 and len(table[2])==3:
         output.append("Двигайся вперед. ")    
    if len(table[0]) ==1 and len(table[1])==3 and len(table[2])==1:
         output.append("Позвони родителям. ")
    if len(table[0]) ==3 and len(table[1])==1 and len(table[2])==1:
         output.append("Не думай, действуй.")        
    if len(table[0]) ==2 and len(table[1])==1 and len(table[2])==2:
         output.append("Весна придёт, говно всплывет. ") 
    if len(table[0]) ==2 and len(table[1])==2 and len(table[2])==1:
         output.append("Думай. ")    
    if len(table[0]) ==1 and len(table[1])==2 and len(table[2])==2:
         output.append("Скотч, купи скотча, лишнего скотча не бывает. ")                                                   
    if len(table[0]) ==2 and len(table[1])==3 and len(table[2])==4:
         output.append("Зацени, как на улице-то пиздато. ")                                                  

    if len(table[0]) ==2 and len(table[1])==4 and len(table[2])==3:
         output.append("Надо было покупать год назад. ")                                                   
    if len(table[0]) ==4 and len(table[1])==2 and len(table[2])==3:
         output.append("Пришло время каминг-аута. ")                                                       
    if len(table[0]) ==4 and len(table[1])==3 and len(table[2])==2:
         output.append("Не мешай. ")  
    if len(table[0]) ==3 and len(table[1])==2 and len(table[2])==4:
         output.append("Забей. ")                                          
    if len(table[0]) ==3 and len(table[1])==4 and len(table[2])==2:
         output.append("Увидишь небо в алмазах. ")                                                    
    if len(table[0]) ==1 and len(table[1])==4 and len(table[2])==4:
         output.append("Продавай. ")                                                    
    if len(table[0]) ==4 and len(table[1])==1 and len(table[2])==4:
         output.append("Покупай. ")                                                    
    if len(table[0]) ==4 and len(table[1])==4 and len(table[2])==1:
         output.append("Выбрось что-то ненужное. ") 
                                                      #second line
    if len(table[3]) ==1 and len(table[4])==1 and len(table[5])==2:
         output.append("Покорми кота ")                                                    
    if len(table[3]) ==1 and len(table[4])==2 and len(table[5])==1:
         output.append("Жаль как бабочка, порхай как перхоть, следи за ногами! ")
    if len(table[3]) ==2 and len(table[4])==1 and len(table[5])==1:
         output.append("Можно попробовать начать класть болт на желания родителей. ")                                                    
    if len(table[3]) ==2 and len(table[4])==2 and len(table[5])==4:
         output.append("Пристегнись. ")
    if len(table[3]) ==2 and len(table[4])==4 and len(table[5])==2:
         output.append("Твой статус определяет сила твоих врагов. ")                                                    
    if len(table[3]) ==4 and len(table[4])==2 and len(table[5])==2:
         output.append("Резче заряди телефон, телефон хуйни не скажет. ")
    if len(table[3]) ==2 and len(table[4])==3 and len(table[5])==3:
         output.append("Никогда не пинай в зад дикобраза. ")                                                    
    if len(table[3]) ==3 and len(table[4])==2 and len(table[5])==3:
         output.append("Ищи суслика, выслеживай его. ")
    if len(table[3]) ==3 and len(table[4])==3 and len(table[5])==2:
         output.append("Мешай. ")                                                    
    if len(table[3]) ==3 and len(table[4])==1 and len(table[5])==4:
         output.append("В итоге все наебнётся.") 
    if len(table[3]) ==3 and len(table[4])==4 and len(table[5])==1:
         output.append("Не увидишь горящие боевые корабли у Ориона. ")                                                    
    if len(table[3]) ==4 and len(table[4])==3 and len(table[5])==1:
         output.append("Самый опасный человек — это тот, кто боится собственной тени. ")
    if len(table[3]) ==4 and len(table[4])==1 and len(table[5])==3:
         output.append("Улыбайся. ")                                                    
    if len(table[3]) ==1 and len(table[4])==3 and len(table[5])==4:
         output.append("Попляши. ")
    if len(table[3]) ==1 and len(table[4])==4 and len(table[5])==3:
         output.append("Помолчи. ") 
    if len(table[3]) ==4 and len(table[4])==4 and len(table[5])==4:
         output.append("Лови момент! Будь счастлив сейчас, потому что завтра ты умрёшь! ") 
                                                      #3d line
    if len(table[6]) ==1 and len(table[7])==1 and len(table[8])==2:
         output.append("Надо ехать. ") 
    if len(table[6]) ==1 and len(table[7])==2 and len(table[8])==1:
         output.append("Не надо никуда ехать. ") 
    if len(table[6]) ==2 and len(table[7])==2 and len(table[8])==4:
         output.append("Посиди в тишине, послушай. ") 
    if len(table[6]) ==2 and len(table[7])==4 and len(table[8])==2:
         output.append("Не кричи волки") 
    if len(table[6]) ==4 and len(table[7])==2 and len(table[8])==2:
         output.append("Все летит к хуям. ") 
    if len(table[6]) ==2 and len(table[7])==3 and len(table[8])==3:
         output.append("БЕГN! ") 
    if len(table[6]) ==3 and len(table[7])==2 and len(table[8])==3:
         output.append("Денег нет. Похуй. ") 
    if len(table[6]) ==3 and len(table[7])==3 and len(table[8])==2:
         output.append("Бросай.") 
    if len(table[6]) ==3 and len(table[7])==1 and len(table[8])==4:
         output.append("Не бросай. ") 
    if len(table[6]) ==3 and len(table[7])==4 and len(table[8])==1:
         output.append("Ожидай неведомой ёбаной хуйни. ") 
    if len(table[6]) ==4 and len(table[7])==3 and len(table[8])==1:
         output.append("Избавься от уёбков") 
    if len(table[6]) ==4 and len(table[7])==1 and len(table[8])==3:
         output.append("Прощай. ") 
    if len(table[6]) ==1 and len(table[7])==3 and len(table[8])==4:
         output.append("Нет. ") 
    if len(table[6]) ==1 and len(table[7])==4 and len(table[8])==3:
         output.append("Да. ") 
    if len(table[6]) ==4 and len(table[7])==4 and len(table[8])==4:
         output.append("Приготовься. ")
    return (output)


# In[ ]:


@bot.message_handler(commands=['predict'])
def old_kumalak(message):
    otpt=''.join(kumalak())
    bot.send_message(message.chat.id, otpt)
    # Если не нужно собирать ничего, кроме количества использований, замените третий аргумент message на None
    botan.track(config.botan_key, message.chat.id, message, 'Классический расклад')
    return


@bot.message_handler(commands=['predict42'])
def new_kumalak42(message):
    otpt=''.join(kumalak42())
    bot.send_message(message.chat.id,otpt)
    # Если не нужно собирать ничего, кроме количества использований, замените третий аргумент message на None
    botan.track(config.botan_key, message.chat.id, message, 'Новый расклад')
    return


@bot.message_handler(func=lambda message: True, content_types=['text'])
def any_mssg(message):
    bot.send_message(message.chat.id, "Введите команду /predict")
    # Если не нужно собирать ничего, кроме количества использований, замените третий аргумент message на None
    botan.track(config.botan_key, message.chat.id, message, 'прочие сообщения')
    return


if __name__ == '__main__':
    
    bot.polling(none_stop=True)


# In[ ]:



