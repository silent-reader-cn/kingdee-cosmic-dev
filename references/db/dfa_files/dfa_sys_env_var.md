# （弃用）系统环境变量-dfa_sys_env_var

## （弃用）系统环境变量-主表 t_dfa_sys_env_var

- **表名称：** （弃用）系统环境变量-主表
- **表名：** t_dfa_sys_env_var

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fevaluate_model | 财务健康评价模型 | int8 | 64 |  | √ | 0 | [财务健康度评价模型类型 dfa_health_evaluate_type](../dfa_files/dfa_health_evaluate_type.md) |
| 3 | fembedding_token | embedding密钥 | varchar | 50 |  | √ | ' ' | embedding密钥 |
| 4 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fmongo_user | mongo用户名 | varchar | 50 |  | √ | ' ' | mongo用户名 |
| 6 | fself_daas_ipo | 是否独享daas-ipo | bpchar | 1 |  | √ | '0' | 是否独享daas-ipo |
| 7 | fdaas_ipo_inner_url | 独享daas-ipo内网地址 | varchar | 50 |  | √ | ' ' | 独享daas-ipo内网地址 |
| 8 | fembedding_address | embedding服务地址 | varchar | 50 |  | √ | ' ' | embedding服务地址 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmongo_endpoint | mongo访问地址 | varchar | 50 |  | √ | ' ' | mongo访问地址 |
| 11 | fmongo_pwd | mongo密码 | varchar | 50 |  | √ | ' ' | mongo密码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_sys_env_var |  | fdaas_ipo_inner_url |
| 2 | pk_dfa_sys_env_var |  | fid |
