# 应付转销记录-ap_transferrecord

## 应付转销记录-主表 t_ap_transferrecord

- **表名称：** 应付转销记录-主表
- **表名：** t_ap_transferrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftransferdate | 转销日期 | timestamp | 0 |  |  | null | 转销日期 |
| 4 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 5 | fsettleamt | 本次核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销金额（本位币） |
| 6 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fexratetype | 汇率类型 | bpchar | 1 |  | √ | ' ' | 汇率类型,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 13 | ftransferuser | 转销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 ec_incomeapply :请款单 pm_purorderbill :采购订单 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 17 | fpricetaxloc | 应付金额（本位币） | numeric | 23 | 10 | √ | 0 | 应付金额（本位币） |
| 18 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fpurdept | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | ftraceid | 本次转销唯一标识 | varchar | 255 |  | √ | ' ' | 本次转销唯一标识 |
| 22 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | funsettledlocamt | 未核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 未核销金额（本位币） |
| 25 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | fsettledlocamt | 已核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已核销金额（本位币） |
| 27 | ftransamount | 本次转销金额 | numeric | 23 | 10 | √ | 0 | 本次转销金额 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | ftransrecordtype | 转销记录类型 | varchar | 30 |  | √ | ' ' | 转销记录类型,枚举: srcbill :源单 redbill :红单 bluebill :蓝单 |
| 30 | ftransferbill | 转销单据 | varchar | 30 |  | √ | ' ' | 转销单据,枚举: finbill :财务应收 prerec :预收单 |
| 31 | fduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 32 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 34 | fpricetax | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 37 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 38 | ftransferno | 转销序号 | varchar | 30 |  | √ | ' ' | 转销序号 |
| 39 | fplanproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 40 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_transrecord_org |  | forgid |
| 2 | idx_ap_transrecord_transno |  | ftransferno |
| 3 | idx_ap_transrecord_traceid |  | ftraceid |
| 4 | idx_ap_transrecord_billno |  | fbillno |
| 5 | pk_t_ap_transferrecord |  | fid |
