# 新增填报项-tctsa_report_items

## 标签单据体-子表 t_tctsa_report_item_label

- **表名称：** 标签单据体-子表
- **表名：** t_tctsa_report_item_label

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | flabelid | 标签 | int8 | 64 |  | √ | 0 | 标签 t_tctb_label_info |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_report_item_label_fk |  | fid |
| 2 | pk_tctsa_report_item_label |  | fentryid |

---

## 新增填报项-主表 t_tctsa_report_item

- **表名称：** 新增填报项-主表
- **表名：** t_tctsa_report_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | ftype | 事项分类 | int8 | 64 |  | √ | 0 | 填报类型 tctsa_report_items_tree |
| 10 | fperiod | 填报周期 | varchar | 30 |  | √ | ' ' | 填报周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |
| 11 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | ffillingtype | 填报类型 | varchar | 50 |  | √ | ' ' | 填报类型,枚举: 1 :金额类填报 2 :数值类填报 3 :文本类填报 |
| 13 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 14 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_report_item |  | fnumber |
| 2 | pk_tctsa_report_item |  | fid |

---

## 新增填报项-多语言表 t_tctsa_report_item_l

- **表名称：** 新增填报项-多语言表
- **表名：** t_tctsa_report_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_report_item_l_0 |  | fid,flocaleid |
| 2 | pk_tctsa_report_item_l |  | fpkid |
