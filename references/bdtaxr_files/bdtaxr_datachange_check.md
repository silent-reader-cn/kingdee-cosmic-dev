# 业务资料变更检查-bdtaxr_datachange_check

## 单据体-子表 t_bdtaxr_datacheck_items

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_datacheck_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fitemnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fitemname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 7 | foperation | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: add :新增 edit :修改 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_datacheck_items |  | fentryid |
| 2 | idx_bdtaxr_datacheck_items_fk |  | fid |

---

## 业务资料变更检查-多语言表 t_bdtaxr_datachange_check_l

- **表名称：** 业务资料变更检查-多语言表
- **表名：** t_bdtaxr_datachange_check_l

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
| 1 | idx_bdtaxr_datachange_check_l |  | fid,flocaleid |
| 2 | pk_bdtaxr_datachange_check_l |  | fpkid |

---

## 业务资料变更检查-主表 t_bdtaxr_datachange_check

- **表名称：** 业务资料变更检查-主表
- **表名：** t_bdtaxr_datachange_check

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckdata | 检查资料 | varchar | 50 |  | √ | ' ' | 检查资料 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fstart | 检查时间范围.开始 | timestamp | 0 |  |  | null | 检查时间范围.开始 |
| 6 | fprocessstatus | 处理状态 | varchar | 50 |  | √ | ' ' | 处理状态,枚举: todo :待处理 done :已处理 no :无需处理 |
| 7 | fprocesscer | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frange | 影响范围 | varchar | 2000 |  | √ | ' ' | 影响范围 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fopinion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 15 | fend | 检查时间范围.结束 | timestamp | 0 |  |  | null | 检查时间范围.结束 |
| 16 | fnumber | 检查编号 | varchar | 30 |  | √ | ' ' | 检查编号 |
| 17 | fcount | 变更数据量 | int8 | 64 |  | √ | 0 | 变更数据量 |
| 18 | fprocesstime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_datachange_check |  | fnumber |
| 2 | pk_bdtaxr_datachange_check |  | fid |
