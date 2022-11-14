#!/bin/bash

# First print the list of crates so that it is visible in the logs
alr --no-tty -n search --list

root_dir="${PWD}"

regex="^([a-z_]*)[[:space:]]+[UX]*[[:space:]]*?([0-9][0-9.a-z+-]+)[[:space:]]+(.*)$"

alr --no-tty -n search --list | while read line; do
    echo $line
    if [[ "$line" =~ "$regex" ]]
    then
        cd "${root_dir}"

        name="${BASH_REMATCH[1]}"
        version="${BASH_REMATCH[2]}"
        base_dir="${name}_${version}"
        output_dir="${PWD}/docs/${base_dir}"
        temp_dir="${PWD}/tmp/${base_dir}"
        echo "name:" $name
        echo "version:" $version


        if [ -d "${output_dir}" ]; then
            echo "Doc for '${name}_${version}' already exists"
        else
            echo "Missing doc for '${name}_${version}'"
            mkdir -p ${temp_dir}
            cd ${temp_dir}
            alr -n get ${name}=${version}
            cd ${name}*
            alr -n exec -P -- gnatdoc4
            index=$(find ${temp_dir} -path */gnatdoc/html/index.html)
            if [ -n "${index}" ]; then
                mkdir -p ${output_dir}
                cp -r $(dirname ${index}) ${output_dir}
            else
                echo "Cannot find generated doc for '${name}_${version}'"
            fi
        fi
    fi
done
    

# push new doc
# git config user.name "${GITHUB_ACTOR}"
# git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
# git remote rm origin || true
# git remote add origin "${remote_repo}"
# git add docs
# git commit --allow-empty --amend -m "Automated deployment: $(date -u) ${GITHUB_SHA}"
# git push origin
