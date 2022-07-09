import random 

chosen_one = ''
enabled_list_dare = []
enabled_list_truth = []



class generator_base:
    """база програми"""

    def __init__():
        """визначення атрибутів"""


    def creative_dare_enable():
        global enabled_list_dare
        enabled_list_dare.append('зроби ваншот/анімацію/комікс/арт, де головними героями є твій любимий персонаж і твій найменш любимий персонаж')
        enabled_list_dare.append('зроби ваншот/арт/анімацію по кросоверу твоєї вселенної з вселенною іншого гравця')
        enabled_list_dare.append("намалюй когось кого ти знаєш якби вони були в твоїй вселенній")
        enabled_list_dare.append("намалюй логотип клона відомого бренду що би підійшов до твоєї вселленної")
        enabled_list_dare.append('покрути колесо фортуни/вибери генератором чисел двох персонажів і зроби комікс/анімацію/ваншот/арт з ними')
        enabled_list_dare.append("зроби бінго по харектеру персонажа, і перевір як засильно ти подібний на того персонажа, перекреслюючи факти що підходять до твого характеру")
        enabled_list_dare.append("зроби комікс/анімацію/ваншот про любиму річ буль якого персонажа")



    def creative_dare_disable():
        global enabled_list_dare
        enabled_list_dare.remove('зроби ваншот/анімацію/комікс/арт, де головними героями є твій любимий персонаж і твій найменш любимий персонаж')
        enabled_list_dare.remove('зроби ваншот/арт/анімацію по кросоверу твоєї вселенної з вселенною іншого гравця')
        enabled_list_dare.remove("намалюй когось кого ти знаєш якби вони були в твоїй вселенній")
        enabled_list_dare.remove("намалюй логотип клона відомого бренду що би підійшов до твоєї вселленної")
        enabled_list_dare.remove('покрути колесо фортуни/вибери генератором чисел двох персонажів і зроби комікс/анімацію/ваншот/арт з ними')
        enabled_list_dare.remove("зроби бінго по харектеру персонажа, і перевір як засильно ти подібний на того персонажа, перекреслюючи факти що підходять до твого характеру")
        enabled_list_dare.remove("зроби комікс/анімацію/ваншот про любиму річ буль якого персонажа")




    def creative_truth_enable():
        global enabled_list_truth
        enabled_list_truth.append('яка гра/філм/мультфілм/серіал/мультсеріал/книга/комікс/аніме/манга серйозно змінила вашу творчість?')
        enabled_list_truth.append("яким був твій перший персонаж? чи подобається він тобі зараз?")
        enabled_list_truth.append("які з ваших персів самі адекватні і розумні?")
        enabled_list_truth.append('який з ваших персонажів є самим найбільшим фанатом романтики')
        enabled_list_truth.append('чи в вас є персонажі-вегетерянці/персонажі-вегани?')
        enabled_list_truth.append('роскажіть про персонажа не створеного вами, який вплинув на вигляд/характер вашого персонажа')


    def creative_truth_disable():
        global enabled_list_truth
        enabled_list_truth.remove('яка гра/філм/мультфілм/серіал/мультсеріал/книга/комікс/аніме/манга серйозно змінила вашу творчість?')
        enabled_list_truth.remove("яким був твій перший персонаж? чи подобається він тобі зараз?")
        enabled_list_truth.remove("які з ваших персів самі адекватні і розумні?")
        enabled_list_truth.remove('який з ваших персонажів є самим найбільшим фанатом романтики')
        enabled_list_truth.remove('чи в вас є персонажі-вегетерянці/персонажі-вегани?')
        enabled_list_truth.remove('роскажіть про персонажа не створеного вами, який вплинув на вигляд/характер вашого персонажа')


            
    def hugs_n_cuddles_dare_enable():
        global enabled_list_dare
        enabled_list_dare.append("обняти будь кого")
        enabled_list_dare.append("групові обнімашки")
        enabled_list_dare.append("обняти будь кого з хлопців")
        enabled_list_dare.append("обняти будь кого з дівчат")
        enabled_list_dare.append("наступний гравець по черзі вирішує кого ти обнімеш")
        enabled_list_dare.append("гравець перед тобою по черзі вирішує кого ти обнімеш")
        enabled_list_dare.append("всі хлопці роблять групові обнімашки")
        enabled_list_dare.append("всі дічвата роблять групові обнімашки")


    def hugs_n_cuddles_dare_disable():
        global enabled_list_dare
        enabled_list_dare.remove("обняти будь кого")
        enabled_list_dare.remove("групові обнімашки")
        enabled_list_dare.remove("обняти будь кого з хлопців")
        enabled_list_dare.remove("обняти будь кого з дівчат")
        enabled_list_dare.remove("наступний гравець по черзі вирішує кого ти обнімеш")
        enabled_list_dare.remove("гравець перед тобою по черзі вирішує кого ти обнімеш")
        enabled_list_dare.remove("всі хлопці роблять групові обнімашки")
        enabled_list_dare.remove("всі дічвата роблять групові обнімашки")


    def general_dare_enable():
        global enabled_list_dare
        enabled_list_dare.append("покачайтеся на підлозі")
        enabled_list_dare.append('підійди до рандомної людини біля тебе і скажи: "а ви не знаєте де тут пятірочка?"')
        enabled_list_dare.append("кажи 'yeet' після кожного речення наступні 3 раунда")
        enabled_list_dare.append("говори ніби тобі 80 років поки не настане твоя черга")
        enabled_list_dare.append('тихо прокричи "амогус сус"')
        enabled_list_dare.append("поводьтеся як коза, яка вмирає")
        enabled_list_dare.append("заспівай будь-яку аісню з твого плейлиста")
        enabled_list_dare.append("запиши на відео наступну дію")
        enabled_list_dare.append("говори з іншим акцентом до твоєї наступної черги")
        enabled_list_dare.append("говори протилежність того що ти хотів сказати до наступною черги")
        enabled_list_dare.append("заспівай 'im a barbie girl'")
        enabled_list_dare.append("дай кожній людині кличку, і називай їх так до твого наступного ходу")
        enabled_list_dare.append("покажи комусь з групи щось одне з цих: останне написане тобою повідомлення, останній пошуковий запит чи останне фото в галереї")
        enabled_list_dare.append("назви один плюс і один мінус кожного гравця")
        enabled_list_dare.append("намалюй якогось гравця з закритими очима, а інші мають вгадати")


    def general_truth_enable():
        global enabled_list_truth
        enabled_list_truth.append("яку гру/мультфіль/фільм/серіал/мултсеріал ви би стерли з цього світу")
        enabled_list_truth.append('в тебе колись був видуманий друг?')
        enabled_list_truth.append("оціни милість будь кого крім тебе")
        enabled_list_truth.append("оціни милість себе")
        enabled_list_truth.append("роскажи про дивний сон який тобі приснився")
        enabled_list_truth.append("роскажи про смішну історію з свого життя")
        enabled_list_truth.append("як думаєш, якби наступив апокаліпсис хто би вмер першим")
        enabled_list_truth.append("коли був останній раз коли ти плакав")
        enabled_list_truth.append("назви безкорисне вміння, яке би ти вивчив")
        enabled_list_truth.append("якщо забрати всі складності перїзду, куди би ти переїхав?")
        enabled_list_truth.append("якби ти би гарантовано не получив ніяких наказань, кого би ти вбив?")
        enabled_list_truth.append("назви три програми в яких ти проводиш найбільше часу")
        enabled_list_truth.append("який твій найлюбиміший фрукт?")
        enabled_list_truth.append("якби ти міг сказати всім людям з будь якого часу якусь інформацію, і вони би її повністю зрозуміли і точно погодилися, що за інформація це би була")
        enabled_list_truth.append("заспівати 'never gonna give you up'")
        enabled_list_truth.append("скажи стидний факт про себе")

        




    def generate_dare():
        """генерація chosen one для дії"""
        global chosen_one
        global enabled_list_dare
        chosen_one = random.choice(enabled_list_dare)
        print("\n" + chosen_one)


    def generate_truth():
        """генерація chosen one для правди"""
        global chosen_one
        global enabled_list_dare
        chosen_one = random.choice(enabled_list_truth)
        print("\n" + chosen_one)