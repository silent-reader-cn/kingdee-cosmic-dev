# 税行日志内容-bdtaxr_linecontent

## 税行日志内容-主表 t_bdtaxr_linecontent

- **表名称：** 税行日志内容-主表
- **表名：** t_bdtaxr_linecontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftaxlinelog | 税行计算日志 | int8 | 64 |  | √ | 0 | [税行计算日志 bdtaxr_taxlinelog](../bastax_files/bdtaxr_taxlinelog.md) |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 单据分录序号 | varchar | 30 |  | √ | ' ' | 单据分录序号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_linecontent |  | fnumber |
| 2 | pk_bdtaxr_linecontent |  | fid |

---

## 税行日志内容-多语言表 t_bdtaxr_linecontent_l

- **表名称：** 税行日志内容-多语言表
- **表名：** t_bdtaxr_linecontent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 单据体-子表 t_bdtaxr_linedetail

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_linedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 执行步骤 | varchar | 200 |  | √ | ' ' | 执行步骤 |
| 3 | ftaxline | 税行 | int8 | 64 |  | √ | 0 | 税行 |
| 4 | fstepno | 步骤序号 | int8 | 64 |  | √ | 0 | 步骤序号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | flogcontent | 日志内容 | varchar | 1500 |  | √ | ' ' | 日志内容 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_linedetail_fk |  | fid |
| 2 | pk_bdtaxr_linedetail |  | fentryid |
