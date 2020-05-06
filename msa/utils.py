from .models import *
import re
import urllib
import request
import requests

def modify_residues(residues):
    res = residues.split('|')
    result = []
    for case in res:
        mod_id = case[case.find('MOD:'):]
        mod_id = mod_id.replace('.','')
        all = case.replace(mod_id,'')
        all = all.replace(',','')
        sites = all.split('/')
        for i in sites:
            i = i.replace('-','')
            positions = re.findall(r"\d+\.?\d*", i)
            position = positions[0]
            abb = i.replace(position, '')
            abb = abb.replace('.','')
            abb = abb.replace(' ','')
            result.append([mod_id,abb,position])

    return result


def modify_enzymes(enzymeString):
    results = []
    enzymes = ''
    result = []

    if enzymeString != None and len(enzymeString) > 0:
        enzymes = re.findall(r'''
                    ([a-zA-Z]*)=\(   #first group is type
                    "([^"]*)"        #second group is name
                    (?:;\ *
                        ( [^\)\.\ ;]+:[^\)\.\ ;]+(?:;\ *[^\)\.\ ;]+:[^\)\.\ ;]+)*)   #third group is ; sep id list (requires:) (optional)
                    )?
                    (?:;\ *
                        ([^;\)\.]*)     #fourth group is rest (optional)
                    )?
                    \)\.?
                ''', enzymeString, re.VERBOSE | re.IGNORECASE)

    for x in enzymes:
        site_num = x[3].count('/')
        sites = x[3]
        # print('enzyme check')
        for i in range(0, site_num + 1):
            # print(id)
            type = x[0]
            # print(x[0])
            obo_dbxref_description = x[1]
            # print(x[1])
            aggkey = x[2]
            # print('aggkey: ', x[2])
            po = sites.find('/')
            if po != -1:
                tem = sites[:po]
                sap = tem.index('-')
                name = tem[:sap]
                location = tem[sap + 1:]
                # print('name: ',name)
                # print('location: ', location)
                sites = sites[po + 1:]
            else:
                tem = sites
                sap = tem.index('-')
                name = tem[:sap]
                location = tem[sap + 1:]
                # print('name: ', name)
                # print('location: ',location)
            if [type,obo_dbxref_description,aggkey,location,name] not in result:
                result.append([type,obo_dbxref_description,aggkey,location,name])
    return result

def modify_xref(definition):
    result = []
    if definition.find('[') != -1:
        p = definition.index('[')
        q = definition.index(']')
        xref = definition[p + 1:q]
        result.append(xref)
    return result

def get_seqs(ids):
    # input ids is a dictionary
    # newids = []
    # for id in ids:
    #     id = 'PR:' + id
    #     newids.append(id)
    # uniprotset = ids
    seqs = []
    for id in ids:
        robj = Sequence()
        unid = ids[id]
        result = requests.get('http://www.uniprot.org/uniprot/' + unid + '.fasta?include=yes').text
        raw = result.split('\n')
        seq = ''.join(raw[1:])
        robj.subject = id
        robj.sequence = seq
        seqs.append(robj)
    return seqs

def get_seq_external(id):
    result = requests.get('http://www.uniprot.org/uniprot/' + id + '.fasta?include=yes').text
    raw = result.split('\n')
    seq = ''.join(raw[1:])
    return seq



























