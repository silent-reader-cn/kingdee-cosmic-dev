# 特殊人员-er_include_employee

## 特殊人员-主表 t_er_inclemployee

- **表名称：** 特殊人员-主表
- **表名：** t_er_inclemployee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftripstandardid | 差旅标准id | int8 | 64 |  | √ | 0 | 差旅标准id |
| 3 | fsourcebilltype | 来源单据标识 | varchar | 30 |  | √ | ' ' | 来源单据标识 |
| 4 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_inclemployee_pkey |  | fid |
| 2 | idx_er_inclemployee_ftripstdid |  | ftripstandardid |

---

## 特殊人员-子表 t_er_employeedetail

- **表名称：** 特殊人员-子表
- **表名：** t_er_employeedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdept | 部门 | varchar | 100 |  | √ | ' ' | 部门 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_employeedetail_fseq |  | fid,fseq |
| 2 | t_er_employeedetail_pkey |  | fdetailid |
| 3 | idx_er_employeedetail_fuserid |  | fuserid |
