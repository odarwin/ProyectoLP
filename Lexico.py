import ply.lex as lex
reserved={'main':'MAIN',
          'List':'LIST',
          'String':'STRING',
            'arguments':'ARGUMENTS',
            'var':'VAR',
          'substring':'SUBSTRING',
          'length':'LENGTH'
          ,'add':'ADD',
          'removeAt':'REMOVEAT',
          'removeLast':'REMOVELAST',
          'remove':'REMOVE',
          'int':'INT',
          'new':'NEW',
          'for':'FOR',
          'if':'IF',
          'else':'ELSE',
          'print':'PRINT',
          'True':'TRUE',
          'False':'FALSE',
          'bool':'BOOL',
          'stdin':'STDIN',
          'readLineSync':'READLINESYNC'
          }

tokens=['ID','LPARENT','RPARENT','LLAVEL','LLAVER','IGUAL','COMILLASIMPLE','PUNTOCOMA',
        'PUNTO','COMA','NUMERO','COMILLADOBLE','DOLAR','CORCHETEL'
           ,'CORCHETER','DOSPUNTOS','MAS','INCREMENTO','MENOS','PRODUCTO',
             'DIVISION','POTENCIA','CADENA','COMPARE','MAYORMENOR','NEWLINE','DOUBLE']+list(reserved.values())
t_CADENA = r'\'[a-zA-Z0-9\!\s]*\''
t_LPARENT=r'\('
t_RPARENT=r'\)'
t_COMPARE = r'[=!]='
t_MAYORMENOR=r'[<>]=?'
t_LLAVEL=r'\{'
t_LLAVER=r'\}'
t_IGUAL=r'='
t_ignore = ' \t'
t_COMILLASIMPLE="'"
t_COMILLADOBLE=r'"'
t_PUNTOCOMA=r';'
t_PUNTO=r'\.'
t_COMA=r','
t_DOLAR=r'\$'
t_CORCHETEL=r'\['
t_CORCHETER=r'\]'
t_DOSPUNTOS=r':'
t_INCREMENTO=r'i\+\+'
t_MAS=r'\+'
t_MENOS = r'-'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
t_STRING= r'\'.*?\''

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("No se ha reconocido '%s'"%t.value[0])
    t.lexer.skip(1)

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno +=len(t.value)

def t_COMMENT(t):
    r'\/\/.*'
    pass
    # Sin valor de retorno. Token descartado

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

'''
-----------PRUEBAS Y EJEMPLOS DE ALLAN COELLO-----------------
    Comprobando el input en Dart
    String name = stdin.readLineSync(); 
    
    Los String comenzaran con comilla simples, no con los dobles
    EJ:   var s1='Hola mundo';
    
    Los numeros enteros se los definen asi:
    int numero=156;
    
    --------------PRUEBAS DE OSCAR GUAMAN PACALLA ----------
    Las listas se definen de la siguiente manera
    List<String> list = ['Juan', 'Ana','Oscar'];
    
    Comprobando una funcion de list
    list.add('Pepe');
     
    Comprobando definicion de maps
    var ciudades = {

                  'Mexico': 'CDMX',
                  'Argentina': 'Buenos Aires',
                  'Espana': 'Madrid',
                  'Colombia':  'Bogota'
                  
                    };

    Comprobando un for:
    for(var i=0;i<list.length;i++){
	print(list[i]);
}
     
'''
# cadena='''
#     String name = stdin.readLineSync();
#
# '''
analizador=lex.lex()
# analizador.input(cadena)
# while True:
#     tokenR=analizador.token()
#     if tokenR!=None:
#         print(tokenR)
#     else:
#         break