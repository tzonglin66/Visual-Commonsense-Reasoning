# 作 者：田宗林
# 时 间：2021/8/13

Token
    text
    idx
    idx_end
    lemma_
    pos_
    tag_
    dep_
    ent_type_
    text_id
    type_id
    ensure_text
show_token
Tokenizer
    default_implementation
    batch_tokenize
    tokenize
    add_special_tokens
    num_special_tokens_for_sequence
    num_special_tokens_for_pair

@Tokenizer.register("whitespace")
@Tokenizer.register("just_spaces")
class WhitespaceTokenizer(Tokenizer)


@Tokenizer.register("spacy")
class SpacyTokenizer(Tokenizer):
    def __init__(
    self,
    language: str = "en_core_web_sm",
    pos_tags: bool = True,
    parse: bool = False,
    ner: bool = False,
    keep_spacy_tokens: bool = False,
    split_on_spaces: bool = False,
    start_tokens: Optional[List[str]] = None,
    end_tokens: Optional[List[str]] = None
    ) -> None
    batch_tokenize
    tokenize

IndexedTokenList = Dict[str, List[Any]]



DataArray = TypeVar("DataArray", torch.Tensor, Dict[str, torch.Tensor], Dict[str, Dict[str, torch.Tensor]])

class Field(Generic[DataArray])
    count_vocab_items
    human_readable_repr
    index
    get_padding_lengths
    as_tensor
    empty_field
    batch_tensors
    duplicate

class SequenceField(Field[DataArray])
    sequence_length
    empty_field

TextFieldTensors = Dict[str, Dict[str, torch.Tensor]]

class TextField(SequenceField[TextFieldTensors]):
    def __init__(
    self, 
    tokens: List[Token], 
    token_indexers: Optional[Dict[str, TokenIndexer]] = None
    ) -> None
    token_indexers
    count_vocab_items
    index
    get_padding_lengths
    sequence_length
    as_tensor
    empty_field
    batch_tensors
    __iter__
    duplicate
    human_readable_repr
