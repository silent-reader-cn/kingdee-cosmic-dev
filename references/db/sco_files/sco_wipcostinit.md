# 在制品成本初始化-sco_wipcostinit

## 实际单据体-子表 t_sco_wipcostinitentry

- **表名称：** 实际单据体-子表
- **表名：** t_sco_wipcostinitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstdamt | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | frealamt | 实际金额 | numeric | 23 | 10 | √ | 0 | 实际金额 |
| 5 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 8 | fsubbomversionid | 子物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 9 | fstdcost | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 10 | fsubmatid | 子物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 11 | fcalcbasis | 计算依据 | varchar | 30 |  | √ | ' ' | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 12 | fcostlevel | 工费级别 | varchar | 30 |  | √ | ' ' | 工费级别,枚举: 2 :本阶 3 :下阶 |
| 13 | fstdprice | 标准单价 | numeric | 23 | 10 | √ | 0 | 标准单价 |
| 14 | fstdqty | 标准用量 | numeric | 23 | 10 | √ | 0 | 标准用量 |
| 15 | frealqty | 实际用量 | numeric | 23 | 10 | √ | 0 | 实际用量 |
| 16 | fdiffamt | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fsubauxptyid | 子物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: 1 :综合 2 :分项 3 :制造费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_wipcostinitentry |  | felementid,fsubelementid |
| 2 | idx_sco_wipcostinitentry2 |  | fid |
| 3 | pk_sco_wipcostinitentry |  | fentryid |

---

## 在制品成本初始化-主表 t_sco_wipcostinit

- **表名称：** 在制品成本初始化-主表
- **表名：** t_sco_wipcostinit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fmaterialid | 所属产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fautocalc | 是否自动计算 | bpchar | 1 |  | √ | '1' | 是否自动计算 |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | finitamt | 实际期初在产品金额 | numeric | 23 | 10 | √ | 0 | 实际期初在产品金额 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | finitqty | 期初在产品数量 | numeric | 23 | 10 | √ | 0 | 期初在产品数量 |
| 17 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | ftotaldiffamt | 总差异 | numeric | 23 | 10 | √ | 0 | 总差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_wipcostinit |  | fid |
| 2 | idx_sco_wipcostinit |  | forgid,fcostcenterid,fcostobjectid |

---

## 在制品成本初始化-多语言表 t_sco_wipcostinit_l

- **表名称：** 在制品成本初始化-多语言表
- **表名：** t_sco_wipcostinit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_wipcostinit_l |  | fpkid |
| 2 | idx_sco_wipcostinit_l |  | fid,flocaleid |
