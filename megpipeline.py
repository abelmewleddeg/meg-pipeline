"""
megpipeline - Python base package for MEG data post-processing.
"""

__version__ = "0.1.0"


class MEGPipeline(Exception):
    """Primary class for MEG pipeline."""
    pass

#Example of method docstring

# def template_function(kind=None):
#     """
#     Return a list of random ingredients as strings.
#
#     :param kind: Optional "kind" of ingredients.
#     :type kind: list[str] or None
#     :raise megpipeline.InvalidKindError: If the kind is invalid.
#     :return: The ingredients list.
#     :rtype: list[str]
#     """
#     return ["shells", "gorgonzola", "parsley"]

    def get_raw_data(self, file_name):
        """
        Return a list of random as strings.

        :param kind: Optional "kind" .
        :type kind: list[str] or None
        :return: the converted data list.
        :rtype: list[str]
        """
        return None

if __name__ == "__main__":

    pipeline = MEGPipeline()

    pipeline.get_raw_data('MEG_DATA/')

    print("test")
