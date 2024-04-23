# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01a2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\7\2Z\n\2")
        buf.write("\f\2\16\2]\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3f\n\3\3")
        buf.write("\4\3\4\3\4\3\4\5\4l\n\4\3\5\3\5\3\5\3\5\5\5r\n\5\3\5\3")
        buf.write("\5\5\5v\n\5\3\5\3\5\5\5z\n\5\3\5\3\5\5\5~\n\5\3\6\3\6")
        buf.write("\3\6\5\6\u0083\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u008e\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0096\n\t\3")
        buf.write("\t\3\t\5\t\u009a\n\t\3\n\3\n\3\n\3\n\5\n\u00a0\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00a7\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00af\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00b6\n\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u00bd\n\16\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u00c8\n\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00cf\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00d6\n\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\7\23\u00de\n\23\f\23\16\23\u00e1\13\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\7\24\u00e9\n\24\f\24\16\24\u00ec\13\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00f4\n\25\f\25\16")
        buf.write("\25\u00f7\13\25\3\26\3\26\3\26\5\26\u00fc\n\26\3\27\3")
        buf.write("\27\3\27\5\27\u0101\n\27\3\30\3\30\5\30\u0105\n\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0110\n")
        buf.write("\31\3\31\5\31\u0113\n\31\3\32\3\32\5\32\u0117\n\32\3\32")
        buf.write("\5\32\u011a\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0125\n\33\3\34\3\34\3\34\5\34\u012a\n\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\5\35\u0133\n\35\3")
        buf.write("\35\3\35\5\35\u0137\n\35\3\35\5\35\u013a\n\35\3\35\5\35")
        buf.write("\u013d\n\35\3\36\3\36\3\36\3\36\5\36\u0143\n\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u014a\n\37\3\37\3\37\5\37\u014e")
        buf.write("\n\37\3 \3 \5 \u0152\n \3 \3 \5 \u0156\n \3!\3!\5!\u015a")
        buf.write("\n!\3!\3!\3!\3!\3\"\3\"\5\"\u0162\n\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u0174\n$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\5\'\u0180\n\'\3\'\3\'\3(\3")
        buf.write("(\3(\5(\u0187\n(\3(\3(\3(\3)\3)\3)\5)\u018f\n)\3)\3)\3")
        buf.write("*\3*\3*\5*\u0196\n*\3*\3*\3*\3+\3+\3+\6+\u019e\n+\r+\16")
        buf.write("+\u019f\3+\2\5$&(,\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\7\3\2\5\7\3")
        buf.write("\2\37%\3\2\26\27\3\2\31\32\3\2\33\35\2\u01b8\2[\3\2\2")
        buf.write("\2\4e\3\2\2\2\6k\3\2\2\2\bm\3\2\2\2\n\u0082\3\2\2\2\f")
        buf.write("\u0084\3\2\2\2\16\u0089\3\2\2\2\20\u008f\3\2\2\2\22\u009f")
        buf.write("\3\2\2\2\24\u00a6\3\2\2\2\26\u00a8\3\2\2\2\30\u00b5\3")
        buf.write("\2\2\2\32\u00bc\3\2\2\2\34\u00be\3\2\2\2\36\u00c7\3\2")
        buf.write("\2\2 \u00ce\3\2\2\2\"\u00d5\3\2\2\2$\u00d7\3\2\2\2&\u00e2")
        buf.write("\3\2\2\2(\u00ed\3\2\2\2*\u00fb\3\2\2\2,\u0100\3\2\2\2")
        buf.write(".\u0104\3\2\2\2\60\u0112\3\2\2\2\62\u0114\3\2\2\2\64\u0124")
        buf.write("\3\2\2\2\66\u0129\3\2\2\28\u012d\3\2\2\2:\u0142\3\2\2")
        buf.write("\2<\u0144\3\2\2\2>\u014f\3\2\2\2@\u0159\3\2\2\2B\u0161")
        buf.write("\3\2\2\2D\u0167\3\2\2\2F\u016c\3\2\2\2H\u0177\3\2\2\2")
        buf.write("J\u017a\3\2\2\2L\u017d\3\2\2\2N\u0183\3\2\2\2P\u018b\3")
        buf.write("\2\2\2R\u0192\3\2\2\2T\u019d\3\2\2\2VW\7\60\2\2WZ\7/\2")
        buf.write("\2XZ\7/\2\2YV\3\2\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\")
        buf.write("\3\2\2\2\\^\3\2\2\2][\3\2\2\2^_\5\4\3\2_`\7\2\2\3`\3\3")
        buf.write("\2\2\2ab\5\6\4\2bc\5\4\3\2cf\3\2\2\2df\5\6\4\2ea\3\2\2")
        buf.write("\2ed\3\2\2\2f\5\3\2\2\2gl\5\b\5\2hi\5\n\6\2ij\5T+\2jl")
        buf.write("\3\2\2\2kg\3\2\2\2kh\3\2\2\2l\7\3\2\2\2mn\7\13\2\2no\7")
        buf.write(",\2\2oq\7)\2\2pr\5\24\13\2qp\3\2\2\2qr\3\2\2\2rs\3\2\2")
        buf.write("\2s}\7*\2\2tv\5T+\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2\2w~\5")
        buf.write("L\'\2xz\5T+\2yx\3\2\2\2yz\3\2\2\2z{\3\2\2\2{~\5R*\2|~")
        buf.write("\5T+\2}u\3\2\2\2}y\3\2\2\2}|\3\2\2\2~\t\3\2\2\2\177\u0083")
        buf.write("\5\f\7\2\u0080\u0083\5\20\t\2\u0081\u0083\5\16\b\2\u0082")
        buf.write("\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\13\3\2\2\2\u0084\u0085\7\t\2\2\u0085\u0086\7,\2\2\u0086")
        buf.write("\u0087\7\36\2\2\u0087\u0088\5 \21\2\u0088\r\3\2\2\2\u0089")
        buf.write("\u008a\7\n\2\2\u008a\u008d\7,\2\2\u008b\u008c\7\36\2\2")
        buf.write("\u008c\u008e\5 \21\2\u008d\u008b\3\2\2\2\u008d\u008e\3")
        buf.write("\2\2\2\u008e\17\3\2\2\2\u008f\u0090\t\2\2\2\u0090\u0095")
        buf.write("\7,\2\2\u0091\u0092\7\'\2\2\u0092\u0093\5\22\n\2\u0093")
        buf.write("\u0094\7(\2\2\u0094\u0096\3\2\2\2\u0095\u0091\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0098\7")
        buf.write("\36\2\2\u0098\u009a\5 \21\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\21\3\2\2\2\u009b\u009c\7-\2\2\u009c")
        buf.write("\u009d\7+\2\2\u009d\u00a0\5\22\n\2\u009e\u00a0\7-\2\2")
        buf.write("\u009f\u009b\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\23\3\2")
        buf.write("\2\2\u00a1\u00a2\5\26\f\2\u00a2\u00a3\7+\2\2\u00a3\u00a4")
        buf.write("\5\24\13\2\u00a4\u00a7\3\2\2\2\u00a5\u00a7\5\26\f\2\u00a6")
        buf.write("\u00a1\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\25\3\2\2\2\u00a8")
        buf.write("\u00a9\t\2\2\2\u00a9\u00ae\7,\2\2\u00aa\u00ab\7\'\2\2")
        buf.write("\u00ab\u00ac\5\22\n\2\u00ac\u00ad\7(\2\2\u00ad\u00af\3")
        buf.write("\2\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\27")
        buf.write("\3\2\2\2\u00b0\u00b6\7-\2\2\u00b1\u00b6\7.\2\2\u00b2\u00b6")
        buf.write("\7\3\2\2\u00b3\u00b6\7\4\2\2\u00b4\u00b6\5\34\17\2\u00b5")
        buf.write("\u00b0\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5\u00b2\3\2\2\2")
        buf.write("\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\31\3\2")
        buf.write("\2\2\u00b7\u00b8\5 \21\2\u00b8\u00b9\7+\2\2\u00b9\u00ba")
        buf.write("\5\32\16\2\u00ba\u00bd\3\2\2\2\u00bb\u00bd\5 \21\2\u00bc")
        buf.write("\u00b7\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\33\3\2\2\2\u00be")
        buf.write("\u00bf\7\'\2\2\u00bf\u00c0\5\36\20\2\u00c0\u00c1\7(\2")
        buf.write("\2\u00c1\35\3\2\2\2\u00c2\u00c3\5 \21\2\u00c3\u00c4\7")
        buf.write("+\2\2\u00c4\u00c5\5\36\20\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c8\5 \21\2\u00c7\u00c2\3\2\2\2\u00c7\u00c6\3\2\2\2")
        buf.write("\u00c8\37\3\2\2\2\u00c9\u00ca\5\"\22\2\u00ca\u00cb\7&")
        buf.write("\2\2\u00cb\u00cc\5\"\22\2\u00cc\u00cf\3\2\2\2\u00cd\u00cf")
        buf.write("\5\"\22\2\u00ce\u00c9\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("!\3\2\2\2\u00d0\u00d1\5$\23\2\u00d1\u00d2\t\3\2\2\u00d2")
        buf.write("\u00d3\5$\23\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6\5$\23\2")
        buf.write("\u00d5\u00d0\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6#\3\2\2")
        buf.write("\2\u00d7\u00d8\b\23\1\2\u00d8\u00d9\5&\24\2\u00d9\u00df")
        buf.write("\3\2\2\2\u00da\u00db\f\4\2\2\u00db\u00dc\t\4\2\2\u00dc")
        buf.write("\u00de\5&\24\2\u00dd\u00da\3\2\2\2\u00de\u00e1\3\2\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0%\3\2\2")
        buf.write("\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\b\24\1\2\u00e3\u00e4")
        buf.write("\5(\25\2\u00e4\u00ea\3\2\2\2\u00e5\u00e6\f\4\2\2\u00e6")
        buf.write("\u00e7\t\5\2\2\u00e7\u00e9\5(\25\2\u00e8\u00e5\3\2\2\2")
        buf.write("\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3")
        buf.write("\2\2\2\u00eb\'\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee")
        buf.write("\b\25\1\2\u00ee\u00ef\5*\26\2\u00ef\u00f5\3\2\2\2\u00f0")
        buf.write("\u00f1\f\4\2\2\u00f1\u00f2\t\6\2\2\u00f2\u00f4\5*\26\2")
        buf.write("\u00f3\u00f0\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3")
        buf.write("\2\2\2\u00f5\u00f6\3\2\2\2\u00f6)\3\2\2\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f8\u00f9\7\30\2\2\u00f9\u00fc\5*\26\2\u00fa")
        buf.write("\u00fc\5,\27\2\u00fb\u00f8\3\2\2\2\u00fb\u00fa\3\2\2\2")
        buf.write("\u00fc+\3\2\2\2\u00fd\u00fe\7\32\2\2\u00fe\u0101\5,\27")
        buf.write("\2\u00ff\u0101\5.\30\2\u0100\u00fd\3\2\2\2\u0100\u00ff")
        buf.write("\3\2\2\2\u0101-\3\2\2\2\u0102\u0105\5B\"\2\u0103\u0105")
        buf.write("\5\60\31\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105")
        buf.write("/\3\2\2\2\u0106\u0113\7,\2\2\u0107\u0113\5\30\r\2\u0108")
        buf.write("\u0109\7)\2\2\u0109\u010a\5 \21\2\u010a\u010b\7*\2\2\u010b")
        buf.write("\u0113\3\2\2\2\u010c\u010d\7,\2\2\u010d\u010f\7)\2\2\u010e")
        buf.write("\u0110\5\32\16\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2")
        buf.write("\2\u0110\u0111\3\2\2\2\u0111\u0113\7*\2\2\u0112\u0106")
        buf.write("\3\2\2\2\u0112\u0107\3\2\2\2\u0112\u0108\3\2\2\2\u0112")
        buf.write("\u010c\3\2\2\2\u0113\61\3\2\2\2\u0114\u0119\5\64\33\2")
        buf.write("\u0115\u0117\5T+\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2")
        buf.write("\2\2\u0117\u0118\3\2\2\2\u0118\u011a\5\62\32\2\u0119\u0116")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\63\3\2\2\2\u011b\u0125")
        buf.write("\5\66\34\2\u011c\u0125\5@!\2\u011d\u0125\58\35\2\u011e")
        buf.write("\u0125\5F$\2\u011f\u0125\5H%\2\u0120\u0125\5J&\2\u0121")
        buf.write("\u0125\5L\'\2\u0122\u0125\5N(\2\u0123\u0125\5R*\2\u0124")
        buf.write("\u011b\3\2\2\2\u0124\u011c\3\2\2\2\u0124\u011d\3\2\2\2")
        buf.write("\u0124\u011e\3\2\2\2\u0124\u011f\3\2\2\2\u0124\u0120\3")
        buf.write("\2\2\2\u0124\u0121\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0123")
        buf.write("\3\2\2\2\u0125\65\3\2\2\2\u0126\u012a\5\f\7\2\u0127\u012a")
        buf.write("\5\20\t\2\u0128\u012a\5\16\b\2\u0129\u0126\3\2\2\2\u0129")
        buf.write("\u0127\3\2\2\2\u0129\u0128\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012c\5T+\2\u012c\67\3\2\2\2\u012d\u012e\7\21\2")
        buf.write("\2\u012e\u012f\7)\2\2\u012f\u0130\5 \21\2\u0130\u0132")
        buf.write("\7*\2\2\u0131\u0133\5T+\2\u0132\u0131\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0136\5\62\32\2\u0135")
        buf.write("\u0137\5T+\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0139\3\2\2\2\u0138\u013a\5:\36\2\u0139\u0138\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u013d\5")
        buf.write("> \2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d9\3")
        buf.write("\2\2\2\u013e\u013f\5<\37\2\u013f\u0140\5:\36\2\u0140\u0143")
        buf.write("\3\2\2\2\u0141\u0143\5<\37\2\u0142\u013e\3\2\2\2\u0142")
        buf.write("\u0141\3\2\2\2\u0143;\3\2\2\2\u0144\u0145\7\23\2\2\u0145")
        buf.write("\u0146\7)\2\2\u0146\u0147\5 \21\2\u0147\u0149\7*\2\2\u0148")
        buf.write("\u014a\5T+\2\u0149\u0148\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014d\5\62\32\2\u014c\u014e\5T+\2")
        buf.write("\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e=\3\2\2")
        buf.write("\2\u014f\u0151\7\22\2\2\u0150\u0152\5T+\2\u0151\u0150")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0155\5\62\32\2\u0154\u0156\5T+\2\u0155\u0154\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156?\3\2\2\2\u0157\u015a\7,\2\2")
        buf.write("\u0158\u015a\5D#\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2")
        buf.write("\2\2\u015a\u015b\3\2\2\2\u015b\u015c\7\36\2\2\u015c\u015d")
        buf.write("\5 \21\2\u015d\u015e\5T+\2\u015eA\3\2\2\2\u015f\u0162")
        buf.write("\7,\2\2\u0160\u0162\5P)\2\u0161\u015f\3\2\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\7\'\2\2\u0164")
        buf.write("\u0165\5\32\16\2\u0165\u0166\7(\2\2\u0166C\3\2\2\2\u0167")
        buf.write("\u0168\7,\2\2\u0168\u0169\7\'\2\2\u0169\u016a\5\32\16")
        buf.write("\2\u016a\u016b\7(\2\2\u016bE\3\2\2\2\u016c\u016d\7\f\2")
        buf.write("\2\u016d\u016e\7,\2\2\u016e\u016f\7\r\2\2\u016f\u0170")
        buf.write("\5 \21\2\u0170\u0171\7\16\2\2\u0171\u0173\5 \21\2\u0172")
        buf.write("\u0174\5T+\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0176\5\64\33\2\u0176G\3\2\2\2\u0177")
        buf.write("\u0178\7\17\2\2\u0178\u0179\5T+\2\u0179I\3\2\2\2\u017a")
        buf.write("\u017b\7\20\2\2\u017b\u017c\5T+\2\u017cK\3\2\2\2\u017d")
        buf.write("\u017f\7\b\2\2\u017e\u0180\5 \21\2\u017f\u017e\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\5")
        buf.write("T+\2\u0182M\3\2\2\2\u0183\u0184\7,\2\2\u0184\u0186\7)")
        buf.write("\2\2\u0185\u0187\5\32\16\2\u0186\u0185\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\7*\2\2\u0189")
        buf.write("\u018a\5T+\2\u018aO\3\2\2\2\u018b\u018c\7,\2\2\u018c\u018e")
        buf.write("\7)\2\2\u018d\u018f\5\32\16\2\u018e\u018d\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\7*\2\2")
        buf.write("\u0191Q\3\2\2\2\u0192\u0193\7\24\2\2\u0193\u0195\5T+\2")
        buf.write("\u0194\u0196\5\62\32\2\u0195\u0194\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\7\25\2\2\u0198")
        buf.write("\u0199\5T+\2\u0199S\3\2\2\2\u019a\u019b\7/\2\2\u019b\u019e")
        buf.write("\7\60\2\2\u019c\u019e\7/\2\2\u019d\u019a\3\2\2\2\u019d")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0U\3\2\2\2\64Y[ekquy}\u0082\u008d")
        buf.write("\u0095\u0099\u009f\u00a6\u00ae\u00b5\u00bc\u00c7\u00ce")
        buf.write("\u00d5\u00df\u00ea\u00f5\u00fb\u0100\u0104\u010f\u0112")
        buf.write("\u0116\u0119\u0124\u0129\u0132\u0136\u0139\u013c\u0142")
        buf.write("\u0149\u014d\u0151\u0155\u0159\u0161\u0173\u017f\u0186")
        buf.write("\u018e\u0195\u019d\u019f")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'and'", 
                     "'or'", "'not'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'<-'", "'='", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'...'", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "AND", "OR", "NOT", "ADD", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULO", "ASSIGNINIT", "EQUAL_NUMBER", 
                      "EQUAL_STRING", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                      "GREATER", "GREATER_EQUAL", "CONCAT", "LBRACKET", 
                      "RBRACKET", "LPARENT", "RPARENT", "COMMA", "ID", "NUMBER_LITERAL", 
                      "STRING_LITERAL", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_function = 3
    RULE_variables = 4
    RULE_implicit_var = 5
    RULE_implicit_dynamic = 6
    RULE_keyword_var = 7
    RULE_list_NUMBER_LIT = 8
    RULE_parameters_list = 9
    RULE_parameter = 10
    RULE_literal = 11
    RULE_list_expr = 12
    RULE_array_literal = 13
    RULE_list_literal = 14
    RULE_exp = 15
    RULE_exp1 = 16
    RULE_exp2 = 17
    RULE_exp3 = 18
    RULE_exp4 = 19
    RULE_exp5 = 20
    RULE_exp6 = 21
    RULE_exp7 = 22
    RULE_exp8 = 23
    RULE_list_stmts = 24
    RULE_stmt = 25
    RULE_declaration_stmt = 26
    RULE_if_stmt = 27
    RULE_list_elif_stmts = 28
    RULE_elif_stmt = 29
    RULE_else_stmt = 30
    RULE_assignment_stmt = 31
    RULE_index_operators = 32
    RULE_index_operators1 = 33
    RULE_for_stmt = 34
    RULE_break_stmt = 35
    RULE_continue_stmt = 36
    RULE_return_stmt = 37
    RULE_call_stmt = 38
    RULE_call_stmt1 = 39
    RULE_block_stmt = 40
    RULE_ignore = 41

    ruleNames =  [ "program", "list_declared", "declared", "function", "variables", 
                   "implicit_var", "implicit_dynamic", "keyword_var", "list_NUMBER_LIT", 
                   "parameters_list", "parameter", "literal", "list_expr", 
                   "array_literal", "list_literal", "exp", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "list_stmts", 
                   "stmt", "declaration_stmt", "if_stmt", "list_elif_stmts", 
                   "elif_stmt", "else_stmt", "assignment_stmt", "index_operators", 
                   "index_operators1", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "call_stmt", "call_stmt1", "block_stmt", 
                   "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    AND=20
    OR=21
    NOT=22
    ADD=23
    MINUS=24
    MULTIPLY=25
    DIVIDE=26
    MODULO=27
    ASSIGNINIT=28
    EQUAL_NUMBER=29
    EQUAL_STRING=30
    NOT_EQUAL=31
    LESS=32
    LESS_EQUAL=33
    GREATER=34
    GREATER_EQUAL=35
    CONCAT=36
    LBRACKET=37
    RBRACKET=38
    LPARENT=39
    RPARENT=40
    COMMA=41
    ID=42
    NUMBER_LITERAL=43
    STRING_LITERAL=44
    NEWLINE=45
    COMMENTS=46
    WS=47
    ERROR_CHAR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def COMMENTS(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMENTS)
            else:
                return self.getToken(ZCodeParser.COMMENTS, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE or _la==ZCodeParser.COMMENTS:
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.COMMENTS]:
                    self.state = 84
                    self.match(ZCodeParser.COMMENTS)
                    self.state = 85
                    self.match(ZCodeParser.NEWLINE)
                    pass
                elif token in [ZCodeParser.NEWLINE]:
                    self.state = 86
                    self.match(ZCodeParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.list_declared()
            self.state = 93
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.declared()
                self.state = 96
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.variables()
                self.state = 103
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def parameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ZCodeParser.FUNC)
            self.state = 108
            self.match(ZCodeParser.ID)
            self.state = 109
            self.match(ZCodeParser.LPARENT)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 110
                self.parameters_list()


            self.state = 113
            self.match(ZCodeParser.RPARENT)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 114
                    self.ignore()


                self.state = 117
                self.return_stmt()
                pass

            elif la_ == 2:
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 118
                    self.ignore()


                self.state = 121
                self.block_stmt()
                pass

            elif la_ == 3:
                self.state = 122
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variables)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.implicit_var()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ZCodeParser.VAR)
            self.state = 131
            self.match(ZCodeParser.ID)
            self.state = 132
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 133
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ZCodeParser.DYNAMIC)
            self.state = 136
            self.match(ZCodeParser.ID)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGNINIT:
                self.state = 137
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 138
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 142
            self.match(ZCodeParser.ID)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 143
                self.match(ZCodeParser.LBRACKET)
                self.state = 144
                self.list_NUMBER_LIT()
                self.state = 145
                self.match(ZCodeParser.RBRACKET)


            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGNINIT:
                self.state = 149
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 150
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_NUMBER_LITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_NUMBER_LIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_NUMBER_LIT" ):
                return visitor.visitList_NUMBER_LIT(self)
            else:
                return visitor.visitChildren(self)




    def list_NUMBER_LIT(self):

        localctx = ZCodeParser.List_NUMBER_LITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_NUMBER_LIT)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 154
                self.match(ZCodeParser.COMMA)
                self.state = 155
                self.list_NUMBER_LIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameters_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters_list" ):
                return visitor.visitParameters_list(self)
            else:
                return visitor.visitChildren(self)




    def parameters_list(self):

        localctx = ZCodeParser.Parameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameters_list)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.parameter()
                self.state = 160
                self.match(ZCodeParser.COMMA)
                self.state = 161
                self.parameters_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 167
            self.match(ZCodeParser.ID)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 168
                self.match(ZCodeParser.LBRACKET)
                self.state = 169
                self.list_NUMBER_LIT()
                self.state = 170
                self.match(ZCodeParser.RBRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(ZCodeParser.STRING_LITERAL, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass
            elif token in [ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(ZCodeParser.STRING_LITERAL)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = ZCodeParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_expr)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.exp()
                self.state = 182
                self.match(ZCodeParser.COMMA)
                self.state = 183
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def list_literal(self):
            return self.getTypedRuleContext(ZCodeParser.List_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.LBRACKET)

            self.state = 189
            self.list_literal()
            self.state = 190
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_literal(self):
            return self.getTypedRuleContext(ZCodeParser.List_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = ZCodeParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_literal)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.exp()
                self.state = 193
                self.match(ZCodeParser.COMMA)
                self.state = 194
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.exp1()
                self.state = 200
                self.match(ZCodeParser.CONCAT)
                self.state = 201
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp2Context,i)


        def EQUAL_NUMBER(self):
            return self.getToken(ZCodeParser.EQUAL_NUMBER, 0)

        def EQUAL_STRING(self):
            return self.getToken(ZCodeParser.EQUAL_STRING, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = ZCodeParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.exp2(0)
                self.state = 207
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL_NUMBER) | (1 << ZCodeParser.EQUAL_STRING) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LESS_EQUAL) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GREATER_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.exp3(0) 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 227
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 228
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 229
                    self.exp4(0) 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def MULTIPLY(self):
            return self.getToken(ZCodeParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ZCodeParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(ZCodeParser.MODULO, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 238
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 239
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 240
                    self.exp5() 
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp5)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(ZCodeParser.NOT)
                self.state = 247
                self.exp5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.MINUS, ZCodeParser.LBRACKET, ZCodeParser.LPARENT, ZCodeParser.ID, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp6)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(ZCodeParser.MINUS)
                self.state = 252
                self.exp6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LBRACKET, ZCodeParser.LPARENT, ZCodeParser.ID, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def exp8(self):
            return self.getTypedRuleContext(ZCodeParser.Exp8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp7)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = ZCodeParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp8)
        self._la = 0 # Token type
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.match(ZCodeParser.LPARENT)
                self.state = 263
                self.exp()
                self.state = 264
                self.match(ZCodeParser.RPARENT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.match(ZCodeParser.ID)
                self.state = 267
                self.match(ZCodeParser.LPARENT)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPARENT) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.STRING_LITERAL))) != 0):
                    self.state = 268
                    self.list_expr()


                self.state = 271
                self.match(ZCodeParser.RPARENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def list_stmts(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtsContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmts" ):
                return visitor.visitList_stmts(self)
            else:
                return visitor.visitChildren(self)




    def list_stmts(self):

        localctx = ZCodeParser.List_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.stmt()
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 275
                    self.ignore()


                self.state = 278
                self.list_stmts()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_stmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.declaration_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 286
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 287
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 288
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 289
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_stmt" ):
                return visitor.visitDeclaration_stmt(self)
            else:
                return visitor.visitChildren(self)




    def declaration_stmt(self):

        localctx = ZCodeParser.Declaration_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_declaration_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.state = 292
                self.implicit_var()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 293
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 294
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 297
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtsContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def list_elif_stmts(self):
            return self.getTypedRuleContext(ZCodeParser.List_elif_stmtsContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ZCodeParser.IF)
            self.state = 300
            self.match(ZCodeParser.LPARENT)
            self.state = 301
            self.exp()
            self.state = 302
            self.match(ZCodeParser.RPARENT)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 303
                self.ignore()


            self.state = 306
            self.list_stmts()
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 307
                self.ignore()


            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 310
                self.list_elif_stmts()


            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 313
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elif_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def list_elif_stmts(self):
            return self.getTypedRuleContext(ZCodeParser.List_elif_stmtsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_elif_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elif_stmts" ):
                return visitor.visitList_elif_stmts(self)
            else:
                return visitor.visitChildren(self)




    def list_elif_stmts(self):

        localctx = ZCodeParser.List_elif_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_list_elif_stmts)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.elif_stmt()
                self.state = 317
                self.list_elif_stmts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.elif_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtsContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(ZCodeParser.ELIF)
            self.state = 323
            self.match(ZCodeParser.LPARENT)
            self.state = 324
            self.exp()
            self.state = 325
            self.match(ZCodeParser.RPARENT)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 326
                self.ignore()


            self.state = 329
            self.list_stmts()
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 330
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtsContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ZCodeParser.ELSE)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 334
                self.ignore()


            self.state = 337
            self.list_stmts()
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 338
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def index_operators1(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operators1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = ZCodeParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 341
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 342
                self.index_operators1()
                pass


            self.state = 345
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 346
            self.exp()
            self.state = 347
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def call_stmt1(self):
            return self.getTypedRuleContext(ZCodeParser.Call_stmt1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_index_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 349
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 350
                self.call_stmt1()
                pass


            self.state = 353
            self.match(ZCodeParser.LBRACKET)
            self.state = 354
            self.list_expr()
            self.state = 355
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operators1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators1" ):
                return visitor.visitIndex_operators1(self)
            else:
                return visitor.visitChildren(self)




    def index_operators1(self):

        localctx = ZCodeParser.Index_operators1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_index_operators1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ZCodeParser.ID)
            self.state = 358
            self.match(ZCodeParser.LBRACKET)
            self.state = 359
            self.list_expr()
            self.state = 360
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ZCodeParser.FOR)
            self.state = 363
            self.match(ZCodeParser.ID)
            self.state = 364
            self.match(ZCodeParser.UNTIL)
            self.state = 365
            self.exp()
            self.state = 366
            self.match(ZCodeParser.BY)
            self.state = 367
            self.exp()
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 368
                self.ignore()


            self.state = 371
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(ZCodeParser.BREAK)
            self.state = 374
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(ZCodeParser.CONTINUE)
            self.state = 377
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ZCodeParser.RETURN)
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPARENT) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.STRING_LITERAL))) != 0):
                self.state = 380
                self.exp()


            self.state = 383
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = ZCodeParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(ZCodeParser.ID)
            self.state = 386
            self.match(ZCodeParser.LPARENT)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPARENT) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.STRING_LITERAL))) != 0):
                self.state = 387
                self.list_expr()


            self.state = 390
            self.match(ZCodeParser.RPARENT)
            self.state = 391
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmt1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_stmt1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt1" ):
                return visitor.visitCall_stmt1(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt1(self):

        localctx = ZCodeParser.Call_stmt1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_call_stmt1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(ZCodeParser.ID)
            self.state = 394
            self.match(ZCodeParser.LPARENT)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPARENT) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.STRING_LITERAL))) != 0):
                self.state = 395
                self.list_expr()


            self.state = 398
            self.match(ZCodeParser.RPARENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(ZCodeParser.BEGIN)
            self.state = 401
            self.ignore()
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.ID))) != 0):
                self.state = 402
                self.list_stmts()


            self.state = 405
            self.match(ZCodeParser.END)
            self.state = 406
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def COMMENTS(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMENTS)
            else:
                return self.getToken(ZCodeParser.COMMENTS, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 411
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                    if la_ == 1:
                        self.state = 408
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 409
                        self.match(ZCodeParser.COMMENTS)
                        pass

                    elif la_ == 2:
                        self.state = 410
                        self.match(ZCodeParser.NEWLINE)
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 413 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.exp2_sempred
        self._predicates[18] = self.exp3_sempred
        self._predicates[19] = self.exp4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




