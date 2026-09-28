# 协议查询-ent_protocol

## 适用组织范围-子表 t_mal_protocolorgentry

- **表名称：** 适用组织范围-子表
- **表名：** t_mal_protocolorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryorgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_protocolorgentry |  | fentryid |
| 2 | idx_t_mal_proentry_fentryid |  | fid,fentryid |

---

## 协议查询-主表 t_mal_protocol

- **表名称：** 协议查询-主表
- **表名：** t_mal_protocol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpricetype | 价格类型 | bpchar | 1 |  | √ | ' ' | 价格类型,枚举: 1 :固定价 2 :折扣 |
| 3 | fgdctrate | 通用折扣率 | int8 | 64 |  | √ | 0 | 通用折扣率 |
| 4 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | fcfmorid | 供方确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fsrcid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 7 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | forgid | 签约单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsrcbillbillno | 来源编号 | varchar | 80 |  | √ | ' ' | 来源编号 |
| 10 | fgendiscountrate | fgendiscountrate | varchar | 50 |  | √ | ' ' |  |
| 11 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | fcfmdate | 供方确认日期 | timestamp | 0 |  |  | null | 供方确认日期 |
| 13 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fprotocolname | 协议名称 | varchar | 512 |  | √ | ' ' | 协议名称 |
| 16 | fissupgood | 供应商维护商品 | bpchar | 1 |  | √ | '0' | 供应商维护商品 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fissrm | 启用供应商协同 | bpchar | 1 |  | √ | '0' | 启用供应商协同 |
| 19 | fpurmode | 采购模式 | bpchar | 1 |  | √ | ' ' | 采购模式,枚举: 1 :集团集采 2 :区域集采 3 :公司自采 |
| 20 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 21 | fbillno | 协议编号 | varchar | 80 |  | √ | ' ' | 协议编号 |
| 22 | fhandledeptid | 经办部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fcontinueprobillno | fcontinueprobillno | int8 | 64 |  | √ | 0 |  |
| 24 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fisautosoldout | 协议失效后自动下架 | bpchar | 1 |  | √ | '0' | 协议失效后自动下架 |
| 29 | fprotocolstatus | 协议状态 | bpchar | 1 |  | √ | ' ' | 协议状态,枚举: A :未生效 B :生效中 C :已失效 D :已终止 E :已作废 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fpurratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 32 | fprotocolsigndate | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 35 | fautogenerategoods | fautogenerategoods | bpchar | 1 |  | √ | '0' |  |
| 36 | fsupplierid | 乙方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 37 | fhandlorid | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 39 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :无需确认 B :待确认 C :已确认 D :已打回 |
| 40 | fexchangetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 41 | fisdifferentarea | 分组织定价 | bpchar | 1 |  | √ | '0' | 分组织定价 |
| 42 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1 | 汇率 |
| 43 | fsrcbilltype | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 44 | fisgoodvisible | 商品全集团可见 | bpchar | 1 |  | √ | '0' | 商品全集团可见 |
| 45 | fpartyald | 甲方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fprosource | 协议来源 | bpchar | 1 |  | √ | ' ' | 协议来源,枚举: 1 :手工维护 2 :合同签订 3 :寻源定标 |
| 48 | fprotocolgroup | 协议分类 | bpchar | 1 |  | √ | ' ' | 协议分类,枚举: 1 :自有供应商协议 2 :电商协议 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_protocol_fbizpartnerid |  | fbizpartnerid |
| 2 | idx_mal_protocol_fbillno |  | fbillno |
| 3 | idx_mal_protocol_forg |  | forgid |
| 4 | pk_t_mal_protocol |  | fid |

---

## 阶梯价-子表 t_mal_protocolladderprice

- **表名称：** 阶梯价-子表
- **表名：** t_mal_protocolladderprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fladprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |
| 2 | fqtyto | 数量至（<） | numeric | 19 | 6 | √ | 0 | 数量至（<） |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fqtyfrom | 数量从 | numeric | 19 | 6 | √ | 0 | 数量从 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_protocolladderprice |  | fdetailid |
| 2 | idx_mal_prolad_fentryid_fseq |  | fentryid,fseq |

---

## 协议清单-子表 t_mal_protocolentry

- **表名称：** 协议清单-子表
- **表名：** t_mal_protocolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialgroup | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fpriceinvaliddate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 9 | fpurplanid | 采买方案 | int8 | 64 |  | √ | 0 | [采买方案 pmm_purchaseplan](../pmm_files/pmm_purchaseplan.md) |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 13 | fminorderqty | 起订量 | numeric | 19 | 6 | √ | 0 | 起订量 |
| 14 | fabandonstatus | 作废状态 | bpchar | 1 |  | √ | ' ' | 作废状态,枚举: A :已作废 |
| 15 | fentrypricetype | 价格类型 | bpchar | 1 |  | √ | 'A' | 价格类型,枚举: A :固定价 B :阶梯价 |
| 16 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 18 | fleadtime | 供货周期（天） | int8 | 64 |  | √ | 0 | 供货周期（天） |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 21 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 22 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 23 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 24 | fpurorgid | 采买组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 26 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 29 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 30 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 31 | fpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 32 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_protocolentry_matid |  | fmaterialid |
| 2 | pk_t_mal_protocolentry |  | fentryid |
| 3 | idx_mal_protocolentry_id |  | fid |

---

## 协议查询-多语言表 t_mal_protocol_l

- **表名称：** 协议查询-多语言表
- **表名：** t_mal_protocol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fprotocolname | 协议名称 | varchar | 512 |  | √ | ' ' | 协议名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_pro_l_flocaleid |  | fid,flocaleid |
| 2 | pk_t_mal_protocol_l |  | fpkid |
