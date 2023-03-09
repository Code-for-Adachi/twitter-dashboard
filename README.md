# twitter-dashboard
twitter dashboard for code for adachi

# usage

1. .env_example を .env にコピーする

```
$ cp .env_example .env
```

2. .env を編集する

```
$ vi .env

TWITTER_API_BEARER_TOKEN="XXXX"

to

TWITTER_API_BEARER_TOKEN="YOUR OWN TWITTER API BEARER TOKEN"
```

3. docker-compose で web, stream_api, redis を起動

```
$ docker-compose up
```

4. http://127.0.0.1:8000 でアクセス
