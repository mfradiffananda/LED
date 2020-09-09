digits = [ '1111110', # 0 ini untuk mempermudah, bayangkan ini nomor LED
 '0110000', # 1
 '1101101', # 2
 '1111001', # 3
 '0110011', # 4
 '1011011', # 5
 '1011111', # 6
 '1110000', # 7
 '1111111', # 8
 '1111011', # 9
 ]
def printNumber(num):
    global digits #berlaku global, diambil dari digit atas
#print(digits)
    digs = str(num) # KENAPA dibuat str? biar kita bisa tahu jumlah digitnya..
    lines = [ '' for l in range(5) ] # ini untuk membuat tempat lampu (ada 5 baris)
    for d in digs:
        segs = [ [' ',' ',' '] for l in range(5) ] # membuat baris lampunya -->initinya mau bikin matrix 5x3
        ptrn = digits[ord(d) - ord('0')] # ini mencari elem dalam list berdasarkan selisih nilai ascii nya. ex: 49-48 = 1
#ptrn = singkatan patern/ pola lampu
#print(ptrn)
        if ptrn[0] == '1':
            segs[0][0] = segs[0][1] = segs[0][2] = '#'
        if ptrn[1] == '1':
            segs[0][2] = segs[1][2] = segs[2][2] = '#'
        if ptrn[2] == '1':
            segs[2][2] = segs[3][2] = segs[4][2] = '#'
        if ptrn[3] == '1':
            segs[4][0] = segs[4][1] = segs[4][2] = '#'
        if ptrn[4] == '1':
            segs[2][0] = segs[3][0] = segs[4][0] = '#'
        if ptrn[5] == '1':
            segs[0][0] = segs[1][0] = segs[2][0] = '#'
        if ptrn[6] == '1':
            segs[2][0] = segs[2][1] = segs[2][2] = '#'
        for l in range(5):
            lines[l] += ''.join(segs[l]) + ' '
    for l in lines:
        print(l)
        
printNumber(int(input("Enter the number you wish to display: ")))