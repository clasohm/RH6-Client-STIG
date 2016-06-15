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


## Rule Comparison Engine
This simple utility allows you to see the rules that exist in the given XML file that are not addressed in your ansible content.

*Important Note:* In order for the utility script to detect ansible content the ansible tasks need to conform to the following standard for the `- name:` directive:

```yml
- name: "SEVERITY | VULN_ID | RULE TITLE"
  some_module:
      param1: foo

# Example
- name: "HIGH | V-38653 | The snmpd service must not use a default password."
  some_module:
      param1: foo
  
```

When the rule is not automated OR explicitly not implemented, then the same convention should be followed but as a comment and without any module directives/parameters

```yml
# VULN_ID not automated/implemented
# - name: "SEVERITY | VULN_ID | RULE TITLE"
```

### Usage

1. Install the python reqs `pip install -r requirements.txt`
2. Run the command `./compare_rules.py -x path/to/xccdf_file_from_disa.xml -a path/to/ansible_roles_dir/`
3. If you wish to see the rule descriptions append a `-v` to the prior command
