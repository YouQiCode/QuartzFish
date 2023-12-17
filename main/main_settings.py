import qfish

print(qfish.lang_settings_welcome1)
print(qfish.lang_settings_welcome2)
print(qfish.lang_settings_welcome3)

print("\n")

def clock_h(clock_h_1):
    clock_h_file = open('clock_h.txt','w')
    clock_h_file.write(clock_h_1)
    clock_h_file.close()
def clock_m(clock_m_1):
    clock_m_file = open('clock_m.txt','w')
    clock_m_file.write(clock_m_1)
    clock_m_file.close()
def clock_ent(clock_ent_1):
    clock_ent_file = open('clock_ent.txt','w')
    clock_ent_file.write(clock_ent_1)
    clock_ent_file.close()

while_i = True
while while_i == True:
    Command = input(qfish.lang_settings_tx)

    if Command == "/help":
        print(qfish.lang_settings_tips_1)

    if Command == "/clock":
        Command = input(qfish.lang_settings_tx_mode)
        clock_h(Command)
        Command = input(qfish.lang_settings_tx_mode)
        clock_m(Command)
        print(qfish.lang_settings_done)

    if Command == "/onclock":
        clock_ent("on")
        print(qfish.lang_settings_done)

    if Command == "/offclock":
        clock_ent("off")
        print(qfish.lang_settings_done)

    print("\n")