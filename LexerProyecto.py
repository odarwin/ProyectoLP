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
          'print':'PRINT'
          }

tokens=['ID','LPARENT','MENORQUE','MAYORQUE','RPARENT',
        'LLAVEL','LLAVER','IGUAL','COMILLASIMPLE','PUNTOCOMA',
        'PUNTO','COMA','NUMERO','COMILLADOBLE','DOLAR','CORCHETEL'
           ,'CORCHETER','DOSPUNTOS','MAS','INCREMENTO','MAYORIGUAL','MENORIGUAL','LLAMADAVARIABLE']+list(reserved.values())

t_LPARENT=r'\('
t_RPARENT=r'\)'
t_MAYORQUE=r'>'
t_MENORQUE=r'<'
t_MENORIGUAL=r'<='
t_MAYORIGUAL=r'>='
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
t_MAS=r'\+'
t_INCREMENTO=r'\+\+'
# t_LLAMADAVARIABLE=r'\$.*'

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


cadena=''' 
        var string = 'Dart is fun';
        var newString = string.substring(0, 5);
        String saludo = "Hola mundo en Dart";
        String saludo3 = "$saludo desde otra variable";
        string = 'dartlang';
        '$string has ${string.length} letters'; 
        List<String> list;
list = ['Juan', 'Ana'];
list.add('Pepe'); 
list.removeAt(2);
list.removeLast(); 
var ciudades = {

  'Mexico': 'CDMX',
  'Argentina': 'Buenos Aires',
  'Espana': 'Madrid',
  'Colombia':  'Bogota'
  
};
fixedLengthList[0] = 87;
List<String> list;
list = ['Juan', 'Ana','Oscar','Santiago'];
for(var i=0;i<list.length;i++){
	print(list[i]);
}
if (isRaining()) {
print("bringRainCoat");
} else if (isSnowing()) {
print("wearJacket");
} else {
print("putTopDown");
}

'''
analizador=lex.lex()
analizador.input(cadena)
while True:
    tokenR=analizador.token()
    if tokenR!=None:
        print(tokenR)
    else:
        break