## Start ray cluster
`ray up cluster-config.yaml`

## Stop ray cluster
`ray down cluster-config.yaml`

## Port forward dashboard 
`ray dashboard cluster-config.yaml`

## Copy files to the head node
```
ray rsync_up cluster-config.yaml main.py /home/ray/main.py
ray rsync_up cluster-config.yaml summarizer.py /home/ray/summarizer.py
ray rsync_up cluster-config.yaml translator.py /home/ray/translator.py
```

## Deploy serve application
`serve deploy app-config.yaml -a http://127.0.0.1:8265`

## Port forward app port
`ray attach cluster-config -p 8000`