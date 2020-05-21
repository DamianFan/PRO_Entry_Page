class EDGE(object):
    """Define cytoscape edge object."""

    def __init__(self):
        pass

    def json(self, e):
        # print('*****input of json******',e)
        """Cytoscape Web Edge"""
        sn, type, tn = e[0], e[1], e[2]
        if type == "is_a":
            (sn, tn) = (tn, sn)
        id = sn + ' (' + type + ') ' + tn
        return '{id: "' + id + '", ID: "' + id + '", Interaction: "' + type + '", Source: "' + e[
            3] + '", source: "' + sn + '", target: "' + tn + '", ' + e[4] + '},'

    def jsjson(self, e):
        # print('*******input of jsjson******',e)
        """Cytoscape.js Edge"""
        sn, type, tn = e[0], e[1], e[2]
        # print('sn,type,tn: ',sn,type,tn)
        if type == "is_a":
            (sn, tn) = (tn, sn)
            # print('(sn.tn)',(sn,tn))
        id = sn + ' (' + type + ') ' + tn
        # print('id = ',id)
        return '{data: {id: "' + id + '", ID: "' + id + '", Interaction: "' + type + '", Source: "' + e[
            3] + '", source: "' + sn + '", target: "' + tn + '", ' + e[4] + '}},'
        # return '{data: {id: "'+id+'", source: "'+sn+'", target: "'+tn+'", '+e[4]+'}},'
