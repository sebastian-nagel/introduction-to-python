
inputs = 1_warmup_and_setup.ipynb \
	2_structured_data_tree_cadastre_konstanz.ipynb \
	3_twitter_api.ipynb

python-workshop-2021-handout.pdf: $(input)
	$(foreach inp,$(inputs),jupyter nbconvert $(inp) --to latex --template report --output tmp/$(addsuffix .tex,$(basename $(inp)));)
	perl -i -lne 'print if (m@^\s*\\tableofcontents\s*$$@ .. m@^\s*\\end\{document\}@) && !m@^\s*\\(?:tableofcontents|end\{document\})\s*$$@' tmp/*.tex
	xelatex python-workshop-2021-handout.tex
	xelatex python-workshop-2021-handout.tex
	xelatex python-workshop-2021-handout.tex

# make serve-slides NOTEBOOK=file.ipynb
serve-slides:
	jupyter nbconvert $(NOTEBOOK) --to slides --post serve

