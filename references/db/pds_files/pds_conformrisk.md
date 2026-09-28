# 其他风险检查-pds_conformrisk

## 检查结果分录-子表 t_pds_conformentry

- **表名称：** 检查结果分录-子表
- **表名：** t_pds_conformentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 寻源项目ID |
| 3 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 4 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 7 | fsysresultid | fsysresultid | int8 | 64 |  | √ | 0 |  |
| 8 | fdescription | 检查详情 | varchar | 1024 |  | √ | ' ' | 检查详情 |
| 9 | fcheckitemid | fcheckitemid | int8 | 64 |  | √ | 0 |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_conformentry |  | fentryid |
| 2 | idx_pds_conformentry_pro |  | fprojectid |
| 3 | idx_pds_conformentry_pid |  | fparentid |
| 4 | idx_pds_conformentry_fid |  | fid |

---

## 其他风险检查-主表 t_pds_conformcheck

- **表名称：** 其他风险检查-主表
- **表名：** t_pds_conformcheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 3 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 4 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_conformcheck_pid |  | fparentid |
| 2 | pk_pds_conformcheck |  | fid |
