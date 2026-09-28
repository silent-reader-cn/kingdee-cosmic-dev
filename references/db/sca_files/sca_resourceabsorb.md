# 费用吸收成本单-sca_resourceabsorb

## 单据体-子表 t_sca_resourceabsorbentry

- **表名称：** 单据体-子表
- **表名：** t_sca_resourceabsorbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 8 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_resourceabsorbentry |  | fentryid |
| 2 | idx_sca_resourceabsorbentry |  | fid,felementid,fsubelementid |

---

## 费用吸收成本单-主表 t_sca_resourceabsorb

- **表名称：** 费用吸收成本单-主表
- **表名：** t_sca_resourceabsorb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | foutputbillno | 完工产量归集单 | varchar | 80 |  | √ | ' ' | 完工产量归集单 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fresourceuserow | 资源耗用量归集单行号 | int8 | 64 |  | √ | 0 | 资源耗用量归集单行号 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fopraid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 10 | fsourcetype | 源单类型 | varchar | 20 |  | √ | ' ' | 源单类型,枚举: R :资源耗用量归集单 F :完工产量归集单 |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 12 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 15 | fsourcebillentryid | 来源单据单据体ID | int8 | 64 |  | √ | 0 | 来源单据单据体ID |
| 16 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 20 | fvouchernum | 凭证字号 | varchar | 60 |  | √ | ' ' | 凭证字号 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fbizdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 23 | fresourceusebillno | 资源耗用量归集单 | varchar | 60 |  | √ | ' ' | 资源耗用量归集单 |
| 24 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 25 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 26 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 27 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 28 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_resourceabsorb |  | fid |
| 2 | idx_sca_resourceabsorb |  | forgid,fcostaccountid,fperiodid |
