from clothing import new_clothing, new_donated_clth, new_sold_clth
from style import check_clothes_set, new_style, to_clothes

#remove spaces from a string
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

# detects which lines of the file are started by 
# the coder and returns their respective index's
def line_search( file_lines, coder ):
    mark_list = []

    for line in file_lines:
        if( line[0:len( coder )] == coder ):
            mark_list.append( file_lines.index( line ) )

    return mark_list

#removes spaces from a list of lines and breaks them at "="
def split_atts( usual_lines ):
    types_list = []
    raw_values_list = []

    for line in usual_lines:
        line_without_space = remove_spaces( line )
        splited_line = line_without_space.split('=')

        types_list.append( splited_line[0] )
        raw_values_list.append( splited_line[1] )

    return [ types_list, raw_values_list ]
    
#Creat and return a clothe using clothe_raw_atts
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

#attribute treatments begin
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

#attribute treatments end

#attributes check
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

#reads a list of clothes from a specific path and returns it
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

#turns an outfit into a single string
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

#updates the file based on a list of clothes
def upadate_clothes( path, clothe_list ):

    file_str = ""

    for clothe in clothe_list:
        file_str = file_str + clothe_to_str( clothe, str( clothe_list.index( clothe ) ) ) + "\n"

    file = open( path, "w" )

    file.write( file_str )

    file.close()

#reads a list of styles from a specific path and returns it
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

#updates the file based on a list of styles
def update_style( styles_list, path, clothes ):
    file_str= ""
    count = 0

    for style in styles_list:
        file_str = file_str + style_to_str( style, count, clothes)
        count = count + 1

    file = open( path, "w" )
    file.write( file_str )
    file.close()

#turns an style into a single string
def style_to_str( style, counter, clothes):
    style_init = "[Style_" + str( counter ) + "]\n"
    name = "name = " + style["name"] + "\n"
    count = "count = " + str( style["count"] ) + "\n"
    clothes_sets = "clothes_sets = ["

    for set in style["clothes_sets"]:
        clths_set = to_clothes(set, clothes)
        check_result = check_clothes_set(clths_set)
        if ( check_result["is_valid"] == True ):
            clothes_sets = clothes_sets + "["

            for id in set:
                clothes_sets = clothes_sets + str( id ) + ','

            clothes_sets = clothes_sets[:-1] + "]"

    clothes_sets = clothes_sets + "]\n\n"

    final_str = style_init + name + count + clothes_sets

    return final_str

#transform a set of ids into a transform a set of clothes( dictionaries )
def set_id_to_set_clothe( matrix_id, clothes_list ):
    matrix_clothe = []

    for list_id in matrix_id:
        line = []

        for id_index in list_id:
            line.append( clothes_list[id_index-1] )
        
        matrix_clothe.append( line )

    return matrix_clothe

#transforms an array of strings into an array of integers
def matrix_str_to_matrix_int( matrix_str ):
    matrix_int  = []

    for list in matrix_str:
        line = []

        for element in list:
            line.append( int( element ) )

        matrix_int.append( line )
    
    return matrix_int

#remove the line breaker "\n" if it is present in the string
def break_line_corrector( line_str ):
    if( line_str[-1:] == '\n' ):
        return line_str[:-1]
    else:
        return line_str

#check the style types
def verify_style_types( types_str ):
    if( types_str[0] == 'name'
    and types_str[1] == 'count'
    and types_str[2] == 'clothes_sets' ):
        return True
    else:
        return False

#Transforms a string into a list with the help of the second_read function
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

#Helps first_read function transform a string into a list
def second_read( str_list_part ):
    count = 0
    char = str_list_part[0]

    while( char != ']' or count == len( str_list_part ) ):
        count = count + 1
        char = str_list_part[count]

    return count

#reads a list of donations from a specific path and returns it
def read_donations( path ):
    file = open( path, "r" )

    file_lines = file.readlines()

    donations_begin_lines = line_search( file_lines, "[Donation_" )

    donated_list = []

    for line_index in donations_begin_lines:
        donation_raw = split_atts( file_lines[ line_index + 1:line_index + 8 ] )

        donation_types_raw = donation_raw[0]
        donation_atts_raw = donation_raw[1]

        # print( donation_types_raw  )

        if( donation_atts_check( donation_types_raw ) == True ):    
            donation = raw_donation_lapidate( donation_atts_raw )

            donated_list.append( donation )
        else:
            print( "ERRO NA ROUPA: [Donation_" + str( line_index ) + "]" ) 

    file.close()

    return donated_list

#Creat and return a donation clothe using clothe_raw_atts
def raw_donation_lapidate( clothe_raw_atts ):
    id = id_raw_lapidate( clothe_raw_atts[0] )
    type = type_raw_lapidate( clothe_raw_atts[1] )
    sex = sex_raw_lapidate( clothe_raw_atts[2] )
    size = size_raw_lapidate( clothe_raw_atts[3] )
    color = color_raw_lapidate( clothe_raw_atts[4] )
    resolved_date = date_raw_lapidate( clothe_raw_atts[5])
    agent = status_raw_lapidate( clothe_raw_atts[6] )

    clothe_result = new_donated_clth( 
        id, type, sex, size, color,
        resolved_date, agent
    )

    if( clothe_result["is_valid"] == True ):
        return clothe_result["content"]
    else:
        return False

#attributes check
def donation_atts_check( donation_atts_raw ):
    if( donation_atts_raw[0] == "id"
    and donation_atts_raw[1] == "type"
    and donation_atts_raw[2] == "sex"
    and donation_atts_raw[3] == "size"
    and donation_atts_raw[4] == "color"
    and donation_atts_raw[5] == "resolved_date"
    and donation_atts_raw[6] == "agent"
 ):
        return True
    else:
        return False

#updates the file based on a list of donations_clothes
def upadate_donation( path, clothe_list ):

    file_str = ""

    for clothe in clothe_list:
        file_str = file_str + donation_to_str( clothe, str( clothe_list.index( clothe ) ) ) + "\n"

    file = open( path, "w" )

    file.write( file_str )

    file.close()

#Transform danation_clothe to a string
def donation_to_str( donation, index_str ):
    lines = []

    lines.append( "[Donation_" + index_str + "]\n" )
    lines.append( "id = " + str( donation["id"] ) + "\n")
    lines.append( "type = " + '"' + donation["type"] + '"\n' )
    lines.append( "sex = " + '"' + donation["sex"] + '"\n' )
    lines.append( "size = " + '"' + donation["size"] + '"\n' )
    lines.append( "color = " + '"' + donation["color"] + '"\n' )

    date = donation["resolved_date"]
    day = f"{date[0]:02d}"
    month = f"{date[1]:02d}"
    year = f"{date[2]:04d}"


    lines.append( "resolved_date = " + '"' + day + "/" + month + "/" + year + '"\n' )

    lines.append( "agent = " + '"' + donation["agent"] + '"\n' )

    lines_unified_str = ""

    for line in lines:
        lines_unified_str = lines_unified_str + line

    return lines_unified_str

#Read list_of_styles using a path
def read_sell( path ):
    file = open( path, "r" )

    file_lines = file.readlines()

    sell_begin_lines = line_search( file_lines, "[Sell_" )

    sold_list = []

    for line_index in sell_begin_lines:
        sell_raw = split_atts( file_lines[ line_index + 1:line_index + 9 ] )

        sell_types_raw = sell_raw[0]
        sell_atts_raw = sell_raw[1]

        # print( sell_types_raw  )

        if( sell_atts_check( sell_types_raw ) == True ):    
            sell = raw_sell_lapidate( sell_atts_raw )

            sold_list.append( sell )
        else:
            print( "ERRO NA ROUPA: [Sell_" + str( line_index ) + "]" ) 

    file.close()

    return sold_list

#Creat a sold_clothe using sell_raw_atts
def raw_sell_lapidate( sell_raw_atts ):
    id = id_raw_lapidate( sell_raw_atts[0] )
    type = type_raw_lapidate( sell_raw_atts[1] )
    sex = sex_raw_lapidate( sell_raw_atts[2] )
    size = size_raw_lapidate( sell_raw_atts[3] )
    color = color_raw_lapidate( sell_raw_atts[4] )
    resolved_date = date_raw_lapidate( sell_raw_atts[5])
    price = price_raw_lapidate( sell_raw_atts[6] )
    agent = status_raw_lapidate( sell_raw_atts[7] )

    sell_result = new_sold_clth( 
        id, type, sex, size, color,
        resolved_date, price, agent
    )

    if( sell_result["is_valid"] == True ):
        return sell_result["content"]
    else:
        return False

#checks if sell_atts_raw and returns if this check was true
def sell_atts_check( sell_atts_raw ):
    if( sell_atts_raw[0] == "id"
    and sell_atts_raw[1] == "type"
    and sell_atts_raw[2] == "sex"
    and sell_atts_raw[3] == "size"
    and sell_atts_raw[4] == "color"
    and sell_atts_raw[5] == "resolved_date"
    and sell_atts_raw[6] == "price"
    and sell_atts_raw[7] == "agent"
 ):
        return True
    else:
        return False

#updates the file based on a list of sell_clothes
def upadate_sell( path, clothe_list ):

    file_str = ""

    for clothe in clothe_list:
        file_str = file_str + sell_to_str( clothe, str( clothe_list.index( clothe ) ) ) + "\n"

    file = open( path, "w" )

    file.write( file_str )

    file.close()

#Transform sold_clothe to a string
def sell_to_str( sell, index_str ):
    lines = []

    lines.append( "[Sell_" + index_str + "]\n" )
    lines.append( "id = " + str( sell["id"] ) + "\n")
    lines.append( "type = " + '"' + sell["type"] + '"\n' )
    lines.append( "sex = " + '"' + sell["sex"] + '"\n' )
    lines.append( "size = " + '"' + sell["size"] + '"\n' )
    lines.append( "color = " + '"' + sell["color"] + '"\n' )

    date = sell["resolved_date"]
    day = f"{date[0]:02d}"
    month = f"{date[1]:02d}"
    year = f"{date[2]:04d}"

    lines.append( "resolved_date = " + '"' + day + "/" + month + "/" + year + '"\n' )
    lines.append( "price = " + str( sell["price"] ) + '\n' )
    lines.append( "agent = " + '"' + sell["agent"] + '"\n' )

    lines_unified_str = ""

    for line in lines:
        lines_unified_str = lines_unified_str + line

    return lines_unified_str
