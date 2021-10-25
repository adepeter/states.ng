#!/bin/bash

PROJECT_NAME='STATESNG API PROJECT'
BACKEND_SERVICE_NAME='statesng'
CONFIG_DIR='configs'
ENV_FILES_DIR="${CONFIG_DIR}/envs/"
SUBDOMAINS=("api" "cpanel" "pages" "www" "admin")

close_color="\e[0m"
color_close="${close_color}"
color_reset="${color_close}"
color_invert="\e[7m"
invert_color="${color_invert}"
default_color="\e[39m"
default_bg="\e[49m"
reset_color="${color_close}"

blink="\e[5m"
bold="\e[1m"
dim_color="\e[2m"
hide_color="\e[8m"
underline="\e[4m"

close_blink="\e[25m"
close_bold="\e[21m"
close_dim="\e[22m"
close_hidden="\e[28m"
close_invert="\e[27m"
close_underline="\e[24m"

black_color="\e[30m"
blue_color="\e[34m"
cyan_color="\e[36m"
green_color="\e[32m"
light_green_color="\e[92m"
majenta_color="\e[35m"
red_color="\e[31m"
white_color="\e[97m"

black_bg="\e[40m"
blue_bg="\e[44m"
cyan_bg="\e[46m"
dark_gray_bg="\e[100m"
green_bg="\e[42m"
light_red_bg="e[101m"
light_gray_bg="\e[47m"
majenta_bg="\e[45m"
red_bg="\e[41m"
white_bg="\e[107m"
yellow_bg="\e[43m"

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
  if [[ ${?} -eq 0 ]]; then
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
  local domain_name_regex="^(https://|https://)?(w{3}\.)?([a-zA-Z0-9]+[-\._]?)*[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}/?$"
  if [[ $domain_name =~ $domain_name_regex ]]; then
    return 0
  fi
  return 1
}

validate_email() {
  local email
  email=$1
  echo "${email}" | grep -E -iqw '^[[:alnum:]]+(\.?[[:alnum:]])+@[[:alnum:]]+(\.[[:alnum:]]+){1,2}$'
  return $?
}

setup_allowed_hosts() {
  echo "Setting up allowed host"
}

setup_postgres() {
  local postgres_db_name postgres_db_user postgres_db_password postgres_env_file="${ENV_FILES_DIR%/}/postgress.env"
  echo "Setting up postgres"
  read -p "Enter your postgres DB name: " postgres_db_name
  read -p "Enter your postgres DB username: " postgres_db_user
  echo "Enter your postgres DB password: "
  read -s
  postgres_db_password=${REPLY}

  echo -e \
    "POSTGRES_DB=${postgres_db_name}\nPOSTGRES_USER=${postgres_db_user}\nPOSTGRES_PASSWORD=${postgres_db_password}" \
    >${postgres_env_file}
}

setup_pgadmin4() {
  echo "Setting up pgadmin4"
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

setup_domain_name() {
  local clean_domain domain_name is_valid=false
  echo -e "DOMAIN NAME SETUP"
  until $is_valid; do
    read -p "Please enter your domain name: " domain_name
    validate_domain_name "${domain_name}"
    if [[ $? -eq 0 ]]; then
      clean_domain=$(cleaned_domain_name "${domain_name}")
      echo "${clean_domain}"
      is_valid=true
    fi
  done
}

setup_email() {
  local email_address is_valid=false
  until $is_valid; do
    read -p "Enter e-mail address: " email_address
    validate_email "${email_address}"
    if [[ $? -eq 0 ]]; then
      echo "${email_address}"
      is_valid=true
    fi
  done
}

setup_statesng() {
  echo "Backend configuration setup"
}

global_configuration_setup() {
  local domain_name email_address secret_key subdomains
  secret_key=$(generate_secret_code)
  echo -e "GENERAL CONFIGURATION"
  echo "This is a one time configuration setup that will be shared across all other subsequent installation"
  domain_name=$(setup_domain_name)
  email_address=$(setup_email)
  subdomains="${domain_name}"
  for subdomain in ${SUBDOMAINS[*]}; do
    if [[ ${SUBDOMAINS[*]: -1} != "${subdomain}" ]]; then
      subdomains+="${subdomain}.${domain_name},"
    elif [[ ${SUBDOMAINS[0]} = "${subdomain}" ]]; then
      subdomains+=","
    else
      subdomains+="${subdomain}.${domain_name}"
    fi
  done
  echo "${subdomains}"
  #    echo -e "ROOT_DOMAIN_NAME=${subdomains}\nLETSENCRYPT_EMAIL=${email_address}\nSTATESNG_SECRET_KEY=${secret_key}" > \
  #    "${ENV_FILES_DIR}/statesng.env"
}

global_configuration_setup

start() {
  echo -e "${bold}WELCOME TO ${PROJECT_NAME}${close_bold}"
  echo ""
  echo ""
  global_configuration_setup
  setup_postgres
  setup_statesng
  setup_pgadmin4
  post_installation_setup
}
