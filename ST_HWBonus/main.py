import itertools


def generate_blocks(characteristics_dict, mode, base_choices):
    blocks = []

    # Generate blocks based on the selected mode
    if mode == "BCC":
        if not base_choices:
            base_choices = {char: [blocks[0]] for char, blocks in characteristics_dict.items()}

        for base_test_values in itertools.product(*base_choices.values()):
            blocks.append(base_test_values)

        for char, abstract_blocks in characteristics_dict.items():
            for base_choice in base_choices[char]:
                for block in abstract_blocks:
                    if block != base_choice:
                        new_test = list(base_choice for base_choice in base_test_values)
                        index = list(characteristics_dict.keys()).index(char)
                        new_test[index] = block
                        blocks.append(tuple(new_test))

    elif mode == "ECC":
        ECC_block = []
        characteristics = list(characteristics_dict.keys())
        abstract_blocks = list(characteristics_dict.values())
        max_length = max(len(blocks) for blocks in abstract_blocks)
        for i in range(max_length):
            combination = []
            # print(abstract_blocks)
            for blocks in abstract_blocks:
                # print(blocks)
                combination.append(blocks[i % len(blocks)])
                # print(combination)
            # print(blocks)
            # blocks.append(tuple(combination))
            ECC_block.append(tuple(combination))
            # print(blocks)
            # print(ECC_block)
            blocks = ECC_block


    elif mode == "ACoC":
        # Generate blocks for ACoC mode
        char_blocks_lists = [abstract_blocks for abstract_blocks in characteristics_dict.values()]
        for combination in itertools.product(*char_blocks_lists):
            blocks.append(combination)


    elif mode == "MBCC":
        if not base_choices:
            print("Error: Base choices must be provided for MBCC.")
            return blocks
        num_base_tests = 0
        num_base_choices = {char: len(choices) for char, choices in base_choices.items()}
        for num_choices in num_base_choices.values():
            num_base_tests += num_choices
        for base_test_values in itertools.product(*base_choices.values()):
            blocks.append(base_test_values)
        for base_test_values in blocks[:num_base_tests]:
            for i, char in enumerate(characteristics_dict.keys()):
                for block in characteristics_dict[char]:
                    if block not in base_choices[char]:
                        new_test = list(base_test_value for base_test_value in base_test_values)
                        new_test[i] = block
                        blocks.append(tuple(new_test))


    return blocks


def main():
    # Prompt the user to enter characteristics and their abstract blocks
    char_blocks_input = input("Enter characteristics and their abstract blocks (e.g., A=[a1,a2]-B=[b1]): ")

    # Split the input into individual characteristic-block pairs
    char_block_pairs = char_blocks_input.split('-')

    # print(char_block_pairs)

    # Initialize a dictionary to store characteristics and their abstract blocks
    characteristics_dict = {}

    # Parse each characteristic-block pair
    for pair in char_block_pairs:
        # Split the pair into characteristic and its abstract blocks
        char_block_split = pair.split('=')
        # print(char_block_split)
        if len(char_block_split) == 2:
            char_name = char_block_split[0].strip()
            # print(char_name)
            abstract_blocks = char_block_split[1].strip().split('[')[1].split(']')[0].split(',')
            # print(abstract_blocks)
            characteristics_dict[char_name] = abstract_blocks
        else:
            print("Invalid input format.")

    # Prompt the user to enter the mode of work
    mode = input("Enter the mode of work (BCC, ECC, ACoC, MBCC): ")

    base_choices = None
    if mode in ["BCC", "MBCC"]:
        base_choices_input = input("Enter base choices (e.g., A=a1,a2, B=b1, C=c1,c2): ")
        base_choices_pairs = base_choices_input.split(',')
        # print(base_choices_pairs)
        base_choices = {}
        for pair in base_choices_pairs:
            char_block_split = pair.split('=')
            if len(char_block_split) == 2:
                char_name = char_block_split[0].strip()
                block_choices = char_block_split[1].strip().split(',')
                base_choices[char_name] = [block.strip() for block in block_choices]
            else:
                print("Invalid input format for base choices.")

    # Generate the blocks based on the characteristics, their abstract blocks, and the selected mode
    blocks = generate_blocks(characteristics_dict, mode, base_choices)

    # Display the generated blocks
    print("Generated blocks:")
    for block in blocks:
        print(block)


if __name__ == "__main__":
    main()
