# 弥补以前年度亏损台账-tccit_mbyqks_acc

## 弥补以前年度亏损台账-主表 t_tccit_mbyqks_acc

- **表名称：** 弥补以前年度亏损台账-主表
- **表名：** t_tccit_mbyqks_acc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fksdqnd | 亏损到期年度 | timestamp | 0 |  |  | null | 亏损到期年度 |
| 5 | fjydmbje | 结余待弥补金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结余待弥补金额 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fhappenyear | 亏损发生年度 | timestamp | 0 |  |  | null | 亏损发生年度 |
| 8 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fyjjznx | 预计结转年限（年） | int8 | 64 |  | √ | 0 | 预计结转年限（年） |
| 12 | fljmbzcksje | 累计弥补、转出亏损金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计弥补、转出亏损金额 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | flossmoney | 亏损金额 | numeric | 23 | 10 | √ | 0.0000000000 | 亏损金额 |
| 16 | flossqiyetype | 亏损企业类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 17 | flosstype | 亏损类型 | varchar | 50 |  | √ | ' ' | 亏损类型,枚举: jnsd :境内所得额亏损 zr :合并、分立转入亏损额 |
| 18 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_mbyqks_acc |  | fbillno |
| 2 | pk_tccit_mbyqks_acc |  | fid |

---

## 单据体-子表 t_tccit_mbyqks_entry

- **表名称：** 单据体-子表
- **表名：** t_tccit_mbyqks_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmbnd | 弥补年度 | timestamp | 0 |  |  | null | 弥补年度 |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmbkslx | 弥补亏损类型 | varchar | 50 |  | √ | ' ' | 弥补亏损类型,枚举: mbks :弥补亏损 flzc :分立转出 |
| 6 | fmbzcksje | 弥补、转出亏损金额 | numeric | 23 | 10 | √ | 0.0000000000 | 弥补、转出亏损金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_mbyqks_entry |  | fentryid |
| 2 | idx_tccit_mbyqks_entry_fk |  | fid |
