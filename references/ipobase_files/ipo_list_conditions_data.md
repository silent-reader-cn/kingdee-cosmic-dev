# IPO上市条件标准值与默认值-ipo_list_conditions_data

## IPO上市条件标准值与默认值-主表 t_ipo_lconditions_data

- **表名称：** IPO上市条件标准值与默认值-主表
- **表名：** t_ipo_lconditions_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 上市条件类型 ipo_list_conditions_type |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fstandardformat | 标准值格式 | varchar | 50 |  | √ | ' ' | 标准值格式 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fdefaultvalue | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fstandardvalue | 标准值 | varchar | 50 |  | √ | ' ' | 标准值 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fquotainfoid | 指标信息 | int8 | 64 |  | √ | 0 | 指标库 ipo_quota_info |
| 16 | fdefaultformat | 默认值格式 | varchar | 50 |  | √ | ' ' | 默认值格式 |
| 17 | fcombofield | 比较符号 | varchar | 50 |  | √ | ' ' | 比较符号,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lconditions_data_name |  | fname |
| 2 | pk_ipo_lconditions_data |  | fid |
| 3 | idx_lconditions_data_number |  | fnumber |

---

## IPO上市条件标准值与默认值-多语言表 t_ipo_lconditions_data_l

- **表名称：** IPO上市条件标准值与默认值-多语言表
- **表名：** t_ipo_lconditions_data_l

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
| 1 | idx_ipo_lconditions_data_l_0 |  | fid |
| 2 | pk_ipo_lconditions_data_l |  | fpkid |
