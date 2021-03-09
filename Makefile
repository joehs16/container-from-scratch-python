install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

lint:
	docker run --rm -i hadolint/hadolint < Dockerfile