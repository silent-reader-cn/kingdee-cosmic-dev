# 业务状态详情-aqap_biz_task

## 业务状态详情-主表 t_aqap_biz_task

- **表名称：** 业务状态详情-主表
- **表名：** t_aqap_biz_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facc_no | 银行账号 | varchar | 255 |  | √ | ' ' | 银行账号 |
| 3 | fprocess_time | 任务处理耗时 | int8 | 64 |  | √ | 0 | 任务处理耗时 |
| 4 | flogger_no | 业务日志号 | varchar | 255 |  | √ | ' ' | 业务日志号 |
| 5 | fwait_time | 任务等待耗时 | int8 | 64 |  | √ | 0 | 任务等待耗时 |
| 6 | fbiz_type | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | frequest_seq | 业务请求流水号 | varchar | 255 |  | √ | ' ' | 业务请求流水号 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fstatus_no | 任务状态 | varchar | 50 |  | √ | '1' | 任务状态,枚举: 1 :创建完成 2 :排队等待 3 :处理中 4 :处理完成 |
| 13 | ffull_time | 任务总耗时 | int8 | 64 |  | √ | 0 | 任务总耗时 |
| 14 | fis_skip | 跳过执行 | varchar | 50 |  | √ | '0' | 跳过执行,枚举: 0 :否 1 :是 |
| 15 | fbank_batch_no | 提交银行批次号 | varchar | 255 |  | √ | ' ' | 提交银行批次号 |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbank_login | 银行前置机 | varchar | 50 |  | √ | ' ' | 银行前置机 |
| 19 | fbiz_no | 业务关联号 | varchar | 255 |  | √ | ' ' | 业务关联号 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fsub_biz_type | 子业务类型 | varchar | 255 |  | √ | ' ' | 子业务类型 |
| 22 | flogger_bank_no | 银行日志号 | varchar | 255 |  | √ | ' ' | 银行日志号 |
| 23 | fbank_version | 银行版本 | varchar | 255 |  | √ | ' ' | 银行版本 |
| 24 | febg_node | 实例节点 | varchar | 50 |  | √ | ' ' | 实例节点 |
| 25 | fbd_biz_type | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 aqap_business_type](../aqap_files/aqap_business_type.md) |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fbd_bank_version | 银行版本 | int8 | 64 |  | √ | 0 | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 28 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_biz_task_2 |  | fbd_biz_type |
| 2 | idx_biz_task_1 |  | fbd_bank_version |
| 3 | idx_cluster_biz_task |  | fnumber |
| 4 | idx_biz_task_6 |  | fcreatetime |
| 5 | pk_aqap_biz_task |  | fid |
| 6 | idx_biz_task_5 |  | fenable,fbank_login,febg_node,fcreatetime |
| 7 | idx_biz_task_4 |  | fenable,fbiz_type,fbank_login,febg_node,fcreatetime |

---

## 业务状态详情-多语言表 t_aqap_biz_task_l

- **表名称：** 业务状态详情-多语言表
- **表名：** t_aqap_biz_task_l

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
| 1 | idx_cluster_biz_task_l |  | fname |
| 2 | pk_aqap_biz_task_l |  | fpkid |
