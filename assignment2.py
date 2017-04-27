#! /usr/bin/env python3

import vcf
import numpy as np
import os
__author__ = 'Frank Ruge'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        self.vcf = vcf.Reader(filename="AmpliseqExome.20141120.NA24385.vcf")
        self.header = self.vcf._header_lines
        self.records = list([i for i in self.vcf])

    def get_average_quality_of_son(self):
        avg_PHRED= np.mean([i.QUAL for i in self.records])
        #1753.77822224
        return avg_PHRED
        
        
    def get_total_number_of_variants_of_son(self):
        count=0
        for record in self.records:
            count+=1
        return count #38526

    
    
    def get_variant_caller_of_vcf(self):
        for record in self.header:
            if "##source=" in record:
                caller=record
            exit
        return(caller.lstrip("##source="))
        
    def get_human_reference_version(self):
        for record in self.header:
            if "##reference=" in record:
                caller=record
            exit
        return(caller.lstrip("##reference="))
        
        
    def get_number_of_indels(self):
        count=0
        for record in self.records:
            if record.is_indel:
                count+=1
        return count
        

    def get_number_of_snvs(self):
        count = 0
        for record in self.records:
            if record.is_snp:
                count += 1
        return count
        
    def get_number_of_heterozygous_variants(self):
        count = 0
        for record in self.records:
            if record.heterozygosity:
                count += 1
        return count

        
    
    def print_summary(self):
        avg_PHRED = assignment1.get_average_quality_of_son(); print("Average PHRED: "+ str(avg_PHRED))
        number_var = assignment1.get_total_number_of_variants_of_son(); print("total_number_of_variants_of_son: " + str(number_var))
        variant_caller = assignment1.get_variant_caller_of_vcf(); print("Variant Caller: "+variant_caller)
        reference_version = assignment1.get_human_reference_version(); print("Reference used: "+reference_version)
        number_indels=assignment1.get_number_of_indels(); print("Number of Indels: "+str(number_indels))
        snv=assignment1.get_number_of_snvs();print("SNPs including SNVs: "+str(snv))
        heterozygous_variants = assignment1.get_number_of_heterozygous_variants();print("Heterozygous variants: "+str(heterozygous_variants))
        
if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2()
    assignment1.print_summary()
    
    

