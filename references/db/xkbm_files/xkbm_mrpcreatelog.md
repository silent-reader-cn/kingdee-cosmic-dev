# 预算MRP操作日志-xkbm_mrpcreatelog

## 预算MRP操作日志-多语言表 t_xkbm_mrpcreatelog_l

- **表名称：** 预算MRP操作日志-多语言表
- **表名：** t_xkbm_mrpcreatelog_l

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
| 1 | pk_xkbm_mrpcreatelog_l |  | fpkid |
| 2 | idx_xkbm_mrplog_l_fname |  | fname |
| 3 | idx_xkbm_mrplog_l_fid |  | fid |

---

## 单据体-子表 t_xkbm_mrpcreatelogentry

- **表名称：** 单据体-子表
- **表名：** t_xkbm_mrpcreatelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstepseq | 步骤顺序 | varchar | 10 |  | √ | ' ' | 步骤顺序 |
| 3 | fstepname | 步骤名称 | varchar | 50 |  | √ | ' ' | 步骤名称 |
| 4 | flogresult | 运行结果 | varchar | 255 |  | √ | ' ' | 运行结果 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fstepstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :正常 C :失败 B :异常 |
| 7 | fdetailed_tag | 详细信息_详情 | text | 0 |  |  | null | 详细信息_详情 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | flogtime | 操作时间 | varchar | 50 |  | √ | ' ' | 操作时间 |
| 10 | fdetailed | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_mrpcreatelogentry |  | fentryid |
| 2 | idx_xkbm_mrplogentry_fid |  | fid |

---

## 预算MRP操作日志-主表 t_xkbm_mrpcreatelog

- **表名称：** 预算MRP操作日志-主表
- **表名：** t_xkbm_mrpcreatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 8 | fcreatestatus | 操作状态 | bpchar | 1 |  | √ | ' ' | 操作状态,枚举: A :创建成功 B :异常终止 C :创建失败 D :运行中 E :无记录 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 计划运算号 | varchar | 30 |  | √ | ' ' | 计划运算号 |
| 11 | fdescription | 操作说明 | varchar | 2000 |  | √ | ' ' | 操作说明 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_mrpcreatelog |  | fid |
| 2 | idx_xkbm_mrplog_fnumber |  | fnumber |
