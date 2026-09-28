# 基础资料demo3-isc_demo_basedata_3

## 用户人员-多选基础资料表 t_isc_demo_base3_md1

- **表名称：** 用户人员-多选基础资料表
- **表名：** t_isc_demo_base3_md1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_base3_md1 |  | fid |
| 2 | t_isc_demo_base3_md1_pkey |  | fpkid |

---

## 任课老师-多选基础资料表 t_isc_demo_basedata_3_mu1

- **表名称：** 任课老师-多选基础资料表
- **表名：** t_isc_demo_basedata_3_mu1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_base3_mu1 |  | fentryid |
| 2 | t_isc_demo_basedata_3_mu1_pkey |  | fpkid |

---

## 关系人-多选基础资料表 t_isc_demo_basedata_3_mu2

- **表名称：** 关系人-多选基础资料表
- **表名：** t_isc_demo_basedata_3_mu2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_3_mu2_pkey |  | fpkid |
| 2 | idx_isc_demo_base3_mu2 |  | fdetailid |

---

## 基础资料demo3-主表 t_isc_demo_basedata_3

- **表名称：** 基础资料demo3-主表
- **表名：** t_isc_demo_basedata_3

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fstatus | fstatus | varchar | 30 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdemo1 | demo1 | int8 | 64 |  | √ | 0 | 基础资料demo1 isc_demo_basedata_1 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_3_pkey |  | fid |
| 2 | idx_isc_demo_base_3 |  | fnumber |

---

## 班级分录信息-子表 t_isc_demo_basedata_3_e1

- **表名称：** 班级分录信息-子表
- **表名：** t_isc_demo_basedata_3_e1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclass | 班级名称 | varchar | 50 |  | √ | ' ' | 班级名称 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_base3_e1 |  | fid |
| 2 | t_isc_demo_basedata_3_e1_pkey |  | fentryid |

---

## 学生分录-子表 t_isc_demo_basedata_3_e2

- **表名称：** 学生分录-子表
- **表名：** t_isc_demo_basedata_3_e2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstu_no | 学号 | varchar | 50 |  | √ | ' ' | 学号 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fstu_name | 学生姓名 | varchar | 50 |  | √ | ' ' | 学生姓名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_base3_e2 |  | fentryid |
| 2 | t_isc_demo_basedata_3_e2_pkey |  | fdetailid |

---

## 基础资料demo3-多语言表 t_isc_demo_basedata_3_l

- **表名称：** 基础资料demo3-多语言表
- **表名：** t_isc_demo_basedata_3_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmulilang_desc | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | f_mulilang_desc | f_mulilang_desc | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_3_l_pkey |  | fpkid |
| 2 | idx_isc_demo_basedata_3_l_0 |  | fid,flocaleid |
