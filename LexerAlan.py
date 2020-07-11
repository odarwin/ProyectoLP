
import ply.lex as lex
reserved = {
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'for': 'FOR',
    'echo': 'ECHO',
    'var': 'VAR',
    'int': 'INT',
    'set': 'SET',
    'list': 'LIST'
}

tokens = [


            "DOUBLE",
             "COMA",
             "BOOL",
             "STRING",
             "MENOS",
             "MAS",
             "PRODUCTO",
             "DIVISION",
             "LPAREN",
             "RPAREN",
             "LCORCH",
             "RCORCH",
             "LLLAV",
             "RLLAV",
             "POTENCIA",
             "MAP",
             "ID",
             "NUM",
             "COMPARA",
             "IGUAL",
             "TRUE",
             "FALSE",
             "PALABRA",
             "COMILLA",
             "DOSPUNTOS"


         ] + list(reserved.values())
t_INT= r'int'
t_COMILLA= r'\''
t_COMA=r','
t_DOSPUNTOS=r':'
t_STRING= r'\'.*?\''
t_VAR= r'var'
t_DOUBLE= r'double'
t_MENOS = r'-'
t_MAS = r'\+'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
t_NUM = r'[0-9]+(.[0-9]+)*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r'\['
t_RCORCH = r'\]'
t_LLLAV = r'\{'
t_RLLAV = r'\}'
t_IGUAL = r'='
t_PALABRA = r'[a-zA-Z]+'
t_COMPARA = r'[!<>=]='
t_IF = r'if'
t_TRUE = r'true'
t_FALSE = r'false'

t_ignore= ' \t'


def t_error(t):
    print("No se ha reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


cadena = "map gifts = { 'first': 'partridge', 'second': 'turtledoves', 'fifth': 'golden rings' } "
print("prueba 2: mapa")
print("Cadena a analizar: "+cadena)
analizadorL = lex.lex()
analizadorL.input(cadena)
while True:
    tokenRec = analizadorL.token()
    if tokenRec != None:
        print(tokenRec)
    else:
        break
