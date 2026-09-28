# 事项任务信息-ipm_basetask_info

## 事项任务信息-主表 t_ipm_basetask_info

- **表名称：** 事项任务信息-主表
- **表名：** t_ipm_basetask_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 事项任务类型 ipm_basetask_type |
| 5 | ftimerequire | 时间要求 | varchar | 100 |  | √ | ' ' | 时间要求 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | flawregulations_tag | 法律法规_详情 | text | 0 |  |  | null | 法律法规_详情 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | ftaskname | 事项名称 | varchar | 200 |  | √ | ' ' | 事项名称 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fmissionguidance_tag | 任务指引_详情 | text | 0 |  |  | null | 任务指引_详情 |
| 15 | fmissionguidance | 任务指引 | varchar | 255 |  |  | null | 任务指引 |
| 16 | flawregulations | 法律法规 | varchar | 255 |  |  | null | 法律法规 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 19 | fcode | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipm_basetask_info |  | fid |
| 2 | idx_info_name_uq |  | fname,fgroupid |

---

## 事项任务信息-多语言表 t_ipm_basetask_info_l

- **表名称：** 事项任务信息-多语言表
- **表名：** t_ipm_basetask_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipm_basetask_info_l |  | fpkid |
| 2 | idx_basetask_info_l_0 |  | fid,flocaleid |
