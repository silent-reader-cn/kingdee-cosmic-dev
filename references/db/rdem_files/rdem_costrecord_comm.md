# 研发公共费用归集单-rdem_costrecord_comm

## 研发公共费用归集单-主表 t_pca_costrec_comm

- **表名称：** 研发公共费用归集单-主表
- **表名：** t_pca_costrec_comm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fdatacreatetype | 数据创建方式 | varchar | 50 |  | √ | ' ' | 数据创建方式,枚举: 0 :手工新增 1 :自动归集 2 :OpenAPI导入 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrcbillid | 来源主单据内码 | int8 | 64 |  | √ | 0 | 来源主单据内码 |
| 8 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcollplanid | 成本来源设置 | int8 | 64 |  | √ | 0 | 成本来源设置 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fsrcbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsrcsystype | 来源业务系统 | varchar | 50 |  | √ | ' ' | 来源业务系统,枚举: 1 :总账 7 :异构系统 |
| 15 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 16 | fisreverse | 冲销凭证 | bpchar | 1 |  | √ | '0' | 冲销凭证 |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsrcbilltypeid | 业务单据类型 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costrec_comm_calorg |  | fcalorgid |
| 2 | idx_pca_costrec_comm_bno |  | fbillno |
| 3 | idx_pca_costrec_comm_account |  | fcostaccountid,fperiodid |
| 4 | pk_pca_costrec_comm |  | fid |

---

## 业务单据明细信息-子表 t_pca_costrec_comm_bill

- **表名称：** 业务单据明细信息-子表
- **表名：** t_pca_costrec_comm_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fallocstatus | 分摊状态 | varchar | 50 |  | √ | ' ' | 分摊状态,枚举: 0 :未分摊 1 :已分摊 2 :分摊中 |
| 4 | fassgrpid | 核算维度值 | int8 | 64 |  | √ | 0 | null 002 |
| 5 | fsrcbillid | 来源单据(体or子体)内码 | int8 | 64 |  | √ | 0 | 来源单据(体or子体)内码 |
| 6 | fcollplanentryid | 来源配置分录id | int8 | 64 |  | √ | 0 | 来源配置分录id |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | ftotalcost | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 10 | faccountviewid | 会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 11 | fsrcbilldate | fsrcbilldate | timestamp | 0 |  |  | null |  |
| 12 | fsrcbillentryseq | 来源单据体序号 | int4 | 32 |  | √ | 0 | 来源单据体序号 |
| 13 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | forigamount | 原始金额 | numeric | 23 | 10 | √ | 0 | 原始金额 |
| 16 | falloctime | 分摊时间 | timestamp | 0 |  |  | null | 分摊时间 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | facctviewbaltype | 金额类型 | varchar | 50 |  | √ | ' ' | 金额类型,枚举: 1 :实际损益发生额 2 :借方 3 :贷方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costrec_comm_bill_accountview |  | faccountviewid,fconvsubelementid |
| 2 | pk_pca_costrec_comm_bill |  | fentryid |
| 3 | idx_pca_costrec_comm_bill_fid |  | fid,fseq |
