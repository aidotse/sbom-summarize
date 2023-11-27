""" Handles a SBOM-file and make it to an object.

Functions:
pp_sbom: Prettyprint the json (SBOM)
count_licenses: Count the different licenses used by the packages in the SBOM.
print_summarize: Print the summarize report.
"""
from pathlib import Path
import json
from collections import Counter


class Sbom:

    def __init__(self, sbom_path: str) -> None:
        """
        Instantiate the SBOM-file as an object.
        Prints a warning if the SBOM-file does not start with the key 'SPDXID'.

        Args:
            sbom_path (str): Path to the SBOM-file.
        """        
        self.sbom_path = Path(sbom_path)
        self.sbom = json.load(self.sbom_path.open())
        if list(self.sbom.keys())[0] != 'SPDXID':
            print('---\nIs this a valid SBOM?')
        self.licenses = []
        self.no_licensed_packages = []
        self.licenses_counter = []
        self.count_licenses()

    def pp_sbom(self) -> None:
        """ Prettyprint the json-file.
        """        
        print(json. dumps(self.sbom, indent=4))

    def count_licenses(self) -> None:
        """
        Extract all licenses stated in the SBOM-file and count them.
        Also counts packages that has no license defined.
        """        
        for package in self.sbom['packages']:
            if package['SPDXID'] not in self.sbom['documentDescribes']:
                if('licenseConcluded' in package):
                    self.licenses.append(package['licenseConcluded'])
                else:
                    self.no_licensed_packages.append(package['name'])

        self.licenses_counter = Counter(self.licenses)

    def print_summarize(self) -> None:
        """ Prints a summarization of the licenses used in the SBOM-file.
        """        
        print('---\nSummarize\nSBOM-file: ', self.sbom_path.name,'\n')

        if len(self.licenses_counter) > 0: 
            print('License count:')
            for license_type in self.licenses_counter:
                print(license_type,':',self.licenses_counter[license_type])
        else:
            print('No packages with licenses found.')
        print('\n')

        if len(self.no_licensed_packages) > 0:
            print('Packages without licenses:')
            for no_lic_pack in self.no_licensed_packages:
                print(no_lic_pack)
        else:
            print('No packages without license found.')

        print('---')

