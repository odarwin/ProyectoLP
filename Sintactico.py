import ply.yacc as sintaxis
import Lexico
tokens = Lexico.tokens
line=1
def p_sentencias(p):
    '''sentencias : asignacion
    | definicion
    | expresion
    | metodos
    | for
    | if'''
    p[0] = p[1]
    line = p.lineno(1)
def p_metodos(p):
    '''metodos : imprimir
    | Msubstring
    | Mlength'''
def p_imprimir(p):
    'imprimir : PRINT LPARENT factor RPARENT PUNTOCOMA'
    p[0] = ('IMPRIMIR')


def p_substring(p):
    'Msubstring : SUBSTRING LPARENT rango RPARENT '
def p_length(p):
    # sera una asignacion o definicion
    'Mlength : LENGTH '

def p_rango(p):
    'rango : factor COMA factor'

def p_listas(p):
    '''listas : elementoTipo'''
    p[0]=[p[1]]

def p_listas2(p):
    '''listas : listas COMA elementoTipo'''
    p[0]=p[1]+[p[3]]
def p_elementoTipo(p):
    '''elementoTipo : CADENA
    | NUMERO
    | BOOL'''
    p[0]=p[1]
def p_tipoDato(p):
    '''tipoDato : INT
    | STRING
    | BOOL'''
def p_definicion(p):
    '''definicion : VAR ID IGUAL expresion PUNTOCOMA
    | VAR ID IGUAL ID PUNTO metodos PUNTOCOMA
    | LIST MAYORMENOR tipoDato MAYORMENOR ID IGUAL CORCHETEL listas CORCHETER PUNTOCOMA'''

def p_if(p):
    '''if : IF condicionIf LLAVEL sentencias LLAVER
    | IF condicionIf LLAVEL sentencias LLAVER else'''
    p[0] = ('IF')
def p_else(p):
    'else : then'
    p[0] = ('THEN')
def p_then(p):
    'then : LLAVEL sentencias LLAVER'

def p_for(p):
    '''for : FOR condicionFor LLAVEL sentencias LLAVER'''
    # p[0] = ('FOR')
def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNTOCOMA
    | ID IGUAL ID PUNTO metodos PUNTOCOMA
    | ID IGUAL CORCHETEL listas CORCHETER PUNTOCOMA'''

def p_expresion_suma(p):
    'expresion : expresion MAS factor'
def p_expresion_resta(p):
    'expresion : expresion MENOS term'
def p_expresion_producto(p):
    'expresion : expresion PRODUCTO term'
def p_expresion_division(p):
    'expresion : expresion DIVISION term'
def p_expresion_potencia(p):
    'expresion : expresion POTENCIA term'

def p_expresion_mayorMenor(p):
    '''expresion : term MAYORMENOR factor'''
    p[0] = p[1] > p[3]

def p_expression_term(p):
    'expresion : term'


def p_condicionif(p):
    '''condicionIf : LPARENT factor COMPARE factor RPARENT
    | LPARENT factor MAYORMENOR factor RPARENT
    | factor MAYORMENOR factor'''

def p_condicionfor(p):
    '''condicionFor : LPARENT definicion condicionIf PUNTOCOMA INCREMENTO RPARENT'''
def p_term_factor(p):
    'term : factor'

def p_factor_num(p):
    'factor : NUMERO'
def p_factor_str(p):
    'factor : CADENA'
def p_factor_var2(p):
    'factor : ID'

def p_factor_for_condicion(p):
    '''factor : ID PUNTO LENGTH'''
def p_factor_expr(p):
    'factor : LPARENT expresion RPARENT'

def p_error(p):
    if p:
        print("Error de Sintaxis en token", p.type)
        # Just discard the token and tell the parser it's okay.
        print("Error en linea: ", line)

        parser.errok()
    else:
        print("Error de sintaxis en linea:", line)

parser = sintaxis.yacc()

contenido='''aqui van los ejemplos'''
result = parser.parse(contenido)
print(result)

# Ejemplos de Darwin Guaman
'''var hola2=hola.length;
var newString = string.substring(0,5);
List<String> list = ['Juan', 'Ana'];'''

# ejemplos de Allan Coello
'''if (a>b){b=0;}
veracidad= False;
if(a>b){ b=2} else { b=3};'''