# 固定填报聚合-tctsa_fixed_filling_aggr

## 固定填报聚合-主表 t_tctsa_fix_filling_aggr

- **表名称：** 固定填报聚合-主表
- **表名：** t_tctsa_fix_filling_aggr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 填报组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftskssqq | 填报所属期起 | timestamp | 0 |  |  | null | 填报所属期起 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 聚合审批编号 | varchar | 300 |  | √ | ' ' | 聚合审批编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftskssqz | 填报所属期止 | timestamp | 0 |  |  | null | 填报所属期止 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_ffa_1 |  | fbillno |
| 2 | pk_tctsa_fix_filling_aggr |  | fid |

---

## 标签-多选基础资料表 t_tctsa_fixed_aggr_label

- **表名称：** 标签-多选基础资料表
- **表名：** t_tctsa_fixed_aggr_label

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [标签 t_tctb_label_info](../tctb_files/t_tctb_label_info.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_fixed_aggr_label_fk |  | fentryid |
| 2 | pk_tctsa_fixed_aggr_label |  | fpkid |

---

## 单据体-子表 t_tctsa_fixedfilling_item

- **表名称：** 单据体-子表
- **表名：** t_tctsa_fixedfilling_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 事项名称 | varchar | 50 |  | √ | ' ' | 事项名称 |
| 3 | fentryorg | 填报组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ffixedfilling | 固定填报项 | int8 | 64 |  | √ | 0 | 固定填报查询 tctsa_fixed_filling_query |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 填报金额 | numeric | 23 | 10 | √ | 0 | 填报金额 |
| 7 | fsxcontent | 填报文本 | varchar | 25 |  | √ | ' ' | 填报文本 |
| 8 | fdescription | 描述 | varchar | 150 |  | √ | ' ' | 描述 |
| 9 | fskssqq | 填报所属期起 | timestamp | 0 |  |  | null | 填报所属期起 |
| 10 | fdecimal | 填报数值 | numeric | 23 | 10 | √ | 0 | 填报数值 |
| 11 | ftmodifier | 填报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fskssqz | 填报所属期止 | timestamp | 0 |  |  | null | 填报所属期止 |
| 13 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :模板引入 1 :系统生成 |
| 14 | fnumber | 事项编号 | varchar | 50 |  | √ | ' ' | 事项编号 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | ffillperiod | 填报周期 | varchar | 50 |  | √ | ' ' | 填报周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |
| 17 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_fixedfilling_item_fk |  | fid |
| 2 | pk_tctsa_fixedfilling_item |  | fentryid |
