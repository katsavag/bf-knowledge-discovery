# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: embeddings.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x65mbeddings.proto\"!\n\x11\x45mbeddingsRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"6\n\x12\x45mbeddingsResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\nembeddings\x18\x02 \x03(\x01\x32L\n\nEmbeddings\x12>\n\x11ProcessEmbeddings\x12\x12.EmbeddingsRequest\x1a\x13.EmbeddingsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'embeddings_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMBEDDINGSREQUEST']._serialized_start=20
  _globals['_EMBEDDINGSREQUEST']._serialized_end=53
  _globals['_EMBEDDINGSRESPONSE']._serialized_start=55
  _globals['_EMBEDDINGSRESPONSE']._serialized_end=109
  _globals['_EMBEDDINGS']._serialized_start=111
  _globals['_EMBEDDINGS']._serialized_end=187
# @@protoc_insertion_point(module_scope)