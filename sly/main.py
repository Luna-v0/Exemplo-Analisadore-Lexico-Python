from sly import Lexer, Parser

class MyLexer(Lexer):
    literals = {"+"}
    tokens = { 'NUMBER' }
    pass

class MyParser(Parser):
    debugfile = 'parser.out'
    tokens = MyLexer.tokens

    def error(self, t):
        print(f"Syntax error at '{t.value}'")
    
    @_('expression1','expression2')
    def statement(self, p):
        return p.expression1 + p.expression2

    @_('expression1',"+",'expression2')
    def expression1(self, p):
        return p[0]


parser = MyParser()
lexer = MyLexer()

string_to_parse = "1 + 2 + 3"

print(parser.parse(string_to_parse))



