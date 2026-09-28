# 业务事项-er_standard_type

## 费用项目范围-子表 t_er_standard_entry

- **表名称：** 费用项目范围-子表
- **表名：** t_er_standard_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitem | 费用项目编码 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_standard_entry |  | fentryid |
| 2 | idx_er_standentry_fid |  | fid |

---

## 业务事项-多语言表 t_er_standard_type_l

- **表名称：** 业务事项-多语言表
- **表名：** t_er_standard_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_standard_type_l_0 |  | fid,flocaleid |
| 2 | pk_t_er_standard_type_l |  | fpkid |

---

## 附件范围-多语言表 t_er_standard_attach_l

- **表名称：** 附件范围-多语言表
- **表名：** t_er_standard_attach_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fattachname | 附件名称 | varchar | 1000 |  | √ | ' ' | 附件名称 |
| 2 | fattdescription | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
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
| 1 | index_er_standard_attach_l_0 |  | fentryid,flocaleid |
| 2 | pk_t_er_standard_attach_l |  | fpkid |

---

## 敏感词-子表 t_er_standard_sensetive

- **表名称：** 敏感词-子表
- **表名：** t_er_standard_sensetive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsensetivefield | 敏感词 | varchar | 1000 |  | √ | ' ' | 敏感词 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsendescription | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fverifyfield | 校验字段 | varchar | 1000 |  | √ | ' ' | 校验字段,枚举: description :事由 expenseentryentity.expensegoodsname :费用明细.商品名称 expenseentryentity.remark :费用明细.备注 invoiceentry.invoicegoodsname :发票信息.商品名称 invoiceentry.makeoutcompname :发票信息.开票公司 invoiceentry.buyerorgname :发票信息.收票公司 invoiceentry.remark_invoice :发票信息.备注 |
| 7 | fverifyflag | 预留校验后台字段标识 | varchar | 1000 |  | √ | ' ' | 预留校验后台字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_standsensetive_fid |  | fid |
| 2 | pk_t_er_standard_sensetive |  | fentryid |

---

## 业务事项-主表 t_er_standard_type

- **表名称：** 业务事项-主表
- **表名：** t_er_standard_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | fctrlstrategy | varchar | 20 |  | √ | ' ' |  |
| 11 | fispreapply | 事前申请 | bpchar | 1 |  | √ | '0' | 事前申请 |
| 12 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 17 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 19 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 20 | fbilltype | 标准类型 | varchar | 255 |  | √ | ' ' | 标准类型,枚举: f1 :通用标准 f2 :会议费标准 f3 :招待费标准 f4 :宣传费标准 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_standard_type |  | fid |
| 2 | idx_standard_type_createorg |  | fcreateorgid |
| 3 | idx_t_er_standard_type_master |  | fmasterid |

---

## 敏感词-多语言表 t_er_standard_sensetive_l

- **表名称：** 敏感词-多语言表
- **表名：** t_er_standard_sensetive_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsensetivefield | 敏感词 | varchar | 1000 |  | √ | ' ' | 敏感词 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fsendescription | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_er_standard_sense_l |  | fentryid,flocaleid |
| 2 | pk_t_er_standard_sensetive_l |  | fpkid |

---

## 附件范围-子表 t_er_standard_attach

- **表名称：** 附件范围-子表
- **表名：** t_er_standard_attach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachname | 附件名称 | varchar | 1000 |  | √ | ' ' | 附件名称 |
| 3 | fattdescription | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachno | 附件编码 | varchar | 1000 |  | √ | ' ' | 附件编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_standard_attach |  | fentryid |
| 2 | index_er_standard_attach_fk |  | fid |

---

## 选择维度-多选基础资料表 t_er_standard_select_dim

- **表名称：** 选择维度-多选基础资料表
- **表名：** t_er_standard_select_dim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 事项维度 er_standard_dimension |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_standard_select_dim |  | fpkid |
| 2 | idx_er_standard_select_dim_fk |  | fid |
