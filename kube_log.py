from kubernetes import client, config
##If using a nonstanrd config
config.load_kube_config()


def get_pods_for_selectfield(namespace):
    '''
    :param namespace:  string
    :return: [(pod1, pod1), (pod2, pod2)...]
    function to create selectfield choice inputs
    '''
    v1 = client.CoreV1Api()
    ret = v1.list_namespaced_pod(namespace)

    return [(i.metadata.name, i.metadata.name) for i in ret.items]

def get_pod_logs(podname, namespace, lines):
    '''
    :param podname: str
    :param namespace: str 
    :param lines: int
    :return: 
    function to get the last n lines of a pod in a specific namesapce
    '''
    v1 = client.CoreV1Api()
    ret = v1.read_namespaced_pod_log(podname, namespace)
    ret = '\n'.join(ret.split('\n')[-(int(lines)+1):])
    return ret

if __name__ == '__main__':
    print(get_pod_logs('speaker-77zkr', 'metallb-system', 10))
    pass
