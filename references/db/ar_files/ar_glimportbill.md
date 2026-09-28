# 按科目引入单据-ar_glimportbill

## 按科目引入单据-主表 t_ar_glimportbill

- **表名称：** 按科目引入单据-主表
- **表名：** t_ar_glimportbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 6 | fschemeid | 方案id | int8 | 64 |  | √ | 0 | [从总账引入初始数据方案 ar_glimportscheme](../ar_files/ar_glimportscheme.md) |
| 7 | fentitykey | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识,枚举: ar_busbill :期初暂估应收单 ar_finarbill :期初财务应收单 ar_receivedbill :期初预收单 ap_busbill :期初暂估应付单 ap_finapbill :期初财务应付单 ap_paidbill :期初预付单 |
| 8 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 9 | fappid | 应用 | varchar | 30 |  | √ | ' ' | 应用,枚举: ar :应收 ap :应付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_glimportbill |  | fid |
| 2 | idx_ar_glimptbill_org_account |  | forgid,faccountid |
| 3 | idx_ar_glimptbill_schemeid |  | fschemeid |
