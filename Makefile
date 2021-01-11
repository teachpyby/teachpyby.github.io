gen_static:
	python3 scripts/gen_static.py \
		--dir 000-basics  \
		--dir 100-pygame  \
		--lesson_template template/lesson.html

gen_rating:
	python3 scripts/gen_rating.py \
		--rating rating/rating.csv \
		--template template/rating.html \
		--output rating/2021.html

serve:
	scripts/run.sh

.PHONY: gen_static serve