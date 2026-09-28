# 纳税期间-tctb_taxyear

## 单据体-子表 t_tctb_taxyear_entity

- **表名称：** 单据体-子表
- **表名：** t_tctb_taxyear_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartyear | 年 | varchar | 50 |  | √ | ' ' | 年,枚举: 0 :每年 1 :次年 |
| 3 | fendmonthandday | 月/日 | timestamp | 0 |  |  | null | 月/日 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmonthly | 月度 | varchar | 50 |  | √ | ' ' | 月度,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 |
| 6 | fhalfyear | 半年度 | varchar | 50 |  | √ | ' ' | 半年度,枚举: 0 :上半年 1 :下半年 |
| 7 | fstartmonthandday | 月/日 | timestamp | 0 |  |  | null | 月/日 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fquarter | 季度 | varchar | 50 |  | √ | ' ' | 季度,枚举: 1 :1 2 :2 3 :3 4 :4 |
| 10 | fendyear | 年 | varchar | 50 |  | √ | ' ' | 年,枚举: 0 :每年 1 :次年 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_taxyear_entity_fk |  | fid |
| 2 | pk_tctb_taxyear_entity |  | fentryid |

---

## 纳税期间-多语言表 t_tctb_taxyear_l

- **表名称：** 纳税期间-多语言表
- **表名：** t_tctb_taxyear_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_taxyear_l_0 |  | fid,flocaleid |
| 2 | pk_tctb_taxyear_l |  | fpkid |

---

## 纳税期间-主表 t_tctb_taxyear

- **表名称：** 纳税期间-主表
- **表名：** t_tctb_taxyear

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fapplicationscope | 适用范围 | varchar | 50 |  | √ | ' ' | 适用范围,枚举: 1 :全局适用 2 :局部适用 |
| 6 | fispreset | 系统预置 | varchar | 50 |  | √ | ' ' | 系统预置,枚举: 1 :是 0 :否 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 9 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fstartdate | 起始日 | timestamp | 0 |  |  | null | 起始日 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_taxyear_num |  | fnumber |
| 2 | pk_tctb_taxyear |  | fid |

---

## 单据体-子表 t_tctb_taxyear_orgentity

- **表名称：** 单据体-子表
- **表名：** t_tctb_taxyear_orgentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_taxyear_orgentity_fk |  | fid |
| 2 | pk_tctb_taxyear_orgentity |  | fentryid |
