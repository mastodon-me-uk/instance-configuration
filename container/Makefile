PROJECT = configurer
ID = mastodon-me-uk/${PROJECT}

build:
	docker build \
		--build-arg PROJECT=${PROJECT} \
		--tag ${ID} .

run:
	docker run \
		--name ${PROJECT} \
		--hostname ${PROJECT} \
		--volume $(shell pwd)/../:/opt/${PROJECT} \
		--network="host" \
		--interactive \
		--tty \
		--rm \
		${ID} \
		bash

exec:
	docker exec \
		--interactive \
		--tty \
		${PROJECT} \
		bash
