aws ecr create-repository --repository-name nostos-genomics-repo \
--image-tag-mutability IMMUTABLE --image-scanning-configuration scanOnPush=true