# Tutorial para eliminar recursos de AWS con aws-nuke

## Introducción

En este tutorial se explicará cómo eliminar recursos de AWS con la herramienta `aws-nuke`. Esta herramienta es útil para eliminar recursos de AWS de forma masiva y rápida. 

## Instalación en MAC

Para instalar `aws-nuke` en MAC, se debe ejecutar el siguiente comando:

```bash
brew install ekristen/tap/aws-nuke
```

Debéis crear un fichero de configuración para utilizar este script añadiendo el número de cuenta de AWS.

NUM_CUENTA: 123456789
IAM_USER: Es el nombre de usuario en IAM Personas que usáis. Lo ponemos como filtro para que no lo borre
IAM_USER_POLICY: Es la política que tiene asignada el usuario. Lo ponemos como filtro para que no lo borre
IAM_USER_ACCESS_KEY: Es la clave de acceso que tiene asignada el usuario. Lo ponemos como filtro para que no lo borre

```yaml
regions:
  - global
accounts:
  "NUM_CUENTA": 
    filters:
      IAMUser:
        - "IAM_USER"
      IAMUserPolicyAttachment:
        - "IAM_USER_POLICY -> AdministratorAccess"
      IAMUserAccessKey:
        - "IAM_USER_ACCESS_KEY -> AKIAQLMG5X3FJSCXBBPK"
blocklist:
- "999999999999"
```

Ejemplo real de configuracion:

```yaml
regions:
  - global
accounts:
  "123456789": 
    filters:
      IAMUser:
        - "tech-user"
      IAMUserPolicyAttachment:
        - "tech-user -> AdministratorAccess"
      IAMUserAccessKey:
        - "tech-user -> AKIAQLMG5X3FJSCXBBPK"
blocklist:
- "999999999999"

```

Aws-nuke necesita tener un alias de cuenta. Un alias es un nombre de cuenta que se puede utilizar en lugar del número de cuenta. Para configurar un alias de cuenta, debes ejecutar el siguiente comando. Cambiad XXX por vuestro nombre

```bash
aws iam create-account-alias --account-alias aws-edem-XXXXX
```

## Ejecución TEST

Una vez instalado, se puede ejecutar el comando `aws-nuke` para eliminar los recursos de AWS. Este commando solo realiza un "test" de los elementos que serían eliminados.

```bash
aws-nuke nuke -c config.yaml
```

```bash
aws-nuke nuke -c nuke-config.yaml                              
aws-nuke - v3.47.1 - 83e1b3bdfb6e388d28d1a9ec736aa996e338a995
Do you really want to nuke the account with the ID 024442158794 and the alias 'edem-aws-specifics'?
Do you want to continue? Enter account alias to continue.
> edem-aws-specifics

starting scan for resources
global - IAMVirtualMFADevice - arn:aws:iam::024442158794:mfa/personaldevice - [Assigned: "true", SerialNumber: "arn:aws:iam::024442158794:mfa/personaldevice"] - filtered: cannot delete root mfa device
global - CloudFrontResponseHeadersPolicy - Managed-SimpleCORS - [ID: "60669652-455b-4ae9-85a4-c4c02393f86c", Name: "Managed-SimpleCORS"] - filtered: cannot delete default CloudFront Response headers policy
global - CloudFrontResponseHeadersPolicy - Managed-CORS-With-Preflight - [ID: "5cc3b908-e619-4b99-88e5-2cf7f45965bd", Name: "Managed-CORS-With-Preflight"] - filtered: cannot delete default CloudFront Response headers policy
global - CloudFrontResponseHeadersPolicy - Managed-CORS-with-preflight-and-SecurityHeadersPolicy - [ID: "eaab4381-ed33-4a86-88ca-d9558dc6cd63", Name: "Managed-CORS-with-preflight-and-SecurityHeadersPolicy"] - filtered: cannot delete default CloudFront Response headers policy
global - CloudFrontResponseHeadersPolicy - Managed-CORS-and-SecurityHeadersPolicy - [ID: "e61eb60c-9c35-4d20-a928-2b84e02af89c", Name: "Managed-CORS-and-SecurityHeadersPolicy"] - filtered: cannot delete default CloudFront Response headers policy
global - CloudFrontResponseHeadersPolicy - Managed-SecurityHeadersPolicy - [ID: "67f7725c-6f97-4210-82d7-5512b31e9d03", Name: "Managed-SecurityHeadersPolicy"] - filtered: cannot delete default CloudFront Response headers policy
global - IAMUser - adminuser - [CreateDate: "2025-03-10T08:55:31Z", Name: "adminuser", PasswordLastUsed: "2025-03-10T09:04:56Z", Path: "/", UserID: "AIDAQLMG5X3FDQTHZS4LC", tag:AKIAQLMG5X3FCTWOISFD: "root", tag:AKIAQLMG5X3FO4KYWNH2: "Secrets"] - would remove
global - IAMUserAccessKey - adminuser -> AKIAQLMG5X3FCTWOISFD - [AccessKeyID: "AKIAQLMG5X3FCTWOISFD", CreateDate: "2025-03-10T09:19:45Z", UserName: "adminuser", tag:AKIAQLMG5X3FCTWOISFD: "root", tag:AKIAQLMG5X3FO4KYWNH2: "Secrets"] - would remove
global - IAMLoginProfile - adminuser - [CreateDate: "2025-03-10T08:55:31Z", UserName: "adminuser"] - would remove
global - CloudFrontDistributionDeployment - E21LY87F6JCOZC - [ID: "E21LY87F6JCOZC", Status: "Deployed"] - would remove
global - CloudFrontDistributionDeployment - EY9TWCWYOHYPX - [ID: "EY9TWCWYOHYPX", Status: "Deployed"] - would remove
global - CloudFrontDistribution - E21LY87F6JCOZC - [LastModifiedTime: "2025-03-11T12:50:38Z"] - would remove
global - CloudFrontDistribution - EY9TWCWYOHYPX - [LastModifiedTime: "2025-03-13T15:15:18Z"] - would remove
INFO[0128] would remove                                  owner=global prop:ID=E3CS07K1C81I71 state=new state_code=0 type=CloudFrontOriginAccessControl
INFO[0128] would remove                                  owner=global prop:ID=EWBTGXP47MLLQ state=new state_code=0 type=CloudFrontOriginAccessControl
global - IAMUserPolicyAttachment - adminuser -> AdministratorAccess - [PolicyArn: "arn:aws:iam::aws:policy/AdministratorAccess", PolicyName: "AdministratorAccess", UserName: "adminuser", tag:user:AKIAQLMG5X3FCTWOISFD: "root", tag:user:AKIAQLMG5X3FO4KYWNH2: "Secrets"] - would remove
global - IAMPolicy - arn:aws:iam::024442158794:policy/service-role/AWSLambdaBasicExecutionRole-9c2bd58a-863c-4d7e-9678-e6fa1385c0ee - [ARN: "arn:aws:iam::024442158794:policy/service-role/AWSLambdaBasicExecutionRole-9c2bd58a-863c-4d7e-9678-e6fa1385c0ee", CreateDate: "2021-09-24T15:02:36Z", Name: "AWSLambdaBasicExecutionRole-9c2bd58a-863c-4d7e-9678-e6fa1385c0ee", Path: "/service-role/", PolicyID: "ANPAQLMG5X3FBXK7CHAO2"] - would remove
global - IAMPolicy - arn:aws:iam::024442158794:policy/msk-iam-policy - [ARN: "arn:aws:iam::024442158794:policy/msk-iam-policy", CreateDate: "2025-03-10T09:38:22Z", Name: "msk-iam-policy", Path: "/", PolicyID: "ANPAQLMG5X3FE5VUW6SMI"] - would remove
global - IAMPolicy - arn:aws:iam::024442158794:policy/service-role/AWSLambdaBasicExecutionRole-44d657e6-3573-441f-bc25-50da37e7dd88 - [ARN: "arn:aws:iam::024442158794:policy/service-role/AWSLambdaBasicExecutionRole-44d657e6-3573-441f-bc25-50da37e7dd88", CreateDate: "2025-03-10T16:40:59Z", Name: "AWSLambdaBasicExecutionRole-44d657e6-3573-441f-bc25-50da37e7dd88", Path: "/service-role/", PolicyID: "ANPAQLMG5X3FI7AAZH3XD"] - would remove
global - IAMPolicy - arn:aws:iam::024442158794:policy/service-role/aws-iot-role-sqsSend_-1476734206 - [ARN: "arn:aws:iam::024442158794:policy/service-role/aws-iot-role-sqsSend_-1476734206", CreateDate: "2021-09-24T15:06:04Z", Name: "aws-iot-role-sqsSend_-1476734206", Path: "/service-role/", PolicyID: "ANPAQLMG5X3FIKV5FAKGS"] - would remove
global - IAMRole - AWSServiceRoleForKafka - [CreateDate: "2025-03-10T10:37:39Z", LastUsedDate: "2025-03-10T18:46:21Z", Name: "AWSServiceRoleForKafka", Path: "/aws-service-role/kafka.amazonaws.com/"] - filtered: cannot delete service roles
global - IAMRole - AWSServiceRoleForSupport - [CreateDate: "2018-07-12T15:04:44Z", LastUsedDate: "2018-07-12T15:04:44Z", Name: "AWSServiceRoleForSupport", Path: "/aws-service-role/support.amazonaws.com/"] - filtered: cannot delete service roles
global - IAMRole - AWSServiceRoleForTrustedAdvisor - [CreateDate: "2018-07-20T03:08:26Z", LastUsedDate: "2018-07-20T03:08:26Z", Name: "AWSServiceRoleForTrustedAdvisor", Path: "/aws-service-role/trustedadvisor.amazonaws.com/"] - filtered: cannot delete service roles
global - IAMRole - ecruser - [CreateDate: "2022-11-24T14:22:09Z", LastUsedDate: "2022-11-24T14:22:09Z", Name: "ecruser", Path: "/"] - would remove
global - IAMRole - msk-iam-role - [CreateDate: "2025-03-10T09:38:22Z", LastUsedDate: "2025-03-10T09:38:22Z", Name: "msk-iam-role", Path: "/"] - would remove
global - IAMRole - processData-role-fxc23qvf - [CreateDate: "2021-09-24T15:02:36Z", LastUsedDate: "2025-03-10T18:41:23Z", Name: "processData-role-fxc23qvf", Path: "/service-role/"] - would remove
global - IAMRole - readkafka-role-s5ym0nvx - [CreateDate: "2025-03-10T16:40:59Z", LastUsedDate: "2025-03-10T17:16:57Z", Name: "readkafka-role-s5ym0nvx", Path: "/service-role/"] - would remove
global - IAMRole - sqsrole - [CreateDate: "2021-09-24T15:06:04Z", LastUsedDate: "2021-09-24T15:06:04Z", Name: "sqsrole", Path: "/service-role/"] - would remove
global - IAMRolePolicy - processData-role-fxc23qvf -> msk-policy - [PolicyName: "msk-policy", role:Path: "/service-role/", role:RoleID: "AROAQLMG5X3FFRZGPULKU", role:RoleName: "processData-role-fxc23qvf"] - would remove
global - IAMRolePolicy - readkafka-role-s5ym0nvx -> msk - [PolicyName: "msk", role:Path: "/service-role/", role:RoleID: "AROAQLMG5X3FPADRLFEF4", role:RoleName: "readkafka-role-s5ym0nvx"] - would remove
global - IAMRolePolicyAttachment - AWSServiceRoleForKafka -> KafkaServiceRolePolicy - [PolicyArn: "arn:aws:iam::aws:policy/aws-service-role/KafkaServiceRolePolicy", PolicyName: "KafkaServiceRolePolicy", RoleCreateDate: "2025-03-10T10:37:39Z", RoleLastUsed: "2025-03-10 18:46:21 +0000 UTC", RoleName: "AWSServiceRoleForKafka", RolePath: "/aws-service-role/kafka.amazonaws.com/"] - filtered: cannot detach from service roles
global - IAMRolePolicyAttachment - AWSServiceRoleForSupport -> AWSSupportServiceRolePolicy - [PolicyArn: "arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy", PolicyName: "AWSSupportServiceRolePolicy", RoleCreateDate: "2018-07-12T15:04:44Z", RoleLastUsed: "2018-07-12 15:04:44 +0000 UTC", RoleName: "AWSServiceRoleForSupport", RolePath: "/aws-service-role/support.amazonaws.com/"] - filtered: cannot detach from service roles
global - IAMRolePolicyAttachment - AWSServiceRoleForTrustedAdvisor -> AWSTrustedAdvisorServiceRolePolicy - [PolicyArn: "arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorServiceRolePolicy", PolicyName: "AWSTrustedAdvisorServiceRolePolicy", RoleCreateDate: "2018-07-20T03:08:26Z", RoleLastUsed: "2018-07-20 03:08:26 +0000 UTC", RoleName: "AWSServiceRoleForTrustedAdvisor", RolePath: "/aws-service-role/trustedadvisor.amazonaws.com/"] - filtered: cannot detach from service roles
global - IAMRolePolicyAttachment - ecruser -> AmazonEC2ContainerRegistryFullAccess - [PolicyArn: "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess", PolicyName: "AmazonEC2ContainerRegistryFullAccess", RoleCreateDate: "2022-11-24T14:22:09Z", RoleLastUsed: "2022-11-24 14:22:09 +0000 UTC", RoleName: "ecruser", RolePath: "/"] - would remove
global - IAMRolePolicyAttachment - msk-iam-role -> msk-iam-policy - [PolicyArn: "arn:aws:iam::024442158794:policy/msk-iam-policy", PolicyName: "msk-iam-policy", RoleCreateDate: "2025-03-10T09:38:22Z", RoleLastUsed: "2025-03-10 09:38:22 +0000 UTC", RoleName: "msk-iam-role", RolePath: "/"] - would remove
global - IAMRolePolicyAttachment - processData-role-fxc23qvf -> AWSLambdaBasicExecutionRole-9c2bd58a-863c-4d7e-9678-e6fa1385c0ee - [PolicyArn: "arn:aws:iam::024442158794:policy/service-role/AWSLambdaBasicExecutionRole-9c2bd58a-863c-4d7e-9678-e6fa1385c0ee", PolicyName: "AWSLambdaBasicExecutionRole-9c2bd58a-863c-4d7e-9678-e6fa1385c0ee", RoleCreateDate: "2021-09-24T15:02:36Z", RoleLastUsed: "2025-03-10 18:41:23 +0000 UTC", RoleName: "processData-role-fxc23qvf", RolePath: "/service-role/"] - would remove
global - IAMRolePolicyAttachment - readkafka-role-s5ym0nvx -> AWSLambdaBasicExecutionRole-44d657e6-3573-441f-bc25-50da37e7dd88 - [PolicyArn: "arn:aws:iam::024442158794:policy/service-role/AWSLambdaBasicExecutionRole-44d657e6-3573-441f-bc25-50da37e7dd88", PolicyName: "AWSLambdaBasicExecutionRole-44d657e6-3573-441f-bc25-50da37e7dd88", RoleCreateDate: "2025-03-10T16:40:59Z", RoleLastUsed: "2025-03-10 17:16:57 +0000 UTC", RoleName: "readkafka-role-s5ym0nvx", RolePath: "/service-role/"] - would remove
global - IAMRolePolicyAttachment - sqsrole -> aws-iot-role-sqsSend_-1476734206 - [PolicyArn: "arn:aws:iam::024442158794:policy/service-role/aws-iot-role-sqsSend_-1476734206", PolicyName: "aws-iot-role-sqsSend_-1476734206", RoleCreateDate: "2021-09-24T15:06:04Z", RoleLastUsed: "2021-09-24 15:06:04 +0000 UTC", RoleName: "sqsrole", RolePath: "/service-role/"] - would remove
Scan complete: 38 total, 26 nukeable, 12 filtered.

The above resources would be deleted with the supplied configuration. Provide --no-dry-run to actually destroy resources.
```

## Ejecución NUKE

Si ya has comprobado que todo lo que se va a eliminar es correcto, puedes ejecutar el comando `aws-nuke` con la opción `nuke` para eliminar los recursos de AWS.

```bash
aws-nuke nuke -c config.yaml --no-dry-run
```

Si ha funcionado deberéis tener una salida como esta:

```bash
Nuke complete: 0 failed, 17 skipped, 17 finished.
```