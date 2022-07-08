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

def clothe_begin( file_lines ):
    mark_list = []

    for line in file_lines:
        if( line[0:10] == "[Clothing_" ):
            mark_list.append( file_lines.index( line ) )

    return mark_list

def clothe_split_atts( clothe_usual_lines ):
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

    clothe = { 
        "id": id,
        "type": type,
        "sex": sex,
        "size": size,
        "color": color,
        "purchase_date": purchase_date,
        "status": status,
        "price": price,
        "styles": styles
    }

    return clothe

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
    and clothe_atts_raw[8] == "styles"):
        return True
    else:
        return False

def read_data( path ):
    file = open( path, "r" )

    file_lines = file.readlines()

    clothes_begin_lines = clothe_begin( file_lines )

    clothe_list = []

    for line_index in clothes_begin_lines:
        clothe_raw = clothe_split_atts( file_lines[ line_index + 1:line_index + 10 ] )

        clothe_types_raw = clothe_raw[0]
        clothe_atts_raw = clothe_raw[1]

        if( atts_check( clothe_types_raw ) == True ):    
            clothe = raw_clothe_lapidate( clothe_atts_raw )

            clothe_list.append( clothe )
        else:
            print( "ERRO NA ROUPA: [Clothing_" + str( line_index ) + "]" ) 

    file.close()

    return clothe_list

def print_clothes( clothes_list ):
    for clothe in clothes_list: 
        print( "id: ",clothe["id"] )
        print( "type: ", clothe["type"] )
        print( "size: ", clothe["size"] )
        print( "color: ", clothe["color"] )
        print( "purchase_date: ",clothe["purchase_date"] )
        print( "status: ", clothe["status"] )
        print( "price: ", clothe["price"] )
        print( "styles: ",clothe["styles"], "\n" )

def clothe_to_str( clothe, index_str ):
    lines = []

    lines.append( "[Clothing_" + index_str + "]\n" )
    lines.append( "id = " + str( clothe["id"] ) + "\n")
    lines.append( "type = " + '"' + clothe["type"] + '"\n' )
    lines.append( "sex = " + '"' + clothe["sex"] + '"\n' )
    lines.append( "size = " + '"' + clothe["size"] + '"\n' )
    lines.append( "color = " + '"' + clothe["color"] + '"\n' )

    date = clothe["purchase_date"]

    for x in range( 0,2 ):
        if( date[x] < 10 ):
            day = "0" + str( date[x] )
        else: 
            month = str( date[x] )

    year = str( date[2] )

    lines.append( "purchase_date = " + '"' + day + "/" + month + "/" + year + '"\n' )

    lines.append( "status = " + '"' + clothe["status"] + '"\n' )
    lines.append( "price = " + str( clothe["price"] ) + "\n")

    styles_line = "styles = [ "
    style_marks = [ '"', '", ', " ]\n" ]

    for style in clothe["styles"]:
        styles_line = styles_line + style_marks[0] + style + style_marks[1]

    if( len( clothe["styles"] ) > 0 ):
        styles_line = styles_line[0:-2] + style_marks[2]
    else:
        styles_line = styles_line[0:-1] + style_marks[2]
    lines.append( styles_line )

    lines_unified_str = ""

    for line in lines:
        lines_unified_str = lines_unified_str + line

    return lines_unified_str

def data_update( path, clothe_list ):

    file_str = ""

    for clothe in clothe_list:
        file_str = file_str + clothe_to_str( clothe, str( clothe_list.index( clothe ) ) ) + "\n"

    file = open( path, "w" )

    file.write( file_str )

    file.close()
