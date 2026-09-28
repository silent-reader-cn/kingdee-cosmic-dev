# 跨境支付附件-aqap_pay_attachment

## 跨境支付附件-主表 t_aqap_pay_attachment

- **表名称：** 跨境支付附件-主表
- **表名：** t_aqap_pay_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freversed1 | reversed1 | varchar | 255 |  |  | null | reversed1 |
| 3 | freversed2 | reversed2 | varchar | 255 |  |  | null | reversed2 |
| 4 | ffile_name | 文件名 | varchar | 255 |  |  | null | 文件名 |
| 5 | freversed3 | reversed3 | varchar | 255 |  |  | null | reversed3 |
| 6 | fbank_status | bank_status | varchar | 50 |  |  | null | bank_status |
| 7 | fbank_batch_seq_id | bank_batch_seq_id | varchar | 50 |  |  | null | bank_batch_seq_id |
| 8 | freversed4 | reversed4 | varchar | 255 |  |  | null | reversed4 |
| 9 | fbank_version_id | bank_version_id | varchar | 50 |  |  | null | bank_version_id |
| 10 | fbank_detail_seq_id | bank_detail_seq_id | varchar | 50 |  |  | null | bank_detail_seq_id |
| 11 | fquery_impl_class_name | query_impl_class_name | varchar | 255 |  |  | null | query_impl_class_name |
| 12 | fdownload_url | 苍穹文件服务下载地址 | varchar | 512 |  |  | null | 苍穹文件服务下载地址 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fimpl_class_name | impl_class_name | varchar | 255 |  |  | null | impl_class_name |
| 18 | fcustomid | custom_id | varchar | 50 |  |  | null | custom_id |
| 19 | ffile_id | 文件id | varchar | 100 |  |  | null | 文件id |
| 20 | fbank_msg | bank_msg | varchar | 255 |  |  | null | bank_msg |
| 21 | fname | 名称 | varchar | 50 |  |  | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fbank_login_id | bank_login_id | varchar | 50 |  |  | null | bank_login_id |
| 25 | ffile_path | 文件路径 | varchar | 255 |  |  | null | 文件路径 |
| 26 | fstatus_name | status_name | varchar | 50 |  |  | null | status_name |
| 27 | fstatus_msg | status_msg | varchar | 50 |  |  | null | status_msg |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 50 |  |  | ' ' | 编码 |
| 30 | fstatus_id | status_id | int8 | 64 |  |  | null | status_id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_pay_attachment |  | fid |
| 2 | idx_aqap_pay_attachment_1 |  | fstatus_id |
| 3 | idx_aqap_pay_attachment |  | fbank_batch_seq_id |

---

## 跨境支付附件-多语言表 t_aqap_pay_attachment_l

- **表名称：** 跨境支付附件-多语言表
- **表名：** t_aqap_pay_attachment_l

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
| 1 | idx_aqap_pay_attachment_l |  | fid |
| 2 | pk_t_aqap_pay_attachment_l |  | fpkid |
