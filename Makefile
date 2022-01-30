
inputs = 1_warmup_and_setup.ipynb \
	2_structured_data_tree_cadastre_konstanz.ipynb \
	3_twitter_api.ipynb \
	4_web_scraping.ipynb \
	5_nlp_ml.ipynb

python-workshop-2022-handout.pdf: $(input)
	$(foreach inp,$(inputs),jupyter nbconvert $(inp) --to latex --template report --output tmp/$(addsuffix .tex,$(basename $(inp)));)
	perl -i -lne 'print if (m@^\s*\\tableofcontents\s*$$@ .. m@^\s*\\end\{document\}@) && !m@^\s*\\(?:tableofcontents|end\{document\})\s*$$@' tmp/*.tex
	xelatex python-workshop-2022-handout.tex
	xelatex python-workshop-2022-handout.tex
	xelatex python-workshop-2022-handout.tex

# make serve-slides NOTEBOOK=file.ipynb
serve-slides:
	jupyter nbconvert $(NOTEBOOK) --to slides --post serve

serve:
	jupyter notebook --ip='*' --NotebookApp.token='' --NotebookApp.password='' --no-browser
