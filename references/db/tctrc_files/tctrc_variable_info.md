# 变量信息-tctrc_variable_info

## 变量信息-主表 t_tctrc_variable

- **表名称：** 变量信息-主表
- **表名：** t_tctrc_variable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | frisknumber | 父页面风险编号 | varchar | 100 |  | √ | ' ' | 父页面风险编号 |
| 4 | fjson | 存储公式 | varchar | 510 |  | √ | ' ' | 存储公式 |
| 5 | ftimedeviationdirection | 时间偏移方向 | varchar | 100 |  | √ | ' ' | 时间偏移方向 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | frowid | 行id | varchar | 100 |  | √ | ' ' | 行id |
| 8 | forderno | 行内排序号 | varchar | 100 |  | √ | ' ' | 行内排序号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | ftimedeviation | 时间偏移 | varchar | 100 |  | √ | ' ' | 时间偏移 |
| 12 | felementnumber | 元素/指标编号 | varchar | 100 |  | √ | ' ' | 元素/指标编号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftimedeviationtype | 时间偏移跨度 | varchar | 100 |  | √ | ' ' | 时间偏移跨度 |
| 16 | fbottom | 是否底层 | bpchar | 1 |  | √ | ' ' | 是否底层 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | ftimedeviationcount | 时间偏移量 | varchar | 100 |  | √ | ' ' | 时间偏移量 |
| 19 | fnumber | 编号 | varchar | 60 |  | √ | ' ' | 编号 |
| 20 | fjson_tag | 存储公式_详情 | text | 0 |  |  | null | 存储公式_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_variable |  | fnumber |
| 2 | t_tctrc_variable_pkey |  | fid |

---

## 变量信息-多语言表 t_tctrc_variable_l

- **表名称：** 变量信息-多语言表
- **表名：** t_tctrc_variable_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctrc_variable_l_pkey |  | fpkid |
| 2 | idx_tctrc_variable_l_0 |  | fid,flocaleid |
