from sly import Lexer, Parser


class MyLexer(Lexer):
    ignore = " \t"
    mais = r"\+"
    menos = r"-"
    vezes = r"\*"
    dividido = r"/"

    tokens = {"numero", "mais", "menos", "vezes", "dividido"}

    @_(r"\d+")
    def numero(self, t):
        t.value = int(t.value)
        return t

    def error(self, t):
        print(f"Lexer error at '{t.value}'")
        self.index += 1


class MyParser(Parser):
    debugfile = "parser.out"
    tokens = MyLexer.tokens

    def error(self, t):
        print(f"Syntax error at '{t.value}'")

    @_(
        "numero mais S",
        "numero menos S",
        "numero vezes S",
        "numero dividido S",
        "numero",
    )
    def S(self, p):
        print(f"Parsing: {p.numero}")

        if len(p) == 1:
            return p.numero
        elif len(p) == 3:
            if p[1] == "+":
                return p.numero + p.S
            elif p[1] == "-":
                return p.numero - p.S
            elif p[1] == "*":
                return p.numero * p.S
            elif p[1] == "/":
                return p.numero / p.S


parser = MyParser()
lexer = MyLexer()

string_to_parse = "1 + 2 + 3"

print(parser.parse(lexer.tokenize(string_to_parse)))
