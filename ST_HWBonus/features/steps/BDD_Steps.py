# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# from main import generate_blocks
#
# from behave import given, when, then
#
#
# @given('characteristics are "{char_blocks}"')
# def set_characteristics(context, char_blocks):
#     char_block_pairs = char_blocks.split('-')
#     characteristics_dict = {}
#     for pair in char_block_pairs:
#         char, blocks = pair.split('=')
#         characteristics_dict[char.strip()] = blocks.strip().split(',')
#     context.characteristics_dict = characteristics_dict
#
#
# @when('the mode is "{mode}"')
# def set_mode(context, mode):
#     context.mode = mode
#
#
# @when('base choices are "{base_choices}"')
# def set_base_choices(context, base_choices):
#     if base_choices == "None":
#         context.base_choices = None
#     else:
#         base_choices_pairs = base_choices.split(',')
#         context.base_choices = {}
#         for pair in base_choices_pairs:
#             char, choices = pair.split('=')
#             context.base_choices[char.strip()] = choices.strip().split(',')
#
#
# @then('generated blocks should be:')
# def check_generated_blocks(context):
#     expected_blocks = [tuple(row.cells) for row in context.table]
#     generated_blocks = generate_blocks(context.characteristics_dict, context.mode, context.base_choices)
#     assert generated_blocks == expected_blocks, f"Expected blocks: {expected_blocks}, Generated blocks: {generated_blocks}"

# features/steps/BDD_Steps.py

# import sys
# import os
#
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# from main import generate_blocks
#
# from behave import given, when, then
#
#
# @given('characteristics are "{char_blocks}"')
# def step_set_characteristics(context, char_blocks):
#     char_block_pairs = char_blocks.split('-')
#     characteristics_dict = {}
#     for pair in char_block_pairs:
#         char, blocks = pair.split('=')
#         characteristics_dict[char.strip()] = blocks.strip()[1:-1].split(',')
#     context.characteristics_dict = characteristics_dict
#
#
# @when('the mode is "{mode}"')
# def step_set_mode(context, mode):
#     context.mode = mode
#
#
# @when('base choices are "{base_choices}"')
# def step_set_base_choices(context, base_choices):
#     if base_choices == "None":
#         context.base_choices = None
#     else:
#         base_choices_pairs = base_choices.split(',')
#         context.base_choices = {}
#         for pair in base_choices_pairs:
#             char, choices = pair.split('=')
#             context.base_choices[char.strip()] = choices.strip().split(',')
#     if context.base_choices:
#         print("Base choices set to:", context.base_choices)
#
#
# @when('no base choices are provided')
# def step_no_base_choices(context):
#     context.base_choices = None
#
#
# @then('generated blocks should be:')
# def step_check_generated_blocks(context):
#     expected_blocks = [tuple(row.cells) for row in context.table]
#     generated_blocks = generate_blocks(context.characteristics_dict, context.mode, context.base_choices)
#     assert generated_blocks == expected_blocks, f"Expected blocks: {expected_blocks}, Generated blocks: {generated_blocks}"
#
#
#
# import sys
# import os
#
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# from main import generate_blocks
#
# from behave import given, when, then
#
#
# @given('characteristics are "{char_blocks}"')
# def step_set_characteristics(context, char_blocks):
#     char_block_pairs = char_blocks.split('-')
#     characteristics_dict = {}
#     for pair in char_block_pairs:
#         char, blocks = pair.split('=')
#         characteristics_dict[char.strip()] = blocks.strip()[1:-1].split(',')
#     context.characteristics_dict = characteristics_dict
#
#
# @when('the mode is "{mode}"')
# def step_set_mode(context, mode):
#     context.mode = mode
#
#
# @when('base choices are "{base_choices}"')
# def step_set_base_choices(context, base_choices):
#     if base_choices == "None":
#         context.base_choices = None
#     else:
#         base_choices_pairs = base_choices.split(',')
#         context.base_choices = {}
#         for pair in base_choices_pairs:
#             char, choices = pair.split('=')
#             context.base_choices[char.strip()] = choices.strip().split(',')
#     if context.base_choices:
#         print("Base choices set to:", context.base_choices)
#
#
# @when('no base choices are provided')
# def step_no_base_choices(context):
#     context.base_choices = None
#
#
# @then('generated blocks should be:')
# def step_check_generated_blocks(context):
#     expected_blocks = [tuple(row.cells) for row in context.table]
#     generated_blocks = generate_blocks(context.characteristics_dict, context.mode, context.base_choices)
#     assert generated_blocks == expected_blocks, f"Expected blocks: {expected_blocks}, Generated blocks: {generated_blocks}"
#
#
# @then('an error message should be displayed')
# def step_check_error_message(context):
#     # Implement this step if needed
#     pass

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from behave import given, then
from main import generate_blocks


@given('characteristics are "{char_blocks}"')
def set_characteristics(context, char_blocks):
    char_block_pairs = char_blocks.split('-')
    characteristics_dict = {}
    for pair in char_block_pairs:
        char, blocks = pair.split('=')
        characteristics_dict[char.strip()] = blocks.strip()[1:-1].split(',')
    context.characteristics_dict = characteristics_dict


@given('the mode is "{mode}"')
def set_mode(context, mode):
    context.mode = mode


@then('generated blocks should be')
def check_generated_blocks(context):
    expected_blocks = [tuple(row.cells) for row in context.table]
    for row in context.table:
        print(tuple(row.cells))
    generated_blocks = generate_blocks(context.characteristics_dict, context.mode, None)
    assert generated_blocks == expected_blocks, f"Expected blocks: {expected_blocks}, Generated blocks: {generated_blocks} "
