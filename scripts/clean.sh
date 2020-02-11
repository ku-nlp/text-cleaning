#!/usr/bin/env bash

set -eu

input_lines=()
while read line
do
  input_lines+=( "${line}" )
done < "${1:-/dev/stdin}"

SPLITTER=''
if [[ -z ${SPLITTER} ]]; then
  columns=1
else
  columns=$(echo ${input_lines[0]} | awk -F ${SPLITTER} '{print NF+1}')
fi


for ((i = 0; i < ${columns}; i++)) {
#    echo "${input_lines[*]}" | awk -F ${SPLITTER} 'print ${i+1}'
#    IFS=$'\n' echo "${input_lines[*]}" | cut -d "${SPLITTER}" -f $((i+1))
  if [[ -z ${SPLITTER} ]]; then
    IFS=$'\n' echo "${input_lines[*]}"; echo hoge
#    echo "${input_lines[*]}"; echo hoge
  elif [[ ${SPLITTER} == '\t' ]]; then
    IFS=$'\n' echo "${input_lines[*]}" | cut -f $((i+1))
  else
    IFS=$'\n' echo "${input_lines[*]}" | cut -d ${SPLITTER} -f $((i+1))
  fi

}
