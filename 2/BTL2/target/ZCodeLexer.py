# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0189\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\5+\u0115\n+\3+\3")
        buf.write("+\3+\7+\u011a\n+\f+\16+\u011d\13+\3,\3,\3-\3-\3.\3.\5")
        buf.write(".\u0125\n.\3.\5.\u0128\n.\3/\6/\u012b\n/\r/\16/\u012c")
        buf.write("\3\60\3\60\7\60\u0131\n\60\f\60\16\60\u0134\13\60\3\61")
        buf.write("\3\61\5\61\u0138\n\61\3\61\6\61\u013b\n\61\r\61\16\61")
        buf.write("\u013c\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u0145\n\62\f")
        buf.write("\62\16\62\u0148\13\62\3\62\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\7\64\u0153\n\64\f\64\16\64\u0156\13\64\3")
        buf.write("\64\3\64\3\65\6\65\u015b\n\65\r\65\16\65\u015c\3\65\3")
        buf.write("\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\7\67")
        buf.write("\u016a\n\67\f\67\16\67\u016d\13\67\3\67\3\67\3\67\5\67")
        buf.write("\u0172\n\67\3\67\3\67\38\38\38\38\38\38\78\u017c\n8\f")
        buf.write("8\168\u017f\138\38\38\38\38\38\58\u0186\n8\38\38\2\29")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W\2Y\2[-]\2_\2a\2c.e/g\60i\61k\62m\63o\64\3\2\17")
        buf.write("\4\2C\\c|\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t")
        buf.write("\2))^^ddhhppttvv\3\2))\3\2$$\3\2\f\f\4\2\f\f\17\17\5\2")
        buf.write("\n\13\16\17\"\"\3\3\f\f\4\2\16\17^^\2\u019b\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2[\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q\3\2\2\2\5v")
        buf.write("\3\2\2\2\7|\3\2\2\2\t\u0083\3\2\2\2\13\u0088\3\2\2\2\r")
        buf.write("\u008f\3\2\2\2\17\u0096\3\2\2\2\21\u009a\3\2\2\2\23\u00a2")
        buf.write("\3\2\2\2\25\u00a7\3\2\2\2\27\u00ab\3\2\2\2\31\u00b1\3")
        buf.write("\2\2\2\33\u00b4\3\2\2\2\35\u00ba\3\2\2\2\37\u00c3\3\2")
        buf.write("\2\2!\u00c6\3\2\2\2#\u00cb\3\2\2\2%\u00d0\3\2\2\2\'\u00d6")
        buf.write("\3\2\2\2)\u00da\3\2\2\2+\u00de\3\2\2\2-\u00e1\3\2\2\2")
        buf.write("/\u00e5\3\2\2\2\61\u00e7\3\2\2\2\63\u00e9\3\2\2\2\65\u00eb")
        buf.write("\3\2\2\2\67\u00ed\3\2\2\29\u00ef\3\2\2\2;\u00f2\3\2\2")
        buf.write("\2=\u00f4\3\2\2\2?\u00f7\3\2\2\2A\u00fa\3\2\2\2C\u00fc")
        buf.write("\3\2\2\2E\u00ff\3\2\2\2G\u0101\3\2\2\2I\u0104\3\2\2\2")
        buf.write("K\u0108\3\2\2\2M\u010a\3\2\2\2O\u010c\3\2\2\2Q\u010e\3")
        buf.write("\2\2\2S\u0110\3\2\2\2U\u0114\3\2\2\2W\u011e\3\2\2\2Y\u0120")
        buf.write("\3\2\2\2[\u0122\3\2\2\2]\u012a\3\2\2\2_\u012e\3\2\2\2")
        buf.write("a\u0135\3\2\2\2c\u013e\3\2\2\2e\u014c\3\2\2\2g\u014e\3")
        buf.write("\2\2\2i\u015a\3\2\2\2k\u0160\3\2\2\2m\u0163\3\2\2\2o\u0175")
        buf.write("\3\2\2\2qr\7v\2\2rs\7t\2\2st\7w\2\2tu\7g\2\2u\4\3\2\2")
        buf.write("\2vw\7h\2\2wx\7c\2\2xy\7n\2\2yz\7u\2\2z{\7g\2\2{\6\3\2")
        buf.write("\2\2|}\7p\2\2}~\7w\2\2~\177\7o\2\2\177\u0080\7d\2\2\u0080")
        buf.write("\u0081\7g\2\2\u0081\u0082\7t\2\2\u0082\b\3\2\2\2\u0083")
        buf.write("\u0084\7d\2\2\u0084\u0085\7q\2\2\u0085\u0086\7q\2\2\u0086")
        buf.write("\u0087\7n\2\2\u0087\n\3\2\2\2\u0088\u0089\7u\2\2\u0089")
        buf.write("\u008a\7v\2\2\u008a\u008b\7t\2\2\u008b\u008c\7k\2\2\u008c")
        buf.write("\u008d\7p\2\2\u008d\u008e\7i\2\2\u008e\f\3\2\2\2\u008f")
        buf.write("\u0090\7t\2\2\u0090\u0091\7g\2\2\u0091\u0092\7v\2\2\u0092")
        buf.write("\u0093\7w\2\2\u0093\u0094\7t\2\2\u0094\u0095\7p\2\2\u0095")
        buf.write("\16\3\2\2\2\u0096\u0097\7x\2\2\u0097\u0098\7c\2\2\u0098")
        buf.write("\u0099\7t\2\2\u0099\20\3\2\2\2\u009a\u009b\7f\2\2\u009b")
        buf.write("\u009c\7{\2\2\u009c\u009d\7p\2\2\u009d\u009e\7c\2\2\u009e")
        buf.write("\u009f\7o\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7e\2\2\u00a1")
        buf.write("\22\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7w\2\2\u00a4")
        buf.write("\u00a5\7p\2\2\u00a5\u00a6\7e\2\2\u00a6\24\3\2\2\2\u00a7")
        buf.write("\u00a8\7h\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7t\2\2\u00aa")
        buf.write("\26\3\2\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7p\2\2\u00ad")
        buf.write("\u00ae\7v\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7n\2\2\u00b0")
        buf.write("\30\3\2\2\2\u00b1\u00b2\7d\2\2\u00b2\u00b3\7{\2\2\u00b3")
        buf.write("\32\3\2\2\2\u00b4\u00b5\7d\2\2\u00b5\u00b6\7t\2\2\u00b6")
        buf.write("\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9\7m\2\2\u00b9")
        buf.write("\34\3\2\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc\7q\2\2\u00bc")
        buf.write("\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7k\2\2\u00bf")
        buf.write("\u00c0\7p\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2\7g\2\2\u00c2")
        buf.write("\36\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7h\2\2\u00c5")
        buf.write(" \3\2\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7n\2\2\u00c8")
        buf.write("\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca\"\3\2\2\2\u00cb")
        buf.write("\u00cc\7g\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce\7k\2\2\u00ce")
        buf.write("\u00cf\7h\2\2\u00cf$\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\u00d3\7i\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7p\2\2\u00d5&\3\2\2\2\u00d6\u00d7\7g\2\2\u00d7")
        buf.write("\u00d8\7p\2\2\u00d8\u00d9\7f\2\2\u00d9(\3\2\2\2\u00da")
        buf.write("\u00db\7c\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7f\2\2\u00dd")
        buf.write("*\3\2\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7t\2\2\u00e0")
        buf.write(",\3\2\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7q\2\2\u00e3")
        buf.write("\u00e4\7v\2\2\u00e4.\3\2\2\2\u00e5\u00e6\7-\2\2\u00e6")
        buf.write("\60\3\2\2\2\u00e7\u00e8\7/\2\2\u00e8\62\3\2\2\2\u00e9")
        buf.write("\u00ea\7,\2\2\u00ea\64\3\2\2\2\u00eb\u00ec\7\61\2\2\u00ec")
        buf.write("\66\3\2\2\2\u00ed\u00ee\7\'\2\2\u00ee8\3\2\2\2\u00ef\u00f0")
        buf.write("\7>\2\2\u00f0\u00f1\7/\2\2\u00f1:\3\2\2\2\u00f2\u00f3")
        buf.write("\7?\2\2\u00f3<\3\2\2\2\u00f4\u00f5\7?\2\2\u00f5\u00f6")
        buf.write("\7?\2\2\u00f6>\3\2\2\2\u00f7\u00f8\7#\2\2\u00f8\u00f9")
        buf.write("\7?\2\2\u00f9@\3\2\2\2\u00fa\u00fb\7>\2\2\u00fbB\3\2\2")
        buf.write("\2\u00fc\u00fd\7>\2\2\u00fd\u00fe\7?\2\2\u00feD\3\2\2")
        buf.write("\2\u00ff\u0100\7@\2\2\u0100F\3\2\2\2\u0101\u0102\7@\2")
        buf.write("\2\u0102\u0103\7?\2\2\u0103H\3\2\2\2\u0104\u0105\7\60")
        buf.write("\2\2\u0105\u0106\7\60\2\2\u0106\u0107\7\60\2\2\u0107J")
        buf.write("\3\2\2\2\u0108\u0109\7]\2\2\u0109L\3\2\2\2\u010a\u010b")
        buf.write("\7_\2\2\u010bN\3\2\2\2\u010c\u010d\7*\2\2\u010dP\3\2\2")
        buf.write("\2\u010e\u010f\7+\2\2\u010fR\3\2\2\2\u0110\u0111\7.\2")
        buf.write("\2\u0111T\3\2\2\2\u0112\u0115\5W,\2\u0113\u0115\7a\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0115\u011b\3")
        buf.write("\2\2\2\u0116\u011a\5W,\2\u0117\u011a\7a\2\2\u0118\u011a")
        buf.write("\5Y-\2\u0119\u0116\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u0118")
        buf.write("\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011cV\3\2\2\2\u011d\u011b\3\2\2\2\u011e")
        buf.write("\u011f\t\2\2\2\u011fX\3\2\2\2\u0120\u0121\t\3\2\2\u0121")
        buf.write("Z\3\2\2\2\u0122\u0124\5]/\2\u0123\u0125\5_\60\2\u0124")
        buf.write("\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2")
        buf.write("\u0126\u0128\5a\61\2\u0127\u0126\3\2\2\2\u0127\u0128\3")
        buf.write("\2\2\2\u0128\\\3\2\2\2\u0129\u012b\t\3\2\2\u012a\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012a\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d^\3\2\2\2\u012e\u0132\7\60\2\2\u012f")
        buf.write("\u0131\t\3\2\2\u0130\u012f\3\2\2\2\u0131\u0134\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133`\3\2\2")
        buf.write("\2\u0134\u0132\3\2\2\2\u0135\u0137\t\4\2\2\u0136\u0138")
        buf.write("\t\5\2\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u013a\3\2\2\2\u0139\u013b\t\3\2\2\u013a\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3")
        buf.write("\2\2\2\u013db\3\2\2\2\u013e\u0146\7$\2\2\u013f\u0145\n")
        buf.write("\6\2\2\u0140\u0141\7^\2\2\u0141\u0145\t\7\2\2\u0142\u0143")
        buf.write("\t\b\2\2\u0143\u0145\t\t\2\2\u0144\u013f\3\2\2\2\u0144")
        buf.write("\u0140\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0148\3\2\2\2")
        buf.write("\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3")
        buf.write("\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\7$\2\2\u014a\u014b")
        buf.write("\b\62\2\2\u014bd\3\2\2\2\u014c\u014d\t\n\2\2\u014df\3")
        buf.write("\2\2\2\u014e\u014f\7%\2\2\u014f\u0150\7%\2\2\u0150\u0154")
        buf.write("\3\2\2\2\u0151\u0153\n\13\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2")
        buf.write("\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\b")
        buf.write("\64\3\2\u0158h\3\2\2\2\u0159\u015b\t\f\2\2\u015a\u0159")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\b\65\3")
        buf.write("\2\u015fj\3\2\2\2\u0160\u0161\13\2\2\2\u0161\u0162\b\66")
        buf.write("\4\2\u0162l\3\2\2\2\u0163\u016b\7$\2\2\u0164\u016a\n\6")
        buf.write("\2\2\u0165\u0166\7^\2\2\u0166\u016a\t\7\2\2\u0167\u0168")
        buf.write("\t\b\2\2\u0168\u016a\t\t\2\2\u0169\u0164\3\2\2\2\u0169")
        buf.write("\u0165\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016d\3\2\2\2")
        buf.write("\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u0171\3")
        buf.write("\2\2\2\u016d\u016b\3\2\2\2\u016e\u016f\7\17\2\2\u016f")
        buf.write("\u0172\7\f\2\2\u0170\u0172\t\r\2\2\u0171\u016e\3\2\2\2")
        buf.write("\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\b")
        buf.write("\67\5\2\u0174n\3\2\2\2\u0175\u017d\7$\2\2\u0176\u017c")
        buf.write("\n\6\2\2\u0177\u0178\7^\2\2\u0178\u017c\t\7\2\2\u0179")
        buf.write("\u017a\t\b\2\2\u017a\u017c\t\t\2\2\u017b\u0176\3\2\2\2")
        buf.write("\u017b\u0177\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017f\3")
        buf.write("\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u0185")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0186\t\16\2\2\u0181")
        buf.write("\u0182\7^\2\2\u0182\u0186\n\7\2\2\u0183\u0184\t\b\2\2")
        buf.write("\u0184\u0186\n\t\2\2\u0185\u0180\3\2\2\2\u0185\u0181\3")
        buf.write("\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188")
        buf.write("\b8\6\2\u0188p\3\2\2\2\26\2\u0114\u0119\u011b\u0124\u0127")
        buf.write("\u012c\u0132\u0137\u013c\u0144\u0146\u0154\u015c\u0169")
        buf.write("\u016b\u0171\u017b\u017d\u0185\7\3\62\2\b\2\2\3\66\3\3")
        buf.write("\67\4\38\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    AND = 20
    OR = 21
    NOT = 22
    ADD = 23
    MINUS = 24
    MULTIPLY = 25
    DIVIDE = 26
    MODULO = 27
    ASSIGNINIT = 28
    EQUAL_NUMBER = 29
    EQUAL_STRING = 30
    NOT_EQUAL = 31
    LESS = 32
    LESS_EQUAL = 33
    GREATER = 34
    GREATER_EQUAL = 35
    CONCAT = 36
    LBRACKET = 37
    RBRACKET = 38
    LPARENT = 39
    RPARENT = 40
    COMMA = 41
    ID = 42
    NUMBER_LITERAL = 43
    STRING_LITERAL = 44
    NEWLINE = 45
    COMMENTS = 46
    WS = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'and'", "'or'", "'not'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'<-'", "'='", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'...'", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "AND", "OR", "NOT", "ADD", 
            "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "ASSIGNINIT", "EQUAL_NUMBER", 
            "EQUAL_STRING", "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", 
            "GREATER_EQUAL", "CONCAT", "LBRACKET", "RBRACKET", "LPARENT", 
            "RPARENT", "COMMA", "ID", "NUMBER_LITERAL", "STRING_LITERAL", 
            "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "AND", 
                  "OR", "NOT", "ADD", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", 
                  "ASSIGNINIT", "EQUAL_NUMBER", "EQUAL_STRING", "NOT_EQUAL", 
                  "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", "CONCAT", 
                  "LBRACKET", "RBRACKET", "LPARENT", "RPARENT", "COMMA", 
                  "ID", "LETTER", "DIGIT", "NUMBER_LITERAL", "INTERGER", 
                  "DECIMAL", "EXPONENT", "STRING_LITERAL", "NEWLINE", "COMMENTS", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STRING_LITERAL_action 
            actions[52] = self.ERROR_CHAR_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	if len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r':
                	raise UncloseString(self.text[1:-2])
            	elif self.text[-1] == '\n':
                	raise UncloseString(self.text[1:-1])
            	else:
                	raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise IllegalEscape(self.text[1:])

     


