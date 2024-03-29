help: ## Outputs this help screen
    @grep -E '(^[a-zA-Z0-9_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
test:
	rm inventory_test.db
	PYTHONPATH=. TEST=1 pytest
start:
	uvicorn main:app --reload