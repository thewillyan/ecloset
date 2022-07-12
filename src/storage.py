from clothing import new_clothing
from style import check_clothes_set, new_style

def remove_spaces( string ):
    string_size = len( string )

    if( string_size > 1 ):
        if( string[-1] == " " ):
            return remove_spaces( string[0:-1] )
        else: 
            return remove_spaces( string[0:-1] ) + string[-1]
    elif( string_size == 1 ):
        if( string[0] == " " ):
            return ""
        else:
            return string[0]
    else:
        return ""

def line_search( file_lines, coder ):
    mark_list = []

    for line in file_lines:
        if( line[0:len( coder )] == coder ):
            mark_list.append( file_lines.index( line ) )

    return mark_list

def split_atts( clothe_usual_lines ):
    types_list = []
    raw_values_list = []

    for line in clothe_usual_lines:
        line_without_space = remove_spaces( line )
        splited_line = line_without_space.split('=')

        types_list.append( splited_line[0] )
        raw_values_list.append( splited_line[1] )

    return [ types_list, raw_values_list ]
    
def raw_clothe_lapidate( clothe_raw_atts ):
    id = id_raw_lapidate( clothe_raw_atts[0] )
    type = type_raw_lapidate( clothe_raw_atts[1] )
    sex = sex_raw_lapidate( clothe_raw_atts[2] )
    size = size_raw_lapidate( clothe_raw_atts[3] )
    color = color_raw_lapidate( clothe_raw_atts[4] )
    purchase_date = date_raw_lapidate( clothe_raw_atts[5])
    status = status_raw_lapidate( clothe_raw_atts[6] )
    price = price_raw_lapidate( clothe_raw_atts[7] )
    styles = styles_raw_lapidate( clothe_raw_atts[8] )

    clothe_result = new_clothing( 
        id, type, sex, size, color,
        purchase_date, status, price
    )


    if( clothe_result["is_valid"] == True ):
        clothe_result["content"]["styles"] = styles
        return clothe_result["content"]
    else:
        return False

def id_raw_lapidate( id_str ):
    return int( id_str )

def type_raw_lapidate( type_str ): 
    return type_str[1:-2]

def sex_raw_lapidate( sex_str ):
    return sex_str[1:-2] 

def size_raw_lapidate( size_str ):
    return size_str[1:-2] 

def color_raw_lapidate( color_str ):
    return color_str[1:-2] 

def date_raw_lapidate( date_str ):
    splited_date = date_str[ 1: -2 ].split( '/' )
    tuple_date = ( int( splited_date[0] ),
     int( splited_date[1] ), int( splited_date[2] ) )

    return tuple_date

def status_raw_lapidate( status_str ):
    return status_str[1:-2] 

def price_raw_lapidate( price_str ):
    return int( price_str )

def styles_raw_lapidate( styles_str ):
    styles_without_brackets_str = styles_str[1:-2]

    styles_raw_list = styles_without_brackets_str.split(',')

    styles_list = []

    for style_raw in styles_raw_list:
        if( len( style_raw ) > 2 ):
            styles_list.append( style_raw[1:-1] )

    return styles_list


def atts_check( clothe_atts_raw ):
    if( clothe_atts_raw[0] == "id"
    and clothe_atts_raw[1] == "type"
    and clothe_atts_raw[2] == "sex"
    and clothe_atts_raw[3] == "size"
    and clothe_atts_raw[4] == "color"
    and clothe_atts_raw[5] == "purchase_date"
    and clothe_atts_raw[6] == "status"
    and clothe_atts_raw[7] == "price"
    and clothe_atts_raw[8] == "styles" ):
        return True
    else:
        return False

def read_clothes( path ):
    file = open( path, "r" )

    file_lines = file.readlines()

    clothes_begin_lines = line_search( file_lines, "[Clothing_" )

    clothe_list = []

    for line_index in clothes_begin_lines:
        clothe_raw = split_atts( file_lines[ line_index + 1:line_index + 10 ] )

        clothe_types_raw = clothe_raw[0]
        clothe_atts_raw = clothe_raw[1]


        if( atts_check( clothe_types_raw ) == True ):    
            clothe = raw_clothe_lapidate( clothe_atts_raw )

            clothe_list.append( clothe )
        else:
            print( "ERRO NA ROUPA: [Clothing_" + str( line_index ) + "]" ) 

    file.close()

    return clothe_list

def clothe_to_str( clothe, index_str ):
    lines = []

    lines.append( "[Clothing_" + index_str + "]\n" )
    lines.append( "id = " + str( clothe["id"] ) + "\n")
    lines.append( "type = " + '"' + clothe["type"] + '"\n' )
    lines.append( "sex = " + '"' + clothe["sex"] + '"\n' )
    lines.append( "size = " + '"' + clothe["size"] + '"\n' )
    lines.append( "color = " + '"' + clothe["color"] + '"\n' )

    date = clothe["purchase_date"]
    day = f"{date[0]:02d}"
    month = f"{date[1]:02d}"
    year = f"{date[2]:04d}"

    lines.append( "purchase_date = " + '"' + day + "/" + month + "/" + year + '"\n' )

    lines.append( "status = " + '"' + clothe["status"] + '"\n' )
    lines.append( "price = " + str( clothe["price"] ) + "\n")
    lines.append( "styles = [" )

    for style in clothe["styles"]:
        lines[-1] = lines[-1] + ' "' + style + '",'

    if( lines[-1][-1] == ","):
        lines[-1] = lines[-1][:-1] + " "
    
    lines[-1] = lines[-1] + "]\n"

    lines_unified_str = ""

    for line in lines:
        lines_unified_str = lines_unified_str + line

    return lines_unified_str

def upadate_clothes( path, clothe_list ):

    file_str = ""

    for clothe in clothe_list:
        file_str = file_str + clothe_to_str( clothe, str( clothe_list.index( clothe ) ) ) + "\n"

    file = open( path, "w" )

    file.write( file_str )

    file.close()

def read_styles( path, clothes_list ):
    styles_list = []

    file = open( path, "r" )

    file_lines = file.readlines()
    styles_begin_lines = line_search( file_lines, "[Style_" )

    for styles_atts_index in styles_begin_lines:
        style_raw = split_atts( file_lines[styles_atts_index+1:styles_atts_index+4] )
        style_raw_types = style_raw[0]
        style_raw_atts = style_raw[1]

        if( verify_style_types( style_raw_types ) == True ):
            for att in range( len( style_raw_atts ) ):
                style_raw_atts[att] = break_line_corrector( style_raw_atts[att] )
            
            name = style_raw_atts[0]
            count = int( style_raw_atts[1] )

            clothe_sets_str = first_read( style_raw_atts[2] )
            clothe_sets_int = matrix_str_to_matrix_int( clothe_sets_str ) 
            clothe_sets = set_id_to_set_clothe( clothe_sets_int, clothes_list )

            style = new_style( name, clothe_sets, count )["content"]
            styles_list.append( style )

    file.close()

    return styles_list

def update_style( styles_list, path ):
    file_str= ""
    count = 0

    for style in styles_list:
        file_str = file_str + style_to_str( style, count ) 
        count = count + 1

    file = open( path, "w" )
    file.write( file_str )
    file.close()

def style_to_str( style, counter ):
    style_init = "[Style_" + str( counter ) + "]\n"
    name = "name = " + style["name"] + "\n"
    count = "count = " + str( style["count"] ) + "\n"
    clothes_sets = "clothes_sets = ["

    for set in style["clothes_sets"]:
        if ( set["is_valid"] == True ): 
            clothes_sets = clothes_sets + "["

            for id in set["content"]:
                clothes_sets = clothes_sets + str( id ) + ','

            clothes_sets = clothes_sets[:-1] + "]"

    clothes_sets = clothes_sets + "]\n\n"

    final_str = style_init + name + count + clothes_sets

    return final_str

def set_id_to_set_clothe( matrix_id, clothes_list ):
    matrix_clothe = []

    for list_id in matrix_id:
        line = []

        for id_index in list_id:
            line.append( clothes_list[id_index-1] )
        
        matrix_clothe.append( line )

    return matrix_clothe

def matrix_str_to_matrix_int( matrix_str ):
    matrix_int  = []

    for list in matrix_str:
        line = []

        for element in list:
            line.append( int( element ) )

        matrix_int.append( line )
    
    return matrix_int

def break_line_corrector( line_str ):
    if( line_str[-1:] == '\n' ):
        return line_str[:-1]
    else:
        return line_str

def verify_style_types( types_str ):
    if( types_str[0] == 'name'
    and types_str[1] == 'count'
    and types_str[2] == 'clothes_sets' ):
        return True
    else:
        return False

def first_read( string ):
    array = []
    pause = 0

    for char in range( 1, len( string ) ):
        if( pause > 0 ):
            pause = pause - 1
        elif( string[char] == '[' ):
            pause = second_read( string[char+1:] )
            
            array.append( string[char+1:char+pause+1].split(',') )
    return array

def second_read( str_list_part ):
    count = 0
    char = str_list_part[0]

    while( char != ']' or count == len( str_list_part ) ):
        count = count + 1
        char = str_list_part[count]

    return count


# clothes_list = read_clothes( "clothes_data.txt" )
# styles_list = read_styles( "styles_data.txt", clothes_list )

# update_style( styles_list, "styles_data.txt" )
# upadate_clothes( "clothes_data.txt", clothes_list )
