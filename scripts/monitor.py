from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

print("=== Nodes ===")
nodes = v1.list_node()
for node in nodes.items:
    node_name = node.metadata.name
    ready = [cond.status for cond in node.status.conditions if cond.type == "Ready"][0]
    print(f"{node_name} - Ready: {ready}")

print("\n=== Pods ===")
pods = v1.list_pod_for_all_namespaces()
for pod in pods.items:
    print(f"{pod.metadata.namespace:<15} {pod.metadata.name:<40} {pod.status.phase}")

print("\n=== Deployments ===")
deployments = apps_v1.list_deployment_for_all_namespaces()
for dep in deployments.items:
    ns = dep.metadata.namespace
    name = dep.metadata.name
    replicas = dep.status.replicas or 0
    ready = dep.status.ready_replicas or 0
    print(f"{ns:<15} {name:<40} Ready: {ready}/{replicas}")
