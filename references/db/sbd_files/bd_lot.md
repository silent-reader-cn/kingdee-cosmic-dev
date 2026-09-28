# 批号主档-bd_lot

## 批号主档-多语言表 t_bd_lot_l

- **表名称：** 批号主档-多语言表
- **表名：** t_bd_lot_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  |  | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_lot_l_pkey |  | fpkid |
| 2 | idx_bd_lot_l_fid |  | fid,flocaleid |

---

## 批号主档-主表 t_bd_lot

- **表名称：** 批号主档-主表
- **表名：** t_bd_lot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsupplierlot | 供应商/自产批号 | varchar | 100 |  | √ | ' ' | 供应商/自产批号 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fproducedeptid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 12 | fmasterfiletypeid | 类型 | int8 | 64 |  | √ | '1401417099242528768' | 批号/序列号类型 bd_masterfile_type |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | flotstatus | 主档状态 | varchar | 5 |  | √ | 'A' | 主档状态,枚举: A :可用 B :不可用 |
| 19 | finstockdate | 首次入库日期 | timestamp | 0 |  |  | null | 首次入库日期 |
| 20 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 23 | fcustomerid | 受托加工客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_lot_number |  | fnumber |
| 2 | idx_bd_lot_unique |  | fnumber,fmasterfiletypeid,fmaterialid |
| 3 | idx_bd_lot_material |  | fmaterialid |
| 4 | t_bd_lot_pkey |  | fid |
