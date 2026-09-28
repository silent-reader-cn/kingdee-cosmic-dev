# 归档组织映射-fpy_syset_orgmapp_bill

## 单据体-子表 tk_fpy_syset_orgmapp_ent

- **表名称：** 单据体-子表
- **表名：** tk_fpy_syset_orgmapp_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  |  | null |  |
| 4 | fk_fpy_mappingtype | 映射方式 | varchar | 50 |  | √ | ' ' | 映射方式,枚举: number :编码 |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fk_fpy_taraccountid | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fk_fpy_srcorgname | 来源组织名称 | varchar | 50 |  | √ | ' ' | 来源组织名称 |
| 9 | fk_fpy_tarorgid | 归档组织编码 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 10 | fk_fpy_srcaccountnum | 来源机构/问题编码 | varchar | 50 |  | √ | ' ' | 来源机构/问题编码 |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态 |
| 14 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | fcreatorid | int8 | 64 |  |  | null |  |
| 16 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态 |
| 18 | fnumber | 来源组织编码 | varchar | 30 |  | √ | ' ' | 来源组织编码 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_syset_orgmapp_ent |  | fentryid |

---

## 归档组织映射-主表 tk_fpy_syset_orgmapp

- **表名称：** 归档组织映射-主表
- **表名：** tk_fpy_syset_orgmapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 8 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_syset_orgmapp |  | fid |
