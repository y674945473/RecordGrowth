# 文本分割器

## TextSplitter
````
TextSplitter是LangChain中用于将长文本分割成短文本的抽象类。

chunk_size:用于指定在分割文本后，每个生成的文本块所允许的最大尺寸（长度）。
chunk_overlap:用于指定在分割文本时，相邻文本块之间的重叠长度。
keep_separator:用于指定在分割文本时，用于将文本块分隔成多个文本块的分隔符。
    1、当 keep_separator = False 时，分割文本时使用的分隔符将不会出现在分割后的文本块中。
    2、当 keep_separator = True 时，等同于 keep_separator = "start"，即分隔符会被保留，并放置在每个对应文本块的开头位置。
    3、当 keep_separator = "end" 时，分隔符会被保留，并放置在每个对应文本块的结尾位置。

TextSplitter的子类有CharacterTextSplitter、TokenTextSplitter、RecursiveCharacterTextSplitter和NLTKTextSplitter。

````