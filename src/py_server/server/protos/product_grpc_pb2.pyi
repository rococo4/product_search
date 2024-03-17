from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ("name", "category", "subcategory", "subproduct", "link_to_product", "link_to_picture", "brand", "weight", "pfck", "information", "stores")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUBCATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUBPRODUCT_FIELD_NUMBER: _ClassVar[int]
    LINK_TO_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    LINK_TO_PICTURE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    PFCK_FIELD_NUMBER: _ClassVar[int]
    INFORMATION_FIELD_NUMBER: _ClassVar[int]
    STORES_FIELD_NUMBER: _ClassVar[int]
    name: str
    category: str
    subcategory: str
    subproduct: str
    link_to_product: str
    link_to_picture: str
    brand: str
    weight: int
    pfck: Pfck
    information: str
    stores: _containers.RepeatedCompositeFieldContainer[Store]
    def __init__(self, name: _Optional[str] = ..., category: _Optional[str] = ..., subcategory: _Optional[str] = ..., subproduct: _Optional[str] = ..., link_to_product: _Optional[str] = ..., link_to_picture: _Optional[str] = ..., brand: _Optional[str] = ..., weight: _Optional[int] = ..., pfck: _Optional[_Union[Pfck, _Mapping]] = ..., information: _Optional[str] = ..., stores: _Optional[_Iterable[_Union[Store, _Mapping]]] = ...) -> None: ...

class Pfck(_message.Message):
    __slots__ = ("protein", "fat", "carbohydrates", "kcal")
    PROTEIN_FIELD_NUMBER: _ClassVar[int]
    FAT_FIELD_NUMBER: _ClassVar[int]
    CARBOHYDRATES_FIELD_NUMBER: _ClassVar[int]
    KCAL_FIELD_NUMBER: _ClassVar[int]
    protein: float
    fat: float
    carbohydrates: float
    kcal: float
    def __init__(self, protein: _Optional[float] = ..., fat: _Optional[float] = ..., carbohydrates: _Optional[float] = ..., kcal: _Optional[float] = ...) -> None: ...

class Store(_message.Message):
    __slots__ = ("name", "price", "link_to_store")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LINK_TO_STORE_FIELD_NUMBER: _ClassVar[int]
    name: str
    price: float
    link_to_store: str
    def __init__(self, name: _Optional[str] = ..., price: _Optional[float] = ..., link_to_store: _Optional[str] = ...) -> None: ...

class ProductResponse(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: Product
    def __init__(self, product: _Optional[_Union[Product, _Mapping]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("search_request",)
    SEARCH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    search_request: str
    def __init__(self, search_request: _Optional[str] = ...) -> None: ...

class ProductRequest(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class ProductResponses(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, product: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
