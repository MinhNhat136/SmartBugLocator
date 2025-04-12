class SourceFile:
    """Class representing each source file"""
    __slots__ = ['all_content', 'comments', 'class_names', 'attributes', 'method_names', 'variables', 'file_name',
                 'pos_tagged_comments', 'exact_file_name', 'package_name', 'total_lines', 'directory']

    def __init__(self, all_content, comments, class_names, attributes, method_names, variables, file_name,
                 package_name, total_lines, directory):
        self.all_content = all_content
        self.comments = comments
        self.class_names = class_names
        self.attributes = attributes
        self.method_names = method_names
        self.variables = variables
        self.file_name = file_name
        self.exact_file_name = file_name[0]
        self.package_name = package_name
        self.pos_tagged_comments = None
        self.total_lines = total_lines
        self.directory = directory

    def __repr__(self):
        return (f"{self.all_content}\n"
                f"{self.comments}\n"
                f"{self.class_names}\n"
                f"{self.attributes}\n"
                f"{self.method_names}\n"
                f"{self.variables}\n"
                f"{self.file_name}\n"
                f"{self.package_name}\n"
                f"{self.pos_tagged_comments}")