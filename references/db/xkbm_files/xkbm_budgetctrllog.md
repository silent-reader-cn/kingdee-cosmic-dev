# 预算控制日志-xkbm_budgetctrllog

## 单据体-子表 t_xkbm_ctrllogentity

- **表名称：** 单据体-子表
- **表名：** t_xkbm_ctrllogentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 日志级别 | varchar | 50 |  | √ | ' ' | 日志级别 |
| 3 | fdescriptions | 操作内容 | varchar | 50 |  | √ | ' ' | 操作内容 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fruleid | 控制规则 | int8 | 64 |  | √ | 0 | 预算控制规则 xkbm_ctrlrule |
| 6 | flogtype | 日志类型 | varchar | 50 |  | √ | ' ' | 日志类型 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | flogtime | 操作时间 | varchar | 50 |  | √ | ' ' | 操作时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrllogentity |  | fentryid |
| 2 | idx_xkbm_ctrllogentity |  | flogtype,fruleid |

---

## 预算控制日志-主表 t_xkbm_budgetctrllog

- **表名称：** 预算控制日志-主表
- **表名：** t_xkbm_budgetctrllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | 预算业务服务 xkbm_businessservice |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillformid | 控制单据 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | falldetailed | 所有信息 | text | 0 |  |  | null | 所有信息 |
| 7 | fcreatetime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 8 | foperatetime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 9 | fmodifier | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 10 | foperationnumber | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 11 | fdescription | 操作说明 | varchar | 2000 |  | √ | ' ' | 操作说明 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 19 | foperationid | 操作ID | varchar | 50 |  | √ | ' ' | 操作ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetctrllog |  | fid |
| 2 | idx_xkbm_budgetctrllog |  | fbillformid,fbillno |

---

## 预算控制日志-多语言表 t_xkbm_budgetctrllog_l

- **表名称：** 预算控制日志-多语言表
- **表名：** t_xkbm_budgetctrllog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetctrllog_l |  | fpkid |
| 2 | idx_xkbm_ctrllog_l_fname |  | fname |
| 3 | idx_xkbm_ctrllog_l_fid |  | fid |
