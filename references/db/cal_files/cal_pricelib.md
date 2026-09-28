# 成本价类别-cal_pricelib

## 成本价类别-主表 t_cal_pricelib

- **表名称：** 成本价类别-主表
- **表名：** t_cal_pricelib

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_pricelib_pkey |  | fid |
| 2 | idx_cal_pricelib_num |  | fnumber |

---

## 单据体-子表 t_cal_pricelibentry

- **表名称：** 单据体-子表
- **表名：** t_cal_pricelibentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricedesc | 取值公式描述 | varchar | 255 |  | √ | ' ' | 取值公式描述 |
| 3 | fpriceexp | 金额取值公式 | varchar | 255 |  | √ | ' ' | 金额取值公式 |
| 4 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentityobject | 业务对象 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 8 | fpricetranexpr | 取值公式 | varchar | 255 |  | √ | ' ' | 取值公式 |
| 9 | fpricename | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 10 | fpriceexp_tag | 金额取值公式_详情 | text | 0 |  |  | null | 金额取值公式_详情 |
| 11 | fisdetail | 是否取明细 | bpchar | 1 |  | √ | '0' | 是否取明细 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fpricenum | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_pricelibe_id |  | fid |
| 2 | t_cal_pricelibentry_pkey |  | fentryid |

---

## 单据体-多语言表 t_cal_pricelibentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_cal_pricelibentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpricename | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
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
| 1 | pk_cal_pricelibentry_l |  | fpkid |
| 2 | idx_cal_pricelibentry_l |  | fentryid,flocaleid |
