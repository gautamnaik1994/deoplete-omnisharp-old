from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'omnisharp'
        self.mark = '[CS]'
        self.filetypes = ['cs']
        self.input_pattern = '\.'
        self.is_bytepos = True
        self.rank = 500

    def get_complete_position(self, context):
        return self.vim.call('OmniSharp#Complete', 1, 0)

    def gather_candidates(self, context):
        return self.vim.call('OmniSharp#Complete', 0, context['complete_str'])
