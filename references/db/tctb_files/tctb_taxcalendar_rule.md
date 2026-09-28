# 税务日历规则-tctb_taxcalendar_rule

## 税务日历规则-多语言表 t_tctb_taxcalendar_rule_l

- **表名称：** 税务日历规则-多语言表
- **表名：** t_tctb_taxcalendar_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_taxcalendar_rule_l_0 |  | fid,flocaleid |
| 2 | pk_tctb_taxcalendar_rule_l |  | fpkid |

---

## 税务日历规则-主表 t_tctb_taxcalendar_rule

- **表名称：** 税务日历规则-主表
- **表名：** t_tctb_taxcalendar_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 5 | fsbjzrnssdlx | 申报截止日纳税时点类型 | varchar | 50 |  | √ | ' ' | 申报截止日纳税时点类型,枚举: beforeendday :终了日前 afterendday :终了日后 endday :终了日 |
| 6 | fsbjzry | 申报截止日_月 | int8 | 64 |  | √ | 0 | 申报截止日_月 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsbjzrt | 申报截止日_天 | int8 | 64 |  | √ | 0 | 申报截止日_天 |
| 9 | ftaxareagroupid | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 10 | fjkjzrnssdlx | 缴款截止日纳税时点类型 | varchar | 50 |  | √ | ' ' | 缴款截止日纳税时点类型,枚举: beforeendday :终了日前 afterendday :终了日后 endday :终了日 |
| 11 | fjkjzrt | 缴款截止日_天 | int8 | 64 |  | √ | 0 | 缴款截止日_天 |
| 12 | fjkjzry | 缴款截止日_月 | int8 | 64 |  | √ | 0 | 缴款截止日_月 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | ftaxcycle | 纳税周期 | varchar | 50 |  | √ | ' ' | 纳税周期,枚举: month :月报 season :季报 halfyear :半年报 year :年报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_taxcalendar_rule |  | fid |
| 2 | idx_caltendar_r_01 |  | fnumber |
