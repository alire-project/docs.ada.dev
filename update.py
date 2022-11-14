from datetime import datetime
import semver
import json
import subprocess
import re
import os

root_dir = os.getcwd()

GLOBAL_DATA_FILE = '_data/global_doc_info.json'

try:
    with open(GLOBAL_DATA_FILE, 'r') as (f, err):
        global_doc_info = json.loads(f.read())
except:
    global_doc_info = {}


def save_global_doc_info():
    with open(os.path.join(root_dir, GLOBAL_DATA_FILE), 'w') as f:
        json.dump(global_doc_info, f, indent=2, sort_keys=True)

def make_crate_index_md(crate):
    with open(os.path.join(root_dir, "crate", crate, "index.md"), 'w') as f:
        f.write("""---
layout: crate
crate: %s
---
""" % crate)

def make_crate_latest_md(crate):
    with open(os.path.join(root_dir, "crate", crate, "latest.md"), 'w') as f:
        f.write("""---
layout: latest_redirect
crate: %s
---
""" % crate)

def make_eror_release_index_md(crate, version, error):
    with open(os.path.join(root_dir, "crate", crate, version, "index.md"), 'w') as f:
        f.write("""---
layout: gnatdoc_error
crate: %s
version: %s
---
```
%s
```
""" % (crate, version, error))

# output = subprocess.run(['alr', '--no-tty', '-n', 'search',
#                             '--list'], stdout=subprocess.PIPE).stdout


# crates = output.decode('utf-8').splitlines()
crates = ["aaa     0.2.6    as a a a",
          "aaa     0.1.0    as a a a",
          "zlib_ada 1.3.0 a a a",
          "tash 8.7.0 a a a",
          "geste 1.1.0 a a a "]

pattern = "^([a-z_]*)[\s]+[UX]*[ ]*?([0-9][0-9.a-z+-]+)[\s]+(.*)$"
for line in crates:
    print(line)
    match = re.search (pattern, line)
    if match:
        # Go to our root directory
        os.chdir(root_dir)

        name = match.group (1)
        version = match.group (2)
        base_dir = os.path.join(name, version)

        doc_output_dir = os.path.join(root_dir, "crate", base_dir)
        tmp_dir = os.path.join(root_dir, "tmp", base_dir)

        if name not in global_doc_info:
            global_doc_info[name] = {'releases': {}}

        if version in global_doc_info[name]['releases']:
            print("Doc for %s %s already exists" % (name, version))
        else:
            release_doc_info = {}

            print("Missing doc for %s %s..." % (name, version))
            get_cmd = ['alr', '-n', 'get', name + "=" + version]

            # Make and enter temp dir for the crate
            os.makedirs(tmp_dir, exist_ok=True)
            os.chdir(tmp_dir)

            # Get the name of the directory where the crate will be downloaded
            getdir = subprocess.run(get_cmd + ["--dirname"],
                                    stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()

            # Get the crate and dependencies
            outcome = subprocess.run(get_cmd,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)
            if outcome.returncode != 0:
                release_doc_info['status'] = "alr get failed"
                release_doc_info['alr_get_error'] = outcome.stdout.decode('utf-8')
                make_eror_release_index_md(name, version,
                                           outcome.stdout.decode('utf-8'))
            else:
                # Enter crate dir
                os.chdir(getdir)

                outcome = subprocess.run(['alr', '-n', 'exec', "-P", "--", "gnatdoc4",
                                          "--output-dir", doc_output_dir, "--no-subprojects"],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT)

                if outcome.returncode == 0:
                    release_doc_info['status'] = "doc build OK"
                    release_doc_info['date'] = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
                else:
                    release_doc_info['status'] = "doc build FAIL"
                    release_doc_info['gnatdoc_error'] = outcome.stdout.decode('utf-8')
                    make_eror_release_index_md(name, version,
                                               outcome.stdout.decode('utf-8'))

            global_doc_info[name]['releases'][version] = release_doc_info

            if ('latest' not in global_doc_info[name]) or \
                   semver.compare(version, global_doc_info[name]['latest']) > 0:
                global_doc_info[name]['latest'] = version

            make_crate_index_md(name)
            make_crate_latest_md(name)
            save_global_doc_info()

print(str(global_doc_info))
save_global_doc_info()
