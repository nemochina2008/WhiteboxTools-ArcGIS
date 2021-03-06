import whitebox
import ast
import json
import os
import sys

wbt = whitebox.WhiteboxTools()
# wbt.set_verbose_mode(True)
# print(wbt.version())
# print(wbt.help())


# tools = wbt.list_tools(['dem'])


# for index, tool in enumerate(tools):
#     print("{}. {}: {}".format(index, tool, tools[tool]))

# def get_tool_params(tool_name):

#     out_str = wbt.tool_parameters(tool_name)
#     start_index = out_str.index('[') + 1
#     end_index = len(out_str.strip()) - 2
#     params = out_str[start_index : end_index]
#     print(params)

#     sub_params = params.split('{"name"')
#     param_list = []

#     for param in sub_params:
#         param = param.strip()
#         if len(param) > 0:
#             item = '"name"' + param
#             item = item[ : item.rfind("}")].strip()
#             param_list.append(item)

#     params_dict = {}
#     for item in param_list:
#         print("{}\n".format(item))
#         param_dict = {}
#         index_name = item.find("name")
#         index_flags = item.find("flags")
#         index_description = item.find("description")
#         index_parameter_type = item.find("parameter_type")
#         index_default_value = item.find("default_value")
#         index_optional = item.find("optional")

#         name = item[index_name - 1 : index_flags - 2].replace('"name":', '')
#         name = name.replace('"', '')
#         param_dict['name'] = name

#         flags = item[index_flags - 1 : index_description -2].replace('"flags":', '')
#         if "--" in flags:
#             flags = flags.split('--')[1][: -2]
#         else:
#             flags = flags.split('-')[1][: -2]
#         param_dict['flags'] = flags

#         desc = item[index_description - 1 : index_parameter_type - 2].replace('"description":', '')
#         desc = desc.replace('"', '')
#         param_dict['description'] = desc

#         param_type = item[index_parameter_type - 1 : index_default_value - 2].replace('"parameter_type":', '')
#         param_type = ast.literal_eval(param_type)
#         param_dict['parameter_type'] = param_type

#         default_value = item[index_default_value - 1 : index_optional - 2].replace('"default_value":', '')
#         param_dict['default_value'] = default_value

#         optional = item[index_optional - 1 :].replace('"optional":', '')
#         param_dict['optional'] = optional

#         params_dict[flags] = param_dict

#     return params_dict

# tool_name = "BreachDepressions"
# print(wbt.tool_parameters(tool_name))


# params = get_tool_params(tool_name)
# print(params)
# print(params.keys())

# print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# lines = wbt.list_tools()
# print(lines)

# # for line in lines:
# #     print(line)

# print(len(lines))

# parameter_types = []

# for param in params:

#     param_type = params[param]['parameter_type']
#     if param_type not in parameter_types:
#         parameter_types.append(param_type)


# print(parameter_types)

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# tools = wbt.list_tools()
# for index, tool in enumerate(sorted(tools)):
#     print("{}: {}".format(index, tool))

# dem = "/media/hdd/Dropbox/git/WhiteboxTools-ArcGIS/testdata/DEM.tif"
# output = "/media/hdd/Dropbox/git/WhiteboxTools-ArcGIS/testdata/output.tif"

# wbt.run_tool("BreachDepressions", '--dem=dem --output=output')

# exe_path = "/home/qiusheng/Downloads/WBT/whitebox_tools"

# cmd = exe_path + ' --run=BreachDepressions  --dem="/media/hdd/Dropbox/git/WhiteboxTools-ArcGIS/testdata/DEM.tif" --output="/media/hdd/Dropbox/git/WhiteboxTools-ArcGIS/testdata/output.tif" -v'
# print(os.popen(cmd).read().rstrip())

# ret = wbt.breach_depressions(dem, output)
# print(ret)
# print(type(ret))

# def redirect_to_file(text):
#     original = sys.stdout
#     sys.stdout = open('/media/hdd/Dropbox/git/WhiteboxTools-ArcGIS/WBT/PRE/redirect.txt', 'w')
#     # print('This is your redirected text:')
#     # print(text)
#     wbt.breach_depressions(dem, output)
#     sys.stdout = original
 
#     print('This string goes to stdout, NOT the file!')

# redirect_to_file('Python rocks!')

# https://goo.gl/bFo2tD

# import sys
# if sys.version_info < (3, 0): 
#     from StringIO import StringIO
# else:
#     from io import StringIO
# old_stdout = sys.stdout
# result = StringIO()
# sys.stdout = result
# # wbt.breach_depressions(dem, output)
# # print("test string")
# sys.stdout = old_stdout
# result_string = result.getvalue()
# print(result_string)

# print('--dem="/path/to/DEM.tif"  --output="/path/to/output.tif"')