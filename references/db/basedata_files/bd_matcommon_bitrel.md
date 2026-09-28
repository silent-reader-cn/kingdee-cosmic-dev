# 物料组织公共信息组织关系-bd_matcommon_bitrel

## 物料组织公共信息组织关系-主表 t_bd_matcommon_bitrel

- **表名称：** 物料组织公共信息组织关系-主表
- **表名：** t_bd_matcommon_bitrel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 3 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_matcommon_bitrel |  | fid |
| 2 | in_t_bd_matcommon_bitrel_ob |  | fuseorgid,fbitindex |
