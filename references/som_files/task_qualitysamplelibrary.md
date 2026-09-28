# 质检样本库-task_qualitysamplelibrary

## 质检样本库-主表 t_tk_checksamplelibrary

- **表名称：** 质检样本库-主表
- **表名：** t_tk_checksamplelibrary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcheckcompletetime | 检查完成时间 | timestamp | 0 |  |  | null | 检查完成时间 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fexpirestate | 超期状态 | bpchar | 1 |  | √ | '1' | 超期状态,枚举: 1 :未超期 2 :超期 |
| 6 | fcompletednum | 已完成样本量 | int8 | 64 |  | √ | 0 | 已完成样本量 |
| 7 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 8 | fplanfinishtime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fstate | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :待分配 1 :处理中 4 :已完成 5 :已关闭 |
| 12 | fissmart | 是否智能方案 | bpchar | 1 |  | √ | '0' | 是否智能方案 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsmartcheckscheme | 智能质检方案 | int8 | 64 |  | √ | 0 | 智能质检方案 task_smartcheckscheme |
| 16 | ftotalnum | 样本总量 | int8 | 64 |  | √ | 0 | 样本总量 |
| 17 | fcheckbegintime | 检查开始时间 | timestamp | 0 |  |  | null | 检查开始时间 |
| 18 | fsimplename | 简称 | varchar | 50 |  | √ | ' ' | 简称 |
| 19 | fcheckscheme | 质检方案 | int8 | 64 |  | √ | 0 | 质检方案 task_qualitycheckscheme |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 样本库编码 | varchar | 60 |  | √ | ' ' | 样本库编码 |
| 22 | freformnum | 整改样本数 | int4 | 32 |  | √ | 0 | 整改样本数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_checksamplelibrary_pkey |  | fid |
| 2 | idx_ssc_qualityscheme |  | fcheckscheme |

---

## 质检样本库-多语言表 t_tk_checksamplelibrary_l

- **表名称：** 质检样本库-多语言表
- **表名：** t_tk_checksamplelibrary_l

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
| 1 | t_tk_checksamplelibrary_l_pkey |  | fpkid |
| 2 | idx_ssc_qualitysampliblan |  | fid,flocaleid |
