class BugReport:
    """Class representing each bug report"""
    __slots__ = ['bug_id', 'summary', 'description', 'fixed_files', 'report_time', 'pos_tagged_summary', 'pos_tagged_description','stack_traces','stack_traces_remove']

    def __init__(self, bug_id, summary, description, fixed_files, report_time):
        self.bug_id = bug_id
        self.summary = summary
        self.description = description
        self.fixed_files = fixed_files
        self.report_time = report_time
        self.pos_tagged_summary = None
        self.pos_tagged_description = None
        self.stack_traces = None
        self.stack_traces_remove = None

    def __repr__(self):
        return (f"{self.summary}\"n"
                f"{self.description}\n"
                f"{self.fixed_files}\n"
                f"{self.report_time}\n"
                f"{self.pos_tagged_summary}\n"
                f"{self.pos_tagged_description}\n"
                f"{self.stack_traces}\n"
                f"{self.stack_traces_remove}")

