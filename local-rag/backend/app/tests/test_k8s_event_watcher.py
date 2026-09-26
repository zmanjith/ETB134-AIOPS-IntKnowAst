from app.live_resources.k8s_event_watcher import KubernetesEventWatcher

watcher = KubernetesEventWatcher()

print("Listening...\n")

for document in watcher.watch_events():

    if document is None:
        continue

    print("=" * 80)

    print(document)

    print("=" * 80)