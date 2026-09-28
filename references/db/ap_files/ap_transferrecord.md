# 应付转销记录-ap_transferrecord

## 应付转销记录-主表 t_ap_transferrecord

- **表名称：** 应付转销记录-主表
- **表名：** t_ap_transferrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftransferdate | 转销日期 | timestamp | 0 |  |  | null | 转销日期 |
| 4 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 5 | fsettleamt | 本次核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销金额（本位币） |
| 6 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 7 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fexratetype | 汇率类型 | bpchar | 1 |  | √ | ' ' | 汇率类型,枚举: 0 :直接汇率 1 :间接汇率 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | ftransferuser | 转销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 ec_incomeapply :请款单 pm_purorderbill :采购订单 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 18 | fpricetaxloc | 应付金额（本位币） | numeric | 23 | 10 | √ | 0 | 应付金额（本位币） |
| 19 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fpurdept | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftraceid | 本次转销唯一标识 | varchar | 255 |  | √ | ' ' | 本次转销唯一标识 |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | funsettledlocamt | 未核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 未核销金额（本位币） |
| 26 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 27 | fsettledlocamt | 已核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 已核销金额（本位币） |
| 28 | ftransamount | 本次转销金额 | numeric | 23 | 10 | √ | 0 | 本次转销金额 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | ftransrecordtype | 转销记录类型 | varchar | 30 |  | √ | ' ' | 转销记录类型,枚举: srcbill :源单 redbill :红单 bluebill :蓝单 |
| 31 | ftransferbill | 转销单据 | varchar | 30 |  | √ | ' ' | 转销单据,枚举: ap_finapbill :财务应付单 cas_paybill :付款单 |
| 32 | fduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 33 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 35 | fpricetax | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 36 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 37 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 38 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 39 | ftransferno | 转销序号 | varchar | 30 |  | √ | ' ' | 转销序号 |
| 40 | fplanproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 41 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

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
