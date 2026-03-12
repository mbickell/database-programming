def get_property_code(filename):
  start_of_code_index = filename.index("/0") + 1
  end_of_code_index = filename.rindex('.')
  return filename[start_of_code_index:end_of_code_index]