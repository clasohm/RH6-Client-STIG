# RH6-Client-STIG


Instructions
============


## STIG Viewer Setup

1. Install java jdk from [bit.ly/javajdk8](https://bit.ly/javajdk8)
2. Install it with admin priveleges with default options
3. Download the STIG viewer [bit.ly/stigview](https://bit.ly/stigview)
4. Download the latest STIG SCAP content from [DISA](http://iase.disa.mil/stigs/scap/Pages/index.aspx). As of this document, the latest version for RHEL 6 is Revision 1, release 11 which can be downloaded [here](http://iasecontent.disa.mil/stigs/zip/Apr2016/U_RedHat_6_V1R11_STIG_SCAP_1-1_Benchmark.zip).
5. Extract the zip file you just downloaded
6. Open the STIG viewer jar file you downloaded earlier.
7. Click on `File` > `Import STIG`, and directory browser should appear
8. Navigate the the location where you extracted the SCAP content and highlight all of the XML files (there should be 4 of them) and click open.
9. Your STIG viewer should now be populated

## Content Creation
1. Check if the rule has already been addressed in the lockdown project [here](https://bit.ly/mpgstig)
2. If so, then copy all of the bits that are related to your desired rule into the proper place in this repository
