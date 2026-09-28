# 协议签订-pmm_protocol_bd

## 协议签订-主表 t_mal_protocol

- **表名称：** 协议签订-主表
- **表名：** t_mal_protocol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpricetype | fpricetype | bpchar | 1 |  | √ | ' ' |  |
| 3 | fgdctrate | fgdctrate | int8 | 64 |  | √ | 0 |  |
| 4 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 5 | fcfmorid | fcfmorid | int8 | 64 |  | √ | 0 |  |
| 6 | fsrcid | fsrcid | int8 | 64 |  | √ | 0 |  |
| 7 | floccurrid | floccurrid | int8 | 64 |  | √ | 0 |  |
| 8 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsrcbillbillno | 来源编号 | varchar | 80 |  | √ | ' ' | 来源编号 |
| 10 | fgendiscountrate | fgendiscountrate | varchar | 50 |  | √ | ' ' |  |
| 11 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 12 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 13 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 15 | fprotocolname | 协议名称 | varchar | 512 |  | √ | ' ' | 协议名称 |
| 16 | fissupgood | fissupgood | bpchar | 1 |  | √ | '0' |  |
| 17 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 18 | fissrm | fissrm | bpchar | 1 |  | √ | '0' |  |
| 19 | fpurmode | 采购模式 | bpchar | 1 |  | √ | ' ' | 采购模式,枚举: 1 :集团集采 2 :区域集采 3 :公司自采 |
| 20 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 21 | fbillno | 协议编号 | varchar | 80 |  | √ | ' ' | 协议编号 |
| 22 | fhandledeptid | fhandledeptid | int8 | 64 |  | √ | 0 |  |
| 23 | fcontinueprobillno | fcontinueprobillno | int8 | 64 |  | √ | 0 |  |
| 24 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 25 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 26 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fbillstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fisautosoldout | 协议失效后自动下架 | bpchar | 1 |  | √ | '0' | 协议失效后自动下架 |
| 29 | fprotocolstatus | 协议状态 | bpchar | 1 |  | √ | ' ' | 协议状态,枚举: A :未生效 B :生效中 C :已失效 D :已终止 E :已作废 |
| 30 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 31 | fpurratedate | fpurratedate | timestamp | 0 |  |  | null |  |
| 32 | fprotocolsigndate | fprotocolsigndate | timestamp | 0 |  |  | null |  |
| 33 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 34 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 35 | fautogenerategoods | fautogenerategoods | bpchar | 1 |  | √ | '0' |  |
| 36 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 37 | fhandlorid | fhandlorid | int8 | 64 |  | √ | 0 |  |
| 38 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :无需确认 B :待确认 C :已确认 D :已打回 |
| 40 | fexchangetype | fexchangetype | bpchar | 1 |  | √ | ' ' |  |
| 41 | fisdifferentarea | 分组织定价 | bpchar | 1 |  | √ | '0' | 分组织定价 |
| 42 | fexchrate | fexchrate | numeric | 19 | 6 | √ | 1 |  |
| 43 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 44 | fisgoodvisible | 商品全集团可见 | bpchar | 1 |  | √ | '0' | 商品全集团可见 |
| 45 | fpartyald | 甲方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 47 | fprosource | 协议来源 | bpchar | 1 |  | √ | ' ' | 协议来源,枚举: 1 :手工维护 2 :合同签订 3 :寻源定标 |
| 48 | fprotocolgroup | fprotocolgroup | bpchar | 1 |  | √ | ' ' |  |

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

## 子单据体-子表 t_mal_protocolladderprice

- **表名称：** 子单据体-子表
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

## 单据体-子表 t_mal_protocolentry

- **表名称：** 单据体-子表
- **表名：** t_mal_protocolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialgroup | fmaterialgroup | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | ftaxrate | numeric | 23 | 10 | √ | 0 |  |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 6 | fpriceinvaliddate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0 |  |
| 9 | fpurplanid | fpurplanid | int8 | 64 |  | √ | 0 |  |
| 10 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 12 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 13 | fminorderqty | 起订量 | numeric | 19 | 6 | √ | 0 | 起订量 |
| 14 | fabandonstatus | fabandonstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fentrypricetype | 价格类型 | bpchar | 1 |  | √ | 'A' | 价格类型,枚举: |
| 16 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 17 | fdctamount | fdctamount | numeric | 23 | 10 | √ | 0 |  |
| 18 | fleadtime | 供货周期（天） | int8 | 64 |  | √ | 0 | 供货周期（天） |
| 19 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 20 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 21 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0 |  |
| 23 | fdctrate | fdctrate | numeric | 23 | 10 | √ | 0 |  |
| 24 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 25 | fdiscounttype | fdiscounttype | varchar | 5 |  | √ | ' ' |  |
| 26 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 29 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 30 | fentrycomment | fentrycomment | varchar | 512 |  | √ | ' ' |  |
| 31 | fpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 32 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |

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
