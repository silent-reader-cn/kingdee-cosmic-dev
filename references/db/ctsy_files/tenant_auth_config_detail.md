# 租户配置分发明细-tenant_auth_config_detail

## 租户配置分发明细-主表 t_bas_tenant_auth_detail

- **表名称：** 租户配置分发明细-主表
- **表名：** t_bas_tenant_auth_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdistributdate | 分发时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 分发时间 |
| 3 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fauthtenantconfigid | 单点认证租户 | int8 | 64 |  | √ | 0 | [租户认证配置 tenant_auth_config](../ctsy_files/tenant_auth_config.md) |
| 5 | fdistribut_status | 分发状态 | bpchar | 1 |  | √ | '0' | 分发状态,枚举: |
| 6 | ftenantconfigid | 分发租户 | int8 | 64 |  | √ | 0 | [租户认证配置 tenant_auth_config](../ctsy_files/tenant_auth_config.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_detail_ftenantconfigid |  | ftenantconfigid |
| 2 | pk_t_bas_tenant_auth_detail |  | fid |
