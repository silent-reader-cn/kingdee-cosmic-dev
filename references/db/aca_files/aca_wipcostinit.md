# 初始化在产品成本-aca_wipcostinit

## 初始化在产品成本-主表 t_aca_wipcostinit

- **表名称：** 初始化在产品成本-主表
- **表名：** t_aca_wipcostinit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fassignedproductid | 所属产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | finitamt | 期初在产品金额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初在产品金额 |
| 12 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fyearinputqty | 本年累计投入数量 | numeric | 23 | 10 | √ | 0 | 本年累计投入数量 |
| 14 | fsource | 数据来源 | varchar | 30 |  | √ | '0' | 数据来源,枚举: manual :手工新增 import :数据导入 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 18 | finitqty | 期初在产品数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初在产品数量 |
| 19 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 20 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fyearfinishqty | 本年累计完工数量 | numeric | 23 | 10 | √ | 0 | 本年累计完工数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_wipcostinit |  | fid |
| 2 | idx_awipcosti_costa |  | fcostaccountid |
| 3 | idx_aca_wipcostinit |  | forgid,fcostcenterid |
| 4 | idx_awipcosti_costobj |  | fcostobjectid |
| 5 | idx_awipcosti_costc |  | fcostcenterid |

---

## 子项物料信息-子表 t_aca_wipcostinitsubentry

- **表名称：** 子项物料信息-子表
- **表名：** t_aca_wipcostinitsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmatyearfinishqty | 本年累计完工数量 | numeric | 23 | 10 | √ | 0 | 本年累计完工数量 |
| 2 | fmatyearinputqty | 本年累计投入数量 | numeric | 23 | 10 | √ | 0 | 本年累计投入数量 |
| 3 | fauxptyid | 子项物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsubqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 6 | fmatversionid | 子项物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 7 | fmatyearfinishamt | 本年累计完工金额 | numeric | 23 | 10 | √ | 0 | 本年累计完工金额 |
| 8 | fsubbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fsubamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 10 | fmatyearinputamt | 本年累计投入金额 | numeric | 23 | 10 | √ | 0 | 本年累计投入金额 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fsubmaterielid | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_wipcostinitsubentry |  | fsubmaterielid,fsubamount |
| 2 | idx_aca_wipcostinitsuben_fentryid |  | fentryid |
| 3 | pk_t_aca_wipcostinitsubentry |  | fdetailid |

---

## 成本信息-子表 t_aca_wipcostinitentry

- **表名称：** 成本信息-子表
- **表名：** t_aca_wipcostinitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fyearinputamt | 本年累计投入金额 | numeric | 23 | 10 | √ | 0 | 本年累计投入金额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 7 | fyearfinishamt | 本年累计完工金额 | numeric | 23 | 10 | √ | 0 | 本年累计完工金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fimporttype | 引入类型 | varchar | 30 |  | √ | '0' | 引入类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_wipcostinitentry |  | fid,fsubelementid |
| 2 | pk_t_aca_wipcostinitentry |  | fentryid |
| 3 | idx_awipcoien_sube |  | fsubelementid |

---

## 初始化在产品成本-多语言表 t_aca_wipcostinit_l

- **表名称：** 初始化在产品成本-多语言表
- **表名：** t_aca_wipcostinit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_wipcostinit_l |  | fpkid |
| 2 | idx_aca_wipcostinit_l |  | fid,flocaleid |
