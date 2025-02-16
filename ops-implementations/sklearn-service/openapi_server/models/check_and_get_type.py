# coding: utf-8



def check_and_get_type(parameter_name,*_accepted_types):
   accepted_types=tuple(_accepted_types)
   def _check_and_get_type(value):
      if not isinstance(value,accepted_types):
         raise Error(f"expecting one of {accepted_types} not {type(value)} for attribute {parameter_name}")
      return value.__class__
   return _check_and_get_type