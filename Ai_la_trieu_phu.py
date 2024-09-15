import random
_Path="D:/Coding/Ai_la_trieu_phu"
Bo_cau_hoi_file_name="Bo cau hoi.txt"
Cau_tra_loi_file_name="Cau tra loi.txt"
Giai_thuong_file_name="Giai thuong.txt"
Bo_cau_hoi=_Path + "/" + Bo_cau_hoi_file_name
Cau_tra_loi=_Path + "/" + Cau_tra_loi_file_name
Giai_thuong=_Path + "/" + Giai_thuong_file_name

with open(Bo_cau_hoi,"r",encoding='utf-8') as f:
    Bo_cau_hoi_list=f.readlines()
with open(Cau_tra_loi,"r",encoding="utf-8") as g:
    Cau_tra_loi_list=g.readlines()
with open(Giai_thuong,"r",encoding="utf-8") as j:
    Giai_thuong_list=j.readlines()
#print(Bo_cau_hoi_list)
#print(Cau_tra_loi_list)
#print(Giai_thuong_list)
print("Chao mung den voi tro choi Ai La Trieu Phu")
CAU_TRA_LOI_LIST_ADJUST = []
for i in Cau_tra_loi_list:
    CAU_TRA_LOI_LIST_ADJUST.append(i.strip())
Giai_thuong_list_adjust = []
for i in Giai_thuong_list:
    Giai_thuong_list_adjust.append(i.strip())
So_thu_tu=0
Cau_hoi_da_ra=[]
Tro_giup=[1,2]
for i in range(15):
    print("Cau hoi thu{}".format(So_thu_tu +1))
    Vi_tri_cau_hoi= random.randint(1,18)
    while Vi_tri_cau_hoi in Cau_hoi_da_ra:
        Vi_tri_cau_hoi=random.randint(1,18)
    print(Bo_cau_hoi_list[Vi_tri_cau_hoi])
    if (1 in Tro_giup) and (2 in Tro_giup):
        tro_giup=int(input("""
                   Ban co muon nhan quyen tro giup duoi day:
                   1.50/50
                   2.Khao sat khan gia tu truong quay
                   3.Khong can tro giup """))
        if tro_giup==1:
            print("Ban da chon quyen tro giup so 1.")
            dap_an_1=CAU_TRA_LOI_LIST_ADJUST[Vi_tri_cau_hoi]
            dap_an_2=chr(random.randint(65,68))
            while dap_an_2.lower()==dap_an_1.lower():
                dap_an_2=chr(random.randint(65,68))
            dap_an_list=[dap_an_1,dap_an_2]
            dap_an_1_display=random.randint(0,1)
            dap_an_2_display=1-dap_an_1_display
            print('{}---{}'.format(dap_an_list[dap_an_1_display],dap_an_list[dap_an_2_display]))
            Tro_giup.remove(1)
        elif tro_giup==2:
            print("Ban da chon quyen tro giup so 2.")
            dap_an_a=random.randint(1,100)
            conlai=100-dap_an_a
            dap_an_b=random.randint(1,conlai)
            conlai-=dap_an_b
            dap_an_c=random.randint(1,conlai)
            conlai-=dap_an_c
            dap_an_d=conlai
            if dap_an_a==100:
                dap_an_b=0
                dap_an_c=0
                dap_an_d=0               
            elif dap_an_b==100:
                dap_a_a=0
                dap_an_c=0
                dap_an_d=0                
            elif dap_an_c==100:
                dap_an_a=0
                dap_an_b=0
                dap_an_d=0
            elif dap_an_d==100:
                dap_an_a=0
                dap_an_c=0
                dap_an_b=0
            dap_an_list_2=[dap_an_a,dap_an_b,dap_an_c,dap_an_d]
            print("A {}%---B {}%---C {}%---D {}%".format(dap_an_list_2[0],dap_an_list_2[1],dap_an_list_2[2],dap_an_list_2[3]))

            Tro_giup.remove(2)
        else:
            print("Ban khong chon quyen tro giup nao.")
            pass
    elif (2 in Tro_giup):
        tro_giup=int(input("""
                   Ban co muon nhan quyen tro giup duoi day:
                   1.Khao sat khan gia tu truong quay
                   2.Khong can tro giup """))
        if tro_giup==1:
            print("Ban da chon quyen tro giup so 2")
            dap_an_a=random.randint(1,100)
            conlai=100-dap_an_a
            dap_an_b=random.randint(1,conlai)
            conlai-=dap_an_b
            dap_an_c=random.randint(1,conlai)
            conlai-=dap_an_c
            dap_an_d=conlai
            if dap_an_a==100:
                dap_an_b=0
                dap_an_c=0
                dap_an_d=0               
            elif dap_an_b==100:
                dap_a_a=0
                dap_an_c=0
                dap_an_d=0                
            elif dap_an_c==100:
                dap_an_a=0
                dap_an_b=0
                dap_an_d=0
            elif dap_an_d==100:
                dap_an_a=0
                dap_an_c=0
                dap_an_b=0
            dap_an_list_2=[dap_an_a,dap_an_b,dap_an_c,dap_an_d]
            print("A {}%---B {}%---C {}%---D {}%".format(dap_an_list_2[0],dap_an_list_2[1],dap_an_list_2[2],dap_an_list_2[3]))
            Tro_giup.remove(2)
        else:
            pass
        
    
    elif(1 in Tro_giup):
        tro_giup=int(input("""
                   Ban co muon nhan quyen tro giup duoi day:
                   1.50/50
                   2.Khong can tro giup """))
        if tro_giup==1:
            print("Ban da chon quyen tro giup so 1.")
            dap_an_1=CAU_TRA_LOI_LIST_ADJUST[Vi_tri_cau_hoi]
            dap_an_2=chr(random.randint(65,68))
            while dap_an_2.lower()==dap_an_1.lower():
                dap_an_2=chr(random.randint(65,68))
            dap_an_list=[dap_an_1,dap_an_2]
            dap_an_1_display=random.randint(0,1)
            dap_an_2_display=1-dap_an_1_display
            print('{}---{}'.format(dap_an_list[dap_an_1_display],dap_an_list[dap_an_2_display]))
            Tro_giup.remove(1)
        else:
            pass
    elif Tro_giup==[]:
        print("Ban da khong con quyen tro giup nao.")
    else:
        pass
    answer=input("Nhap vao cau tra loi cua ban:")
    
      
    if answer.upper()==(CAU_TRA_LOI_LIST_ADJUST[Vi_tri_cau_hoi]).upper():
        if So_thu_tu==14:
            print("Ban da tra loi dung het cac cau hoi!. Giai thuong cua ban la {}d!".format(Giai_thuong_list[So_thu_tu]))
            break
        else:
            print("Ban da tra loi dung! Giai thuong cua ban luc nay la {}d! ".format(Giai_thuong_list_adjust[So_thu_tu]))
            Tieptuc=input("Ban co muon tiep tuc choi khong (Yes or no):")
            if Tieptuc.lower()=="yes":  
                Cau_hoi_da_ra.append(Vi_tri_cau_hoi)
                So_thu_tu+=1
                continue
            else:
                print("Ban da ket thuc chuong trinh! Giai thuong cua ban la {}d!".format(Giai_thuong_list_adjust[So_thu_tu]))
                break

    else:
        if So_thu_tu==0:
            print("Ban da tra loi sai. Vi sai cau dau tien nen ban khong duoc giai thuong!")
            break
        else:
            print("Ban da tra loi sai. Ban se duoc nhan {}d!".format(Giai_thuong_list_adjust[0]))
            break
        
