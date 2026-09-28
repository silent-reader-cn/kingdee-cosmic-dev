# 费用吸收成本单-sco_resourceabsorb

## 单据体-子表 t_sco_resourceabsorbentry

- **表名称：** 单据体-子表
- **表名：** t_sco_resourceabsorbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 5 | fbaseworkhour | 基准单位 | varchar | 30 |  | √ | ' ' | 基准单位,枚举: 1 :时 2 :分 3 :秒 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fbaseqty | 基准单位数量 | numeric | 23 | 10 | √ | 0 | 基准单位数量 |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fbaseamount | 基准单位金额 | numeric | 23 | 10 | √ | 0 | 基准单位金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_resourceabsorbentry |  | fentryid |
| 2 | idx_sco_resourceabsorbentry |  | fid,felementid,fsubelementid |

---

## 费用吸收成本单-主表 t_sco_resourceabsorb

- **表名称：** 费用吸收成本单-主表
- **表名：** t_sco_resourceabsorb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | foutputbillno | 完工产量归集单 | varchar | 80 |  | √ | ' ' | 完工产量归集单 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fcalcbasis | 计算依据 | varchar | 10 |  | √ | ' ' | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fresourceuserow | 资源耗用量归集单行号 | int8 | 64 |  | √ | 0 | 资源耗用量归集单行号 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fopraid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 11 | fsourcetype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: R :资源耗用量归集单 F :完工产量归集单 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 sco_keycol |
| 14 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fsourcebillentryid | 来源单据单据体ID | int8 | 64 |  | √ | 0 | 来源单据单据体ID |
| 18 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 22 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fdescription | 工序说明 | varchar | 255 |  | √ | ' ' | 工序说明 |
| 25 | fbizdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 26 | fresourceusebillno | 资源耗用量归集单 | varchar | 80 |  | √ | ' ' | 资源耗用量归集单 |
| 27 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 29 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 31 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 32 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fkeycol | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_resourceabsorb |  | forgid,fcostaccountid,fperiodid |
| 2 | idx_sco_resourceabsorb_cb |  | fcostobjectid |
| 3 | idx_resourceabsorb_resid |  | fsourcebillid |
| 4 | pk_sco_resourceabsorb |  | fid |
| 5 | idx_sco_resourceabsorb_no |  | fbillno |
