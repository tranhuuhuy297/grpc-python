# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookstore.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x62ookstore.proto\"L\n\x11\x42ookSearchRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x16\n\x0eprice_per_book\x18\x03 \x01(\x02\")\n\x12\x42ookSearchResponse\x12\x13\n\x0btotal_price\x18\x01 \x01(\x02\x32S\n\x11\x42ookSearchService\x12>\n\x0f\x42ulkSearchBooks\x12\x12.BookSearchRequest\x1a\x13.BookSearchResponse\"\x00(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bookstore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BOOKSEARCHREQUEST']._serialized_start=19
  _globals['_BOOKSEARCHREQUEST']._serialized_end=95
  _globals['_BOOKSEARCHRESPONSE']._serialized_start=97
  _globals['_BOOKSEARCHRESPONSE']._serialized_end=138
  _globals['_BOOKSEARCHSERVICE']._serialized_start=140
  _globals['_BOOKSEARCHSERVICE']._serialized_end=223
# @@protoc_insertion_point(module_scope)
