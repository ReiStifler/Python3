# # function
# def compara_times():
#     SP = int()
#     CO = int()

#     for i in range(len(jogadores)):
#         if "0" == jogadores[i]:
#             SP += 1
#         elif "1" == jogadores[i]:
#             CO += 1

#     if SP >= 7 and CO >= 7:
#         print("BORA UM VIRTUAL NO CODEFORCES")

#     elif SP >= 7 or CO >= 7:
#         if SP > CO:
#             print("VAI TIMAO")
#         else:
#             print("VAMO TRICOLOR")
#     else:
#         print("BORA UM VIRTUAL NO CODEFORCES")


# # main

# jogadores = input()

# compara_times()


s = input()

corinthias = s.count("0" * 7)
saopaulo = s.count("1" * 7)

if corinthias > 0 and saopaulo > 0:
    print("JOGO PESADO")
elif corinthias > 0:
    print("VAI TIMAO")
elif saopaulo > 0:
    print("VAMO TRICOLOR")
else:
    print("BORA UM VIRTUAL NO CODEFORCES")
