# 我的常用人员-src_usualuser

## 人员分录-子表 t_src_usualuserentry

- **表名称：** 人员分录-子表
- **表名：** t_src_usualuserentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 3 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 4 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | femail | 电子邮箱 | varchar | 50 |  | √ | ' ' | 电子邮箱 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 8 | fnumber | 工号 | varchar | 36 |  | √ | ' ' | 工号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fbidderid | 姓名 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_usualusere_fid |  | fid |
| 2 | pk_src_usualuserentry |  | fentryid |

---

## 我的常用人员-主表 t_src_usualuser

- **表名称：** 我的常用人员-主表
- **表名：** t_src_usualuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcompkey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_usualuser |  | fid |
| 2 | idx_src_usualuser_ckey |  | fcompkey |
