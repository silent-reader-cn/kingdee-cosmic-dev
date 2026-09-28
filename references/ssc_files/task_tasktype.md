# 任务类型-task_tasktype

## 任务类型-主表 t_tk_tasktype

- **表名称：** 任务类型-主表
- **表名：** t_tk_tasktype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fqualityjudge | 任务属性 | bpchar | 1 |  | √ | '0' | 任务属性,枚举: 0 :审单任务 1 :质检任务 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fssccenterid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fcoefficient | 标准系数 | numeric | 23 | 2 | √ | 0.00 | 标准系数 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_tasktype_pkey |  | fid |
| 2 | index_ssc_tasktype |  | fnumber |

---

## 任务类型-多语言表 t_tk_tasktype_l

- **表名称：** 任务类型-多语言表
- **表名：** t_tk_tasktype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_tasktype_l_pkey |  | fpkid |
| 2 | index_ssc_tasktype_l |  | fid,flocaleid |

---

## 单据体-子表 t_tk_dynamicfield

- **表名称：** 单据体-子表
- **表名：** t_tk_dynamicfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 3 | ffieldsourcetype | 字段来源类型 | bpchar | 1 |  | √ | '0' | 字段来源类型,枚举: 0 :系统固定字段 1 :任务类型字段 2 :单据类型字段 |
| 4 | ffieldtype | 字段类型 | bpchar | 1 |  | √ | '0' | 字段类型,枚举: 0 :字符串 1 :日期 2 :数字 3 :日期时间 |
| 5 | ffieldname | 字段 | varchar | 50 |  | √ | ' ' | 字段 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fisshow | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_dynamicfield |  | fid |
| 2 | t_tk_dynamicfield_pkey |  | fentryid |
