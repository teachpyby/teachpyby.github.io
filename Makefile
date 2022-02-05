PYTHON = pipenv run python

install:
	pipenv install

gen_static:
	${PYTHON} scripts/gen_static.py \
		--dir 000-basics  \
		--dir 000-turtle  \
		--dir 100-pygame  \
		--lesson_template template/lesson.html

gen_rating:
	${PYTHON} scripts/gen_rating.py \
		--rating rating/rating.csv \
		--template template/rating.html \
		--output rating/2021.html

gen_all: gen_static gen_rating

serve: gen_all
	scripts/run.sh

.PHONY: gen_static gen_rating serve install
