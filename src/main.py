""" Print out a summarize of the licenses in the selected sbom. """
import sys
import os

from sbom.sbom import Sbom

def find_sbom_path() -> str:
    """Generates a path to the sbom-file. If only one file exists, no arg is needed.

    Raises:
        FileNotFoundError: If no files are found in the folder.
        FileNotFoundError: If the only item in the folder is a folder, 
        Exception: If multiple items exist and no arg is entered.

    Returns:
        str: Path to the sbom-file.
    """      
    sbom_path_prefix = 'sbom/'
    sbom_path = ''
    folder_items = os.listdir('sbom')
    if len(folder_items) < 1:
        raise FileNotFoundError('No sbom found!')
    if len(folder_items) == 1:
        if os.path.isfile(sbom_path_prefix + folder_items[0]):
            sbom_path = sbom_path_prefix + folder_items[0]
        else:
            raise FileNotFoundError('Put the sbom-file directly under the sbom folder')
    if len(folder_items) > 1:
        if len(sys.argv) < 2:
            raise Exception('Multiple folder items found. Enter the name as an argument.')
        else:
            sbom_path = sbom_path_prefix + sys.argv[1]
    return sbom_path


def main() -> None:
    """ Main function.
    """    
    sbom_obj = Sbom(find_sbom_path())
    sbom_obj.print_count_licenses()

if __name__ == '__main__':
    main()