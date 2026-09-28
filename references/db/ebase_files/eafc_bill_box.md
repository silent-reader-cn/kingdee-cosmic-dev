# 文件盒子关系表-eafc_bill_box

## 文件盒子关系表-主表 tk_eafc_bill_box

- **表名称：** 文件盒子关系表-主表
- **表名：** tk_eafc_bill_box

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_box_name | 盒子题名 | varchar | 500 |  | √ | ' ' | 盒子题名 |
| 3 | fk_fpy_box_user | 装盒人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fk_fpy_box_date | 装盒日期 | timestamp | 0 |  |  | null | 装盒日期 |
| 5 | fk_eafc_boxid | 盒子id | int8 | 64 |  | √ | 0 | 盒子id |
| 6 | fk_eafc_updatetime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fk_eafc_bill_uniid | 文件唯一编码 | varchar | 50 |  | √ | ' ' | 文件唯一编码 |
| 8 | fk_eafc_box_serialno | 盒内序号 | int4 | 32 |  | √ | 0 | 盒内序号 |
| 9 | fk_fpy_box_serial | 装盒时间 | int8 | 64 |  | √ | 0 | 装盒时间 |
| 10 | fk_eafc_billid | 文件主键id | int8 | 64 |  | √ | 0 | 文件主键id |
| 11 | fk_eafc_createtime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fk_eafc_shelf_location_ob | 上架位置 | int8 | 64 |  | √ | 0 | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 13 | fk_eafc_box_num | 盒号 | varchar | 500 |  | √ | ' ' | 盒号 |
| 14 | fk_eafc_business | 分类 | int8 | 64 |  | √ | 0 | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_bill_box_fk_boxid |  | fk_eafc_boxid |
| 2 | pk_eafc_bill_box |  | fid |
| 3 | idx__eafc_bill_box_fk_billid |  | fk_eafc_billid |
