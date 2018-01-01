# [19.1.1. email.message: 電子メールメッセージの表現](https://docs.python.jp/3/library/email.message.html)

< [19.1. email — 電子メールと MIME 処理のためのパッケージ](https://docs.python.jp/3/library/email.html) < [19. インターネット上のデータの操作](https://docs.python.jp/3/library/netdata.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/email/message.py](https://github.com/python/cpython/tree/3.6/Lib/email/message.py)

ほぼ英文。和訳されていない……。

まともなコード例もない……。

参考

* https://qiita.com/denzow/items/a42d344fa343cd80cf86
* http://今日覚えたこと.biz/?p=1637

> The central class in the email package is the EmailMessage class, imported from the email.message module. It is the base class for the email object model. EmailMessage provides the core functionality for setting and querying header fields, for accessing message bodies, and for creating or modifying structured messages.

> An email message consists of headers and a payload (which is also referred to as the content). Headers are RFC 5322 or RFC 6532 style field names and values, where the field name and value are separated by a colon. The colon is not part of either the field name or the field value. The payload may be a simple text message, or a binary object, or a structured sequence of sub-messages each with their own set of headers and their own payload. The latter type of payload is indicated by the message having a MIME type such as multipart/* or message/rfc822.

> The conceptual model provided by an EmailMessage object is that of an ordered dictionary of headers coupled with a payload that represents the RFC 5322 body of the message, which might be a list of sub-EmailMessage objects. In addition to the normal dictionary methods for accessing the header names and values, there are methods for accessing specialized information from the headers (for example the MIME content type), for operating on the payload, for generating a serialized version of the message, and for recursively walking over the object tree.

> The EmailMessage dictionary-like interface is indexed by the header names, which must be ASCII values. The values of the dictionary are strings with some extra methods. Headers are stored and returned in case-preserving form, but field names are matched case-insensitively. Unlike a real dict, there is an ordering to the keys, and there can be duplicate keys. Additional methods are provided for working with headers that have duplicate keys.

> The payload is either a string or bytes object, in the case of simple message objects, or a list of EmailMessage objects, for MIME container documents such as multipart/* and message/rfc822 message objects.

以下、Google翻訳。

> 電子メールパッケージの中央クラスは、email.messageモジュールからインポートされたEmailMessageクラスです。電子メールオブジェクトモデルの基本クラスです。 EmailMessageは、ヘッダーフィールドの設定と照会、メッセージ本文へのアクセス、および構造化メッセージの作成または変更のためのコア機能を提供します。

> 電子メールメッセージは、ヘッダーとペイロード（コンテンツとも呼ばれます）で構成されます。ヘッダーはRFC 5322またはRFC 6532スタイルのフィールド名と値で、フィールド名と値はコロンで区切られます。コロンはフィールド名またはフィールド値の一部ではありません。ペイロードは、単純なテキストメッセージ、バイナリオブジェクト、または独自のヘッダーセットとそれぞれのペイロードを持つサブメッセージの構造化されたシーケンスです。後者のタイプのペイロードは、multipart / *またはmessage / rfc822のようなMIMEタイプを有するメッセージによって示される。

> EmailMessageオブジェクトによって提供される概念モデルは、メッセージのRFC 5322本体（サブEmailMessageオブジェクトのリストである可能性がある）を表すペイロードと結合された順序付けられたヘッダーの辞書のものです。ヘッダー名と値にアクセスするための通常の辞書メソッドに加えて、ヘッダー（たとえばMIMEコンテンツタイプ）から特殊な情報にアクセスする方法、ペイロードで操作する方法、メッセージのシリアル化バージョンを生成する方法、およびオブジェクトツリーを再帰的に歩くためのものです。

> EmailMessageディクショナリのようなインターフェイスは、ヘッダー名でインデックス付けされます。ヘッダー名はASCII値でなければなりません。辞書の値は、いくつかの余分なメソッドを持つ文字列です。ヘッダーは保存され、大文字小文字を区別した形式で返されますが、フィールド名は大文字と小文字を区別しません。実際の辞書とは異なり、キーには順序があり、キーが重複する可能性があります。重複したキーを持つヘッダーを操作するための追加のメソッドが用意されています。

> ペイロードは、単純なメッセージオブジェクトの場合は文字列オブジェクトまたはバイトオブジェクト、multipart / *およびmessage / rfc822メッセージオブジェクトなどのMIMEコンテナドキュメントの場合はEmailMessageオブジェクトのリストです。

属性|概要
----|----
class email.message.EmailMessage(policy=default)|If policy is specified use the rules it specifies to update and serialize the representation of the message. If policy is not set, use the default policy, which follows the rules of the email RFCs except for line endings (instead of the RFC mandated \r\n, it uses the Python standard \n line endings). For more information see the policy documentation.
as_string(unixfrom=False, maxheaderlen=None, policy=None)|Return the entire message flattened as a string. When optional unixfrom is true, the envelope header is included in the returned string. unixfrom defaults to False. For backward compatibility with the base Message class maxheaderlen is accepted, but defaults to None, which means that by default the line length is controlled by the max_line_length of the policy. The policy argument may be used to override the default policy obtained from the message instance. This can be used to control some of the formatting produced by the method, since the specified policy will be passed to the Generator.
__str__()|Equivalent to as_string(policy=self.policy.clone(utf8=True). Allows str(msg) to produce a string containing the serialized message in a readable format.
as_bytes(unixfrom=False, policy=None)|Return the entire message flattened as a bytes object. When optional unixfrom is true, the envelope header is included in the returned string. unixfrom defaults to False. The policy argument may be used to override the default policy obtained from the message instance. This can be used to control some of the formatting produced by the method, since the specified policy will be passed to the BytesGenerator.
__bytes__()|Equivalent to as_bytes(). Allows bytes(msg) to produce a bytes object containing the serialized message.
is_multipart()|Return True if the message’s payload is a list of sub-EmailMessage objects, otherwise return False. When is_multipart() returns False, the payload should be a string object (which might be a CTE encoded binary payload). Note that is_multipart() returning True does not necessarily mean that "msg.get_content_maintype() == 'multipart'" will return the True. For example, is_multipart will return True when the EmailMessage is of type message/rfc822.
set_unixfrom(unixfrom)|Set the message’s envelope header to unixfrom, which should be a string. (See mboxMessage for a brief description of this header.)
get_unixfrom()|メッセージのエンベロープヘッダを返します。エンベロープヘッダが設定されていない場合は None が返されます。
__len__()|複製されたものもふくめてヘッダ数の合計を返します。
__contains__(name)|Return true if the message object has a field named name. Matching is done without regard to case and name does not include the trailing colon. Used for the in operator. For example:
__getitem__(name)|Return the value of the named header field. name does not include the colon field separator. If the header is missing, None is returned; a KeyError is never raised.
__setitem__(name, val)|Add a header to the message with field name name and value val. The field is appended to the end of the message’s existing headers.
__delitem__(name)|メッセージのヘッダから、name という名前をもつフィールドをすべて除去します。たとえこの名前をもつヘッダが存在していなくても例外は発生しません。
keys()|メッセージ中にあるすべてのヘッダのフィールド名のリストを返します。
values()|メッセージ中にあるすべてのフィールドの値のリストを返します。
items()|メッセージ中にあるすべてのヘッダのフィールド名とその値を 2-タプルのリストとして返します。
get(name, failobj=None)|Return the value of the named header field. This is identical to __getitem__() except that optional failobj is returned if the named header is missing (failobj defaults to None).
get_all(name, failobj=None)|name の名前をもつフィールドのすべての値からなるリストを返します。該当する名前のヘッダがメッセージ中に含まれていない場合は failobj (デフォルトでは None) が返されます。
add_header(_name, _value, **_params)|拡張ヘッダ設定。このメソッドは __setitem__() と似ていますが、追加のヘッダ・パラメータをキーワード引数で指定できるところが違っています。 _name に追加するヘッダフィールドを、 _value にそのヘッダの 最初の 値を渡します。
replace_header(_name, _value)|Replace a header. Replace the first header found in the message that matches _name, retaining header order and field name case of the original header. If no matching header is found, raise a KeyError.
get_content_type()|Return the message’s content type, coerced to lower case of the form maintype/subtype. If there is no Content-Type header in the message return the value returned by get_default_type(). If the Content-Type header is invalid, return text/plain.
get_content_maintype()|そのメッセージの主 content-type を返します。これは get_content_type() によって返される文字列の maintype 部分です。
get_content_subtype()|そのメッセージの副 content-type (sub content-type、subtype) を返します。これは get_content_type() によって返される文字列の subtype 部分です。
get_default_type()|デフォルトの content-type を返します。ほどんどのメッセージではデフォルトの content-type は text/plain ですが、メッセージが multipart/digest コンテナに含まれているときだけ例外的に message/rfc822 になります。
set_default_type(ctype)|Set the default content type. ctype should either be text/plain or message/rfc822, although this is not enforced. The default content type is not stored in the Content-Type header, so it only affects the return value of the get_content_type methods when no Content-Type header is present in the message.
set_param(param, value, header='Content-Type', requote=True, charset=None, language='', replace=False)|Set a parameter in the Content-Type header. If the parameter already exists in the header, replace its value with value. When header is Content-Type (the default) and the header does not yet exist in the message, add it, set its value to text/plain, and append the new parameter value. Optional header specifies an alternative header to Content-Type.
del_param(param, header='content-type', requote=True)|Remove the given parameter completely from the Content-Type header. The header will be re-written in place without the parameter or its value. Optional header specifies an alternative to Content-Type.
get_filename(failobj=None)|そのメッセージ中の Content-Disposition ヘッダにある、 filename パラメータの値を返します。目的のヘッダに filename パラメータがない場合には Content-Type ヘッダにある name パラメータを探します。それも無い場合またはヘッダが無い場合には failobj が返されます。返される文字列はつねに email.utils.unquote() によって unquote されます。
get_boundary(failobj=None)|そのメッセージ中の Content-Type ヘッダにある、 boundary パラメータの値を返します。目的のヘッダが欠けていたり、 boundary パラメータがない場合には failobj が返されます。返される文字列はつねに email.utils.unquote() によって unquote されます。
set_boundary(boundary)|メッセージ中の Content-Type ヘッダにある、 boundary パラメータに値を設定します。 set_boundary() は必要に応じて boundary を quote します。そのメッセージが Content-Type ヘッダを含んでいない場合、 HeaderParseError が発生します。
get_content_charset(failobj=None)|そのメッセージ中の Content-Type ヘッダにある、 charset パラメータの値を返します。値はすべて小文字に変換されます。メッセージ中に Content-Type がなかったり、このヘッダ中に charaset パラメータがない場合には failobj が返されます。
get_charsets(failobj=None)|メッセージ中に含まれる文字セットの名前をすべてリストにして返します。そのメッセージが multipart である場合、返されるリストの各要素がそれぞれの subpart のペイロードに対応します。それ以外の場合、これは長さ 1 のリストを返します。
is_attachment()|Content-Disposition ヘッダが存在し、その (大文字小文字を区別しない) 値が attachment の場合、 True を返します。 それ以外の場合は False を返します。
get_content_disposition()|Return the lowercased value (without parameters) of the message’s Content-Disposition header if it has one, or None. The possible values for this method are inline, attachment or None if the message follows RFC 2183.
walk()|walk() メソッドは多目的のジェネレータで、これはあるメッセージオブジェクトツリー中のすべての part および subpart をわたり歩くのに使えます。順序は深さ優先です。おそらく典型的な用法は、 walk() を for ループ中でのイテレータとして使うことでしょう。ループを一回まわるごとに、次の subpart が返されるのです。
get_body(preferencelist=('related', 'html', 'plain'))|メッセージの "本体" の最有力候補となる MIME 部を返します。
iter_attachments()|Return an iterator over all of the immediate sub-parts of the message that are not candidate "body" parts. That is, skip the first occurrence of each of text/plain, text/html, multipart/related, or multipart/alternative (unless they are explicitly marked as attachments via Content-Disposition: attachment), and return all remaining parts. When applied directly to a multipart/related, return an iterator over the all the related parts except the root part (ie: the part pointed to by the start parameter, or the first part if there is no start parameter or the start parameter doesn’t match the Content-ID of any of the parts). When applied directly to a multipart/alternative or a non-multipart, return an empty iterator.
iter_parts()|Return an iterator over all of the immediate sub-parts of the message, which will be empty for a non-multipart. (See also walk().)
get_content(*args, content_manager=None, **kw)|Call the get_content() method of the content_manager, passing self as the message object, and passing along any other arguments or keywords as additional arguments. If content_manager is not specified, use the content_manager specified by the current policy.
set_content(*args, content_manager=None, **kw)|Call the set_content() method of the content_manager, passing self as the message object, and passing along any other arguments or keywords as additional arguments. If content_manager is not specified, use the content_manager specified by the current policy.
make_related(boundary=None)|Convert a non-multipart message into a multipart/related message, moving any existing Content- headers and payload into a (new) first part of the multipart. If boundary is specified, use it as the boundary string in the multipart, otherwise leave the boundary to be automatically created when it is needed (for example, when the message is serialized).
make_alternative(boundary=None)|Convert a non-multipart or a multipart/related into a multipart/alternative, moving any existing Content- headers and payload into a (new) first part of the multipart. If boundary is specified, use it as the boundary string in the multipart, otherwise leave the boundary to be automatically created when it is needed (for example, when the message is serialized).
make_mixed(boundary=None)|Convert a non-multipart, a multipart/related, or a multipart-alternative into a multipart/mixed, moving any existing Content- headers and payload into a (new) first part of the multipart. If boundary is specified, use it as the boundary string in the multipart, otherwise leave the boundary to be automatically created when it is needed (for example, when the message is serialized).
add_related(*args, content_manager=None, **kw)|If the message is a multipart/related, create a new message object, pass all of the arguments to its set_content() method, and attach() it to the multipart. If the message is a non-multipart, call make_related() and then proceed as above. If the message is any other type of multipart, raise a TypeError. If content_manager is not specified, use the content_manager specified by the current policy. If the added part has no Content-Disposition header, add one with the value inline.
add_alternative(*args, content_manager=None, **kw)|If the message is a multipart/alternative, create a new message object, pass all of the arguments to its set_content() method, and attach() it to the multipart. If the message is a non-multipart or multipart/related, call make_alternative() and then proceed as above. If the message is any other type of multipart, raise a TypeError. If content_manager is not specified, use the content_manager specified by the current policy.
add_attachment(*args, content_manager=None, **kw)|If the message is a multipart/mixed, create a new message object, pass all of the arguments to its set_content() method, and attach() it to the multipart. If the message is a non-multipart, multipart/related, or multipart/alternative, call make_mixed() and then proceed as above. If content_manager is not specified, use the content_manager specified by the current policy. If the added part has no Content-Disposition header, add one with the value attachment. This method can be used both for explicit attachments (Content-Disposition: attachment and inline attachments (Content-Disposition: inline), by passing appropriate options to the content_manager.
clear()|ペイロードとヘッダの全てを削除します。
clear_content()|Remove the payload and all of the Content- headers, leaving all other headers intact and in their original order.
preamble|MIME ドキュメントの形式では、ヘッダ直後にくる空行と最初の multipart 境界をあらわす文字列のあいだにいくらかのテキスト (訳注: preamble, 序文) を埋めこむことを許しています。このテキストは標準的な MIME の範疇からはみ出しているので、MIME 形式を認識するメールソフトからこれらは通常まったく見えません。しかしメッセージのテキストを生で見る場合、あるいはメッセージを MIME 対応していないメールソフトで見る場合、このテキストは目に見えることになります。
epilogue|The epilogue attribute acts the same way as the preamble attribute, except that it contains text that appears between the last boundary and the end of the message. As with the preamble, if there is no epilog text this attribute will be None.
defects|defects 属性はメッセージを解析する途中で検出されたすべての問題点 (defect、障害) のリストを保持しています。解析中に発見されうる障害についてのより詳細な説明は email.errors を参照してください。
class email.message.MIMEPart(policy=default)|This class represents a subpart of a MIME message. It is identical to EmailMessage, except that no MIME-Version headers are added when set_content() is called, since sub-parts do not need their own MIME-Version headers.

> 脚注

> [1]	Originally added in 3.4 as a provisional module. Docs for legacy message class moved to email.message.Message: Representing an email message using the compat32 API.

