# 形象库-fatvs_employee

## 形象库-主表 t_fatvs_employee

- **表名称：** 形象库-主表
- **表名：** t_fatvs_employee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentrystatus | 入职状态 | bpchar | 1 |  | √ | '0' | 入职状态,枚举: 0 :未入职 1 :已入职 |
| 3 | fadded | 已新增 | bpchar | 1 |  | √ | '0' | 已新增 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | favatar | 形象照 | varchar | 255 |  | √ | ' ' | 形象照 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fdepartment | 组织架构 | varchar | 100 |  | √ | ' ' | 组织架构 |
| 10 | fpositionid | 虚拟职位 | int8 | 64 |  | √ | 0 | [虚拟职位 fatvs_position](../fatvs_files/fatvs_position.md) |
| 11 | fusertype | 员工类型 | bpchar | 1 |  | √ | ' ' | 员工类型,枚举: 0 :系统预置 1 :自定义 |
| 12 | fofficeid | 办公室 | int8 | 64 |  | √ | 0 | [办公室 fatvs_office](../fatvs_files/fatvs_office.md) |
| 13 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbirthday | 出生年月 | timestamp | 0 |  |  | null | 出生年月 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fmotto | 座右铭 | varchar | 100 |  | √ | ' ' | 座右铭 |
| 18 | fgender | 性别 | bpchar | 1 |  | √ | ' ' | 性别,枚举: 0 :男 1 :女 |
| 19 | fentrytime | 入职时间 | timestamp | 0 |  |  | null | 入职时间 |
| 20 | fduty | 职责 | varchar | 255 |  | √ | ' ' | 职责 |
| 21 | fsimplepinyin | 姓名简拼 | varchar | 50 |  | √ | ' ' | 姓名简拼 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 工号 | varchar | 50 |  | √ | ' ' | 工号 |
| 24 | fimage | 头像照 | varchar | 255 |  | √ | ' ' | 头像照 |
| 25 | ffullpinyin | 姓名全拼 | varchar | 100 |  | √ | ' ' | 姓名全拼 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fatvs_employee |  | fid |
| 2 | idx_fatvs_emp_office |  | fofficeid |

---

## 形象库-多语言表 t_fatvs_employee_l

- **表名称：** 形象库-多语言表
- **表名：** t_fatvs_employee_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 3 | fmotto | 座右铭 | varchar | 100 |  | √ | ' ' | 座右铭 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fatvs_employee_l |  | fpkid |
| 2 | idx_fatvs_emp_l_fid |  | fid,flocaleid |
