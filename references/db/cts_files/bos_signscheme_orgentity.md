# 签名组织实体-bos_signscheme_orgentity

## 签名组织实体-主表 t_bd_signschemeorg

- **表名称：** 签名组织实体-主表
- **表名：** t_bd_signschemeorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 签名方案 | int8 | 64 |  | √ | 0 | [签名方案 sign_scheme](../cts_files/sign_scheme.md) |
| 2 | fisincludesuborg | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 3 | forgid | 签名组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fentryid | fentryid | varchar | 20 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_signschemeorg_id |  | fid |
| 2 | t_bd_signschemeorg_pkey |  | fentryid |
