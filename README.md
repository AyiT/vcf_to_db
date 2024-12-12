# vcf_to_db
Read a vcf format file and save variant records into a postgresql db
1. Python Script
Python version 3.8 is used with packages described in pkg.txt
Use >>>pip install -r pkg.txt
to install described packages.
Python files :
- vcf.py which handle a vcf file and insert data.
- record.py which handle the variant records of a vcf file.
- db.py which establish a connection to a posgresql data base
- main.py which set the path to the vcf file, the parameters for the db connection and lunch the
program.

Improvement to do :
i- Create classes that match the database tables. (Variant, Changes, Type)
Each class will have a class method to insert object in DB
ii- Split insert_records method from vcf.py into smaller and more readable functions and
move the insertion part to db.py
iii- Improve the time of execution.

2. Data:
Chromosome 22 INDEL and SNP vcf file download from the dutch Allele Frequency
Database GoNL (http://www.nlgenome.nl/)
File: gonl.chr22.snps_indels.r5.vcf

3. Database
Comment :
Variant main attributes are described in VRAIANT table.
A variant type (SNP, INDEL, …) is stored in VCLASS table.
Variants alternative allele information are described in CHANGES table.
In the current case, one alternative allele is described for a variant but the schema is
designed in order to be able to store variant with several alternative alleles.
Materials:
Database creation script is saved as vdb.sql
PostgreSQL version 12 is used to create the database.
Improvement to do:
i- Set tuple (Chrom, Pos) in table Variant as unique.
ii- Remove the quotes from table creation.
Example:
public.VCLASS instead of public.“VCLASS”



