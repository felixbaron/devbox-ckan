# CKAN - Data portal platform

## How to install CKAN

```Shell
git clone --depth=1 https://github.com/ckan/ckan.git
cd ckan/contrib/docker
cp .env.template .env
docker-compose up -d --build
# On Windows
start http://localhost:5000
```
