# 固定填报查询-tctsa_fixed_filling_query

## 固定填报查询-主表 t_tctsa_fix_filling_query

- **表名称：** 固定填报查询-主表
- **表名：** t_tctsa_fix_filling_query

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fworkflowno | 当前审批编号 | varchar | 300 |  | √ | ' ' | 当前审批编号 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 填报组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | famount | 填报金额 | numeric | 23 | 10 | √ | 0.0000000000 | 填报金额 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fsxcontent | 填报文本 | varchar | 50 |  | √ | ' ' | 填报文本 |
| 11 | fskssqq | 填报所属期起 | timestamp | 0 |  |  | null | 填报所属期起 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fdecimal | 填报数值 | numeric | 23 | 2 | √ | 0 | 填报数值 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fskssqz | 填报所属期止 | timestamp | 0 |  |  | null | 填报所属期止 |
| 16 | fgroup | 填报类型 | int8 | 64 |  | √ | 0 | [填报类型 tctsa_report_items_tree](../tctsa_files/tctsa_report_items_tree.md) |
| 17 | fsbbid | 长整数(用于关联填报设置主键) | int8 | 64 |  | √ | 0 | 长整数(用于关联填报设置主键) |
| 18 | ftstatus | 填报状态 | varchar | 50 |  | √ | ' ' | 填报状态 |
| 19 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :模板引入 1 :系统生成 |
| 20 | fnumber | 事项编号 | varchar | 50 |  | √ | ' ' | 事项编号 |
| 21 | ffillperiod | 填报周期 | varchar | 50 |  | √ | ' ' | 填报周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |
| 22 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 23 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [标签 t_tctb_label_info](../tctb_files/t_tctb_label_info.md) |
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
