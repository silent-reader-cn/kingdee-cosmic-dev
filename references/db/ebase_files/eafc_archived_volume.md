# 案卷保管清册关系表-eafc_archived_volume

## 案卷保管清册关系表-主表 t_eafc_archived_volume

- **表名称：** 案卷保管清册关系表-主表
- **表名：** t_eafc_archived_volume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | feafc_archived_uniqueid | 保管清册唯一id | varchar | 100 |  | √ | ' ' | 保管清册唯一id |
| 8 | feafc_volumeid | 案卷主键id | int8 | 64 |  | √ | 0 | 案卷主键id |
| 9 | fk_fpy_textfield | fk_fpy_textfield | varchar | 50 |  | √ | ' ' |  |
| 10 | feafc_archivedlistid | 保管清册主键id | int8 | 64 |  | √ | 0 | 保管清册主键id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | feafc_batch_num | 归档批次号 | varchar | 50 |  | √ | ' ' | 归档批次号 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_archived_list_id |  | feafc_archivedlistid |
| 2 | pk__eafc_archived_volume |  | fid |
| 3 | idx_eafc_archived_volume_id |  | feafc_volumeid |
