deoplete-omnisharp
==================

### Required

- Neovim
- deoplete.nvim: https://github.com/neovim/neovim/
- omnisharp-vim: https://github.com/OmniSharp/omnisharp-vim

### Installation

Instructions are for vim-plug and were only tested on Linux:

	" Installs deoplete.nvim:
	Plug 'Shougo/deoplete.nvim'
	" Installs and builds OmniSharp
	Plug 'OmniSharp/omnisharp-vim', { 'do': 'cd server && xbuild' }
	" Installs vim-dispatch (required to launch OmniSharp server)
	Plug 'tpope/vim-dispatch'
	" Installs this source
	Plug 'https://gitlab.com/mixedCase/deoplete-omnisharp.git'

Optionally you may also install syntastic and unite.vim/ctrlp.vim for extra OmniSharp functionality unrelated to this particular plugin.

### FAQ

Q: Why are completions so slow?  
A: This plugin is mostly a hack to get OmniSharp working with deoplete. While deoplete supports fast, asynchronous calls to the OmniSharp server, I would have to recreate a lot of omnisharp-vim functionality to make it work and it's not something I wish to do myself, so I just call omnisharp-vim from deoplete, producing a synchronous call that slows things down a bit.

Q: Can you add X functionality?  
A: No, sorry. I just made this (with help from Shougo) to get OmniSharp to work when I needed it, I don't even program in C#/.net unless I really have to.

Q: But can I submit pull requests?  
A: Definitely! As long as it doesn't break it for me and adds value I'll probably merge it.

Q: You don't seem very interested in maintaining this plugin, can I become a maintainer?  
A: Sure, if you make a couple PRs that add value to the plugin, just ask and I'll give you full commit rights. Or fork it, if that's more your style :).

### License

The MIT License. Full copy of the license included.
