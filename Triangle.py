print( "\033c" )

rows = int( input( "enter the number of Rows : " ) )

for i in range( 1, rows + 1 ):
    
    for j in range( 1, i + 1 ):
        
        print( "*", end = " " )
    
    print()