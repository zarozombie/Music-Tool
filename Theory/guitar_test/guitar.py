import config

import notes
import scales

#------------------Guitar String-----------------------------
first_str = "E" 
second_str = "B"
third_str = "G"
fourth_str = "D"
fifth_str = "A"
sixth_str = "E"
nut = 0


#----------------------Converting Notes to numbers-------------------

first_stri = notes.con_note(first_str)
second_stri = notes.con_note(second_str)
third_stri = notes.con_note(third_str)
fourth_stri = notes.con_note(fourth_str)
fifth_stri = notes.con_note(fifth_str)
sixth_stri = notes.con_note(sixth_str)


#------------------------calculate maj scale-------------------------------------
# maj_scale = scales.majscale(sixth_str)
maj_scale = scales.majscale("c")
print("Major Scale:", maj_scale)

first = notes.con_note(maj_scale[0])
second = notes.con_note(maj_scale[1])
third = notes.con_note(maj_scale[2])
fourth = notes.con_note(maj_scale[3])
fifth = notes.con_note(maj_scale[4])
sixth = notes.con_note(maj_scale[5])
seventh = notes.con_note(maj_scale[6])

first_id = notes.con_note(maj_scale[0])
second_id = notes.con_note(maj_scale[1])
third_id = notes.con_note(maj_scale[2])
fourth_id = notes.con_note(maj_scale[3])
fifth_id = notes.con_note(maj_scale[4])
sixth_id = notes.con_note(maj_scale[5])
seventh_id = notes.con_note(maj_scale[6])

#Sixth String E Maj Scale ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'] | Number conversion 0 , 2, 4, 5, 7 , 9, 11
#-------------------------------ID note to fret --------------------------

def fret_identify(gtrstring, note):
    '''this function determins if the note is higher or lower note number than guitar string  
    then it returns an answer'''
    if gtrstring <= note:
        ans = abs(gtrstring - note)
        return ans
    elif gtrstring > note:
        add_interval = 12 - gtrstring
        ans = add_interval + note
        return ans

def fret_order(start_fret, next_fret):
    '''this function determins if next interval or fret is lower and if is it will change it to a highe note '''
    if start_fret > next_fret:
        return next_fret + 12
    elif start_fret <= next_fret:
        return next_fret

def octave(note):
    octave = note + 12
    return octave

def scale_to_frets(guitar_string, first, second, third, fourth, fifth, sixth, seventh):
    ''' this function takes is note intervals and then outputs frets on a specific string'''
    string_first = fret_identify(guitar_string, first)

    string_second = fret_identify(guitar_string, second)
    string_second = fret_order(string_first, string_second)

    string_third = fret_identify(guitar_string, third)
    string_third = fret_order(string_first, string_third)

    string_fourth = fret_identify(guitar_string, fourth)
    string_fourth = fret_order(string_first, string_fourth)

    string_fifth = fret_identify(guitar_string, fifth)
    string_fifth = fret_order(string_first, string_fifth)

    string_sixth = fret_identify(guitar_string, sixth)
    string_sixth = fret_order(string_first, string_sixth)

    string_seventh = fret_identify(guitar_string, seventh)
    string_seventh = fret_order(string_first, string_seventh)
    string_frets = [string_first, string_second, string_third, string_fourth, string_fifth, string_sixth, string_seventh]
    return string_frets
    # return string_first

#---------------------Fret board variables-----------------------------

#----- A string Frets for C Maj Scale-------



#----- low E Frets for Maj scale

High_E_String = scale_to_frets(fifth_stri, first, second, third, fourth, fifth, sixth, seventh)
B_String = scale_to_frets(fourth_stri, first, second, third, fourth, fifth, sixth, seventh)
G_String = scale_to_frets(third_stri, first, second, third, fourth, fifth, sixth, seventh)
D_String = scale_to_frets(fourth_stri, first, second, third, fourth, fifth, sixth, seventh)
A_String = scale_to_frets(fifth_stri, first, second, third, fourth, fifth, sixth, seventh)
Low_E_String = scale_to_frets(sixth_stri, first, second, third, fourth, fifth, sixth, seventh)
# 'Subtact: {} - {} = {}'.format(x, y, py_subtract)
print('a string: {}'.format(A_String))
print("A String:", A_String[0], A_String[1], A_String[2], A_String[3], A_String[4], A_String[5], A_String[6])
print("Low E String:", Low_E_String[0], Low_E_String[1], Low_E_String[2], Low_E_String[3], Low_E_String[4], Low_E_String[5], Low_E_String[6])
