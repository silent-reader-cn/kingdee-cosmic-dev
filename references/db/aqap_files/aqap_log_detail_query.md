# 日志查看-aqap_log_detail_query

## 日志查看-主表 t_aqap_log_detail

- **表名称：** 日志查看-主表
- **表名：** t_aqap_log_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fopenorgid | 开户公司 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifytime1 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | flogger_detail_no | 银行日志号 | varchar | 50 |  | √ | ' ' | 银行日志号 |
| 5 | flog_time | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 6 | fbussiness_request_pay |  | varchar | 255 |  | √ | ' ' |  |
| 7 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | faccount | 银行账户 | varchar | 50 |  | √ | ' ' | 银行账户 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbankinterface | 银行接口信息 | varchar | 50 |  | √ | ' ' | 银行接口信息 |
| 11 | fnumber1 | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fenablerid | 启用人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcreatetime1 | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fbiz_name | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 15 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 16 | fbussiness_request_pay_tag | 详情 | varchar | 255 |  |  | null | 详情 |
| 17 | fother_log |  | varchar | 255 |  | √ | ' ' |  |
| 18 | fother_log_pay |  | varchar | 255 |  | √ | ' ' |  |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fname1 | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 21 | fcreator1 | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fenable1 | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fbankinterfaceid | 银行接口ID | varchar | 50 |  | √ | ' ' | 银行接口ID |
| 24 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 25 | fother_log_tag | 详情 | varchar | 255 |  |  | null | 详情 |
| 26 | ftranstype | 传输类型 | varchar | 50 |  | √ | ' ' | 传输类型,枚举: send :发送 Receiver :接收 exceptionSend :发送异常 exceptionReceive :接收类型 |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fbd_bank_version | 银行版本 | int8 | 64 |  |  | null | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fbussiness_request |  | varchar | 255 |  | √ | ' ' |  |
| 31 | fcompanyid | 资金组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fbussiness_response_pay_tag | 详情 | varchar | 255 |  |  | null | 详情 |
| 33 | fbd_biz_name | 业务类型 | int8 | 64 |  |  | null | [业务类型 aqap_business_type](../aqap_files/aqap_business_type.md) |
| 34 | fbank_log_pay_tag | 详情 | varchar | 255 |  |  | null | 详情 |
| 35 | fbussiness_response_tag | 详情 | varchar | 255 |  |  | null | 详情 |
| 36 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 39 | fbank_log |  | varchar | 255 |  | √ | ' ' |  |
| 40 | fbussiness_response |  | varchar | 255 |  | √ | ' ' |  |
| 41 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fmodifier1 | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fpayeeacnt | 收款账户 | varchar | 50 |  | √ | ' ' | 收款账户 |
| 46 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 47 | fbank_log_pay |  | varchar | 255 |  | √ | ' ' |  |
| 48 | flogger_batch_no | 业务日志号 | varchar | 50 |  | √ | ' ' | 业务日志号 |
| 49 | fmasterid1 | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 50 | fbussiness_request_tag | 详情 | varchar | 255 |  |  | null | 详情 |
| 51 | fother_log_pay_tag | 详情 | varchar | 255 |  |  | null | 详情 |
| 52 | fbank_log_tag | 详情 | varchar | 255 |  |  | null | 详情 |
| 53 | fbussiness_response_pay |  | varchar | 255 |  | √ | ' ' |  |
| 54 | fstatus1 | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_log_detail_pkey |  | fid |

---

## 日志查看-多语言表 t_aqap_log_detail_l

- **表名称：** 日志查看-多语言表
- **表名：** t_aqap_log_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fname1 | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_log_detail_l |  | fpkid |
