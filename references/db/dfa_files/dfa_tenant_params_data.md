# 数据中心集成配置数据-dfa_tenant_params_data

## 数据中心集成配置数据-主表 t_dfa_tenant_params_data

- **表名称：** 数据中心集成配置数据-主表
- **表名：** t_dfa_tenant_params_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fendpoint | 访问地址 | varchar | 255 |  | √ | ' ' | 访问地址 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fitemgroupname | 报表项目分组编码 | varchar | 255 |  | √ | ' ' | 报表项目分组编码 |
| 4 | findustryid | findustryid | int8 | 64 |  | √ | 0 |  |
| 5 | fuser | 用户 | varchar | 255 |  | √ | ' ' | 用户 |
| 6 | fappsec | 应用秘钥 | varchar | 1024 |  | √ | ' ' | 应用秘钥 |
| 7 | fdatacenterid | 数据中心ID | varchar | 50 |  | √ | ' ' | 数据中心ID |
| 8 | fx_acgw_identity | 身份标识 | varchar | 1024 |  | √ | ' ' | 身份标识 |
| 9 | fappid | 应用ID | varchar | 255 |  | √ | ' ' | 应用ID |
| 10 | fdatasourcetype | 来源类型 | varchar | 50 |  | √ | '0' | 来源类型,枚举: |
| 11 | fitemgroupcode | 报表项目分组编码 | varchar | 50 |  | √ | ' ' | 报表项目分组编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_tenant_params_data_m0 |  | findustryid |
| 2 | pk_dfa_tenant_params_data |  | fid |
