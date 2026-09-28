# 预留方案适用组织-msmod_scheme_orgentity

## 预留方案适用组织-主表 t_msmod_schorg

- **表名称：** 预留方案适用组织-主表
- **表名：** t_msmod_schorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 预留方案 | int8 | 64 |  | √ | 0 | [预留方案 msmod_reserve_scheme](../mscommon_files/msmod_reserve_scheme.md) |
| 2 | fisincludesuborg | 包含下级 | bpchar | 1 |  | √ | ' ' | 包含下级 |
| 3 | forgid | 适用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_schorg_fid |  | fid |
| 2 | pk_t_msmod_schorg |  | fentryid |
