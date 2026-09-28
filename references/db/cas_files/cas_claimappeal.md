# 收款申诉单-cas_claimappeal

## 收款申诉单-主表 t_cas_claimbill

- **表名称：** 收款申诉单-主表
- **表名：** t_cas_claimbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foppunit | foppunit | varchar | 255 |  | √ | ' ' |  |
| 3 | fsourceid | fsourceid | varchar | 50 |  | √ | ' ' |  |
| 4 | fclaimtype | 类型 | varchar | 2 |  | √ | ' ' | 类型,枚举: 0 :认领 1 :变更 2 :申诉 3 :调整 4 :作废 |
| 5 | frecpayer | 付款人 | varchar | 255 |  | √ | ' ' | 付款人 |
| 6 | frecbilltype | 收款单单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdraftbillexpiredate | fdraftbillexpiredate | timestamp | 0 |  |  | null |  |
| 9 | frecviewpayee | frecviewpayee | varchar | 255 |  | √ | ' ' |  |
| 10 | fdrawername | fdrawername | varchar | 80 |  | √ | ' ' |  |
| 11 | fsourceclaimid | fsourceclaimid | int8 | 64 |  | √ | 0 |  |
| 12 | fdraftbilltypeid | fdraftbilltypeid | int8 | 64 |  | √ | 0 |  |
| 13 | foppbanknumber | foppbanknumber | varchar | 200 |  | √ | ' ' |  |
| 14 | fpaymentee | fpaymentee | varchar | 255 |  | √ | ' ' |  |
| 15 | fpaymenttype | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 other :其他 cas_othercontactunit :其他往来单位 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fisnoticemerge | fisnoticemerge | bpchar | 1 |  | √ | '0' |  |
| 19 | freamount | freamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 20 | frejectreason | frejectreason | varchar | 255 |  | √ | ' ' |  |
| 21 | fpayeetype | fpayeetype | varchar | 50 |  | √ | ' ' |  |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fclaimedamount | fclaimedamount | numeric | 23 | 10 | √ | 0 |  |
| 24 | frecviewpayer | frecviewpayer | varchar | 255 |  | √ | ' ' |  |
| 25 | funclaimamount | funclaimamount | numeric | 23 | 10 | √ | 0 |  |
| 26 | ftradetime | ftradetime | timestamp | 0 |  |  | null |  |
| 27 | fdatasource | fdatasource | varchar | 30 |  | √ | ' ' |  |
| 28 | frecpayee | frecpayee | varchar | 50 |  | √ | ' ' |  |
| 29 | fbankid | fbankid | int8 | 64 |  | √ | 0 |  |
| 30 | fnextauditor | fnextauditor | varchar | 50 |  | √ | ' ' |  |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | faccountbankid | faccountbankid | int8 | 64 |  | √ | 0 |  |
| 33 | fsinglestream | fsinglestream | bpchar | 1 |  | √ | '0' |  |
| 34 | frecpaytype | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 35 | ftradeid | ftradeid | varchar | 50 |  | √ | ' ' |  |
| 36 | fclaimno | fclaimno | varchar | 50 |  | √ | ' ' |  |
| 37 | foppbank | foppbank | varchar | 255 |  | √ | ' ' |  |
| 38 | fbusinesstype | fbusinesstype | varchar | 30 |  | √ | ' ' |  |
| 39 | fpayamount | fpayamount | numeric | 23 | 10 | √ | 0 |  |
| 40 | ffee | ffee | numeric | 23 | 10 | √ | 0 |  |
| 41 | fclaimamount | fclaimamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fpaybilltype | fpaybilltype | int8 | 64 |  | √ | 0 |  |
| 44 | fsourcetype | fsourcetype | varchar | 30 |  | √ | ' ' |  |
| 45 | fclaimstatus | fclaimstatus | varchar | 2 |  | √ | ' ' |  |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | ftradedetailno | ftradedetailno | varchar | 50 |  | √ | ' ' |  |
| 49 | ftradeno | ftradeno | varchar | 50 |  | √ | ' ' |  |
| 50 | fpaytype | fpaytype | int8 | 64 |  | √ | 0 |  |
| 51 | frecpayorg | frecpayorg | int8 | 64 |  | √ | 0 |  |
| 52 | fisconfireworkflow | fisconfireworkflow | varchar | 50 |  | √ | ' ' |  |
| 53 | fhandlestatus | fhandlestatus | varchar | 30 |  | √ | '0' |  |
| 54 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 55 | frecbasetype | frecbasetype | varchar | 50 |  | √ | ' ' |  |
| 56 | frecbasepayee | frecbasepayee | int8 | 64 |  | √ | 0 |  |
| 57 | fcenterorg | fcenterorg | int8 | 64 |  | √ | 0 |  |
| 58 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 59 | fbasepaymenttype | fbasepaymenttype | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_claimbill_cb |  | fbillstatus,fclaimno |
| 2 | t_cas_claimbill_pkey |  | fid |
| 3 | idx_cas_claimbill_bo |  | fbillno |
| 4 | idx_cas_claimbill_co |  | fclaimno |

---

## 单据体-子表 t_cas_claimdetailentry

- **表名称：** 单据体-子表
- **表名：** t_cas_claimdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsaleman | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | fconbillid | fconbillid | int8 | 64 |  | √ | 0 |  |
| 4 | fitemnameid | 款项名称 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 5 | fecorebillno | fecorebillno | varchar | 64 |  | √ | '' |  |
| 6 | fconbillentity | fconbillentity | varchar | 255 |  | √ | ' ' |  |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 10 | fconbillentryid | fconbillentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 13 | fcorebillno | 核心单据编号 | varchar | 30 |  | √ | ' ' | 核心单据编号 |
| 14 | fconbillrownum | fconbillrownum | varchar | 255 |  | √ | ' ' |  |
| 15 | fconbillnumber | fconbillnumber | varchar | 255 |  | √ | ' ' |  |
| 16 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 17 | fsettlecur | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fecorebillentryseq | fecorebillentryseq | int8 | 64 |  | √ | 0 |  |
| 19 | freceivableamount | 应收金额 | numeric | 19 | 6 | √ | 0.000000 | 应收金额 |
| 20 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: ar_finarbill :财务应收单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_paybill :付款单 fr_glreim_paybill :总账付款单 fr_glreim_recbill :总账收款单 |
| 21 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fpurdept | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 24 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 26 | fcontactunittype | 往来单位类型 | varchar | 80 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 27 | fcorebillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 28 | frectype | frectype | int8 | 64 |  | √ | 0 |  |
| 29 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 30 | fecorebilltype | fecorebilltype | varchar | 32 |  | √ | '' |  |
| 31 | factamt | 实收金额 | numeric | 19 | 6 | √ | 0.000000 | 实收金额 |
| 32 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 33 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 34 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fredisctamount | 折后金额折币别 | numeric | 19 | 6 | √ | 0 | 折后金额折币别 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fcorebillentryid | fcorebillentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_claimd_id |  | fid |
| 2 | t_cas_claimdetailentry_pkey |  | fentryid |
