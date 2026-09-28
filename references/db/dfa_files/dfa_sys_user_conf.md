# 系统用户配置-dfa_sys_user_conf

## 系统用户配置-主表 t_dfa_sys_user_conf

- **表名称：** 系统用户配置-主表
- **表名：** t_dfa_sys_user_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbos_user | 系统用户 | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fcur_data_center | 当前数据中心 | int8 | 64 |  | √ | 0 | [租户数据中心 dfa_tenant_datacenter](../dfa_files/dfa_tenant_datacenter.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_sys_user_conf |  | fbos_user |
| 2 | pk_dfa_sys_user_conf |  | fid |
