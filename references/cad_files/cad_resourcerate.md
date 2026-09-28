# 资源标准费用价目表-cad_resourcerate

## 资源标准费用价目表-主表 t_cad_resourcerate

- **表名称：** 资源标准费用价目表-主表
- **表名：** t_cad_resourcerate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 5 | fcalcbasis | 计算依据 | varchar | 10 |  | √ | null | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 6 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fresourcetypeid | fresourcetypeid | varchar | 30 |  | √ | ' ' |  |
| 10 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 11 | fqty | 费率 | numeric | 23 | 10 | √ | 0.0000000000 | 费率 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fresourceunitid | 资源单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 17 | fworkhourunitid | fworkhourunitid | int8 | 64 |  | √ | 0 |  |
| 18 | fpreworkhourprice | fpreworkhourprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fdatasrc | 数据来源 | varchar | 30 |  | √ | 'manual' | 数据来源,枚举: manual :手工新增 contract :采购合同 order :采购订单 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 22 | fworkhourunit | fworkhourunit | varchar | 30 |  | √ | ' ' |  |
| 23 | fvalue | fvalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 25 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | frealworkhourprice | frealworkhourprice | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_resourcerate_df |  | fcosttypeid,fresourceid |
| 2 | t_cad_resourcerate_pkey |  | fid |

---

## 附加制造费用-子表 t_cad_resourcerateentry

- **表名称：** 附加制造费用-子表
- **表名：** t_cad_resourcerateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattaamt | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 3 | fattaqty | 标准费率 | numeric | 23 | 10 | √ | 0.0000000000 | 标准费率 |
| 4 | fattaeleid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 5 | fattasubeleid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_resourcerateentry |  | fid,fattasubeleid,fattaeleid |
| 2 | t_cad_resourcerateentry_pkey |  | fentryid |

---

## 资源标准费用价目表-多语言表 t_cad_resourcerate_l

- **表名称：** 资源标准费用价目表-多语言表
- **表名：** t_cad_resourcerate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_resourcerate_l_pkey |  | fpkid |
| 2 | index_cad_resourcerate_l_df |  | fid,flocaleid |
