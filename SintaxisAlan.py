import ply.yacc as sintaxis
import Lexico

tokens = Lexico.tokens
line = 1


def p_sentencias(p):
    '''sentencias : asignacion
    | metodos
    | expresion
    '''
    p[0] = p[1]
    line = p.lineno(1)


def p_sentencias_control(p):
    '''sentencias : for'''
    p[0] = p[1]


def p_metodos(p):
    'metodos : imprimir'
    p[0] = ('IMPRIMIR')



def p_imprimir(p):
    '''imprimir : PRINT LPARENT factor RPARENT PUNTOCOMA'''


def p_if(p):
    '''if : IF LPARENT condicion RPARENT then
    | IF LPARENT condicion RPARENT then else
    '''
    p[0] = ('IF')


def p_else(p):
    'else : then'
    p[0] = ('THEN')


def p_for(p):
    'for : FOR LPARENT VAR condicion PUNTOCOMA condicion PUNTOCOMA instruccion RPARENT then'
    p[0] = ('FOR')


def p_then(p):
    'then : LLAVEL sentencias LLAVER'


def p_asignacion(p):
    'asignacion : ID ASIGNACION expresion'
    p[0] = ('ASIGNACION')


def p_expresion_suma(p):
    'expresion : term MAS factor'
    p[0] = p[1] + p[3]


def p_expresion_resta(p):
    'expresion : term MENOS factor'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expresion : term'
    p[0] = p[1]


def p_expresion_producto(p):
    'expresion : expresion PRODUCTO term'
    p[0] = p[1] * p[3]


def p_expresion_division(p):
    'expresion : expresion DIVISION term'
    p[0] = p[1] / p[3]


def p_expresion_mayor(p):
    'expresion : term MAYORQUE factor'
    p[0] = p[1] > p[3]


def p_expresion_menor(p):
    'expresion : term MENORQUE factor'
    p[0] = p[1] < p[3]


# validar con expresiones
def p_condicion(p):
    '''condicion : factor IGUAL factor
        | factor MAYORQUE factor
    | factor MENORQUE factor
    | factor ASIGNACION factor
    | factor DIFERENTE factor
    | compuesta
    '''


def p_compuesta(p):
    '''compuesta : LPARENT condicion RPARENT'''


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_set(p):
    'factor : NEW SET LPARENT RPARENT'
    p[0] = ('CONJUNTO')


def p_factor_num(p):
    'factor : NUMERO'
    p[0] = p[1]



def p_factor_pal(p):
    'factor : PALABRA'
    p[0] = p[1]


def p_factor_str(p):
    'factor : STRING'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPARENT expresion RPARENT'
    p[0] = p[2]


def p_factor_lista(p):
    'factor : LISTA'
    p[0] = ('LISTA')


def p_factor_booleano(p):
    'factor : BOOLEANO'
    p[0] = ('BOOLEANO')


def p_factor_objeto(p):
    'factor : OBJETO'
    p[0] = ('OBJETO')


def p_error(p):
    if p:
        print("Error de Sintaxis en token", p.type)
        # Just discard the token and tell the parser it's okay.
        print("Error en linea: ", line)

        parser.errok()
    else:
        print("Error de sintaxis en linea:", line)


# Construir parser
parser = sintaxis.yacc()
while True:
    try:
        s = input('<JS?> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)