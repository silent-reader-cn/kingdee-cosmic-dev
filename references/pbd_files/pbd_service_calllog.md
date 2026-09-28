# 接口调用记录-pbd_service_calllog

## 接口调用记录-主表 t_pbd_calllog

- **表名称：** 接口调用记录-主表
- **表名：** t_pbd_calllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | foperator | 业务操作 | varchar | 50 |  | √ | ' ' | 业务操作 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 调用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ftriggertype | 触发类别 | varchar | 50 |  | √ | ' ' | 触发类别,枚举: A :业务操作 B :条件触发 |
| 9 | fcalldatetime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | flink | 连接配置方案 | int8 | 64 |  | √ | 0 | 连接配置 pbd_credit_link |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcalluserid | 调用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillentity | 单据或组件 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fprogrammeid | 业务调用方案 | int8 | 64 |  | √ | 0 | 业务调用方案 pbd_service_programme |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_calllog_fbillno |  | fbillno |
| 2 | idx_pbd_calllog_calls |  | forgid,fprogrammeid,fcalldatetime |
| 3 | pk_pbd_calllog |  | fid |

---

## 单据体-子表 t_pbd_calllog_entryentity

- **表名称：** 单据体-子表
- **表名：** t_pbd_calllog_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresult_tag | 接口调用结果_详情 | text | 0 |  |  | null | 接口调用结果_详情 |
| 3 | fstandardapi | 标准接口名称 | int8 | 64 |  | √ | 0 | 接口标准化管理 pbd_standard_api |
| 4 | fplatformapi | 来源接口名称 | int8 | 64 |  | √ | 0 | 外部系统API pbd_extsys_api |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcalltime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 7 | fresult | 接口调用结果 | varchar | 255 |  | √ | ' ' | 接口调用结果 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsource | 数据来源 | bpchar | 1 |  | √ | ' ' | 数据来源,枚举: A :外部实时数据 B :本地数据 |
| 10 | frequest_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 11 | frequest | 请求参数 | varchar | 255 |  | √ | ' ' | 请求参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_calllog_entryentity |  | fentryid |
| 2 | idx_pbd_calllog_entry_fid_fseq |  | fid,fseq |
