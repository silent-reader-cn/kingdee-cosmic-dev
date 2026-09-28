# 参标类型(后台元数据)-src_member_biztype

## 参标类型(后台元数据)-主表 t_src_referencetype

- **表名称：** 参标类型(后台元数据)-主表
- **表名：** t_src_referencetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | 参标类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 |  |
| 3 | fentryid | 我的任务 | int8 | 64 |  | √ | 0 | [我的任务 src_memberclarify](../src_files/src_memberclarify.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_referencetype |  | fpkid |
| 2 | idx_src_reftype_bid |  | fbasedataid |
| 3 | idx_src_reftype_eid |  | fentryid |
