import datetime
import vcf
import db
##Initialisation

def main(vcf_path, db_param):
    ##Connection to DB
    aconnection = db.Conn(db_param['database'], db_param['host'], db_param['port'], db_param['user'], db_param['password'])
    avcf = vcf.Vcf(vcf_path)
    avcf.insert_records(aconnection)



vcf_path = "C:/Users/ayite/Documents/Sophia Genetics/DBSG/gonl.chr22.snps_indels.r5.vcf"
#vcf_path = "C:/Users/ayite/Documents/DBSG/test.vcf"

db_param={}
db_param['database'] = 'vdb'
db_param['host'] = '127.0.0.1'
db_param['port'] = '5432'
db_param['user'] = 'usertest'
db_param['password'] = 'ofdb'

start_time = datetime.datetime.now()
print(start_time)
main(vcf_path,db_param)
end_time = datetime.datetime.now()
print("started at:")
print(start_time)
print("finished at:")
print(end_time)