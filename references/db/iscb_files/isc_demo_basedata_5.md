# 基础资料demo5-isc_demo_basedata_5

## 基础资料demo5-主表 t_isc_demo_basedata_5

- **表名称：** 基础资料demo5-主表
- **表名：** t_isc_demo_basedata_5

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | falias_name | 别名 | varchar | 100 |  | √ | ' ' | 别名 |
| 8 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_5_pkey |  | fid |
| 2 | idx_isc_demo_base_5 |  | fnumber |

---

## 学生分录-子表 t_isc_demo_basedata_5_e2

- **表名称：** 学生分录-子表
- **表名：** t_isc_demo_basedata_5_e2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstu_no | 学号 | varchar | 100 |  | √ | ' ' | 学号 |
| 2 | fstu_address_tag | fstu_address_tag | text | 0 |  |  | null |  |
| 3 | fparent | 监护人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fstu_height | 身高 | numeric | 23 | 10 | √ | 0.0000000000 | 身高 |
| 6 | fstu_age | 年龄 | int8 | 64 |  | √ | 0 | 年龄 |
| 7 | fstu_address | 家庭住址 | varchar | 510 |  | √ | ' ' | 家庭住址 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fstu_gender | 性别 | bpchar | 1 |  | √ | ' ' | 性别 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fstu_name | 姓名 | varchar | 100 |  | √ | ' ' | 姓名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_5_e2_pkey |  | fdetailid |
| 2 | idx_isc_demo_basedt_5_e2 |  | fstu_no |

---

## 班级分录-子表 t_isc_demo_basedata_5_e1

- **表名称：** 班级分录-子表
- **表名：** t_isc_demo_basedata_5_e1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclass | 班级名称 | varchar | 100 |  | √ | ' ' | 班级名称 |
| 3 | fhead_teacher | 班主任 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fclass_type | 班级类别 | varchar | 30 |  | √ | ' ' | 班级类别,枚举: arts :文科 science :理科 physical :体育 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcount | 整数 | int8 | 64 |  | √ | 0 | 整数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_basedt_5_e1 |  | fhead_teacher |
| 2 | t_isc_demo_basedata_5_e1_pkey |  | fentryid |

---

## 基础资料demo5-多语言表 t_isc_demo_basedata_5_l

- **表名称：** 基础资料demo5-多语言表
- **表名：** t_isc_demo_basedata_5_l

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
| 1 | t_isc_demo_basedata_5_l_pkey |  | fpkid |
| 2 | idx_isc_demo_base_5_l |  | fid,flocaleid |

---

## 任课老师-多选基础资料表 t_isc_demo_basedata_5_mu1

- **表名称：** 任课老师-多选基础资料表
- **表名：** t_isc_demo_basedata_5_mu1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_base5_mu1 |  | fentryid |
| 2 | t_isc_demo_basedata_5_mu1_pkey |  | fpkid |

---

## 关系人-多选基础资料表 t_isc_demo_basedata_5_mu2

- **表名称：** 关系人-多选基础资料表
- **表名：** t_isc_demo_basedata_5_mu2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_5_mu2_pkey |  | fpkid |
| 2 | idx_isc_demo_base5_mu2 |  | fdetailid |

---

## 用户人员-多选基础资料表 t_isc_demo_base5_md1

- **表名称：** 用户人员-多选基础资料表
- **表名：** t_isc_demo_base5_md1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_base5_md1 |  | fid |
| 2 | t_isc_demo_base5_md1_pkey |  | fpkid |
