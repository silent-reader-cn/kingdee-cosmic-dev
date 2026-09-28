# 系统配置-dfa_sysconfig

## 系统配置-主表 t_dfa_sysconfig

- **表名称：** 系统配置-主表
- **表名：** t_dfa_sysconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreate | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fencryptvalue | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fswitch | 参数值 | bpchar | 1 |  | √ | '0' | 参数值 |
| 6 | fvalue | 真实值 | varchar | 2000 |  | √ | ' ' | 真实值 |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :文本 2 :密文 3 :开关 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ftextvalue | 参数值 | varchar | 1000 |  | √ | ' ' | 参数值 |
| 11 | fenable | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :启用 2 :禁用 |
| 12 | fdesc | 说明 | varchar | 100 |  | √ | ' ' | 说明 |
| 13 | fcode | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_sysconfig |  | fid |
| 2 | idx_dfa_sysconfig_m01 |  | fcode |
