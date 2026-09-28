# 库存更新日志记录-scp_inventorylog_record

## 库存更新日志记录-主表 t_pur_inventorylog

- **表名称：** 库存更新日志记录-主表
- **表名：** t_pur_inventorylog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | foperation | 操作 | varchar | 100 |  | √ | ' ' | 操作 |
| 7 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_inventorylog_sup |  | fsupplierid,fmaterialid |
| 2 | idx_pur_inventorylog_org |  | forgid,fsupplierid,fmaterialid |
| 3 | pk_pur_inventorylog |  | fid |
