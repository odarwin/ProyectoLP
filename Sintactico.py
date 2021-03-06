import ply.yacc as sintaxis
import Lexico
tokens = Lexico.tokens
line=1
def p_sentencias(p):
    '''sentencias : asignacion
    | sentencias asignacion
    | definicion
    | sentencias definicion
    | expresion
    | sentencias expresion
    | metodos
    | sentencias metodos
    | for
    | sentencias for
    | if
    | sentencias if'''
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

def p_sets1(p):
    '''set : elementoTipo'''
    p[0] = [p[1]]
def p_sets2(p):
    '''set : set COMA elementoTipo'''
    p[0]=p[1]+[p[3]]
def p_listas(p):
    '''listas : elementoTipo'''
    p[0]=[p[1]]

def p_listas2(p):
    '''listas : listas COMA elementoTipo'''
    p[0]=p[1]+[p[3]]
def p_elementoTipo(p):
    '''elementoTipo : CADENA
    | NUMERO
    | booleano'''
    p[0]=p[1]
def p_booleano(p):
    '''booleano : TRUE
    | FALSE'''
def p_tipoDato(p):
    '''tipoDato : INT
    | STRING
    | BOOL'''
def p_definicion(p):
    '''definicion : VAR ID IGUAL expresion PUNTOCOMA
    | tipoDato ID IGUAL expresion PUNTOCOMA
    | VAR ID IGUAL ID PUNTO metodos PUNTOCOMA
    | LIST MAYORMENOR tipoDato MAYORMENOR ID IGUAL CORCHETEL listas CORCHETER PUNTOCOMA
    | definicionSet'''
def p_definicionSet(p):
    '''definicionSet : VAR ID IGUAL LLAVEL set LLAVER PUNTOCOMA'''

def p_if(p):
    '''if : IF condicionIf LLAVEL sentencias LLAVER
    | IF condicionIf LLAVEL sentencias LLAVER else'''
    p[0] = ('IF')
def p_else(p):
    'else : ELSE then'
    # p[0] = ('THEN')
def p_then(p):
    'then : LLAVEL sentencias LLAVER'

def p_for(p):
    '''for : FOR condicionFor LLAVEL sentencias LLAVER'''
    # p[0] = ('FOR')
def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNTOCOMA
    | ID IGUAL ID PUNTO metodos PUNTOCOMA
    | ID IGUAL CORCHETEL listas CORCHETER PUNTOCOMA'''
def p_expresion_incremento(p):
    '''expresion : ID MAS MAS PUNTOCOMA'''
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
    # p[0] = p[1] > p[3]

def p_expression_term(p):
    'expresion : term'


def p_condicionif(p):
    '''condicionIf : LPARENT factor COMPARE factor RPARENT
    | LPARENT factor MAYORMENOR factor RPARENT
    | factor MAYORMENOR factor'''

def p_condicionfor(p):
    '''condicionFor : LPARENT definicion condicionIf PUNTOCOMA incremento2 RPARENT'''
def p_incremento2(p):
    '''incremento2 : ID MAS MAS'''
def p_term_factor(p):
    'term : factor'
def p_factor_length(p):
    '''factor : ID PUNTO Mlength'''
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

error = []
# Captura de errores
def p_error(p):
    stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])
    error.pop()
    valor = 'Error de sintaxis en el input! Parser State:{} {} . {}. Chequee la sintaxis adecuada'.format(parser.state,stack_state_str,p)
    error.append(valor)
parser = sintaxis.yacc()

contenido='''
List<String> lista = ['Juan', 'Ana'];
int count=0;
for(var x=1;i<lista.length;i++){
    print('hola');
    count ++;
}
'''
result = parser.parse(contenido)
print(result)

# Ejemplos de Darwin Guaman
'''var hola2=hola.length;
var newString = string.substring(0,5);
List<String> list = ['Juan', 'Ana'];
for(var x=1;i<li.length;i++){
    print('hola');
    count++;
}
'''

# ejemplos de Alan Coello
'''if (a>b){b=0;}
veracidad= False;
if(a>b){ b=2} else { b=3};'''