now = `date +"%H:%M:%S"`
timestamp = \033[90m$(now)\033[0m

COLOR_RESET = \033[0m
COLOR_GRAY = \033[90m
COLOR_RED = \033[31m
COLOR_GREEN = \033[32m
COLOR_YELLOW = \033[33m
COLOR_BLUE = \033[34m

log = @echo "$(timestamp) $(1)|$(2)|$(3)$(COLOR_RESET)"

log_trace = $(call log,$(COLOR_GRAY),TRACE,$(1))
log_debug = $(call log,$(COLOR_BLUE),DEBUG,$(1))
log_info = $(call log,$(COLOR_GREEN),INFO,$(1))
log_warn = $(call log,$(COLOR_YELLOW),WARN,$(1))
log_error = $(call log,$(COLOR_RED),ERROR,$(1))

.PHONY: all log_tester create_venv clean_venv install run

log_tester:
	$(call log_trace,"This is a trace message")
	$(call log_debug,"This is a debug message")
	$(call log_info,"This is an info message")
	$(call log_warn,"This is a warning message")
	$(call log_error,"This is an error message")

create_venv:
	$(call log_info,"Creating virtual environment")
	python3 -m venv venv

clean_venv:
	$(call log_info,"Cleaning virtual environment")
	rm -rf venv

install:
	$(call log_info,"Installing dependencies")
	venv/bin/pip install -r requirements.txt

run:
	$(call log_info,"Running the application")
	#PYTHONUNBUFFERED=1 venv/bin/python src/pdf-extract-text-2.py
	venv/bin/python pdf-extract-text-2.py
