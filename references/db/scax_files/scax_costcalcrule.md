# 卷算数据归集方案-scax_costcalcrule

## 优先级排序-子表 t_scax_costcalcrulesort

- **表名称：** 优先级排序-子表
- **表名：** t_scax_costcalcrulesort

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsortby | 来源字段 | varchar | 50 |  | √ | ' ' | 来源字段,枚举: 1 :审核时间 2 :修改时间 3 :同步时间 |
| 3 | fsort | 排序次序 | varchar | 50 |  | √ | ' ' | 排序次序,枚举: asc :升序 desc :降序 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costcalcrulesort |  | fentryid |
| 2 | idx_scax_costcalcrulesort |  | fid |

---

## 卷算数据归集方案-主表 t_scax_costcalcrule

- **表名称：** 卷算数据归集方案-主表
- **表名：** t_scax_costcalcrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusereadyhour | fusereadyhour | bpchar | 1 |  | √ | ' ' |  |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fuseyield | 考虑成品率 | bpchar | 1 |  | √ | ' ' | 考虑成品率 |
| 6 | flossformula | 损耗率计算公式 | varchar | 50 |  | √ | ' ' | 损耗率计算公式,枚举: 0 :不考虑 1 :子项标准用量 *（1 + 损耗率） 2 :子项标准用量 / (1 - 损耗率) |
| 7 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | frulefilter_tag | 过滤规则_详情 | text | 0 |  |  | null | 过滤规则_详情 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | frouterulefilter | 过滤规则 | varchar | 255 |  | √ | ' ' | 过滤规则 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | frulefilter | 过滤规则 | varchar | 255 |  | √ | ' ' | 过滤规则 |
| 13 | fcosttype | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcostaccount | 关联成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | froutesource | froutesource | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcostpriceplan | 取价方案 | int8 | 64 |  | √ | 0 | 取价方案 scax_costpriceplan |
| 19 | foutsourcepricerule | foutsourcepricerule | int8 | 64 |  | √ | 0 |  |
| 20 | fbomsource | BOM来源 | varchar | 50 |  | √ | ' ' | BOM来源,枚举: costbom :成本BOM |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fpurpricerule | fpurpricerule | int8 | 64 |  | √ | 0 |  |
| 24 | frouterulefilter_tag | 过滤规则_详情 | text | 0 |  |  | null | 过滤规则_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costcalcrule |  | fid |
| 2 | idx_scax_costcalcrule |  | fcosttype |
| 3 | idx_scax_costcalcrule_number |  | fbillno |

---

## 工艺路线优先级排序-子表 t_scax_calcruleroutesort

- **表名称：** 工艺路线优先级排序-子表
- **表名：** t_scax_calcruleroutesort

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsortby | 来源字段 | varchar | 50 |  | √ | ' ' | 来源字段,枚举: 1 :审核时间 2 :修改时间 3 :同步时间 |
| 3 | fsort | 排序次序 | varchar | 50 |  | √ | ' ' | 排序次序,枚举: asc :升序 desc :降序 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_costcalcruleroutesort |  | fid |
| 2 | pk_scax_calcruleroutesort |  | fentryid |

---

## 卷算数据归集方案-多语言表 t_scax_costcalcrule_l

- **表名称：** 卷算数据归集方案-多语言表
- **表名：** t_scax_costcalcrule_l

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
| 1 | idx_scax_costcalcrule_l |  | fid,flocaleid |
| 2 | pk_scax_costcalcrule_l |  | fpkid |
