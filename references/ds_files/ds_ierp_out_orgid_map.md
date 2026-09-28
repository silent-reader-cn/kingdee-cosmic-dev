# 苍穹与外部组织ID映射-ds_ierp_out_orgid_map

## 苍穹与外部组织ID映射-主表 t_ds_ierp_out_orgid_map

- **表名称：** 苍穹与外部组织ID映射-主表
- **表名：** t_ds_ierp_out_orgid_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferpparentid | 苍穹组织上级ID | int8 | 64 |  | √ | 0 | 苍穹组织上级ID |
| 3 | fdingparentid | 钉钉组织上级ID | int8 | 64 |  | √ | 0 | 钉钉组织上级ID |
| 4 | fdingid | 钉钉组织ID | int8 | 64 |  | √ | 0 | 钉钉组织ID |
| 5 | ferpid | 苍穹组织ID | int8 | 64 |  | √ | 0 | 苍穹组织ID |
| 6 | ferpnumber | 苍穹组织编码 | varchar | 100 |  | √ | ' ' | 苍穹组织编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ds_ierp_out_orgid_map |  | fdingid |
| 2 | pk_t_ds_ierp_out_orgid_map |  | fid |
