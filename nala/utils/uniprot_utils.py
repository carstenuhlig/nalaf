from itertools import chain
import requests
from nala.utils.cache import Cacheable

class Uniprot(Cacheable):
    """
    Helper class that accesses the database identifier mapping service from Uniprot.
    and returns a list of 2-tuple with the requested geneid and the corresponding Uniprot ID.
    """

    def __init__(self):
        super().__init__()
        self.url = 'http://www.uniprot.org/mapping/'

    def get_uniprotid_for_entrez_geneid(self, *list_geneids):
        return_dict = {}
        not_found_geneids = []

        for geneid in list_geneids:
            if geneid in self.cache:
                return_dict[geneid] = self.cache[geneid]
            else:
                not_found_geneids.append(geneid)

        for k, v in self.cache.items():
            print(k, v)

        print(not_found_geneids, return_dict)
        if len(not_found_geneids) == 0:
            return return_dict

        params = {
            'from': 'P_ENTREZGENEID',
            'to': 'ACC',
            'format': 'tab',
            'query': ' '.join([str(x) for x in not_found_geneids])
        }

        r = requests.get(self.url, params)
        results = r.text.splitlines()[1:]
        if not results:
            return return_dict

        found_genes = {}

        for line in results:
            geneid, uniprotid = line.split('\t')
            if geneid in found_genes:
                found_genes[geneid].append(uniprotid)
            else:
                found_genes[geneid] = [uniprotid]

        for key, value in found_genes.items():
            # print(key, value)
            self.cache[key] = value

        for k, v in self.cache.items():
            print(k, v)

        return return_dict.update(found_genes)