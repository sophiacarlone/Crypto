#Sophia Carlone
#Assignment 2 (RSA)

#decoding Tino assignment

n = 401176095417973966709598173895071753748557917040639570425619195728544844303847155653940253730660047984491108866472981267533141840100541197666663914164310761257160819987763890923686906035180659528992823000569761385264681838436145958115123166157611023309453739140974388973861930367226818116824494031101275698641212559333635648544322471164994803460042224217770707438123462120517462326680002590440858722541668402570184329527460322385506067210680416451879135870952324628875511750587627146360839073727558725313125259689488992624464649960188268189551840486484165555846118295675216102027176607646800765511968665345930969999222994931587298218367001529482687333716443715689708678004598549982375354478980165904781112008835594805370407908770971024107372059627740155576349231274440514877660034858750925775106956437394173379984675928529823749385310708129470381321708060334298618246434777721248654873205114493801005570324040161417481684787784646534822866361942373536860479758283821711049709263670963382290846382233137153936999167352340599263777014895822668032594696326957440398637612871515213926194656156628065853372309400423024019299328866352656252308308532927249691538087121847354287854587072726195077853044942116011060841284996807036625735660508735427651979838847975685918672987209743726650206880352774407959924134673613745098899492467446775486456799042951128299203169501641313191491956528007006599490994737679573123155682982654396579616413900142657778762795385721088495786944469142626650087557299080806459606841916124125158426782599018495961886504230722886338043031255406170868924334429607795169305818010672896921498789646922115486702700687845303566833237284361425378528290578754261740504350826493529175736668666043279338341851488683817922443760753264620955439860998479637837246281187948350756955986073085461838400759660134637357113027933808298663483043676455137010762339107430337833929806386529963710191150458454868609297273543340110979243464018187743437561298217797584214626183335264946400715979443435353153554598750006637735948063788237013323810902452663456517385733988209711599081108772973597995357113311770792062602229672071893645359095845482257808578612790126501441644637405880413617104999144334403595957207517032782598926783886123203603934601817753923638704474027049869566754511312484605365413668507701302177004417465165765395904423000328356956843749774819641181769990414257998517005505805557273272108916536854894905194836995923094614628529420316160824217845313627236681
e = 168908785040642244849306148347368451580903136820542901508310988187455899853482577764082299538567511639733682138686232666019091402099234073206775217111548489201990601502975689153037702543627977695110512723515684719146891957214194890355411354437805942878620655148063860209505901294317582322644026444356311127489
#n = 0;
#e = 0;
#filename1 = "ne.txt" #change
filename2 = "original.txt" #change
message = ""
letters = []
encrypted = {}

#fpublic = open(filename1, "r")
fmessage = open(filename2, "r")

#n = int(fpublic.read())
#e = int(fpublic.read())

for x in fmessage:
    letters.append(int(x))

#fpublic.close()
fmessage.close()

for m in range(128):
    encrypted[(pow(m, e, n))] = m

for l in letters:
    if l in encrypted:
        message += (chr(encrypted.get(l)))

print(message)