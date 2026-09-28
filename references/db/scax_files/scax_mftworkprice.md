# 作业价格维护-scax_mftworkprice

## 作业价格维护-主表 t_scax_mftworkprice

- **表名称：** 作业价格维护-主表
- **表名：** t_scax_mftworkprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 8 | fdatasrc | 数据来源 | varchar | 25 |  | √ | ' ' | 数据来源,枚举: manual :手工新增 contract :采购合同 order :采购订单 costupdate :成本更新 |
| 9 | fworksplitid | 作业分割方案 | int8 | 64 |  | √ | 0 | 作业分割方案 scax_worksplit |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 15 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 16 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_mftworkprice |  | fid |
| 2 | idx_scax_mftworkprice |  | fbillno |

---

## 作业价格维护-多语言表 t_scax_mftworkprice_l

- **表名称：** 作业价格维护-多语言表
- **表名：** t_scax_mftworkprice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_mftworkprice_l |  | fpkid |
| 2 | idx_scax_mftworkprice_l |  | fid,flocaleid |

---

## 成本要素明细-子表 t_scax_mftworkpricedetail

- **表名称：** 成本要素明细-子表
- **表名：** t_scax_mftworkpricedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubbaseunitprice | 拆分费率基准单位转化费率 | numeric | 23 | 10 | √ | 0 | 拆分费率基准单位转化费率 |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | fsubweight | 子要素权重 | numeric | 23 | 10 | √ | 0 | 子要素权重 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fsubelementprice | 子要素拆分费率 | numeric | 23 | 10 | √ | 0 | 子要素拆分费率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_mftworkpricedetail |  | fentryid |
| 2 | pk_scax_mftworkpricedetail |  | fdetailid |

---

## 价格维护-子表 t_scax_mftworkpriceentry

- **表名称：** 价格维护-子表
- **表名：** t_scax_mftworkpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 权重 | numeric | 23 | 10 | √ | 0 | 权重 |
| 3 | fworktypeid | 作业类型 | int8 | 64 |  | √ | 0 | 作业类型 scax_worktype |
| 4 | fbaseunitnum | 基准单位分子 | numeric | 23 | 10 | √ | 0 | 基准单位分子 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseunitden | 基准单位分母 | numeric | 23 | 10 | √ | 0 | 基准单位分母 |
| 7 | fbaseunit | 基准单位 | varchar | 30 |  | √ | ' ' | 基准单位,枚举: 1 :时 2 :分 3 :秒 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fworksrc | 作业来源 | varchar | 30 |  | √ | ' ' | 作业来源,枚举: 0 :机器 1 :人工 |
| 10 | fprice | 标准费率 | numeric | 23 | 10 | √ | 0 | 标准费率 |
| 11 | funit | 价格单位 | varchar | 30 |  | √ | ' ' | 价格单位,枚举: 1 :时 2 :分 3 :秒 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_mftworkpriceentry |  | fentryid |
| 2 | idx_scax_mftworkpriceentry |  | fid |
