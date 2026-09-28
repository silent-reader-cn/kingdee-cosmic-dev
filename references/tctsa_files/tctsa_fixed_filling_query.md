# 固定填报查询-tctsa_fixed_filling_query

## 固定填报查询-主表 t_tctsa_fix_filling_query

- **表名称：** 固定填报查询-主表
- **表名：** t_tctsa_fix_filling_query

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 填报组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | famount | 填报金额 | numeric | 23 | 10 | √ | 0.0000000000 | 填报金额 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fsxcontent | 填报文本 | varchar | 50 |  | √ | ' ' | 填报文本 |
| 10 | fskssqq | 填报所属期起 | timestamp | 0 |  |  | null | 填报所属期起 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdecimal | 填报数值 | numeric | 23 | 2 | √ | 0 | 填报数值 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fskssqz | 填报所属期止 | timestamp | 0 |  |  | null | 填报所属期止 |
| 15 | fgroup | 填报类型 | int8 | 64 |  | √ | 0 | 填报类型 tctsa_report_items_tree |
| 16 | fsbbid | 长整数(用于关联填报设置主键) | int8 | 64 |  | √ | 0 | 长整数(用于关联填报设置主键) |
| 17 | ftstatus | 填报状态 | varchar | 50 |  | √ | ' ' | 填报状态 |
| 18 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :模板引入 1 :系统生成 |
| 19 | fnumber | 事项编号 | varchar | 50 |  | √ | ' ' | 事项编号 |
| 20 | ffillperiod | 填报周期 | varchar | 50 |  | √ | ' ' | 填报周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |
| 21 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_fix_filling_query |  | forgid,fskssqq,fskssqz,ftaxtype |
| 2 | pk_tctsa_fix_filling_query |  | fid |

---

## 固定填报查询-多语言表 t_tctsa_fix_filling_query_l

- **表名称：** 固定填报查询-多语言表
- **表名：** t_tctsa_fix_filling_query_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 事项名称 | varchar | 50 |  | √ | ' ' | 事项名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_fix_filling_query_l |  | fid,flocaleid |
| 2 | pk_tctsa_fix_filling_query_l |  | fpkid |

---

## 标签-多选基础资料表 t_tctsa_fixed_duo_label

- **表名称：** 标签-多选基础资料表
- **表名：** t_tctsa_fixed_duo_label

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 标签 t_tctb_label_info |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_fixed_duo_label |  | fpkid |
| 2 | idx_tctsa_fixed_duo_label_fk |  | fid |
