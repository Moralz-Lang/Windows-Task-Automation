def pretty_processes(process_list):
    """Return a nicely formatted list of processes"""
    pretty = []
    for proc in process_list:
        pretty.append({
            "pid": proc.get("pid"),
            "name": proc.get("name"),
            "exe": proc.get("exe"),
            "cmdline": proc.get("cmdline"),
        })
    return pretty
