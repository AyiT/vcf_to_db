import db
class Record:
    def __init__(self, arecord):
        self.chrom = arecord['CHROM']
        self.pos = arecord['POS']
        self.rsid = arecord['ID']
        self.ref = arecord['REF']
        self.alt = arecord['ALT']
        self.ac = self.get_info(arecord)['AC']
        self.af = self.get_info(arecord)['AF']
        self.an = self.get_info(arecord)['AN']
        self.set = self.get_info(arecord)['set']


    def get_info(self,arecord):
        info = arecord['INFO']
        d = {}
        for element in info.split(';'):
            if len(element.split('=')) == 2:
                d[element.split('=')[0]] = element.split('=')[1]
        return(d)

    def get_chrom(self):
        return(self.chrom)

    def get_pos(self):
        return(self.pos)

    def get_rsid(self):
        return(self.rsid)

    def get_ref(self):
        return(self.ref)

    def get_alt(self):
        return(self.alt)

    def get_ac(self):
        return(self.ac)

    def get_af(self):
        return(self.af)

    def get_an(self):
        return(self.an)

    def get_set(self):
        return(self.set)
