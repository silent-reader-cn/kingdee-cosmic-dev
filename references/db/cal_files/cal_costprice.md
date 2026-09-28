# 成本取价来源设置-cal_costprice

## 成本价-多语言表 t_cal_costpriceentry_l

- **表名称：** 成本价-多语言表
- **表名：** t_cal_costpriceentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | fpricename | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costprceel_eid |  | fentryid,flocaleid |
| 2 | t_cal_costpriceentry_l_pkey |  | fpkid |

---

## 成本取价来源设置-主表 t_cal_costprice

- **表名称：** 成本取价来源设置-主表
- **表名：** t_cal_costprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 4 | fpricelib | 成本价类别设置 | varchar | 80 |  | √ | ' ' | 成本价类别设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costprice_num |  | fnumber |
| 2 | t_cal_costprice_pkey |  | fid |

---

## 成本价-子表 t_cal_costpriceentry

- **表名称：** 成本价-子表
- **表名：** t_cal_costpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprices | 成本价 | varchar | 255 |  | √ | ' ' | 成本价,枚举: |
| 3 | fbillfilterdesc | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 4 | fcostpricelib | 成本价类别 | varchar | 2000 |  | √ | ' ' | 成本价类别,枚举: |
| 5 | fpriceexp | fpriceexp | varchar | 255 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentityobject | 业务对象 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设,枚举: 1 : 0 : |
| 9 | fpricetranexpr | fpricetranexpr | varchar | 255 |  | √ | ' ' |  |
| 10 | fbillfilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 11 | fhascurrentperiod | 追溯是否包含当期 | bpchar | 1 |  | √ | ' ' | 追溯是否包含当期,枚举: 1 :是 0 :否 |
| 12 | fbillfilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 13 | ftype | 取价方式 | varchar | 10 |  | √ | ' ' | 取价方式,枚举: A :最新 B :加权 C :出库单据同步 |
| 14 | fpricename | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fbeforeperiod | 取价追溯期间 | int8 | 64 |  | √ | 0 | 取价追溯期间 |
| 16 | fenable | 单据状态 | bpchar | 1 |  | √ | '1' | 单据状态,枚举: 0 :禁用 1 :可用 |
| 17 | fpriceplugin | 取价插件 | int8 | 64 |  | √ | 0 | 核算预置插件 cal_plugin |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fpricenum | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costpricee_id |  | fid |
| 2 | t_cal_costpriceentry_pkey |  | fentryid |
