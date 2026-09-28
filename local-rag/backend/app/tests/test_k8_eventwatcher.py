from live_resources.k8s_event_watcher import KubernetesEventWatcher

watcher = KubernetesEventWatcher()
print("Watching Kubernetes events...")

for document in watcher.watch_events():
    if document is not None:
        print(document.json())
    