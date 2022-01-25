# edirect_wrap_server
Build a simple wrap server to throw queries as API to the Entrez Direct installed PC from other PC.

## Attention

This tool is very primitive.
It directly executes Edirect commands received in Json with `edirect.execute`. Normally, you may need to apply sanitization and other security measures.
Please use this only in a LAN environment where the executor can be limited.

## Prerequirements

- Install Edirect and Python3 on the server(linux)
   - To install Edirect, simply follow the instructions on the [official docs](https://www.ncbi.nlm.nih.gov/books/NBK179288/) and execute a following command
   - `sh -c "$(curl -fsSL ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"`

To check if Edirect is available from Python, try a script like the following(refered from official docs).
If you get an error, make sure you have a PATH to the Edirect installation location.

```
import sys
import os
import shutil

sys.path.insert(1, os.path.dirname(shutil.which('xtract')))
import edirect

print(edirect.execute("efetch -db nuccore -id NM_000518.5 -format fasta"))
```

## How to use

1. Copy `app.py` file to the server
2. Run the server by following command; `python app.py`
3. POST json request to the server
    - I used the CURL command to verify it worked
    - `curl -X POST -d @sample.json http://localhost:3000`


Request json format is like this:

```
{
        "query": "efetch -db nuccore -id NM_000518.5 -format fasta"
}
```

Then you will get this result.

```
{"message": ">NM_000518.5 Homo sapiens hemoglobin subunit beta (HBB), mRNA\nACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGA\nGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGC\nAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATG\nCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGC\nTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGAT\nCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCA\nCCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCA\nCTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACT\nGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"}
```
