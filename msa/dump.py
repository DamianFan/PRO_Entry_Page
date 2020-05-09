import json


def dump_view(d):
    seqRec = []
    print('dump_view, d.order',d.order)
    for id in d.order:
        obj = d.records[id]
        r = obj.seqRecord
        a = {
            "id": id,
            "name": r.name,
            "sites": r.description,
            "enzymes": ", ".join(obj.enzymes).replace(':', '_'),
            "group": r.annotations["relationship"],
            "definition": r.annotations["definition"]
        }
        if not id.startswith("PR:"):
            a["id"] = "iPTM:" + id
        seqRec.append(a)

    return json.dumps({
        "stat": d.stat,
        "seqRec": seqRec,
        "dv": dict(d.dv.__dict__),
        "dvseq": [
            {'group': d.records[id].seqRecord.annotations["relationship"], 'seq': [dict(i.__dict__) for i in d.records[id].dvSeq]}
            for id in d.order],
        "ov": dict(d.ov.__dict__),
        "ovseq": [
            {'group': d.records[id].seqRecord.annotations["relationship"], 'seq': [dict(i.__dict__) for i in d.records[id].ovSeq]}
            for id in d.order]
    })
