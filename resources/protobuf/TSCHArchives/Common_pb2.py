# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TSCHArchives.Common.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import TSPMessages_pb2
import TSKArchives_pb2
import TSDArchives_pb2
import TSSArchives_pb2
import TSCH3DArchives_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TSCHArchives.Common.proto',
  package='TSCH',
  serialized_pb='\n\x19TSCHArchives.Common.proto\x12\x04TSCH\x1a\x11TSPMessages.proto\x1a\x11TSKArchives.proto\x1a\x11TSDArchives.proto\x1a\x11TSSArchives.proto\x1a\x14TSCH3DArchives.proto\"\xa3\x01\n\x1bSparseReferenceArrayArchive\x12\x13\n\x0bnum_entries\x18\x01 \x02(\r\x12\x38\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\'.TSCH.SparseReferenceArrayArchive.Entry\x1a\x35\n\x05\x45ntry\x12\r\n\x05index\x18\x01 \x02(\r\x12\x1d\n\x05value\x18\x02 \x02(\x0b\x32\x0e.TSP.Reference\"B\n\x0bRectArchive\x12\x1a\n\x06origin\x18\x01 \x02(\x0b\x32\n.TSP.Point\x12\x17\n\x04size\x18\x02 \x02(\x0b\x32\t.TSP.Size\"5\n\x1b\x43hartsNSNumberDoubleArchive\x12\x16\n\x0enumber_archive\x18\x01 \x01(\x01\"7\n$ChartsNSArrayOfNSNumberDoubleArchive\x12\x0f\n\x07numbers\x18\x01 \x03(\x01\"\xd0\x01\n\x1c\x44\x45PRECATEDChart3DFillArchive\x12\x1e\n\x04\x66ill\x18\x01 \x01(\x0b\x32\x10.TSD.FillArchive\x12\x38\n\rlightingmodel\x18\x02 \x01(\x0b\x32!.TSCH.Chart3DLightingModelArchive\x12\x15\n\rtextureset_id\x18\x03 \x01(\t\x12)\n\tfill_type\x18\x04 \x01(\x0e\x32\x16.TSCH.FillPropertyType\x12\x14\n\x0cseries_index\x18\x05 \x01(\r\"@\n\x11\x43hartStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"C\n\x14\x43hartNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"A\n\x12LegendStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"D\n\x15LegendNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"D\n\x15\x43hartAxisStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"G\n\x18\x43hartAxisNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"F\n\x17\x43hartSeriesStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"I\n\x1a\x43hartSeriesNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02*\xfa\x04\n\tChartType\x12\x16\n\x12undefinedChartType\x10\x00\x12\x15\n\x11\x63olumnChartType2D\x10\x01\x12\x12\n\x0e\x62\x61rChartType2D\x10\x02\x12\x13\n\x0flineChartType2D\x10\x03\x12\x13\n\x0f\x61reaChartType2D\x10\x04\x12\x12\n\x0epieChartType2D\x10\x05\x12\x1c\n\x18stackedColumnChartType2D\x10\x06\x12\x19\n\x15stackedBarChartType2D\x10\x07\x12\x1a\n\x16stackedAreaChartType2D\x10\x08\x12\x16\n\x12scatterChartType2D\x10\t\x12\x14\n\x10mixedChartType2D\x10\n\x12\x16\n\x12twoAxisChartType2D\x10\x0b\x12\x15\n\x11\x63olumnChartType3D\x10\x0c\x12\x12\n\x0e\x62\x61rChartType3D\x10\r\x12\x13\n\x0flineChartType3D\x10\x0e\x12\x13\n\x0f\x61reaChartType3D\x10\x0f\x12\x12\n\x0epieChartType3D\x10\x10\x12\x1c\n\x18stackedColumnChartType3D\x10\x11\x12\x19\n\x15stackedBarChartType3D\x10\x12\x12\x1a\n\x16stackedAreaChartType3D\x10\x13\x12\x1e\n\x1amultiDataColumnChartType2D\x10\x14\x12\x1b\n\x17multiDataBarChartType2D\x10\x15\x12\x15\n\x11\x62ubbleChartType2D\x10\x16\x12\x1f\n\x1bmultiDataScatterChartType2D\x10\x17\x12\x1e\n\x1amultiDataBubbleChartType2D\x10\x18*j\n\x08\x41xisType\x12\x15\n\x11\x61xis_type_unknown\x10\x00\x12\x0f\n\x0b\x61xis_type_x\x10\x01\x12\x0f\n\x0b\x61xis_type_y\x10\x02\x12\x11\n\raxis_type_pie\x10\x03\x12\x12\n\x0e\x61xis_type_size\x10\x04*g\n\rScatterFormat\x12\x1a\n\x16scatter_format_unknown\x10\x00\x12\x1d\n\x19scatter_format_separate_x\x10\x01\x12\x1b\n\x17scatter_format_shared_x\x10\x02*l\n\x0fSeriesDirection\x12\x1c\n\x18series_direction_unknown\x10\x00\x12\x1b\n\x17series_direction_by_row\x10\x01\x12\x1e\n\x1aseries_direction_by_column\x10\x02*\xe3\x01\n\x0fNumberValueType\x12\x1a\n\x16numberValueTypeDecimal\x10\x00\x12\x1b\n\x17numberValueTypeCurrency\x10\x01\x12\x1d\n\x19numberValueTypePercentage\x10\x02\x12\x1d\n\x19numberValueTypeScientific\x10\x03\x12\x1b\n\x17numberValueTypeFraction\x10\x04\x12\x17\n\x13numberValueTypeBase\x10\x05\x12#\n\x16numberValueTypeUnknown\x10\x99\xf8\xff\xff\xff\xff\xff\xff\xff\x01*\xba\x01\n\x13NegativeNumberStyle\x12\x1c\n\x18negativeNumberStyleMinus\x10\x00\x12\x1a\n\x16negativeNumberStyleRed\x10\x01\x12\"\n\x1enegativeNumberStyleParentheses\x10\x02\x12(\n$negativeNumberStyleRedAndParentheses\x10\x03\x12\x1b\n\x17negativeNumberStyleNone\x10\x04*\xeb\x02\n\x10\x46ractionAccuracy\x12\x1f\n\x1b\x66ractionAccuracyConflicting\x10\x00\x12)\n\x1c\x66ractionAccuracyUpToOneDigit\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12*\n\x1d\x66ractionAccuracyUpToTwoDigits\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12,\n\x1f\x66ractionAccuracyUpToThreeDigits\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1a\n\x16\x66ractionAccuracyHalves\x10\x02\x12\x1c\n\x18\x66ractionAccuracyQuarters\x10\x04\x12\x1b\n\x17\x66ractionAccuracyEighths\x10\x08\x12\x1e\n\x1a\x66ractionAccuracySixteenths\x10\x10\x12\x1a\n\x16\x66ractionAccuracyTenths\x10\n\x12\x1e\n\x1a\x66ractionAccuracyHundredths\x10\x64')

_CHARTTYPE = _descriptor.EnumDescriptor(
  name='ChartType',
  full_name='TSCH.ChartType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='undefinedChartType', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='columnChartType2D', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='barChartType2D', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='lineChartType2D', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='areaChartType2D', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='pieChartType2D', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stackedColumnChartType2D', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stackedBarChartType2D', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stackedAreaChartType2D', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='scatterChartType2D', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='mixedChartType2D', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='twoAxisChartType2D', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='columnChartType3D', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='barChartType3D', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='lineChartType3D', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='areaChartType3D', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='pieChartType3D', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stackedColumnChartType3D', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stackedBarChartType3D', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stackedAreaChartType3D', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='multiDataColumnChartType2D', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='multiDataBarChartType2D', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='bubbleChartType2D', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='multiDataScatterChartType2D', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='multiDataBubbleChartType2D', index=24, number=24,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1253,
  serialized_end=1887,
)

ChartType = enum_type_wrapper.EnumTypeWrapper(_CHARTTYPE)
_AXISTYPE = _descriptor.EnumDescriptor(
  name='AxisType',
  full_name='TSCH.AxisType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='axis_type_unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='axis_type_x', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='axis_type_y', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='axis_type_pie', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='axis_type_size', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1889,
  serialized_end=1995,
)

AxisType = enum_type_wrapper.EnumTypeWrapper(_AXISTYPE)
_SCATTERFORMAT = _descriptor.EnumDescriptor(
  name='ScatterFormat',
  full_name='TSCH.ScatterFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='scatter_format_unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='scatter_format_separate_x', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='scatter_format_shared_x', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1997,
  serialized_end=2100,
)

ScatterFormat = enum_type_wrapper.EnumTypeWrapper(_SCATTERFORMAT)
_SERIESDIRECTION = _descriptor.EnumDescriptor(
  name='SeriesDirection',
  full_name='TSCH.SeriesDirection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='series_direction_unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='series_direction_by_row', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='series_direction_by_column', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2102,
  serialized_end=2210,
)

SeriesDirection = enum_type_wrapper.EnumTypeWrapper(_SERIESDIRECTION)
_NUMBERVALUETYPE = _descriptor.EnumDescriptor(
  name='NumberValueType',
  full_name='TSCH.NumberValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='numberValueTypeDecimal', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='numberValueTypeCurrency', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='numberValueTypePercentage', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='numberValueTypeScientific', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='numberValueTypeFraction', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='numberValueTypeBase', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='numberValueTypeUnknown', index=6, number=-999,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2213,
  serialized_end=2440,
)

NumberValueType = enum_type_wrapper.EnumTypeWrapper(_NUMBERVALUETYPE)
_NEGATIVENUMBERSTYLE = _descriptor.EnumDescriptor(
  name='NegativeNumberStyle',
  full_name='TSCH.NegativeNumberStyle',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='negativeNumberStyleMinus', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='negativeNumberStyleRed', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='negativeNumberStyleParentheses', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='negativeNumberStyleRedAndParentheses', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='negativeNumberStyleNone', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2443,
  serialized_end=2629,
)

NegativeNumberStyle = enum_type_wrapper.EnumTypeWrapper(_NEGATIVENUMBERSTYLE)
_FRACTIONACCURACY = _descriptor.EnumDescriptor(
  name='FractionAccuracy',
  full_name='TSCH.FractionAccuracy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyConflicting', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyUpToOneDigit', index=1, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyUpToTwoDigits', index=2, number=-2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyUpToThreeDigits', index=3, number=-3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyHalves', index=4, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyQuarters', index=5, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyEighths', index=6, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracySixteenths', index=7, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyTenths', index=8, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fractionAccuracyHundredths', index=9, number=100,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2632,
  serialized_end=2995,
)

FractionAccuracy = enum_type_wrapper.EnumTypeWrapper(_FRACTIONACCURACY)
undefinedChartType = 0
columnChartType2D = 1
barChartType2D = 2
lineChartType2D = 3
areaChartType2D = 4
pieChartType2D = 5
stackedColumnChartType2D = 6
stackedBarChartType2D = 7
stackedAreaChartType2D = 8
scatterChartType2D = 9
mixedChartType2D = 10
twoAxisChartType2D = 11
columnChartType3D = 12
barChartType3D = 13
lineChartType3D = 14
areaChartType3D = 15
pieChartType3D = 16
stackedColumnChartType3D = 17
stackedBarChartType3D = 18
stackedAreaChartType3D = 19
multiDataColumnChartType2D = 20
multiDataBarChartType2D = 21
bubbleChartType2D = 22
multiDataScatterChartType2D = 23
multiDataBubbleChartType2D = 24
axis_type_unknown = 0
axis_type_x = 1
axis_type_y = 2
axis_type_pie = 3
axis_type_size = 4
scatter_format_unknown = 0
scatter_format_separate_x = 1
scatter_format_shared_x = 2
series_direction_unknown = 0
series_direction_by_row = 1
series_direction_by_column = 2
numberValueTypeDecimal = 0
numberValueTypeCurrency = 1
numberValueTypePercentage = 2
numberValueTypeScientific = 3
numberValueTypeFraction = 4
numberValueTypeBase = 5
numberValueTypeUnknown = -999
negativeNumberStyleMinus = 0
negativeNumberStyleRed = 1
negativeNumberStyleParentheses = 2
negativeNumberStyleRedAndParentheses = 3
negativeNumberStyleNone = 4
fractionAccuracyConflicting = 0
fractionAccuracyUpToOneDigit = -1
fractionAccuracyUpToTwoDigits = -2
fractionAccuracyUpToThreeDigits = -3
fractionAccuracyHalves = 2
fractionAccuracyQuarters = 4
fractionAccuracyEighths = 8
fractionAccuracySixteenths = 16
fractionAccuracyTenths = 10
fractionAccuracyHundredths = 100



_SPARSEREFERENCEARRAYARCHIVE_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='TSCH.SparseReferenceArrayArchive.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='TSCH.SparseReferenceArrayArchive.Entry.index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='TSCH.SparseReferenceArrayArchive.Entry.value', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=244,
  serialized_end=297,
)

_SPARSEREFERENCEARRAYARCHIVE = _descriptor.Descriptor(
  name='SparseReferenceArrayArchive',
  full_name='TSCH.SparseReferenceArrayArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_entries', full_name='TSCH.SparseReferenceArrayArchive.num_entries', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entries', full_name='TSCH.SparseReferenceArrayArchive.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SPARSEREFERENCEARRAYARCHIVE_ENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=134,
  serialized_end=297,
)


_RECTARCHIVE = _descriptor.Descriptor(
  name='RectArchive',
  full_name='TSCH.RectArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='TSCH.RectArchive.origin', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='TSCH.RectArchive.size', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=299,
  serialized_end=365,
)


_CHARTSNSNUMBERDOUBLEARCHIVE = _descriptor.Descriptor(
  name='ChartsNSNumberDoubleArchive',
  full_name='TSCH.ChartsNSNumberDoubleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_archive', full_name='TSCH.ChartsNSNumberDoubleArchive.number_archive', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=367,
  serialized_end=420,
)


_CHARTSNSARRAYOFNSNUMBERDOUBLEARCHIVE = _descriptor.Descriptor(
  name='ChartsNSArrayOfNSNumberDoubleArchive',
  full_name='TSCH.ChartsNSArrayOfNSNumberDoubleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numbers', full_name='TSCH.ChartsNSArrayOfNSNumberDoubleArchive.numbers', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=422,
  serialized_end=477,
)


_DEPRECATEDCHART3DFILLARCHIVE = _descriptor.Descriptor(
  name='DEPRECATEDChart3DFillArchive',
  full_name='TSCH.DEPRECATEDChart3DFillArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fill', full_name='TSCH.DEPRECATEDChart3DFillArchive.fill', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lightingmodel', full_name='TSCH.DEPRECATEDChart3DFillArchive.lightingmodel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='textureset_id', full_name='TSCH.DEPRECATEDChart3DFillArchive.textureset_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fill_type', full_name='TSCH.DEPRECATEDChart3DFillArchive.fill_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='series_index', full_name='TSCH.DEPRECATEDChart3DFillArchive.series_index', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=480,
  serialized_end=688,
)


_CHARTSTYLEARCHIVE = _descriptor.Descriptor(
  name='ChartStyleArchive',
  full_name='TSCH.ChartStyleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSCH.ChartStyleArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=690,
  serialized_end=754,
)


_CHARTNONSTYLEARCHIVE = _descriptor.Descriptor(
  name='ChartNonStyleArchive',
  full_name='TSCH.ChartNonStyleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSCH.ChartNonStyleArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=756,
  serialized_end=823,
)


_LEGENDSTYLEARCHIVE = _descriptor.Descriptor(
  name='LegendStyleArchive',
  full_name='TSCH.LegendStyleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSCH.LegendStyleArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=825,
  serialized_end=890,
)


_LEGENDNONSTYLEARCHIVE = _descriptor.Descriptor(
  name='LegendNonStyleArchive',
  full_name='TSCH.LegendNonStyleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSCH.LegendNonStyleArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=892,
  serialized_end=960,
)


_CHARTAXISSTYLEARCHIVE = _descriptor.Descriptor(
  name='ChartAxisStyleArchive',
  full_name='TSCH.ChartAxisStyleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSCH.ChartAxisStyleArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=962,
  serialized_end=1030,
)


_CHARTAXISNONSTYLEARCHIVE = _descriptor.Descriptor(
  name='ChartAxisNonStyleArchive',
  full_name='TSCH.ChartAxisNonStyleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSCH.ChartAxisNonStyleArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=1032,
  serialized_end=1103,
)


_CHARTSERIESSTYLEARCHIVE = _descriptor.Descriptor(
  name='ChartSeriesStyleArchive',
  full_name='TSCH.ChartSeriesStyleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSCH.ChartSeriesStyleArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=1105,
  serialized_end=1175,
)


_CHARTSERIESNONSTYLEARCHIVE = _descriptor.Descriptor(
  name='ChartSeriesNonStyleArchive',
  full_name='TSCH.ChartSeriesNonStyleArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSCH.ChartSeriesNonStyleArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=1177,
  serialized_end=1250,
)

_SPARSEREFERENCEARRAYARCHIVE_ENTRY.fields_by_name['value'].message_type = TSPMessages_pb2._REFERENCE
_SPARSEREFERENCEARRAYARCHIVE_ENTRY.containing_type = _SPARSEREFERENCEARRAYARCHIVE;
_SPARSEREFERENCEARRAYARCHIVE.fields_by_name['entries'].message_type = _SPARSEREFERENCEARRAYARCHIVE_ENTRY
_RECTARCHIVE.fields_by_name['origin'].message_type = TSPMessages_pb2._POINT
_RECTARCHIVE.fields_by_name['size'].message_type = TSPMessages_pb2._SIZE
_DEPRECATEDCHART3DFILLARCHIVE.fields_by_name['fill'].message_type = TSDArchives_pb2._FILLARCHIVE
_DEPRECATEDCHART3DFILLARCHIVE.fields_by_name['lightingmodel'].message_type = TSCH3DArchives_pb2._CHART3DLIGHTINGMODELARCHIVE
_DEPRECATEDCHART3DFILLARCHIVE.fields_by_name['fill_type'].enum_type = TSCH3DArchives_pb2._FILLPROPERTYTYPE
_CHARTSTYLEARCHIVE.fields_by_name['super'].message_type = TSSArchives_pb2._STYLEARCHIVE
_CHARTNONSTYLEARCHIVE.fields_by_name['super'].message_type = TSSArchives_pb2._STYLEARCHIVE
_LEGENDSTYLEARCHIVE.fields_by_name['super'].message_type = TSSArchives_pb2._STYLEARCHIVE
_LEGENDNONSTYLEARCHIVE.fields_by_name['super'].message_type = TSSArchives_pb2._STYLEARCHIVE
_CHARTAXISSTYLEARCHIVE.fields_by_name['super'].message_type = TSSArchives_pb2._STYLEARCHIVE
_CHARTAXISNONSTYLEARCHIVE.fields_by_name['super'].message_type = TSSArchives_pb2._STYLEARCHIVE
_CHARTSERIESSTYLEARCHIVE.fields_by_name['super'].message_type = TSSArchives_pb2._STYLEARCHIVE
_CHARTSERIESNONSTYLEARCHIVE.fields_by_name['super'].message_type = TSSArchives_pb2._STYLEARCHIVE
DESCRIPTOR.message_types_by_name['SparseReferenceArrayArchive'] = _SPARSEREFERENCEARRAYARCHIVE
DESCRIPTOR.message_types_by_name['RectArchive'] = _RECTARCHIVE
DESCRIPTOR.message_types_by_name['ChartsNSNumberDoubleArchive'] = _CHARTSNSNUMBERDOUBLEARCHIVE
DESCRIPTOR.message_types_by_name['ChartsNSArrayOfNSNumberDoubleArchive'] = _CHARTSNSARRAYOFNSNUMBERDOUBLEARCHIVE
DESCRIPTOR.message_types_by_name['DEPRECATEDChart3DFillArchive'] = _DEPRECATEDCHART3DFILLARCHIVE
DESCRIPTOR.message_types_by_name['ChartStyleArchive'] = _CHARTSTYLEARCHIVE
DESCRIPTOR.message_types_by_name['ChartNonStyleArchive'] = _CHARTNONSTYLEARCHIVE
DESCRIPTOR.message_types_by_name['LegendStyleArchive'] = _LEGENDSTYLEARCHIVE
DESCRIPTOR.message_types_by_name['LegendNonStyleArchive'] = _LEGENDNONSTYLEARCHIVE
DESCRIPTOR.message_types_by_name['ChartAxisStyleArchive'] = _CHARTAXISSTYLEARCHIVE
DESCRIPTOR.message_types_by_name['ChartAxisNonStyleArchive'] = _CHARTAXISNONSTYLEARCHIVE
DESCRIPTOR.message_types_by_name['ChartSeriesStyleArchive'] = _CHARTSERIESSTYLEARCHIVE
DESCRIPTOR.message_types_by_name['ChartSeriesNonStyleArchive'] = _CHARTSERIESNONSTYLEARCHIVE

class SparseReferenceArrayArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Entry(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SPARSEREFERENCEARRAYARCHIVE_ENTRY

    # @@protoc_insertion_point(class_scope:TSCH.SparseReferenceArrayArchive.Entry)
  DESCRIPTOR = _SPARSEREFERENCEARRAYARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.SparseReferenceArrayArchive)

class RectArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECTARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.RectArchive)

class ChartsNSNumberDoubleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARTSNSNUMBERDOUBLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.ChartsNSNumberDoubleArchive)

class ChartsNSArrayOfNSNumberDoubleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARTSNSARRAYOFNSNUMBERDOUBLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.ChartsNSArrayOfNSNumberDoubleArchive)

class DEPRECATEDChart3DFillArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEPRECATEDCHART3DFILLARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.DEPRECATEDChart3DFillArchive)

class ChartStyleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARTSTYLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.ChartStyleArchive)

class ChartNonStyleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARTNONSTYLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.ChartNonStyleArchive)

class LegendStyleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEGENDSTYLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.LegendStyleArchive)

class LegendNonStyleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEGENDNONSTYLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.LegendNonStyleArchive)

class ChartAxisStyleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARTAXISSTYLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.ChartAxisStyleArchive)

class ChartAxisNonStyleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARTAXISNONSTYLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.ChartAxisNonStyleArchive)

class ChartSeriesStyleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARTSERIESSTYLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.ChartSeriesStyleArchive)

class ChartSeriesNonStyleArchive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARTSERIESNONSTYLEARCHIVE

  # @@protoc_insertion_point(class_scope:TSCH.ChartSeriesNonStyleArchive)


# @@protoc_insertion_point(module_scope)
