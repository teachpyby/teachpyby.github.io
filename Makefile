gen_static:
	python3 scripts/gen_static.py \
		--dir 000-basics  \
		--dir 100-pygame  \
		--lesson_template template/lesson.html

serve:
	scripts/run.sh

.PHONY: gen_static serve