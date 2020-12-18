import ply.lex as lex
import ply.yacc as yacc

def create_lexer():
    # List of token names
    tokens = (
    'NUMBER',
    'PLUS',
    'TIMES',
    'LPAREN',
    'RPAREN',
    )

    # Regular expression rules for simple tokens
    t_PLUS    = r'\+'
    t_TIMES   = r'\*'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'

    # A regular expression rule with some action code
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)    
        return t

    # Error handling rule
    def t_error(t):
        t.lexer.skip(1)

    return tokens, lex.lex()


def create_parser(tokens, lexer, ver):
    if ver == 1:
        def p_expression_plus(p):
            'expression : expression PLUS term'
            p[0] = p[1] + p[3]

        def p_expression_times(p):
            'expression : expression TIMES term'
            p[0] = p[1] * p[3]

        def p_expression_term(p):
            'expression : term'
            p[0] = p[1]

        def p_term_number(p):
            'term : NUMBER'
            p[0] = p[1]

        def p_term_brackets(p):
            'term : LPAREN expression RPAREN'
            p[0] = p[2]

    elif ver == 2:
        def p_expression_times(p):
            'expression : expression TIMES term'
            p[0] = p[1] * p[3]
        
        def p_expression_term(p):
            'expression : term'
            p[0] = p[1]
        
        def p_term_plus(p):
            'term : term PLUS summand'
            p[0] = p[1] + p[3]
        
        def p_term_summand(p):
            'term : summand'
            p[0] = p[1]
        
        def p_summand_number(p):
            'summand : NUMBER'
            p[0] = p[1]
        
        def p_summand_brackets(p):
            'summand : LPAREN expression RPAREN'
            p[0] = p[2]

    # Error rule for syntax errors
    def p_error(p):
        print("Syntax error in input!")

    return yacc.yacc()


def do_math(ver):
    tokens, lexer = create_lexer()
    parser = create_parser(tokens, lexer, ver)

    with open("inputs/aoc_input_18.txt") as f:
        sum = 0
        for line in f:
            sum += parser.parse(line)
    return sum


print("Part 1: " + str(do_math(1)))
print("Part 1: " + str(do_math(2)))