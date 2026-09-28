# 采购计划协议F7-ssm_purschdorder_f7

## 采购计划协议F7-分表 t_ssm_purschdorder_s

- **表名称：** 采购计划协议F7-分表
- **表名：** t_ssm_purschdorder_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffullfillsupplieraddr | ffullfillsupplieraddr | varchar | 512 |  | √ | ' ' |  |
| 3 | faddress | faddress | varchar | 512 |  | √ | ' ' |  |
| 4 | ffullfillcontactid | ffullfillcontactid | int8 | 64 |  | √ | 0 |  |
| 5 | ffullfillsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 6 | fcontactid | fcontactid | int8 | 64 |  | √ | 0 |  |
| 7 | finvoicesupplierid | finvoicesupplierid | int8 | 64 |  | √ | 0 |  |
| 8 | freceivesupplierid | freceivesupplierid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ssm_purschdorder_s |  | fid |
| 2 | idx_t_purschdorder_s |  | ffullfillsupplierid |

---

## 采购计划协议F7-主表 t_ssm_purschdorder

- **表名称：** 采购计划协议F7-主表
- **表名：** t_ssm_purschdorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fshipsdp | fshipsdp | int8 | 64 |  | √ | 0 |  |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fconfirmstatus | fconfirmstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fexchangemethod | fexchangemethod | varchar | 50 |  | √ | ' ' |  |
| 7 | fschedweeks | fschedweeks | int8 | 64 |  | √ | 0 |  |
| 8 | fschedmonths | fschedmonths | int8 | 64 |  | √ | 0 |  |
| 9 | fpaymenttermid | fpaymenttermid | int8 | 64 |  | √ | 0 |  |
| 10 | fscheddays | fscheddays | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fchangestatus | fchangestatus | bpchar | 1 |  | √ | ' ' |  |
| 13 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0 |  |
| 14 | fenddate | 订单截止日期 | timestamp | 0 |  |  | null | 订单截止日期 |
| 15 | fpricelistid | fpricelistid | int8 | 64 |  |  | null |  |
| 16 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 17 | fsdpedigroup | fsdpedigroup | varchar | 8 |  | √ | ' ' |  |
| 18 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 19 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 20 | fincludetax | fincludetax | bpchar | 1 |  | √ | '1' |  |
| 21 | ffirmdays | ffirmdays | int8 | 64 |  | √ | 0 |  |
| 22 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 23 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 24 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 25 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 26 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 27 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 28 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 31 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 32 | fisinitbill | fisinitbill | bpchar | 1 |  | √ | '0' |  |
| 33 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 34 | fsafetydays | fsafetydays | int8 | 64 |  | √ | 0 |  |
| 35 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 36 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 37 | fsettlementmethodid | fsettlementmethodid | int8 | 64 |  | √ | 0 |  |
| 38 | fpaymode | fpaymode | varchar | 8 |  | √ | ' ' |  |
| 39 | fsubversion | fsubversion | varchar | 50 |  | √ | ' ' |  |
| 40 | fstartdate | 订单起始日期 | timestamp | 0 |  |  | null | 订单起始日期 |
| 41 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 42 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 43 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 44 | fprocureorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 46 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 47 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 48 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ssm_purschdorder_billno |  | fbillno,fid |
| 2 | pk_ssm_purschdorder |  | fid |
