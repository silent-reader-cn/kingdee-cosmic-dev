# 设备库存管理-bdm_equip_stock_manage

## 设备库存管理-主表 t_bdm_equip_stock_manage

- **表名称：** 设备库存管理-主表
- **表名：** t_bdm_equip_stock_manage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fequipmentno | 设备编号 | varchar | 50 |  | √ | ' ' | 设备编号 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | feinvoicestock | 电票库存 | int8 | 64 |  | √ | 0 | 电票库存 |
| 8 | finvoicestock | 普票库存 | int8 | 64 |  | √ | 0 | 普票库存 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fepname | 企业名称 | varchar | 50 |  | √ | ' ' | 企业名称 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fequipmenttype | 设备类型 | varchar | 50 |  | √ | ' ' | 设备类型,枚举: |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fespecialinvoicestock | 电专库存 | int8 | 64 |  | √ | 0 | 电专库存 |
| 15 | ftaxno | ftaxno | varchar | 50 |  | √ | ' ' |  |
| 16 | fspecialinvoicestock | 专票库存 | int8 | 64 |  | √ | 0 | 专票库存 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_equip_stock_manage |  | fequipmentno |
| 2 | pk_bdm_equip_stock_manage |  | fid |
