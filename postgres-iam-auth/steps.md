#### Grant permissions to servcieaccount 
  > Doc: https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-policy-binding
    -> roles/cloudsql.instanceUser
    -> roles/cloudsql.client


#### Create role which will be assigned to serviceaccount user: 
  > Doc: https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-db-roles
    
```sql
    CREATE DATABASE appdb;
    CREATE ROLE approle;
    GRANT approle TO postgres;
    ALTER DATABASE appdb OWNER TO approle;
    GRANT CONNECT ON DATABASE appdb to approle;
    GRANT USAGE ON SCHEMA public TO approle;
    ALTER ROLE "<cloudrun-service-account>" SET role = approle;
```

#### Add serviceaccount to postgres
   
#### Code 
  > Doc: https://docs.cloud.google.com/sql/docs/postgres/iam-logins#python
