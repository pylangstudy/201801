# [19.1.3. email.generator: MIME 文書の生成(原文)](https://docs.python.jp/3/library/email.generator.html)

< [19.1. email — 電子メールと MIME 処理のためのパッケージ](https://docs.python.jp/3/library/email.html) < [19. インターネット上のデータの操作](https://docs.python.jp/3/library/netdata.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/email/generator.py](https://github.com/python/cpython/tree/3.6/Lib/email/generator.py)

> One of the most common tasks is to generate the flat (serialized) version of the email message represented by a message object structure. You will need to do this if you want to send your message via smtplib.SMTP.sendmail() or the nntplib module, or print the message on the console. Taking a message object structure and producing a serialized representation is the job of the generator classes.

> As with the email.parser module, you aren’t limited to the functionality of the bundled generator; you could write one from scratch yourself. However the bundled generator knows how to generate most email in a standards-compliant way, should handle MIME and non-MIME email messages just fine, and is designed so that the bytes-oriented parsing and generation operations are inverses, assuming the same non-transforming policy is used for both. That is, parsing the serialized byte stream via the BytesParser class and then regenerating the serialized byte stream using BytesGenerator should produce output identical to the input [1]. (On the other hand, using the generator on an EmailMessage constructed by program may result in changes to the EmailMessage object as defaults are filled in.)

> The Generator class can be used to flatten a message into a text (as opposed to binary) serialized representation, but since Unicode cannot represent binary data directly, the message is of necessity transformed into something that contains only ASCII characters, using the standard email RFC Content Transfer Encoding techniques for encoding email messages for transport over channels that are not "8 bit clean".

以下、Google翻訳。

> 最も一般的なタスクの1つは、メッセージオブジェクト構造によって表される電子メールメッセージのフラット（シリアライズされた）バージョンを生成することです。 smtplib.SMTP.sendmail（）またはnntplibモジュール経由でメッセージを送信する場合や、メッセージをコンソールに出力する場合は、これを行う必要があります。メッセージオブジェクト構造体を取得し、直列化された表現を生成することは、ジェネレータクラスの仕事です。

> email.parserモジュールと同様に、バンドルされたジェネレータの機能に限定されません。あなたは一から自分自身を書くことができます。しかしバンドルされたジェネレータは標準準拠の方法でほとんどの電子メールを生成する方法を知っており、MIMEと非MIMEの電子メールメッセージをうまく処理し、バイト指向の解析と生成操作が逆であるように設計されています。両方のために変換ポリシーが使用されます。つまり、BytesParserクラスを介してシリアル化されたバイトストリームを解析し、次にBytesGeneratorを使用してシリアル化されたバイトストリームを再生成すると、入力[1]と同じ出力が生成されます。 （一方、プログラムによって作成されたEmailMessageでジェネレータを使用すると、デフォルトが埋め込まれた状態でEmailMessageオブジェクトが変更されることがあります）。

> Generatorクラスは、メッセージを（2進ではなく）テキストのシリアライズされた表現にフラット化するために使用できますが、Unicodeはバイナリデータを直接表現できないため、メッセージはASCII文字のみを含むものに変換されますコンテンツ転送「8ビットクリーン」ではないチャネル上のトランスポートのために電子メールメッセージをエンコードするためのエンコーディング技術。

属性|概要
----|----
class email.generator.BytesGenerator(outfp, mangle_from_=None, maxheaderlen=None, *, policy=None)|Return a BytesGenerator object that will write any message provided to the flatten() method, or any surrogateescape encoded text provided to the write() method, to the file-like object outfp. outfp must support a write method that accepts binary data.
flatten(msg, unixfrom=False, linesep=None)|Print the textual representation of the message object structure rooted at msg to the output file specified when the BytesGenerator instance was created.
clone(fp)|Return an independent clone of this BytesGenerator instance with the exact same option settings, and fp as the new outfp.
write(s)|Encode s using the ASCII codec and the surrogateescape error handler, and pass it to the write method of the outfp passed to the BytesGenerator’s constructor.
class email.generator.Generator(outfp, mangle_from_=None, maxheaderlen=None, *, policy=None)|Return a Generator object that will write any message provided to the flatten() method, or any text provided to the write() method, to the file-like object outfp. outfp must support a write method that accepts string data.
flatten(msg, unixfrom=False, linesep=None)|Print the textual representation of the message object structure rooted at msg to the output file specified when the Generator instance was created.
clone(fp)|Return an independent clone of this Generator instance with the exact same options, and fp as the new outfp.
write(s)|Write s to the write method of the outfp passed to the Generator’s constructor. This provides just enough file-like API for Generator instances to be used in the print() function.
class email.generator.DecodedGenerator(outfp, mangle_from_=None, maxheaderlen=None, fmt=None, *, policy=None)|Act like Generator, except that for any subpart of the message passed to Generator.flatten(), if the subpart is of main type text, print the decoded payload of the subpart, and if the main type is not text, instead of printing it fill in the string fmt using information from the part and print the resulting filled-in string.

> 脚注

> [1]	This statement assumes that you use the appropriate setting for unixfrom, and that there are no policy settings calling for automatic adjustments (for example, refold_source must be none, which is not the default). It is also not 100% true, since if the message does not conform to the RFC standards occasionally information about the exact original text is lost during parsing error recovery. It is a goal to fix these latter edge cases when possible.

