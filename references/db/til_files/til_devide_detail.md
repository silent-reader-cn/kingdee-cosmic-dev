# 分摊明细-til_devide_detail

## 单据体-子表 t_til_devide_entity

- **表名称：** 单据体-子表
- **表名：** t_til_devide_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdevidetax | 分摊税额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊税额 |
| 3 | fprojectid | 预缴项目编码 | int8 | 64 |  | √ | 0 | 预缴项目信息 tcvat_prepay_project_info |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合同金额 |
| 6 | fdeviceratio | 分摊比例 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_til_devide_entity |  | fentryid |
| 2 | idx_til_devide_entity_fk |  | fid |

---

## 分摊明细-主表 t_til_devide_detail

- **表名称：** 分摊明细-主表
- **表名：** t_til_devide_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdevidetype | 分摊方式 | varchar | 50 |  | √ | ' ' | 分摊方式,枚举: a :按合同金额分摊 b :按自定义比例分摊 c :按自定义金额分摊 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 11 | finvoiceid | 发票id | varchar | 50 |  | √ | ' ' | 发票id |
| 12 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 13 | fsumtaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 14 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_til_devide_detail |  | fid |
| 2 | idx_til_devide_detail |  | forgid,finvoicecode,finvoiceno,fbaseinvoicetype |
