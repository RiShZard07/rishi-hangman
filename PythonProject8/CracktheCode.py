import string #import string module

# calculates alphabet frequencies from the file input.txt
def get_alphabet_frequencies(filename):
    freq = [0] * 26 #initialized list of 26 zeros(letters a - z)
    totalletters = 0 #counts total numbers of letters in file
    myfile = open(filename) #opens the file

    # goes through each line and character in order to count letter frequencies
    for line in myfile:
        for c in line:
            if c.isascii() and c.isalpha(): # checks if character is letter
                index = ord(c.lower()) - ord('a') # converts letter to index (0-25)
                freq[index] += 1
                totalletters += 1

    myfile.close() #closes file

    # converts count to frequency proportion using equation rounds to 4 decimal places
    for i in range(26):
        freq[i] = round(freq[i] / totalletters, 4)

    return freq #returns frequency list

#decodes file using substitution cipher
def output_decoded_file(filename, sub_cipher):
    for line in filename: # goes through each line in file
        for c in line: # goes through each character
            if c.isascii() and c.isalpha(): #checks if its a letter
                isupper = c.isupper() # saves case
                index = ord(c.lower()) - ord('a') #index for substitution
                decodedchar = sub_cipher[index] #substitute character
                if isupper:
                    print(decodedchar.upper(), end='') #saves upper case
                else:
                    print(decodedchar, end='') #saves lower case
            else:
                print(c, end='') # non letters printed
#main function
def main():
    filename = input("Input Filename: ") #gets file name from user
    # prints frequency list
    frequencies = get_alphabet_frequencies(filename)
    print(frequencies)

    decode_sub_cipher = ['m', 'k', 'g', 'o', 'e', 'w', 'c', 'z', 'l', 'u', 'q', 'b', 's', 'p', 'i', 'v', 'a', 'x',
                             'f', 'y', 'h', 'n', 't', 'r', 'j', 'd']
    output_decoded_file(open(filename), decode_sub_cipher)

main() #calls main function

"""
STEP 2 - Output:
[0.0394, 0.0567, 0.0014, 0.0778, 0.0008, 0.0007, 0.0915, 0.0221, 0.0607, 0.0259, 0.0262, 0.082, 0.0095, 0.0287, 0.0471, 0.0091, 0.1217, 0.0157, 0.0689, 0.024, 0.0688, 0.0158, 0.002, 0.0233, 0.0595, 0.0207]
"""

"""
STEP 5 - First 30 lines of output:
/Users/rishikeshavadamarla/PycharmProjects/PythonProject8/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject8/CracktheCode.py 
Input Filename: input.txt
[0.0394, 0.0567, 0.0014, 0.0778, 0.0008, 0.0007, 0.0915, 0.0221, 0.0607, 0.0259, 0.0262, 0.082, 0.0095, 0.0287, 0.0471, 0.0091, 0.1217, 0.0157, 0.0689, 0.024, 0.0688, 0.0158, 0.002, 0.0233, 0.0595, 0.0207]
cja nkotarc ypcahxaky axoos od cja ykabc ybclxz
cjfl axoos fl dok cja pla od bhzoha bhzujaka fh cja phfcai lcbcal bhi qolc ocjak nbkcl od cja uokmi bc ho rolc bhi ufcj bmqolc ho kalckfrcfohl ujbcloavak. zop qbz ronz fc, yfva fc bubz ok ka-pla fc phiak cja cakql od cja nkotarc ypcahxaky mfrahla fhrmpiai ufcj cjfl axoos ok ohmfha bc uuu.ypcahxaky.oky. fd zop bka hoc morbcai fh cja phfcai lcbcal, zop ufmm jbva co rjars cja mbul od cja rophckz ujaka zop bka morbcai xadoka plfhy cjfl axoos.
rkaifcl: nkoiprai xz bmag rbxbm dok cja lcbhibki axoosl nkotarc, xblai oh b ckbhlrkfncfoh nkoiprai dok nkotarc ypcahxaky bplckbmfb.
*** lcbkc od cja nkotarc ypcahxaky axoos cja ykabc ybclxz ***
cja ykabc ybclxz
xz
d. lrocc dfcwyakbmi

wamib
cjah uabk cja yomi jbc, fd cjbc ufmm qova jak;
fd zop rbh xophra jfyj, xophra dok jak coo,
cfmm lja rkz “movak, yomi-jbccai, jfyj-xophrfhy movak,
f qplc jbva zop!”
cjoqbl nbksa i’fhvfmmfakl
f

fh qz zophyak bhi qoka vpmhakbxma zabkl qz dbcjak ybva qa loqa bivfra cjbc f’va xaah cpkhfhy ovak fh qz qfhi avak lfhra.
“ujahavak zop daam mfsa rkfcfrfwfhy bhzoha,” ja comi qa, “tplc kaqaqxak cjbc bmm cja naonma fh cjfl uokmi jbvah’c jbi cja bivbhcbyal cjbc zop’va jbi.”
ja ifih’c lbz bhz qoka, xpc ua’va bmubzl xaah phplpbmmz roqqphfrbcfva fh b kalakvai ubz, bhi f phiaklcooi cjbc ja qabhc b ykabc iabm qoka cjbh cjbc. fh rohlaepahra, f’q fhrmfhai co kalakva bmm tpiyaqahcl, b jbxfc cjbc jbl onahai pn qbhz rpkfopl hbcpkal co qa bhi bmlo qbia qa cja vfrcfq od hoc b dau vacakbh xokal. cja bxhokqbm qfhi fl epfrs co iacarc bhi bccbrj fclamd co cjfl epbmfcz ujah fc bnnabkl fh b hokqbm nakloh, bhi lo fc rbqa bxopc cjbc fh rommaya f ubl phtplcmz brrplai od xafhy b nomfcfrfbh, xarbpla f ubl nkfvz co cja larkac ykfadl od ufmi, phshouh qah. qolc od cja rohdfiahral uaka phlopyjc—dkaepahcmz f jbva dafyhai lmaan, nkaorrpnbcfoh, ok b jolcfma mavfcz ujah f kabmfwai xz loqa phqflcbsbxma lfyh cjbc bh fhcfqbca kavambcfoh ubl epfvakfhy oh cja jokfwoh; dok cja fhcfqbca kavambcfohl od zophy qah, ok bc mablc cja cakql fh ujfrj cjaz agnkall cjaq, bka plpbmmz nmbyfbkflcfr bhi qbkkai xz oxvfopl lpnnkallfohl. kalakvfhy tpiyaqahcl fl b qbccak od fhdfhfca jona. f bq lcfmm b mfccma bdkbfi od qfllfhy loqacjfhy fd f dokyac cjbc, bl qz dbcjak lhoxxfljmz lpyyalcai, bhi f lhoxxfljmz kanabc, b lahla od cja dphibqahcbm iarahrfal fl nbkrammai opc phaepbmmz bc xfkcj.
bhi, bdcak xoblcfhy cjfl ubz od qz comakbhra, f roqa co cja biqfllfoh cjbc fc jbl b mfqfc. rohiprc qbz xa dophiai oh cja jbki kors ok cja uac qbkljal, xpc bdcak b rakcbfh nofhc f ioh’c rbka ujbc fc’l dophiai oh. ujah f rbqa xbrs dkoq cja ablc mblc bpcpqh f damc cjbc f ubhcai cja uokmi co xa fh phfdokq bhi bc b lokc od qokbm bccahcfoh dokavak; f ubhcai ho qoka kfocopl agrpklfohl ufcj nkfvfmayai ymfqnlal fhco cja jpqbh jabkc. ohmz ybclxz, cja qbh ujo yfval jfl hbqa co cjfl xoos, ubl agaqnc dkoq qz kabrcfoh—ybclxz, ujo kankalahcai avakzcjfhy dok ujfrj f jbva bh phbddarcai lrokh. fd naklohbmfcz fl bh phxkosah lakfal od lprralldpm yalcpkal, cjah cjaka ubl loqacjfhy yokyaopl bxopc jfq, loqa jafyjcahai lahlfcfvfcz co cja nkoqflal od mfda, bl fd ja uaka kambcai co oha od cjola fhckfrbca qbrjfhal cjbc kayflcak abkcjepbsal cah cjoplbhi qfmal bubz. cjfl kalnohlfvahall jbi hocjfhy co io ufcj cjbc dmbxxz fqnkallfohbxfmfcz ujfrj fl ifyhfdfai phiak cja hbqa od cja “rkabcfva caqnakbqahc”—fc ubl bh agckbokifhbkz yfdc dok jona, b koqbhcfr kabifhall lprj bl f jbva havak dophi fh bhz ocjak nakloh bhi ujfrj fc fl hoc mfsamz f ljbmm avak dfhi bybfh. ho—ybclxz cpkhai opc bmm kfyjc bc cja ahi; fc fl ujbc nkazai oh ybclxz, ujbc dopm iplc dmobcai fh cja ubsa od jfl ikabql cjbc caqnokbkfmz rmolai opc qz fhcakalc fh cja bxokcfva lokkoul bhi ljokc-ufhiai ambcfohl od qah.
qz dbqfmz jbva xaah nkoqfhahc, uamm-co-io naonma fh cjfl qfiima ualcakh rfcz dok cjkaa yahakbcfohl. cja rbkkbubzl bka loqacjfhy od b rmbh, bhi ua jbva b ckbifcfoh cjbc ua’ka ialrahiai dkoq cja ipsal od xprrmaprj, xpc cja brcpbm dophiak od qz mfha ubl qz ykbhidbcjak’l xkocjak, ujo rbqa jaka fh dfdcz-oha, lahc b lpxlcfcpca co cja rfvfm ubk, bhi lcbkcai cja ujomalbma jbkiubka xplfhall cjbc qz dbcjak rbkkfal oh coibz.
f havak lbu cjfl ykabc-phrma, xpc f’q lpnnolai co moos mfsa jfq—ufcj lnarfbm kadakahra co cja kbcjak jbki-xofmai nbfhcfhy cjbc jbhyl fh dbcjak’l oddfra. f ykbipbcai dkoq hau jbvah fh 1915, tplc b epbkcak od b rahcpkz bdcak qz dbcjak, bhi b mfccma mbcak f nbkcfrfnbcai fh cjbc iambzai capcohfr qfykbcfoh shouh bl cja ykabc ubk. f ahtozai cja rophcak-kbfi lo cjokopyjmz cjbc f rbqa xbrs kalcmall. fhlcabi od xafhy cja ubkq rahcka od cja uokmi, cja qfiima ualc hou laaqai mfsa cja kbyyai aiya od cja phfvakla—lo f iarfiai co yo ablc bhi mabkh cja xohi xplfhall. avakzxoiz f shau ubl fh cja xohi xplfhall, lo f lpnnolai fc ropmi lpnnokc oha qoka lfhyma qbh. bmm qz bphcl bhi phrmal cbmsai fc ovak bl fd cjaz uaka rjoolfhy b nkan lrjoom dok qa, bhi dfhbmmz lbfi, “ujz—za-al,” ufcj vakz ykbva, jalfcbhc dbral. dbcjak bykaai co dfhbhra qa dok b zabk, bhi bdcak vbkfopl iambzl f rbqa ablc, nakqbhahcmz, f cjopyjc, fh cja lnkfhy od cuahcz-cuo.
cja nkbrcfrbm cjfhy ubl co dfhi kooql fh cja rfcz, xpc fc ubl b ubkq labloh, bhi f jbi tplc madc b rophckz od ufia mbuhl bhi dkfahimz ckaal, lo ujah b zophy qbh bc cja oddfra lpyyalcai cjbc ua cbsa b jopla coyacjak fh b roqqpcfhy couh, fc lophiai mfsa b ykabc fiab. ja dophi cja jopla, b uabcjak-xabcah rbkixobki xphybmou bc afyjcz b qohcj, xpc bc cja mblc qfhpca cja dfkq okiakai jfq co ubljfhycoh, bhi f uahc opc co cja rophckz bmoha. f jbi b ioy—bc mablc f jbi jfq dok b dau ibzl phcfm ja kbh bubz—bhi bh omi ioiya bhi b dfhhflj uoqbh, ujo qbia qz xai bhi roosai xkabsdblc bhi qpccakai dfhhflj uflioq co jaklamd ovak cja amarckfr lcova.
fc ubl mohamz dok b ibz ok lo phcfm oha qokhfhy loqa qbh, qoka karahcmz bkkfvai cjbh f, lconnai qa oh cja kobi.
“jou io zop yac co ualc ayy vfmmbya?” ja blsai jamnmallmz.
f comi jfq. bhi bl f ubmsai oh f ubl mohamz ho mohyak. f ubl b ypfia, b nbcjdfhiak, bh okfyfhbm laccmak. ja jbi rblpbmmz rohdakkai oh qa cja dkaaioq od cja hafyjxopkjooi.
bhi lo ufcj cja lphljfha bhi cja ykabc xpklcl od mabval ykoufhy oh cja ckaal, tplc bl cjfhyl ykou fh dblc qovfal, f jbi cjbc dbqfmfbk rohvfrcfoh cjbc mfda ubl xayfhhfhy ovak bybfh ufcj cja lpqqak.
cjaka ubl lo qprj co kabi, dok oha cjfhy, bhi lo qprj dfha jabmcj co xa npmmai iouh opc od cja zophy xkabcj-yfvfhy bfk. f xopyjc b iowah vompqal oh xbhsfhy bhi rkaifc bhi fhvalcqahc larpkfcfal, bhi cjaz lcooi oh qz ljamd fh kai bhi yomi mfsa hau qohaz dkoq cja qfhc, nkoqflfhy co phdomi cja ljfhfhy larkacl cjbc ohmz qfibl bhi qokybh bhi qbarahbl shau. bhi f jbi cja jfyj fhcahcfoh od kabifhy qbhz ocjak xoosl xalfial. f ubl kbcjak mfcakbkz fh rommaya—oha zabk f ukoca b lakfal od vakz lomaqh bhi oxvfopl aifcokfbml dok cja zbma haul—bhi hou f ubl yofhy co xkfhy xbrs bmm lprj cjfhyl fhco qz mfda bhi xaroqa bybfh cjbc qolc mfqfcai od bmm lnarfbmflcl, cja “uamm-kophiai qbh.” cjfl flh’c tplc bh anfykbq—mfda fl qprj qoka lprralldpmmz moosai bc dkoq b lfhyma ufhiou, bdcak bmm.
"""

