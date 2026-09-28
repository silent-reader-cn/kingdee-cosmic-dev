# 成本取价配置-cal_pricescheme

## 单据体-多语言表 t_cal_priceschemeentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_cal_priceschemeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpriceremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_priceschemeel_id |  | fentryid,flocaleid |
| 2 | t_cal_priceschemeentry_l_pkey |  | fpkid |

---

## 单据体-子表 t_cal_priceschemeentry

- **表名称：** 单据体-子表
- **表名：** t_cal_priceschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdestprice | 适用对象成本价类别 | varchar | 2000 |  | √ | ' ' | 适用对象成本价类别,枚举: |
| 3 | fpriceremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fdestdisplay | 适用对象成本价类别 | varchar | 2000 |  | √ | ' ' | 适用对象成本价类别 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpricedisplay | 成本价类别 | varchar | 80 |  | √ | ' ' | 成本价类别 |
| 7 | fsrcprice | 成本价类别 | varchar | 2000 |  | √ | ' ' | 成本价类别,枚举: |
| 8 | fsrcdisplay | 单价类别 | varchar | 2000 |  | √ | ' ' | 单价类别 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpricesetting | 成本价 | varchar | 30 |  | √ | ' ' | 成本价,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_priceschemeentry_pkey |  | fentryid |
| 2 | idx_cal_priceschemee_id |  | fid |

---

## 成本取价配置-主表 t_cal_pricescheme

- **表名称：** 成本取价配置-主表
- **表名：** t_cal_pricescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fpriceobject | 取价用途 | bpchar | 1 |  | √ | ' ' | 取价用途,枚举: A :成本汇总维护取价 B :成本维护取价 C :单据同步取价 D :循环入库单取价 E :出库核算零成本取价 G :组织间交易取价 H :结存负单价取价 I :无源单出库退回取价 J :外部单据取成本价 K :返工领料取价 L :初始化数据录入取价 M :其他存货核算取价 O :套件权重维护取价 |
| 5 | fbillfilterdesc | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 6 | fentityobject | 适用对象 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fbillfilter_tag | 过滤条件（隐藏）_详情 | text | 0 |  |  | null | 过滤条件（隐藏）_详情 |
| 9 | fbillfilter | 过滤条件（隐藏） | varchar | 255 |  | √ | ' ' | 过滤条件（隐藏） |
| 10 | fpricedimension | 取价维度 | varchar | 100 |  | √ | ' ' | 取价维度,枚举: A :成本主体+物料 B :成本主体+物料+划分依据 C :成本主体+物料+划分依据+核算维度 |
| 11 | fpriceremark | fpriceremark | varchar | 255 |  | √ | ' ' |  |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_pricescheme_pkey |  | fid |
| 2 | idx_cal_pricescheme_num |  | fnumber |

---

## 成本取价配置-多语言表 t_cal_pricescheme_l

- **表名称：** 成本取价配置-多语言表
- **表名：** t_cal_pricescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_pricescheme_l_pkey |  | fpkid |
| 2 | idx_cal_priceschemel_id |  | fid,flocaleid |
