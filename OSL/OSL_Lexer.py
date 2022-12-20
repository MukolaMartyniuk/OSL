import Lexer

RESERVED = 'RESERVED'
STRING      = 'STRING'
INT  = "INT"
ID       = 'ID'

token_exprs = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'\:=',                   RESERVED),
    (r'\(',                    RESERVED),
    (r'\)',                    RESERVED),
    (r';',                     RESERVED),
    (r'\+',                    RESERVED),
    (r'-',                     RESERVED),
    (r'\*',                    RESERVED),
    (r'any',                   RESERVED),
    (r'anyOf',                 RESERVED),
    (r'sizeOf',                RESERVED),
    (r'noneOf',                RESERVED),
    (r'space',                 RESERVED),
    (r'tab',                   RESERVED),
    (r'new',                   RESERVED),
    (r'/',                     RESERVED),
    (r'<=',                    RESERVED),
    (r'<',                     RESERVED),
    (r'>=',                    RESERVED),
    (r'>',                     RESERVED),
    (r'!=',                    RESERVED),
    (r'=',                     RESERVED),
    (r'and',                   RESERVED),
    (r'or',                    RESERVED),
    (r'not',                   RESERVED),
    (r'if',                    RESERVED),
    (r'then',                  RESERVED),
    (r'else',                  RESERVED),
    (r'while',                 RESERVED),
    (r'do',                    RESERVED),
    (r'end',                   RESERVED),
    (r'[0-9]+',                INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
    (r'~[A-Za-z][A-Za-z0-9_]*', STRING),
]

def imp_lex(characters):
    return Lexer.lex(characters, token_exprs)
