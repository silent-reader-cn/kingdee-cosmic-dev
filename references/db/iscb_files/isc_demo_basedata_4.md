# 基础资料demo4-isc_demo_basedata_4

## 基础资料demo4-主表 t_isc_demo_basedata_4

- **表名称：** 基础资料demo4-主表
- **表名：** t_isc_demo_basedata_4

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdemo2 | demo2 | int8 | 64 |  | √ | 0 | 基础资料demo2 isc_demo_basedata_2 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_base_4 |  | fnumber |
| 2 | t_isc_demo_basedata_4_pkey |  | fid |

---

## 单据体-子表 t_isc_demo_basedata_e4

- **表名称：** 单据体-子表
- **表名：** t_isc_demo_basedata_e4

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsex | 性别 | bpchar | 1 |  | √ | ' ' | 性别 |
| 3 | fbirthday | 出生时间 | timestamp | 0 |  |  | null | 出生时间 |
| 4 | fuser | 用户 | varchar | 100 |  | √ | ' ' | 用户 |
| 5 | fage | 年龄 | int8 | 64 |  | √ | 0 | 年龄 |
| 6 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fheight | 小数 | numeric | 23 | 10 | √ | 0.0000000000 | 小数 |
| 9 | fpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_base_e3 |  | fid |
| 2 | t_isc_demo_basedata_e4_pkey |  | fentryid |
