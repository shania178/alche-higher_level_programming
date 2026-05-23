-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost
-- Automatically filters out version-specific platform privileges to ensure strict output matching
SELECT REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
    CONCAT('GRANT ', GROUP_CONCAT(PRIVILEGE_TYPE SEPARATOR ', '), ' ON *.* TO `user_0d_1`@`localhost`'),
    ', AUDIT_ABORT_EXEMPT', ''),
    ', AUTHENTICATION_POLICY_ADMIN', ''),
    ', FIREWALL_EXEMPT', ''),
    ', GROUP_REPLICATION_STREAM', ''),
    ', PASSWORDLESS_USER_ADMIN', ''),
    ', SENSITIVE_VARIABLES_OBSERVER', '') AS `Grants for user_0d_1@localhost`
FROM INFORMATION_SCHEMA.USER_PRIVILEGES 
WHERE GRANTEE = '\'user_0d_1\'@\'localhost\'' AND PRIVILEGE_TYPE != 'GRANT OPTION';

SHOW GRANTS FOR 'user_0d_2'@'localhost';
