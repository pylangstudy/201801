# [19.1.2. email.parser: 電子メールメッセージのパース](https://docs.python.jp/3/library/email.parser.html)

< [19.1. email — 電子メールと MIME 処理のためのパッケージ](https://docs.python.jp/3/library/email.html) < [19. インターネット上のデータの操作](https://docs.python.jp/3/library/netdata.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/email/parser.py](https://github.com/python/cpython/tree/3.6/Lib/email/parser.py)

ほぼ英文。和訳されていない……。コード例もない……。

参考

* https://qiita.com/stkdev/items/a44976fb81ae90a66381

> Message object structures can be created in one of two ways: they can be created from whole cloth by creating an EmailMessage object, adding headers using the dictionary interface, and adding payload(s) using set_content() and related methods, or they can be created by parsing a serialized representation of the email message.

> The email package provides a standard parser that understands most email document structures, including MIME documents. You can pass the parser a bytes, string or file object, and the parser will return to you the root EmailMessage instance of the object structure. For simple, non-MIME messages the payload of this root object will likely be a string containing the text of the message. For MIME messages, the root object will return True from its is_multipart() method, and the subparts can be accessed via the payload manipulation methods, such as get_body(), iter_parts(), and walk().

> There are actually two parser interfaces available for use, the Parser API and the incremental FeedParser API. The Parser API is most useful if you have the entire text of the message in memory, or if the entire message lives in a file on the file system. FeedParser is more appropriate when you are reading the message from a stream which might block waiting for more input (such as reading an email message from a socket). The FeedParser can consume and parse the message incrementally, and only returns the root object when you close the parser.

> Note that the parser can be extended in limited ways, and of course you can implement your own parser completely from scratch. All of the logic that connects the email package’s bundled parser and the EmailMessage class is embodied in the policy class, so a custom parser can create message object trees any way it finds necessary by implementing custom versions of the appropriate policy methods.

以下、Google翻訳。

> メッセージオブジェクト構造は、EmailMessageオブジェクトを作成し、辞書インターフェイスを使用してヘッダを追加し、set_content（）および関連するメソッドを使用してペイロードを追加することによって布全体から作成することも、電子メールメッセージのシリアライズされた表現を解析することによって作成される。

> 電子メールパッケージは、MIMEドキュメントを含むほとんどの電子メールドキュメント構造を理解する標準パーサーを提供します。パーサにバイト、文字列、またはファイルオブジェクトを渡すことができます。パーサーは、オブジェクト構造のルートEmailMessageインスタンスを返します。単純な非MIMEメッセージの場合、このルートオブジェクトのペイロードは、おそらくメッセージのテキストを含む文字列になります。 MIMEメッセージの場合、ルートオブジェクトはis_multipart（）メソッドからTrueを返し、サブパートはget_body（）、iter_parts（）、walk（）などのペイロード操作メソッドを介してアクセスできます。

> 実際には、Parser APIとインクリメンタルなFeedParser APIの2つのパーサーインタフェースが使用可能です。 Parser APIは、メッセージのテキスト全体がメモリにある場合、またはメッセージ全体がファイルシステム上のファイルに存在する場合に最も便利です。 FeedParserは、より多くの入力を待つことを阻む可能性があるストリームからメッセージを読み取っているとき（ソケットからの電子メールメッセージの読み取りなど）、より適切です。 FeedParserは、メッセージを徐々に消費して解析することができ、パーサーを閉じるとルートオブジェクトのみを返します。

> パーサは限られた方法で拡張することができます。もちろん、独自のパーサーを最初から完全に実装することもできます。電子メールパッケージのバンドルされたパーサーとEmailMessageクラスを接続するすべてのロジックはポリシークラスに実装されているため、カスタムパーサーは、適切なポリシーメソッドのカスタムバージョンを実装することによって、必要に応じてメッセージオブジェクトツリーを作成できます。

## [19.1.2.1. FeedParser API](https://docs.python.jp/3/library/email.parser.html#feedparser-api)

> The BytesFeedParser, imported from the email.feedparser module, provides an API that is conducive to incremental parsing of email messages, such as would be necessary when reading the text of an email message from a source that can block (such as a socket). The BytesFeedParser can of course be used to parse an email message fully contained in a bytes-like object, string, or file, but the BytesParser API may be more convenient for such use cases. The semantics and results of the two parser APIs are identical.

> The BytesFeedParser’s API is simple; you create an instance, feed it a bunch of bytes until there’s no more to feed it, then close the parser to retrieve the root message object. The BytesFeedParser is extremely accurate when parsing standards-compliant messages, and it does a very good job of parsing non-compliant messages, providing information about how a message was deemed broken. It will populate a message object’s defects attribute with a list of any problems it found in a message. See the email.errors module for the list of defects that it can find.

> Here is the API for the BytesFeedParser:

以下、Google翻訳。

> email.feedparserモジュールからインポートされたBytesFeedParserは、ブロックする可能性のあるソース（ソケットなど）から電子メールメッセージのテキストを読み取る際に必要となる、電子メールメッセージのインクリメンタル解析に役立つAPIを提供します。 BytesFeedParserはもちろん、バイトのようなオブジェクト、文字列、またはファイルに完全に含まれる電子メールメッセージを解析するために使用できますが、BytesParser APIはそのような使用例の方が便利です。 2つのパーサーAPIのセマンティクスと結果は同じです。

> BytesFeedParserのAPIは単純です。インスタンスを作成し、それ以上フィードがなくなるまでバイトの束をフィードし、パーサを閉じてルートメッセージオブジェクトを取得します。 BytesFeedParserは、標準に準拠したメッセージを解析する際に非常に正確であり、メッセージがどのように壊れたとみなされたかに関する情報を提供する、非準拠のメッセージの解析に非常に適しています。メッセージオブジェクトのdefect属性に、メッセージ内で見つかった問題のリストが挿入されます。見つけ出すことができる欠陥のリストについては、email.errorsモジュールを参照してください。

> BytesFeedParserのAPIは次のとおりです。

属性|概要
----|----
class email.parser.BytesFeedParser(_factory=None, *, policy=policy.compat32)|Create a BytesFeedParser instance. Optional _factory is a no-argument callable; if not specified use the message_factory from the policy. Call _factory whenever a new message object is needed.
    feed(data)|    Feed the parser some more data. data should be a bytes-like object containing one or more lines. The lines can be partial and the parser will stitch such partial lines together properly. The lines can have any of the three common line endings: carriage return, newline, or carriage return and newline (they can even be mixed).
    close()|    Complete the parsing of all previously fed data and return the root message object. It is undefined what happens if feed() is called after this method has been called.
class email.parser.FeedParser(_factory=None, *, policy=policy.compat32)|Works like BytesFeedParser except that the input to the feed() method must be a string. This is of limited utility, since the only way for such a message to be valid is for it to contain only ASCII text or, if utf8 is True, no binary attachments.

## [19.1.2.2. Parser API](https://docs.python.jp/3/library/email.parser.html#parser-api)

> The BytesParser class, imported from the email.parser module, provides an API that can be used to parse a message when the complete contents of the message are available in a bytes-like object or file. The email.parser module also provides Parser for parsing strings, and header-only parsers, BytesHeaderParser and HeaderParser, which can be used if you’re only interested in the headers of the message. BytesHeaderParser and HeaderParser can be much faster in these situations, since they do not attempt to parse the message body, instead setting the payload to the raw body.

属性|概要
----|----
class email.parser.BytesParser(_class=None, *, policy=policy.compat32)|Create a BytesParser instance. The _class and policy arguments have the same meaning and semantics as the _factory and policy arguments of BytesFeedParser.
    parse(fp, headersonly=False)|    Read all the data from the binary file-like object fp, parse the resulting bytes, and return the message object. fp must support both the readline() and the read() methods.
    parsebytes(bytes, headersonly=False)|    Similar to the parse() method, except it takes a bytes-like object instead of a file-like object. Calling this method on a bytes-like object is equivalent to wrapping bytes in a BytesIO instance first and calling parse().
class email.parser.BytesHeaderParser(_class=None, *, policy=policy.compat32)|Exactly like BytesParser, except that headersonly defaults to True.
class email.parser.Parser(_class=None, *, policy=policy.compat32)|This class is parallel to BytesParser, but handles string input.
    parse(fp, headersonly=False)|    Read all the data from the text-mode file-like object fp, parse the resulting text, and return the root message object. fp must support both the readline() and the read() methods on file-like objects.
    parsestr(text, headersonly=False)|    Similar to the parse() method, except it takes a string object instead of a file-like object. Calling this method on a string is equivalent to wrapping text in a StringIO instance first and calling parse().
class email.parser.HeaderParser(_class=None, *, policy=policy.compat32)|Exactly like Parser, except that headersonly defaults to True.
email.message_from_bytes(s, _class=None, *, policy=policy.compat32)|Return a message object structure from a bytes-like object. This is equivalent to BytesParser().parsebytes(s). Optional _class and strict are interpreted as with the BytesParser class constructor.
message_from_binary_file(fp, _class=None, *, policy=policy.compat32)|Return a message object structure tree from an open binary file object. This is equivalent to BytesParser().parse(fp). _class and policy are interpreted as with the BytesParser class constructor.
email.message_from_string(s, _class=None, *, policy=policy.compat32)|Return a message object structure from a string. This is equivalent to Parser().parsestr(s). _class and policy are interpreted as with the Parser class constructor.
email.message_from_file(fp, _class=None, *, policy=policy.compat32)|Return a message object structure tree from an open file object. This is equivalent to Parser().parse(fp). _class and policy are interpreted as with the Parser class constructor.

## [19.1.2.3. 追記事項](https://docs.python.jp/3/library/email.parser.html#additional-notes)

> 以下はテキスト解析の際に適用されるいくつかの規約です:

* Most non-multipart type messages are parsed as a single message object with a string payload. These objects will return False for is_multipart(), and iter_parts() will yield an empty list.
* All multipart type messages will be parsed as a container message object with a list of sub-message objects for their payload. The outer container message will return True for is_multipart(), and iter_parts() will yield a list of subparts.
* Most messages with a content type of message/* (such as message/delivery-status and message/rfc822) will also be parsed as container object containing a list payload of length 1. Their is_multipart() method will return True. The single element yielded by iter_parts() will be a sub-message object.
* Some non-standards-compliant messages may not be internally consistent about their multipart-edness. Such messages may have a Content-Type header of type multipart, but their is_multipart() method may return False. If such messages were parsed with the FeedParser, they will have an instance of the MultipartInvariantViolationDefect class in their defects attribute list. See email.errors for details.

以下、Google翻訳。

*ほとんどのマルチパート以外のタイプのメッセージは、文字列ペイロードを持つ単一のメッセージオブジェクトとして解析されます。これらのオブジェクトはis_multipart（）に対してFalseを返し、iter_parts（）は空のリストを生成します。
*すべてのマルチパートタイプのメッセージは、ペイロード用のサブメッセージオブジェクトのリストを持つコンテナメッセージオブジェクトとして解析されます。外部コンテナメッセージはis_multipart（）に対してTrueを返し、iter_parts（）はサブパートのリストを生成します。
*メッセージ/ *（message / delivery-statusやmessage / rfc822など）のコンテンツタイプを持つほとんどのメッセージも、長さ1のリストペイロードを含むコンテナオブジェクトとして解析されます。is_multipart（）メソッドはTrueを返します。 iter_parts（）によって生成される単一の要素は、サブメッセージオブジェクトになります。
*規格に準拠していないメッセージの中には、それらの複数の部分について内部的に一貫性がないものもあります。そのようなメッセージはmultipart型のContent-Typeヘッダーを持つかもしれませんが、is_multipart（）メソッドはFalseを返します。このようなメッセージがFeedParserで解析された場合、そのオブジェクトはその欠陥属性リストにMultipartInvariantViolationDefectクラスのインスタンスを持ちます。詳細については、email.errorsを参照してください。

