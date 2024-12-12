import pandas as pd
import os.path
import record
import sys
class Vcf:
    def __init__(self, path):
        self.path = self.set_path(path)
        self.meta = self.set_meta()
        self.df = self.set_df()

    def set_path(self, vcf_path):
        if os.path.isfile(vcf_path):
            return(vcf_path)
        else:
            print("File {0} do not exist".format(vcf_path))
            sys.exit(1)

    def set_meta(self):
        print("1-Reading vcf header")
        comment=[]
        with open(self.path) as fp:
            for line in fp:
                if (line[:1] =='#'):
                    comment.append(line)
                else:
                    break
        if (comment[-1][:6] =='#CHROM'):
            return comment
        else:
            print("Head is missing or Head is not well formed in vcf file")

    def set_df(self):
        print("2-Reading vcf variants")
        columns_name = self.meta[-1][1:].rstrip().split('\t')
        len_meta = len(self.meta)
        dataf = pd.read_csv(sep = '\t', header = None, skiprows = len_meta, filepath_or_buffer=self.path)
        dataf.columns = columns_name
        return(dataf)

    def get_path(self):
        return(self.path)

    def get_meta(self):
        return(self.meta)

    def get_df(self):
        return(self.df)

    def get_records(self):
        records =[]
        for index,row in self.df.iterrows():
            arecord = record.Record(row)
            records.append(arecord)
        return (records)

    def insert_records(self,acconnection):
        records = self.get_records()
        print("3-Connection to database")
        conn = acconnection.connect()
        cur = conn.cursor()
        count = 0
        print("4-Variants insertion")
        for record in records:
            class_id = ''
            variant_id = ''
            chrom = record.get_chrom()
            pos = record.get_pos()
            print(pos)
            rsid = record.get_rsid()
            ref = record.get_ref()
            alt = record.get_alt()
            ac = record.get_ac()
            af = record.get_af()
            an = record.get_an()
            set = record.get_set()

            #try:
            ###INSERT INTO TABLE VCLASS
            cur.execute('select class_id from public."VCLASS" where type = \''+set+'\';')
            row = cur.fetchone()
            if row == None:
                sql_string_1 = "INSERT INTO public.\"VCLASS\" (type) VALUES ('%s') RETURNING class_id;" % set
                cur.execute(sql_string_1)
                class_id = cur.fetchone()[0]
            else:
                class_id = row[0]


            ###INSERT INTO TABLE VARIANT
            sql_string_2 = "INSERT INTO public.\"VARIANT\" (class_id, rsid, pos, chrom, reference, an) VALUES ('%s','%s','%s','%s','%s', '%s') RETURNING variant_id;" % (str(class_id), rsid, str(pos), str(chrom),ref, str(an))
            cur.execute(sql_string_2)
            variant_id = cur.fetchone()[0]

            ###INSERT INTO TABLE CHANGE
            sql_string_3 = "INSERT INTO public.\"CHANGES\" (variant_id, alt, ac, af) VALUES ('%s','%s','%s','%s');" % (str(variant_id), alt, str(ac), str(af))
            cur.execute(sql_string_3)

            count+=1
            #except:
            #    print("Can not insert:")
            #    print(pos)

        ## Information

        ## Close communication with the database
        cur.close()
        conn.commit()
        conn.close()
        print(" {0} variants over {1} are inserted into database".format(count, len(records)))
