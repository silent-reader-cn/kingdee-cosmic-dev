# 发票数据同步-tdm_invoice_sync

## 同步组织-多选基础资料表 t_tdm_invoice_org

- **表名称：** 同步组织-多选基础资料表
- **表名：** t_tdm_invoice_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_invoice_org |  | fpkid |
| 2 | idx_tdm_invoice_org_fk |  | fid |

---

## 发票类型-多选基础资料表 t_tdm_invoice_type

- **表名称：** 发票类型-多选基础资料表
- **表名：** t_tdm_invoice_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_invoice_type_fk |  | fid |
| 2 | pk_tdm_invoice_type |  | fpkid |

---

## 发票数据同步-主表 t_tdm_invoice_sync

- **表名称：** 发票数据同步-主表
- **表名：** t_tdm_invoice_sync

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatetype | 日期类型 | varchar | 50 |  | √ | ' ' | 日期类型,枚举: 0 :开票时间 1 :所属税期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fstartbillingdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 同步组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsynctype | 同步类型 | varchar | 50 |  | √ | ' ' | 同步类型,枚举: 0 :手工同步 1 :定时同步 |
| 9 | fsuccessrows | 成功行数 | int8 | 64 |  | √ | 0 | 成功行数 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fbusinesslinks | 业务环节 | varchar | 30 |  | √ | ' ' | 业务环节,枚举: input :进项发票 output :销项发票 all :进项发票,销项发票 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fendbillingdate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 14 | fexecutstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 1 :执行中 2 :成功 3 :部分失败 4 :失败 |
| 15 | ffailrows | 失败行数 | int8 | 64 |  | √ | 0 | 失败行数 |
| 16 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 19 | fdeallog | 记录日志 | varchar | 200 |  | √ | ' ' | 记录日志 |
| 20 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | ftotalrows | 总行数 | int8 | 64 |  | √ | 0 | 总行数 |
| 23 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: 1 :进项发票 2 :销项发票 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_invoice_sync |  | fid |
| 2 | idx_tdm_invoice_sync |  | forgid,fstartdate,fenddate |
