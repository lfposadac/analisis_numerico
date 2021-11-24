from  gaussiana  import  formaMatrizAumentada , sustitucionProgresiva , sustitucionRegresiva , pivoteoParcial , intercambioMarcas , reordenar

A  =  eval ( input ( "Ingrese A:" ))
b  =  eval ( input ( "Ingrese b:" ))
etapa  =  0

L  = []
para  i  en  rango ( len ( A )):
    fila  = []
    para  j  en  rango ( len ( A )):
        si  yo  ! =  j :
            fila . añadir ( 0.0 )
        otra cosa :
            fila . añadir ( 1.0 )
    L . añadir ( fila )
U  = [[ 0.0  para  i  en el  rango ( len ( A ))] para  j  en el  rango ( len ( A ))]
A  = [[ float ( i ) para  i  en  j ] para  j  en  A ]
U [ 0 ] = [ i  por  i  en  A [ 0 ]]
def  factorizacionLU ( A , b , n , etapa ):
    Ab  =  formaMatrizAumentada ( A , b )  
    marcas  = [ i  para  i  en el  rango ( n )]                   
    para  k  en el  rango ( n - 1 ):
        L [ k ] [ k ] =  1
        Ab , mayor  =  pivoteoParcial ( Ab , n , k , True )
        si  alcalde  ! =  k :
            marcas  =  intercambioMarcas ( marcas , mayor , k )
        mults_aux  = {}
        para  i  en el  rango ( k + 1 , n ):
            mults_aux [( i , k )] =  multiplicador  =  Ab [ i ] [ k ] /  Ab [ k ] [ k ]
            para  j  en el  rango ( k , n + 1 ):
                Ab [ i ] [ j ] - = ( multiplicador  *  Ab [ k ] [ j ])
        para  i , j  en  mults_aux :
            Ab [ i ] [ j ] =  mults_aux [( i , j )]
        para  i , j  en  mults_aux :
            L [ i ] [ j ] =  Ab [ i ] [ j ]
        etapa  + =  1
        imprimir ()
        print ( f "Etapa { etapa } " )
        imprimir ()
        porque  yo  en  Ab :
            resultado  =  ""
            para  j  en  i [: len ( Ab )]:
                resultado  + =  f " { j : .10e } "
            imprimir ( resultado )
        imprimir ()
        imprimir ( "L:" )
        para  yo  en  L :
            resultado  =  ""
            para  j  en  i :
                resultado  + =  f " { j : .10e } "
            imprimir ( resultado )
        imprimir ()
        imprimir ( "U:" )
        i  =  Ab [ etapa ]
        U [ etapa ] =  i [: len ( Ab )]
        para  yo  en  U :
            resultado  =  ""
            para  j  en  i :
                resultado  + =  f " { j : .10e } "
            imprimir ( resultado )
        imprimir ()
        print ( "P: (marcas)" )
        resultado  =  ""
        para  i  en  marcas :
            l  =  flotar ( i )
            resultado  + =  "{0: .10e}" . formato ( l ) + ""
        imprimir ( resultado )
        imprimir ()
    return  Ab , marcas

imprimir ()
print ( "LU con pivoteo parcial:" )
imprimir ()
imprimir ( "Resultados" )
imprimir ()
print ( f "Etapa { etapa } " )
imprimir ()
para  yo  en  A :
    resultado  =  ""
    para  j  en  i :
        resultado  + =  f " { j : .10e } "
    imprimir ( resultado )
Ab , marcas  =  factorizacionLU ( A , b , len ( A ), etapa )

b  =  reordenar ( b , marcas )
Lb  =  formaMatrizAumentada ( L , b )
z  =  sustitucion Progresiva ( Lb , len ( L ))
Uz  =  formaMatrizAumentada ( U , z )
x  =  sustitucionRegresiva ( Uz , len ( U ))
imprimir ()
print ( "Despues de aplicar sustitucion progresiva y regresiva" )
imprimir ()
imprimir ( "x:" )
para  yo  en  x :
    imprimir ( i )



