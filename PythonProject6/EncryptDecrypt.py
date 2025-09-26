def CeasarCipher():
    """
    - Encrypts/decrypts a message from a file using the Caesar Cipher technique
    """

    # get secretkey from user from -25 to 25
    secretkey = int(input("Secret Key: "))
    if secretkey >= -25 and secretkey <= 25:
        filename = input("Input Filename: ")
        # Opens file for reading
        my_file = open(filename)
        # processes each line in the file
        for line in my_file:
            # converts everything to lowercase only
            line = line.lower()
            # initial index for character loop
            i = 0
            # while-loop to process each character
            while i < len(line):
                if  line[i].isalpha(): # only alphabet characters are encrypted everything else ignored
                    ascii_c = ord(line[i]) # characters converted to ASCII
                    ascii_c = ascii_c - ord('a') # normalize to the 0-25 range
                    ascii_c = (ascii_c + secretkey) % 26 # circular shift
                    ascii_c = ascii_c + ord('a') # Print encrypted/decrypted characters
                    print(chr(ascii_c), end='') # shift the number back to be in range 97 to 122 and convert it back into a character using the char() function.
                else:
                    print(line[i], end='')
                i += 1
    else:
        print("Bad key.") # if key error is invalid not in range

def main():
    """
    - main function calls ceasar cipher function
    """
    CeasarCipher()

main()

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject6/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject6/EncryptDecrypt.py 
Secret Key: 21
Input Filename: gettysburg_address.txt
ajpm nxjmz viy nzqzi tzvmn vbj jpm avoczmn wmjpbco ajmoc ji ocdn xjiodizio,
v izr ivodji, xjixzdqzy di gdwzmot, viy yzydxvozy oj ocz kmjkjndodji ocvo vgg 
hzi vmz xmzvozy zlpvg.

ijr rz vmz zibvbzy di v bmzvo xdqdg rvm, oznodib rczoczm ocvo ivodji, jm vit 
ivodji nj xjixzdqzy viy nj yzydxvozy, xvi gjib ziypmz. rz vmz hzo ji v bmzvo 
wvoogz-adzgy ja ocvo rvm. rz cvqz xjhz oj yzydxvoz v kjmodji ja ocvo adzgy, vn 
v adivg mznodib kgvxz ajm ocjnz rcj czmz bvqz oczdm gdqzn ocvo ocvo ivodji 
hdbco gdqz. do dn vgojbzoczm adoodib viy kmjkzm ocvo rz ncjpgy yj ocdn.

wpo, di v gvmbzm nzinz, rz xvi ijo yzydxvoz - rz xvi ijo xjinzxmvoz - rz xvi ijo 
cvggjr - ocdn bmjpiy. ocz wmvqz hzi, gdqdib viy yzvy, rcj nompbbgzy czmz, cvqz 
xjinzxmvozy do, avm vwjqz jpm kjjm kjrzm oj vyy jm yzomvxo. ocz rjmgy rdgg gdoogz 
ijoz, ijm gjib mzhzhwzm rcvo rz nvt czmz, wpo do xvi izqzm ajmbzo rcvo oczt ydy 
czmz. do dn ajm pn ocz gdqdib, mvoczm, oj wz yzydxvozy czmz oj ocz piadidnczy 
rjmf rcdxc oczt rcj ajpbco czmz cvqz ocpn avm nj ijwgt vyqvixzy. do dn mvoczm 
ajm pn oj wz czmz yzydxvozy oj ocz bmzvo ovnf mzhvdidib wzajmz pn - ocvo amjh ocznz 
cjijmzy yzvy rz ovfz dixmzvnzy yzqjodji oj ocvo xvpnz ajm rcdxc oczt bvqz ocz gvno 
apgg hzvnpmz ja yzqjodji - ocvo rz czmz cdbcgt mznjgqz ocvo ocznz yzvy ncvgg ijo cvqz 
ydzy di qvdi - ocvo ocdn ivodji, piyzm bjy, ncvgg cvqz v izr wdmoc ja amzzyjh - viy 
ocvo bjqzmihzio ja ocz kzjkgz, wt ocz kzjkgz, ajm ocz kzjkgz, ncvgg ijo kzmdnc 
amjh ocz zvmoc.


Process finished with exit code 0
"""

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject6/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject6/EncryptDecrypt.py 
Secret Key: -8
Input Filename: secret_letter.txt
rfwd, vzjjs tk xhtyx zxji f "xunwfq qthpnsl" yjhmsnvzj yt
xjfq ymj qfxy qjyyjw xmj bwtyj gjktwj mjw jcjhzynts:

xnwj, rd gwtymjw-ns-qfb, mfansl gd lti'x bnqq, ktw rd xnsx
n ymnsp, ymwtbs rdxjqk nsyt ymj utbjw tk ymj vzjjs rd htzxns,
fy bmtxj mfsix n mfaj xzkkjwji rzhm ktw fqrtxy ybjsyd djfwx,
n mfaj knsfqqd gjjs htsijrsji yt ijfym gd mjw fsi mjw
jxyfyjx.

n mfaj fxpji ktw rd ufujwx, bmnhm ymjd mfaj yfpjs fbfd, ns
twijw ymfy n rnlmy rfpj rd bnqq, gzy n mfaj gjjs zsfgqj yt
wjhtajw fsdymnsl tk zxj yt rj, tw jajs ljy qjfaj jnymjw yt rfpj
rd bnqq kwjjqd tw yt mfaj rd gtid htsajdji fkyjw rd ijfym, f
x n btzqi bnxm, yt dtzw pnslitr bmjwj n mfi ymj mtstzw yt gj
vzjjs, dtzw xnxyjw fsi tqi fqqd.

n fr yt gj jcjhzyji qnpj f hwnrnsfq fy jnlmy ns ymj rtwsnsl.


Process finished with exit code 0
"""

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject6/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject6/EncryptDecrypt.py 
Secret Key: -13
Input Filename: secret_message.txt
tvmnte fxlltzxl mktglfbmmxw ur xgbzft:

hixktmbhg utkutkhllt, 1941:
kxvhggtblltgvx wboblbhg ykhf dnkmbghpt ghkma-pxlm hy lxuxsa hg max
yebzam vhkkbwhk mhptkwl wnukhpdb, hihvadt. tmmtvd uxzng tm 18:30
ahnkl. bgytgmkr kxzbfxgm 3 zhxl lehper unm lnkxer yhkptkwl.
17:06 ahnkl [khftg gnfxkte b] bgytgmkr kxzbfxgm 3 hg max yebzam
vhkkbwhk lmtkmbgz 16 df xtlm hy dtfxgxv.

lnuftkbgx n-264 (dtibmtgexnmgtgm atkmpbz ehhdl), 1942
ykhf ehhdl, ktwbh-mxexzktf 1132/19 vhgmxgml: yhkvxw mh lnufxkzx
ngwxk tmmtvd, wxima vatkzxl. etlm xgxfr ehvtmbhg 08:30 ahnkl,
lxt ljntkx tc9863, yheehpbgz 220 wxzkxxl, 8 dghml.
[ikxllnkx] 14 fbeebutkl yteebgz, [pbgw] ghkma-ghkma-xtlm 4,
oblbubebmr 10.


Process finished with exit code 0
"""

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject6/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject6/EncryptDecrypt.py 
Secret Key: -6
Input Filename: secret_speech.txt
k uca vq aqw vqfca, oa htkgpfu, uq gxgp vjqwij yg hceg vjg fkhhkewnvkgu qh vqfca cpf vqoqttqy, k uvknn jcxg c ftgco. kv ku c ftgco fggrna tqqvgf kp vjg cogtkecp ftgco.
k jcxg c ftgco vjcv qpg fca vjku pcvkqp yknn tkug wr cpf nkxg qwv vjg vtwg ogcpkpi qh kvu etggf: "yg jqnf vjgug vtwvju vq dg ugnh-gxkfgpv: vjcv cnn ogp ctg etgcvgf gswcn."
k jcxg c ftgco vjcv qpg fca qp vjg tgf jknnu qh igqtikc vjg uqpu qh hqtogt uncxgu cpf vjg uqpu qh hqtogt uncxg qypgtu yknn dg cdng vq ukv fqyp vqigvjgt cv vjg vcdng qh dtqvjgtjqqf.
k jcxg c ftgco vjcv qpg fca gxgp vjg uvcvg qh okuukuukrrk, c uvcvg uygnvgtkpi ykvj vjg jgcv qh kplwuvkeg, uygnvgtkpi ykvj vjg jgcv qh qrrtguukqp, yknn dg vtcpuhqtogf kpvq cp qcuku qh htggfqo cpf lwuvkeg.
k jcxg c ftgco vjcv oa hqwt nkvvng ejknftgp yknn qpg fca nkxg kp c pcvkqp yjgtg vjga yknn pqv dg lwfigf da vjg eqnqt qh vjgkt umkp dwv da vjg eqpvgpv qh vjgkt ejctcevgt.
k jcxg c ftgco vqfca.
k jcxg c ftgco vjcv qpg fca, fqyp kp cncdcoc, ykvj kvu xkekqwu tcekuvu, ykvj kvu iqxgtpqt jcxkpi jku nkru ftkrrkpi ykvj vjg yqtfu qh kpvgtrqukvkqp cpf pwnnkhkecvkqp; qpg fca tkijv vjgtg kp cncdcoc, nkvvng dncem dqau cpf dncem iktnu yknn dg cdng vq lqkp jcpfu ykvj nkvvng yjkvg dqau cpf yjkvg iktnu cu ukuvgtu cpf dtqvjgtu.
k jcxg c ftgco vqfca.


Process finished with exit code 0
"""

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject6/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject6/EncryptDecrypt.py 
Secret Key: 30
Bad key.

Process finished with exit code 0
"""
