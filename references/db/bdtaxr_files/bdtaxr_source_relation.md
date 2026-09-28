# 税源关联关系表-bdtaxr_source_relation

## 税源关联关系表-多语言表 t_bdtaxr_source_relation_l

- **表名称：** 税源关联关系表-多语言表
- **表名：** t_bdtaxr_source_relation_l

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
| 1 | idx_bdtaxr_source_relation_l_0 |  | fid,flocaleid |
| 2 | pk_bdtaxr_source_relation_l |  | fpkid |

---

## 税源关联关系表-主表 t_bdtaxr_source_relation

- **表名称：** 税源关联关系表-主表
- **表名：** t_bdtaxr_source_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplytemplates | 适用模板类型 | varchar | 50 |  | √ | ' ' | 适用模板类型,枚举: ccxws :财产行为税 latyj :土地增值税预缴税源 latwp :土地增值税尾盘税源 latqs :土地增值税清算税源 qtsf_tysbb :通用申报表（税及附征税费） qtsf_fsstysbb :非税收入通用申报表 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frelationtype | 关联类型 | varchar | 50 |  | √ | ' ' | 关联类型,枚举: master_slave :主从关系 mapping :映射关系 |
| 7 | fsource | 税源表 | varchar | 50 |  | √ | ' ' | 税源表 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fsourcetemp | 税源暂存表 | varchar | 50 |  | √ | ' ' | 税源暂存表 |
| 15 | fmappingfield | 映射字段 | varchar | 50 |  | √ | ' ' | 映射字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_source_relation |  | fid |
| 2 | idx_t_bd_sr_num |  | fnumber |
