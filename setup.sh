#!/bin/bash

BACKEND_SERVICE_NAME='statesng'
CONFIG_DIR='config'
ENV_FILES_DIR="${CONFIG_DIR}/envs"

color_close="\e[0m"
red_color="\e[31m"
green_color="\e[32m"
blue_color="\e[34m"
blink="\e[5m"
bold="\e[1m"
underline="\e[4m"
cyan_color="\e[36m"
majenta_color="\e[35m"
red_bg="\e[41m"
green_bg="\e[42m"
blue_bg="\e[44m"
majenta_bg="\e[45m"
cyan_bg="\e[46m"

base_docker_command_for_backend() {
  echo "docker-compose exec ${BACKEND_SERVICE_NAME} python manage.py"
}

cleaned_domain_name() {
  if [[ ${#*} -ne 1 ]]; then
    echo "You must supply a URL to validate"
    exit 1
  fi
  local domain_name=$1
  case ${domain_name} in
https://)
  domain_name=${domain_name#https://}
  ;;
http://)
  domain_name=${domain_name#http://}
  ;;
www.)
  domain_name=${domain_name#www.}
  ;;
https://www.)
  domain_name=${domain_name#https://www.}
  ;;
http://www.)
  domain_name=${domain_name#http://www.}
  ;;
esac

  echo "${domain_name}" | grep -q '/'
  if [[ "'${?}'" -eq 0 ]]; then
    domain_name=${domain_name%/}
  fi
  echo "${domain_name#https://}"
}

generate_random() {
  echo "Generating random"
}

grep_match_domain_name() {
  local domain_name_regex="(https://|https://)?(w{3}\.)?([a-zA-Z0-9]+[-\._]?)*[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}/?$"
  echo "${domain_name_regex}"
}

generate_secret_code() {
  local random_code secret_code
  random_code=$(tr -cd "'[[:alnum:][:punct:]]'" </dev/urandom | tr -d "'[\"\']'" | head -c 50)
  secret_code="django-secure-${random_code}"
  echo "${secret_code}"
}

trim_whitespaces() {
  { test $# -ne 1 && echo "Argument must just be one" || test -z "${1}" && echo "First argument cannot be blank"; } && exit 1
  echo "${1}" | grep -Eq "^[[:space:]]+$"
  test $? -eq 0 && echo "Argument cannot start and end with ${#1} whitespaces" && exit 1
  echo "${1}" | tr -d "[:space:]"
}


validate_domain_name() {
  local domain_name=${1}
  local is_valid_domain=false
  local domain_name_regex="^(https://|https://)?(w{3}\.)?([a-zA-Z0-9]+[-\._]?)*[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}/?$"
  if [[ $domain_name =~ $domain_name_regex ]]; then
    echo 0
    return 0
  fi
  echo 1
  return 1
}

validate_email() {
  if [[ $# -eq 1 ]]; then
    local email=$1
    echo "${email}" | grep -E -iqw '^[a-z0-9]+@[a-z0-9]+(\.[a-z0-9]+)+$'
    local grep_result=$?
    if [[ ${#email} -gt 3 ]]; then
      if [[ ${email} =~ [[:space:]] ]]; then
        echo -e "${red_color}Email cannot contain space${color_close}"
        return 1
      elif [[ $grep_result -ne 0 ]]; then
        echo -e "${majenta_color}${email} is not a valid email${color_close}"
        return 2
      else
        return 0
      fi
    else
      echo -e "${majenta_color}E-mail supplied doesn't seem to be of valid length${color_close}"
      return 3
    fi
  elif [[ ${#} -lt 1 ]]; then
    echo -e "${red_bg}${bold}You need to supply a positional email argument${color_close}"
    exit 1
  else
    echo -e "Argument must be one"
    exit 2
  fi
}

setup_allowed_hosts() {
  echo "Setting up allowed host"
}

setup_postgres() {
  echo "Setting up postgres"
}

setup_pgadmin4() {
  echo "Setting up pgadmin4"
}

setup_email() {
  echo "Setting up email"
}

make_migrations() {
  $(base_docker_command_for_backend) makemigrations
}

migrate() {
  $(base_docker_command_for_backend) migrate
}

collect_static_files() {
  $(base_docker_command_for_backend) collectstatic --no-input
}

post_installation_setup() {
  make_migrations
  migrate
  collect_static_files
}
